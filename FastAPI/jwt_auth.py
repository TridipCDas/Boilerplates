from datetime import datetime, timedelta
from typing import Optional
from fastapi import FastAPI, status, HTTPException,Header
from pydantic import BaseModel
from jose import jwt, JWTError

SECRET_KEY = "f4f110eda8b37184243c674e6247f5aebb6f52aae722dc353b4e9c5752118539"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1

app = FastAPI()


class User(BaseModel):
    username : str
    password : str

#You can check with your DB here
REGISTERED_USERS=["JohnSnow"]

def create_access_token(data:dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta( minutes = 15)
    to_encode.update({"exp":expire})
    print('To-encode-data ::',to_encode)
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@app.post("/login")
async def login(user:User):
    data = user.dict()
    username = data['username']
    password = data['password']

    if username not in ["JohnSnow","Shannara"] and password!= "password":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token({"username":username},access_token_expires)

    return {"token": access_token}

@app.get("/view")
async def view_details(Authorization:Optional[str] = Header(None)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        token = Authorization.split()[1]
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("username")
        if username in REGISTERED_USERS:
            return {"message":" You are welcome to the site"}
        else:
            raise credentials_exception
    except JWTError:
        raise credentials_exception


#NOTE:Check  OAuth2PasswordBearer once.
"""
For generating the SECRET Key, type
openssl rand -hex 32

"""