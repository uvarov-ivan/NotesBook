main_menu = '''\nГлавное меню:
    1. Открыть записную книгу
    2. Сохранить записную книгу
    3. Показать заметки
    4. Добавить заметку
    5. Найти заметку
    6. Изменить заметку
    7. Удалить заметку
    8. Выход\n
    -> '''

new_note = {'heading': 'Введите заголовок заметки -> ', 'note_body': 'Введите заметку -> '}

note_added = 'Заметка сохранена!'

nb_is_open = 'Записная книга уже открыта!'

load_nb = 'Записная книга открыта!'

nb_saved = 'Записная книга сохранена!'

search_note = 'Введите искомое слово -> '

change_note = 'Введите новую заметку -> '

input_id = 'Введите id нужной заметки -> '

note_changed = 'Заметка изменена!'

note_not_found = 'Заметка не найдена!'

def del_note (heading:str):
    return f'Заметка -= {heading}=- успешно удалена!'