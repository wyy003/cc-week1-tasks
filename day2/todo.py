import json
import sys
import os

TODO_FILE = 'todo.json'

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w', encoding='utf-8') as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

def add_todo(task):
    todos = load_todos()
    todos.append({'task': task, 'done': False})
    save_todos(todos)
    print(f"已添加：{task}")

def list_todos():
    todos = load_todos()
    if not todos:
        print("没有待办事项")
        return
    for i, todo in enumerate(todos, 1):
        status = '✓' if todo['done'] else ' '
        print(f"{i}. [{status}] {todo['task']}")

def done_todo(index):
    todos = load_todos()
    if 1 <= index <= len(todos):
        todos[index - 1]['done'] = True
        save_todos(todos)
        print(f"已完成：{todos[index - 1]['task']}")
    else:
        print("无效的编号")

def remove_todo(index):
    todos = load_todos()
    if 1 <= index <= len(todos):
        task = todos.pop(index - 1)
        save_todos(todos)
        print(f"已删除：{task['task']}")
    else:
        print("无效的编号")

if len(sys.argv) < 2:
    print("用法：python todo.py [add|list|done|rm] [参数]")
    sys.exit(1)

command = sys.argv[1]

if command == 'add' and len(sys.argv) > 2:
    add_todo(sys.argv[2])
elif command == 'list':
    list_todos()
elif command == 'done' and len(sys.argv) > 2:
    done_todo(int(sys.argv[2]))
elif command == 'rm' and len(sys.argv) > 2:
    remove_todo(int(sys.argv[2]))
else:
    print("无效的命令")
