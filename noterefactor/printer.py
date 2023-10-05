def print_all(notes):
    if len(notes) == 0:
        print("Список пуст")
    else:
        for note in notes:
            print(f"ID: {note['id']}")
            print(f"Тема: {note['topic']}")
            print(f"Содержание: {note['content']}")
            print(f"Дата создания: {note['create_at']}")
            print(f"Дата последнего изменения: {note['update_at']}")
            print()