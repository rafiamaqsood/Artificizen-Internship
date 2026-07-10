from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from datetime import datetime,timedelta ,timezone
from jose import JWTError, jwt
from database import SessionLocal
from models import User
from config import SECRET_KEY, ALGORITHM , ACCESS_TOKEN_EXPIRE_MINUTES

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/token"
)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire =datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire})
    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

def get_current_user(
    token: str = Depends(oauth2_scheme)
):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        username = payload.get("sub")
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )
    db = SessionLocal()
    user = db.query(User).filter(
        User.username == username
    ).first()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )
    return user

def require_admin(
    current_user = Depends(
        get_current_user
    )
):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admins only"
        )
    return current_user