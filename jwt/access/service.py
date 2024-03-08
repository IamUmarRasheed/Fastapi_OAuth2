from datetime import datetime, timedelta, timezone  # Importing necessary modules
from typing import Annotated  # Importing Annotated from typing
from fastapi import Depends, HTTPException, status  # Importing necessary modules from FastAPI
from fastapi.security import OAuth2PasswordBearer  # Importing OAuth2PasswordBearer for authentication
from model import TokenData, User, UserInDB  # Importing necessary data models
from data import fake_users_db  # Importing fake user database
from jose import jwt, JWTError  # Importing JWT functionality for token generation and verification
from passlib.context import CryptContext  # Importing CryptContext for password hashing

# Defining constants
SECRET_KEY = "090e3ba2a1d93d843715cb8cec50e1730e20991c62b04e7e249ef9b378d1490c"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Defining OAuth2 scheme for token authentication
oauth_scheme = OAuth2PasswordBearer(tokenUrl='token')

# Creating CryptContext instance for password hashing
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

# Function to hash password
def get_password_hash(password):
    return pwd_context.hash(password)

# Function to verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Function to retrieve user from database
def get_user(db, username):
    if username in db:
        user_dic = db[username]
        return UserInDB(**user_dic)

# Function to authenticate user
def authenticate_user(fake_db, username: str, password: str):
    user = get_user()
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
