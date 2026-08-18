from fastapi import FastAPI, Request

from todo import todo_router

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

@app.get('/ip')
def test(req : Request):
    ip = req.client.host
    print(ip)

    return ip

print(1, __name__)

if __name__ == "__main__":
    print('api.py 파일 직접 실행')

    import uvicorn
    uvicorn.run("api:app", port=8000, reload=True, host="0.0.0.0")

