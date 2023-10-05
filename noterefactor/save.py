def save_notes(notes):
    with open('note.json', "w") as file:
        json.dump(notes, file)