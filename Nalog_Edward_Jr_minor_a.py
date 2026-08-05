# Notepad System (Authentication, Authorization, and CRUD)
from prettytable import PrettyTable
from datetime import datetime
import os

users:list['User'] = []   
note_list:list['Notepad'] = []
current_user = None
is_logged_in = False

class User:
    def __init__(self, full_name, username, password):
        self.full_name = full_name
        self.username = username
        self.password = password

    def __repr__(self):
        return f'{self.full_name=}, {self.username=}, {self.password=}'
    
class Notepad():
    def __init__(self, owner, title, description, date_created):
        self.owner = owner
        self.title = title
        self.description = description
        self.date_created = date_created

    def __repr__(self):
        return f'By: {self.owner}\n\t\t{self.title}\n{self.description}\nLast Updated: {self.date_created}'

def show_menu(has_account = False):
    if has_account:
        print("""
[0] Logout
[1] List Notes
[2] Create Note
[3] Update Note
[4] Delete Note
[5] Describe Note
""")
        return
    print("""
[0] Exit
[1] Login
[2] Register
""")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def prompt(string, cast=str):
    """Inputs are casted into specific datatype to avoid error"""
    value = input(f"{string}: ").strip()
    return cast(value)


def find_user(username):
    for user in users:
        if user.username == username:
            return user


def find_note(notepad):
    global current_user
    for note in note_list:
        if note.title == notepad:
            if note.owner == current_user:
                return note


def list_notes():
    global current_user
    index = 0

    print("""
        NOTE LISTS:
""")

    if not note_list:
        print("No list yet")
        return
    # print("Note List:")
    note_list_table = PrettyTable(title="Note List", field_names=["Index", "Title", "Date Created"])
    for note in note_list:
        index += 1
        if note.owner == current_user:
            note_list_table.add_row((index, note.title, note.date_created))
    print(note_list_table)


def describe_note():
    clear_screen()
    list_notes()
    note = find_note(prompt("Note Title"))
    clear_screen()
    print(note)

def update_note():
    list_notes()
    note = find_note(prompt("Note Title"))
    nt = prompt("New Title (Leave Blank to Stay Unchanged)")
    if nt != '':
        note.title = nt
    nd = prompt("New Description (Leave Blank to Stay Unchanged)")
    if nd != '':
        note.description = nd
    clear_screen()


def delete_note():
    # use .remove()
    list_notes()
    choice = prompt("Choose which Item to Remove (By Number)", int)
    confirm = prompt("Are you sure? y/n")
    if confirm == 'y':
        note_list.remove(note_list[choice-1])
        clear_screen()
        print("Note Deleted.")
    elif confirm == 'n':
        clear_screen()
        print("Deletion Cancelled.")
        return
    else:
        clear_screen()
        print("Invalid Input.")
    


def login():
    global is_logged_in
    global current_user

    clear_screen()

    print("""
        LOG-IN
""")
    us = find_user(prompt("User"))
    if us is None:
        clear_screen()
        print("User does not exist")
        return
    pw = prompt("Password")
    if us.password != pw:
        clear_screen()
        print("Wrong Password")
        return
    clear_screen()
    current_user = us.username
    is_logged_in = True

    
def register():
    global current_user

    clear_screen()

    print("""
        REGISTER
""")

    un = prompt("Full Name")
    us = prompt("User")
    if find_user(us) is None:
        pw = prompt("Password")
        cw = prompt("Confirm Password")
        if pw != cw:
            clear_screen()
            print("Password does not match.")
            return None
    else:
        clear_screen()
        print("User Already Exists.")
        return
    users.append(User(un, us, pw))
    clear_screen()


def create_note():
    global note_list

    clear_screen()
    print("""
        CREATE NOTE
""")
    note_title = prompt("Title")
    note_description = prompt("Description")
    date_created = datetime.now()
    note_list.append(Notepad(current_user, note_title, note_description, date_created.strftime("%Y-%m-%d %H:%M:%S")))
    clear_screen()


def match_choice(choice, has_account = False):
    global is_logged_in
    global current_user

    if has_account:
            match choice:
                case '0':
                    is_logged_in = False
                    current_user = None
                case '1':
                    list_notes()
                case '2':
                    create_note()
                case '3':
                    update_note()
                case '4':
                    delete_note()
                case '5':
                   describe_note()
                case _:
                    print("Invalid Input")
    else:
        match choice:
            case '0':
                return True
            case '1':
                login()
            case '2':
                register()
            case _:
                print("Invalid Input")



def main():
    clear_screen()
    while True:
        show_menu(is_logged_in)
        choice = prompt("Choice")
        clear_screen()
        y = match_choice(choice, is_logged_in)
        if y is True:
            break
        """
        yey
        """

                
if __name__ == "__main__":
    main()