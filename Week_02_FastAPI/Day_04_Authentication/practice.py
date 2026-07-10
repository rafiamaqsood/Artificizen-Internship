from fastapi import FastAPI ,HTTPException, Depends, Header
from jose import jwt
from datetime import timedelta, datetime,timezone
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext

app= FastAPI()
#JWT config
SECRET_KEY="mysecret"
ALGORITHM ="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

#password hashing setup

pwd_context =CryptContext(schemes=["bcrypt"])


#Oauth setup

oauth2_schema=OAuth2PasswordBearer(tokenUrl="login")

# dummy user data
fake_user_db={
    "admin":{
        "username":"admin",
        "hashed_password":pwd_context.hash("!234")
    }
}

#hash password

def hash_password(password:str):
    return pwd_context.hash(password)

#verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

def create_token(data:dict):
    to_encode =data.copy()
    expire =datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({
        "exp": expire
    })
    token=jwt.encode(to_encode, SECRET_KEY, algorithm =ALGORITHM)
    return token

#Logi API (OAuth2 form)
@app.post("/login")
def login (form_data:OAuth2PasswordRequestForm=Depends()):
    user =fake_user_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
        status_code=400,
        detail="Invalid username or passowrd"
    )
    access_token=create_token({"sub":user["username"]})
    return{
        "access_token": access_token,
        "token_type":"bearer"
    }
    
def verify_token(token:str= Depends(oauth2_schema)):
    try:
        payload=jwt.decode(token, SECRET_KEY, algorithms =[ALGORITHM])
        username:str=payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )
        return username
    except jwt.JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

#protected route
@app.get("/protected")
def protected_route(username:str =Depends(verify_token)):
    return{
        "message":"you have access to this protected route",
        "user":username
    }

# #Logi API (Token Generate)
# @app.post("/login")
# def login (username:str , password:str):
#     if username!="admin" or password!="1234":
#         raise HTTPException(
#             status_code=401,
#             detail="Invalid usename or password"
#         )
#     token =create_token({
#         "sub":username
#     })
#     return{
#         "access_token" : token
#     }

#Token verify

# def verify_token(token:str= Header(None)):
#     try:
#         payload=jwt.decode(token, SECRET_KEY, algorithms =[ALGORITHM])
#         return payload
#     except:
#         raise HTTPException(
#             status_code=401,
#             detail="Invalid or expired token"
#         )
    
#protected route
# @app.get("/secure")
# def secure_data(user= Depends(verify_token)):
#     return{
#         "message": "Secure Data Accessed",
#         "user":user
#     }