todo_list = []

d1 = {
    'id': 1684,
    'item': 'item1'
}

# Create
# d1을 리스트에 추가
todo_list.append(d1)
print(todo_list)

d2 = {
    'id': 29681,
    'item': 'item2'
}
todo_list.append(d2)
print(todo_list)

# Read
# id가 29681인 것의 딕셔너리 출력
for todo in todo_list:
    if todo.get('id') == 29681:
        print(todo)

# Update
# id가 29681인 것의 item을 '아이템2'로 바꾼뒤 todo_list 출력
for todo in todo_list:
    if todo.get('id') == 29681:
        todo['item'] = '아이템2'
print(todo_list)


# Delete
# id가 29681인 것의
# index를 찾아내고
# pop으로 해당 index를 지우세요
for i in range(len(todo_list)) :
    print('i', i)
    if todo_list[i].get('id') == 29681:
        todo_list.pop(i)
        break
print(todo_list)

todo_list = [ todo for todo in todo_list if todo['id'] != 29681 ]
print('-'*30)
print(todo_list)


# 할 일
# crud.py
# todo_list에 CRUD하는 라우터를 설정하고
# api.py를 실행해서 테스트하기

# 이케이케 해도 되고
# /crud/c
# /crud/r
# /crud/u
# /crud/d

# 이렇게 할 수 있을까요?
# /crud [GET, POST, PUT, DELETE]

