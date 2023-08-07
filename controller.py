import model
import text
import view


def run():
    while True:
        choice = view.main_menu()

        match choice:
            case 1:
                if model.notes_book:
                    view.print_message(text.nb_is_open)
                else:
                    model.open_nb()
                    view.print_message(text.load_nb)
            case 2:
                model.save_nb()
                view.print_message(text.nb_saved)
            case 3:
                nb = model.notes_book
                view.print_nb(nb)
            case 4:
                model.add_note(view.input_note())
            case 5:
                nb = model.search_note(view.input_search(text.search_note))
                if nb:
                    view.print_nb(nb)
                else:
                    view.print_message(text.note_not_found)
            case 6:
                nb = model.search_note(view.input_search(text.search_note))
                if nb:
                    view.print_nb(nb)
                    if len(nb) != 1:
                        index = input(text.input_id)
                        view.print_message(model.change_note(index))
                    else:
                        view.print_message(model.change_note(nb[0].get('id')))
                else:
                    view.print_message(text.note_not_found)
            case 7:
                nb = model.search_note(view.input_search(text.search_note))
                if nb:
                    view.print_nb(nb)
                    if len(nb) != 1:
                        index = input(text.input_id)
                        view.print_message(text.del_note(model.delete_note(index)))
                    else:
                        view.print_message(text.del_note(model.delete_note(nb[0].get('id'))))
                else:
                    view.print_message(text.note_not_found)
            case 8:
                break
