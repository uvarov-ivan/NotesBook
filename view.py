import text

def main_menu() -> int:
    while True:
        choice = input(text.main_menu)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)

def input_note() -> dict[str, str]:
    new = {}

    for key, txt in text.new_note.items():
        value = input(txt)
        if value:
            new[key] = value
    return new

def print_message(msg: str):
    print('\n' + '=' * len(msg))
    print(msg)
    print('=' * len(msg) + '\n')

def print_nb(nb: list[dict[str, str]]):

    for note in nb:
        print(f'{note.get("id"):>3} {note.get("heading"):<15} {note.get("note_body"):<20}')

def input_search(message) -> str:
    return input(message)