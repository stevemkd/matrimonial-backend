# Quick Deploy to Render

## 🚀 Quick Steps

### 1. Generate Production Secret Key
```bash
python generate_secret_key.py
```
Copy the generated SECRET_KEY and add it to your `.env` file.

### 2. Update .env for Production
```bash
SECRET_KEY=your-generated-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-app-name.onrender.com,*.render.com
```

### 3. Push to GitHub
```bash
# If you haven't pushed to GitHub yet:
git remote add origin https://github.com/yourusername/matrimonial-backend.git
git branch -M main
git push -u origin main

# If already connected:
git push origin main
```

### 4. Deploy to Render

1. Go to [render.com](https://render.com)
2. Click **New** → **Web Service**
3. **Connect GitHub**: Select your repository
4. **Settings**:
   - Root Directory: `backend`
   - Runtime: `Python 3`
   - Build: `pip install -r requirements.txt`
   - Start: `python manage.py runserver 0.0.0.0:$PORT`
5. **Environment Variables**:
   - `PYTHON_VERSION=3.13.0`
   - `DJANGO_SETTINGS_MODULE=backend.settings`
   - `SECRET_KEY`: Your generated key
   - `DEBUG=False`
   - `ALLOWED_HOSTS`: Your domain
   - Database: Configure MySQL connection

6. **Deploy**!

### 5. Set Up Database

After deployment:
1. Go to your web service on Render
2. Click **Shell**
3. Run:
   ```bash
   python manage.py migrate
   python manage.py populate_data
   ```

### 6. Update React Native App

Update your API URL in the React Native app:
```javascript
// src/config/api.js
const API_BASE_URL = 'https://your-app-name.onrender.com/api';
```

## ✅ Done!

Your matrimonial API is now live on Render! 🎊
