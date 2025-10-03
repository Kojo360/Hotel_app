Deployment checklist for Vercel (ensure migrations run and avoid read-only media errors)

1) Ensure project environment variables (Project Settings > Environment Variables):
   - DATABASE_URL: set to your Postgres connection string (e.g. $POSTGRES_URL) and make it available at Build & Production.
   - SECRET_KEY, DEBUG, ALLOWED_HOSTS, CSRF_TRUSTED_ORIGINS, WHITENOISE_USE_FINDERS, USE_STATIC_DATA as needed.

2) Deploy behavior:
   - `build.sh` now runs `collectstatic` and will run `python manage.py migrate --noinput` during build only if `DATABASE_URL` is set during build.
   - If your `DATABASE_URL` is not available at build time, either:
     * Set it in Vercel's Project Environment Variables with the "Build & Development" scope; or
     * Run migrations manually after deployment using a one-off command in the Vercel dashboard or via a serverless function that runs migrations on startup (not recommended).

3) Verifying migrations applied:
   - After deployment, open the Vercel deployment and check the Build Logs for the `Running migrations during build...` message and successful "Applying ... OK" lines.
   - If you don't see that, run migrations manually from your local machine by setting DATABASE_URL temporarily and running:

```powershell
$env:DATABASE_URL = "<your DATABASE_URL>"
C:/Users/KC-USER/AppData/Local/Microsoft/WindowsApps/python3.13.exe manage.py migrate --noinput
```

4) Preventing Read-only filesystem errors:
   - `settings.py` now attempts to write into the repo `media/` folder and falls back to the OS temp dir if that fails. This prevents OSError at runtime when an admin accidentally uploads a file.
   - Recommended: Because the app uses URLFields for images, instruct admins to paste HTTPS image URLs; file uploads are not persisted across serverless deployments.

5) Troubleshooting server errors after deploy:
   - Check Vercel Function logs for the failing request. Look for tracebacks mentioning `OSError: Read-only file system` or `FieldFile.save()`.
   - If you see image/file save tracebacks, ensure migrations that alter ImageField -> URLField are applied to the production DB.
   - You can tail logs in the Vercel dashboard or use the Vercel CLI: `vercel logs <deployment-url> --since 1h`.

6) Next steps (optional):
   - If you need file uploads, configure an external object storage (S3, DigitalOcean Spaces, etc.) and set Django's DEFAULT_FILE_STORAGE to use that backend. This is a larger change.

Optional: S3 / Object Storage setup
----------------------------------
If you want admins to upload images (instead of pasting URLs) you can enable an S3-compatible storage backend.

1) Add the following environment variables to Vercel:
   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY
   - AWS_STORAGE_BUCKET_NAME
   - AWS_S3_REGION_NAME (optional)
   - AWS_S3_CUSTOM_DOMAIN (optional)

2) The app will enable S3 storage automatically when `AWS_STORAGE_BUCKET_NAME` is set. The build step will still run migrations if `DATABASE_URL` is present.

3) Required Python packages were added to `requirements.txt`: `django-storages[boto3]` and `boto3`.

4) Once S3 is enabled, `ImageField`/`FileField` storage will use S3 and files will be persisted and served from the bucket.

If you'd like, I can prepare a small management command or a one-off endpoint to run migrations safely on the deployed app, or I can add a brief CI step for migrations in your GitHub workflow. Tell me which you prefer.