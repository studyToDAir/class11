from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from todo import Todo

app = FastAPI()
templates = Jinja2Templates(directory='templates/')

todo_list = []
# # 임시 테스트 260821 todair@naver.com
# # TODO 생성페이지 완성 후 삭제
# todo = Todo(id=999, item='test')
# todo_list.append(todo)
# todo_list.append(todo)
# todo_list.append(todo)

@app.get('/list')
def list(request: Request) :
    print('/list')

    return templates.TemplateResponse(
        request, 
        'list.html',
        {
            'list': todo_list
        }
    )

@app.get('/add')
def add(request: Request) :
    print('/add 실행')
    return templates.TemplateResponse(
        request, 
        'add.html'
    )

@app.post('/api/add')
def apiAdd(todo:Todo = Form()):
    print('/api/add 실행')
    print('todo:', todo)

    todo_list.append(todo)

    return RedirectResponse(
        url='/list',
        status_code=303 # 303: 무조건 GET으로 다시 들어오게 한다
    )

@app.get('/detail/{id}')
def detail(request: Request, id:int):
    print('/detail/{id} 실행')
    print('id:', id)

    result = None
    for todo in todo_list:
        print(todo)
        if todo.id == id:
            result = todo

    print('result', result)
    return templates.TemplateResponse(
        request, 
        'detail.html',
        {
            'todo': result
        }
    )

@app.get('/update')
def detail(request: Request, id:int):
    print('/update')
    print('id', id)

    result = None
    for todo in todo_list:
        print(todo)
        if todo.id == id:
            result = todo

    print('result', result)
    return templates.TemplateResponse(
        request, 
        'update.html',
        {
            'todo': result
        }
    )

@app.post('/api/update')
def apiAdd(todo:Todo = Form()):
    print('/api/update 실행')
    print('todo:', todo)

    for t in todo_list:
        if t.id == todo.id:
            t.item = todo.item

    return RedirectResponse(
        # url='/detail/'+todo.id,
        url='/list',
        status_code=303 # 303: 무조건 GET으로 다시 들어오게 한다
    )

@app.post('/api/delete')
def apiAdd(todo:Todo = Form()):
    print('/api/delete 실행')
    print('todo:', todo)

    for i in range(len(todo_list)) :
        if todo_list[i].id == todo.id:
            todo_list.pop(i)
            break

    return RedirectResponse(
        # url='/detail/'+todo.id,
        url='/list',
        status_code=303 # 303: 무조건 GET으로 다시 들어오게 한다
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", port=8000, reload=True, host="0.0.0.0")
