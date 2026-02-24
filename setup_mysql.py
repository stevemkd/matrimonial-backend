#!/usr/bin/env python3
"""
MySQL setup script for Django matrimonial app
Run this script to create the database and user
"""

import mysql.connector
from mysql.connector import Error
import getpass

def setup_mysql_database():
    print("MySQL Database Setup for Django Matrimonial App")
    print("=" * 50)
    
    # Get MySQL credentials from user
    try:
        print("\nPlease enter your MySQL credentials:")
        host = input("Host (default: localhost): ") or 'localhost'
        user = input("Username (default: root): ") or 'root'
        password = getpass.getpass("Password: ")
        
        # Connect to MySQL server (without specifying database)
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS matrimonial_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            print("✓ Database 'matrimonial_db' created or already exists")
            
            # Create user if it doesn't exist (optional - you can use root)
            cursor.execute("CREATE USER IF NOT EXISTS 'django_user'@'localhost' IDENTIFIED BY 'django_password'")
            cursor.execute("GRANT ALL PRIVILEGES ON matrimonial_db.* TO 'django_user'@'localhost'")
            cursor.execute("FLUSH PRIVILEGES")
            print("✓ User 'django_user' created with privileges")
            
            cursor.close()
            connection.close()
            
            print("\n" + "=" * 50)
            print("✅ MySQL setup completed successfully!")
            print("\nDatabase Configuration:")
            print(f"  Host: {host}")
            print(f"  Database: matrimonial_db")
            print(f"  User: django_user")
            print(f"  Password: django_password")
            print("\nNext steps:")
            print("1. Update your .env file with these credentials")
            print("2. Run: python manage.py migrate")
            print("=" * 50)
            
    except Error as e:
        print(f"\n❌ Error: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure MySQL server is installed and running")
        print("2. Check your MySQL username and password")
        print("3. On Windows, MySQL might be running on XAMPP/WAMP")
        print("4. Try using 'root' with no password if you just installed MySQL")
        
        print("\nAlternative: Manual Database Setup")
        print("If this script doesn't work, you can manually create the database:")
        print("1. Open MySQL Workbench or phpMyAdmin")
        print("2. Run: CREATE DATABASE matrimonial_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
        print("3. Update your .env file with your MySQL credentials")

if __name__ == "__main__":
    setup_mysql_database()
