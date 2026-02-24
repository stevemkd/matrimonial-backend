#!/usr/bin/env python3
"""
Generate a Django secret key for production use.
"""

import sys
import os
from django.core.management.utils import get_random_secret_key

def generate_secret_key():
    """Generate a new Django secret key."""
    secret_key = get_random_secret_key()
    print(f"Generated SECRET_KEY: {secret_key}")
    print("\nAdd this to your .env file:")
    print(f"SECRET_KEY={secret_key}")
    print("\nOr set it as an environment variable in Render.")

if __name__ == "__main__":
    generate_secret_key()
