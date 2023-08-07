import datetime
import json

import text

notes_book: list[dict[str, str]] = []
file_name = 'notes.json'

def open_nb():
    global notes_book
    with open(file_name, 'r', encoding='UTF-8') as file:
        notes_book = json.load(file)


def save_nb():
    global notes_book

    with open(file_name, 'w', encoding='UTF-8') as file:
        json.dump(notes_book, file)


def add_note(new: dict[str,str]) -> str:
    global notes_book
    if len(notes_book) > 0:
        new_id = int(notes_book[-1].get('id')) + 1
        new['id'] = str(new_id)
    else:
        new['id'] = '1'
    new['time'] = datetime.datetime.now().strftime("%H:%M:%S %d.%m.%Y")
    notes_book.append(new)
    return text.note_added

def change_note(id: str) -> str:
    global notes_book
    for note in notes_book:
        if note.get('id') == id:
            note['note_body'] = input(text.change_note)
    return text.note_changed


def search_note(word: str) -> list[dict[str,str]]:
    global notes_book
    res: list[dict[str, str]] = []
    for note in notes_book:
        for field in note.values():
            if word.lower( ) in field.lower():
                res.append(note)
    return res

def delete_note(id: str) -> str:
    global notes_book
    for ind in enumerate(notes_book):
        if id == notes_book[ind[0]].get('id'):
            return notes_book.pop(ind[0]).get('heading')
