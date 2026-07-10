from fastapi import FastAPI ,Depends ,HTTPException
from database import engine, Base , get_db
from sqlalchemy.orm import Session
from models import User , UserRegister
from fastapi.security import OAuth2PasswordRequestForm
from security import verify_password ,hash_password
from auth import create_access_token , get_current_user , require_admin

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/auth/register")
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):
    # Check if username already exists
    existing_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    hashed_password = hash_password(user.password)

    new_user = User(
        username=user.username,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User Created"
    }
@app.post("/auth/token")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.username == form_data.username
    ).first()
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Wrong username or password"
        )
    if not verify_password(
        form_data.password,
        user.password
    ):
        raise HTTPException(
        status_code=401,
        detail="Wrong username or password"
    )
    
    token = create_access_token(
        {
            "sub": user.username,
            "role": user.role
        }
    )
    return {
        "access_token": token,
        "token_type": "bearer"
    }
@app.get("/users/me")
def get_me(
    current_user = Depends(
        get_current_user
    )
):
    return current_user

@app.delete("/users/{id}")
def delete_user(
    id: int,
    admin: User = Depends(require_admin),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == id).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    db.delete(user)
    db.commit()

    return {
        "message": "User deleted successfully"
    }