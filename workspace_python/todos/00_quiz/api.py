import fastapi
app = fastapi.FastAPI()

from fastapi import FastAPI
app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get('/quiz/1/gugu')
def gugu(dan : int) :
    # dan = int(dan)
    print('dan', dan)
    for i in range(1, 10) :
        print(f'{dan}x{i}={dan*i}')

@app.get('/quiz/2/hap')
def gugu(x:int, y:int = 0) :
    print(f'x:{x}, y:{y}')
    print(x+y)

@app.get('/quiz/3/calc')
def gugu(x:int, y:int, op) :
    print(f'x:{x}, y:{y}, op:{op}')
    result = 0
    if op == "+" :
        result = x+y
    elif op == "-" :
        result = x-y
    elif op == "*" :
        result = x*y
    elif op == "/" :
        result = x/y

    print(result)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app")
