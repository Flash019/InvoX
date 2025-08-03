from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from backend.database import collection
from backend.hashing import Hash
from backend import token

router = APIRouter(tags=["Authentication"])

@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends()):
    user = collection.find_one({"email": request.username})
    if not user:
        raise HTTPException(status_code=404, detail="Invalid Credentials")
    if not Hash.verify(user["password"], request.password):
        raise HTTPException(status_code=400, detail="Incorrect password")
    access_token = token.create_access_token(data={"sub": user["email"]})
    return {"access_token": access_token, "token_type": "bearer"}
