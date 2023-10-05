def load_all():
    try:
        with open('note.json', 'r') as file:
            notes = json.load(file)
            return notes
    except FileNotFoundError:
        return []