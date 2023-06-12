from fastapi import FastAPI
from models import session,User


app=FastAPI()

@app.get('/')
def hello():
    return {"details":"hello welcome to fastapi"}

@app.get('/users')
def all_users():
    users=session.query(User).all()
    return users