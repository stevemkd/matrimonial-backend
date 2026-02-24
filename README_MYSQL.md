# Django MySQL Setup Guide

## Prerequisites
- Python 3.8+
- MySQL Server installed and running
- pip

## Installation Steps

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Install MySQL Connector (if not already installed)
On Windows:
```bash
pip install mysqlclient
```

On Ubuntu/Debian:
```bash
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
pip install mysqlclient
```

On macOS:
```bash
brew install mysql-client
pip install mysqlclient
```

### 3. Setup MySQL Database
Run the setup script:
```bash
python setup_mysql.py
```

Or manually create the database:
```sql
CREATE DATABASE matrimonial_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 4. Configure Environment Variables
Copy the example environment file:
```bash
cp .env.example .env
```

Edit `.env` file with your MySQL credentials:
```
DB_NAME=matrimonial_db
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
```

### 5. Run Django Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (optional)
```bash
python manage.py createsuperuser
```

### 7. Test the Setup
```bash
python manage.py runserver
```

## Troubleshooting

### Common Issues:

1. **mysqlclient installation error**:
   - Windows: Install Microsoft Visual C++ Build Tools
   - Linux: Install python3-dev and mysql development headers
   - macOS: Install mysql-client via Homebrew

2. **Connection refused**:
   - Make sure MySQL server is running
   - Check if MySQL is listening on correct port (default: 3306)

3. **Access denied**:
   - Verify MySQL user credentials
   - Ensure user has privileges on the database

4. **Character encoding issues**:
   - The setup uses utf8mb4 for full Unicode support
   - Make sure your MySQL server supports utf8mb4

## Database Configuration

The Django app is configured to use:
- **Database Engine**: MySQL
- **Character Set**: utf8mb4 (supports emojis and special characters)
- **Collation**: utf8mb4_unicode_ci (case-insensitive Unicode sorting)

## Environment Variables

All sensitive configuration is loaded from `.env` file:
- Database credentials
- Django secret key
- Debug mode setting

Never commit `.env` file to version control!
