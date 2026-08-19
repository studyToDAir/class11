from fastapi import FastAPI, Request, HTTPException

from todo import todo_router
from crud import crud_router

app = FastAPI()

# 크로스 도메인 CORS 해결 코드
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get('/')
def welcome() -> dict :
    return {
        "message": "Hello World2"
    }

app.include_router(todo_router)
# app.include_router(crud_router, prefix='/crud')
app.include_router(crud_router, prefix='/api/v1')
app.include_router(crud_router)

@app.get('/ip')
def test(req : Request):
    ip = req.client.host
    print(ip)

    return ip

@app.get('/err')
def err():
    print('/err 실행')

    raise HTTPException(
        status_code=403,
        detail="글씨 아무거나 asdofihweo"
    )

@app.get('/html')
def html():
    return "<h1>hello world</h1>"

print(1, __name__)

if __name__ == "__main__":
    print('api.py 파일 직접 실행')

    import uvicorn
    uvicorn.run("api:app", port=8000, reload=True, host="0.0.0.0")

