import json
import datetime

def save_notes(notes):
    with open('notion.json', "w", encoding='utf-8') as file:
        json.dump(notes, file, ensure_ascii=False, indent=1)

def show_all():
    try:
        with open('notion.json', 'r', encoding='utf-8') as file:
            notes = json.load(file)
            return notes
    except FileNotFoundError:
        return []


def append_note():
    topic = input("Введите тему заметки: ")
    content = input("Введите содержание: ")
    created_date = datetime.date.today().strftime("%Y-%m-%d")
    created_time = datetime.datetime.now().time().strftime("%H:%M:%S")
    update_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    note = {
        'id': len(notes) + 1,
        'topic': topic,
        'content': content,
        'created_date': created_date, 
        'created_time': created_time,
        'update_at': update_at
    }

    notes.append(note)
    save_notes(notes)
    print("Заметка добавлена!")


def delete_note():
    note_id = int(input("Введите id для удаления: "))
    for note in notes: 
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print(f"Заметка №{note['id']} удалена")
            return
    print(f"Заметки с №{note['id']} не найдено")


def edit_note():
    note_id = int(input("Введине id заметки: "))
    for note in notes:
        if note['id'] == note_id:
            topic = input("Введите новый заголовок: ")
            content = input("Введите новое описание заметки: ")
            note['topic'] = topic
            note['content'] = content
            note['update_at'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print(f"Заметка №{note['id']} отредактирована")
            return
    print("Заметка не найдена")


def print_all(notes):
    if len(notes) == 0:
        print("Список пуст")
    else:
        for note in notes:
            print(f"ID: {note['id']}")
            print(f"Тема: {note['topic']}")
            print(f"Содержание: {note['content']}")
            print(f"Дата создания: {note['created_date']}")
            print(f"Время создания: {note['created_time']}")
            print(f"Дата последнего изменения: {note['update_at']}")
            print()


def select_notes():
    input_date = input("Введите дату (ГГГГ-ММ-ДД): ")
    try:
        date = datetime.datetime.strptime(input_date, "%Y-%m-%d")
        formatted_date = date.strftime("%Y-%m-%d")
        selected_notes = [note for note in notes if note['created_date'] == formatted_date]
        print_all(selected_notes)
    except ValueError:
        print("Дата введенна неправильно")


# entry point
notes = show_all()

while True:
    print("1. Вывести список заметок")
    print("2. Добавить заметку")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Выбрать заметки по дате")
    print("0. Выйти")
    
    choice = input("Выберите действие: ")
    
    if choice == '1':
        print_all(notes)
    elif choice == '2':
        append_note()
    elif choice == '3':
        edit_note()
    elif choice == '4':
        delete_note()
    elif choice == '5':
        select_notes()
    elif choice == '0':
        break
    else:
        print("Некорректный выбор, попробуйте ещё раз")

print("Работа с заметками завершена")