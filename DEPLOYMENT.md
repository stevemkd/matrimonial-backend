# Django Matrimonial API - Deployment Guide

## Deploy to Render

This guide will help you deploy your Django matrimonial API to Render.

### Prerequisites

1. **Render Account**: Create a free account at [render.com](https://render.com)
2. **GitHub Repository**: Push your code to GitHub
3. **MySQL Database**: Set up a MySQL database on Render

### Step 1: Prepare Your Code

1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Generate Production Secret Key**:
   ```bash
   python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
   ```

### Step 2: Set Up Database on Render

1. Go to Render Dashboard
2. Click **New** → **PostgreSQL** (or MySQL)
3. Name: `matrimonial-db`
4. Choose **Free** plan
5. Click **Create Database**
6. Note the connection details (username, password, host, port)

### Step 3: Deploy Web Service

1. Go to Render Dashboard
2. Click **New** → **Web Service**
3. **Connect GitHub**: Select your repository
4. **Build & Deploy Settings**:
   - Branch: `main`
   - Root Directory: `backend`
   - Runtime: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python manage.py runserver 0.0.0.0:$PORT`

5. **Environment Variables**:
   ```
   PYTHON_VERSION=3.13.0
   DJANGO_SETTINGS_MODULE=backend.settings
   SECRET_KEY=your-generated-secret-key
   DEBUG=False
   ALLOWED_HOSTS=your-app-name.onrender.com
   DB_NAME=matrimonial_db
   DB_USER=your-db-username
   DB_PASSWORD=your-db-password
   DB_HOST=your-db-host
   DB_PORT=5432
   ```

6. Click **Advanced Settings** and add:
   - Health Check Path: `/api/`
   - Auto-Deploy: ✅

7. Click **Create Web Service**

### Step 4: Configure CORS

Update your `.env` file in production:
```bash
CORS_ALLOWED_ORIGINS=*
```

### Step 5: Run Migrations

1. Go to your web service on Render
2. Click **Shell**
3. Run:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py populate_data
   ```

### Step 6: Update React Native App

Update your API configuration in the React Native app:

```javascript
// src/config/api.js
export const API_CONFIG = {
  BASE_URL_ANDROID: 'https://your-app-name.onrender.com/api',
  BASE_URL_IOS: 'https://your-app-name.onrender.com/api',
  BASE_URL_DEVICE: 'https://your-app-name.onrender.com/api',
  
  getBaseUrl() {
    return this.BASE_URL_ANDROID; // or appropriate platform
  }
};
```

### Environment Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | `django-insecure-...` |
| `DEBUG` | Debug mode | `False` |
| `ALLOWED_HOSTS` | Allowed domains | `*.onrender.com` |
| `DB_NAME` | Database name | `matrimonial_db` |
| `DB_USER` | Database user | `your_db_user` |
| `DB_PASSWORD` | Database password | `your_db_password` |
| `DB_HOST` | Database host | `your-db-host` |
| `DB_PORT` | Database port | `5432` |

### Troubleshooting

#### Common Issues:

1. **Database Connection Error**:
   - Verify database credentials
   - Check if database is running
   - Ensure CORS is properly configured

2. **404 Errors**:
   - Check ALLOWED_HOSTS setting
   - Verify API endpoints are correct
   - Ensure Django is running on correct port

3. **Migration Errors**:
   - Run `python manage.py migrate` in shell
   - Check database schema compatibility

4. **CORS Issues**:
   - Set `CORS_ALLOWED_ORIGINS=*` in settings
   - Verify React Native app URL is correct

### Production Checklist

- [ ] Generate new SECRET_KEY
- [ ] Set DEBUG=False
- [ ] Configure ALLOWED_HOSTS
- [ ] Set up production database
- [ ] Run migrations
- [ ] Populate sample data
- [ ] Test API endpoints
- [ ] Update React Native app URL
- [ ] Test authentication flow

### Support

For deployment issues:
- Check Render logs
- Review Django error pages
- Verify environment variables
- Test database connection

Your matrimonial API is now ready for production! 🚀
