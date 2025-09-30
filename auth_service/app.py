from fastapi import FastAPI, HTTPException, Form
from datetime import datetime, timedelta
from fastapi.middleware.cors import CORSMiddleware
import os, json, jwt, bcrypt

AUTH_SECRET = os.getenv("AUTH_SECRET","change-this-secret")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

def load_users():
    # users_seed.json должен лежать рядом с app.py внутри /app
    with open("users_seed.json","r", encoding="utf-8") as f:
        return {u["username"]: u for u in json.load(f)}

USERS = load_users()

def verify_password(plain: str, hashed: str) -> bool:
    # hashed ожидается в формате bcrypt: $2b$...
    return bcrypt.checkpw(plain.encode("utf-8"), hashed.encode("utf-8"))

@app.post("/token")
def login(username: str = Form(...), password: str = Form(...)):
    user = USERS.get(username)
    if not user or not verify_password(password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    payload = {
        "sub": username,
        "role_id": user.get("role_id", 0),
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    }
    token = jwt.encode(payload, AUTH_SECRET, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}

@app.get("/verify")
def verify(token: str):
    try:
        payload = jwt.decode(token, AUTH_SECRET, algorithms=[ALGORITHM])
        return {"valid": True, "payload": payload}
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
