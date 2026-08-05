# Notepad System (Authentication, Authorization, and CRUD)
from prettytable import PrettyTable
from datetime import datetime
import os

users:list['User'] = []   
note_list:list['Notepad'] = []
current_user = None
is_logged_in = False

"""CLASSES"""
class User:
    def __init__(self, full_name, username, password):
        self.full_name = full_name
        self.username = username
        self.password = password

    def __repr__(self):
        return f'{self.full_name=}, {self.username=}, {self.password=}'

 
class Notepad():
    def __init__(self, owner, title, description, date_created, date_updated=""):
        self.owner = owner
        self.title = title
        self.description = description
        self.date_created = date_created
        self.date_updated = date_updated

    def __repr__(self):
        return f'By: {self.owner}\n\t\t{self.title}\n{self.description}\nLast Updated: {self.date_updated}'


"""HELPER FUNCTIONS"""
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
    try:
        return cast(value)
    except ValueError as e:
        return print(f'{e}: Value should be a {cast}.')


def index_correction(index):
    """Grabs the right item from note_list"""
    user_notes = [note for note in note_list if note.owner == current_user]
    if index is None:
        return
    
    if index < 1 or index > len(user_notes):
        print("Index Out of Range.")
        return None
    
    return user_notes[index-1]


"""NOTES MANIPULATORS"""
def find_user(username):
    for user in users:
        if user.username == username:
            return user


def find_note(notepad):
    """Finds a notepad from the current user"""
    global current_user
    for note in note_list:
        if note.owner == current_user:
            if note.title == notepad:
                return note

    
def list_notes():
    """List all notes from the current user"""
    global current_user
    index = 0
    
    has_list = False
    note_list_table = PrettyTable(title="Note List", field_names=["Index", "Title", "Date Created", "Date Updated"])
    for note in note_list:
        if note.owner == current_user:
            index += 1
            note_list_table.add_row((index, note.title, note.date_created, note.date_updated))
            has_list = True
    if has_list:
        print(note_list_table)
        return True
    print("No list yet.")
    return False


def create_note():
    """Notes created will only be accessible by the owner who made it"""
    global note_list

    clear_screen()
    print("""
        CREATE NOTE
""")
    note_title = prompt("Title")
    note_description = prompt("Description")
    date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note_list.append(Notepad(current_user, note_title, note_description, date_now, date_updated=date_now))
    clear_screen()


def update_note():
    """List the available notes for user to pick from and update note based on number"""
    if not list_notes():
        return
    choice = prompt("Choose which Note to Update (By Number)", int)
    match choice:
        case '':
            return "Invalid Input."
    note = index_correction(choice)
    if note is None:
        return
    note = index_correction(choice)
    
    nt = prompt("New Title (Leave Blank to Stay Unchanged)")
    if nt != '':
        note.title = nt
    nd = prompt("New Description (Leave Blank to Stay Unchanged)")
    if nd != '':
        note.description = nd
    note.date_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    clear_screen()


def delete_note():
    """List the available notes for user to pick from and delete note based on number"""
    
    if not list_notes():
        return

    choice = prompt("Choose which Item to Remove (By Number)", int)
    match choice:
        case '':
            return "Invalid Input."
    note = index_correction(choice) 
    if note is not None:
        confirm = prompt("Are you sure? y/n").lower()
        if confirm == 'y':
            note_list.remove(note)
            clear_screen()
            print("Note Deleted.")
        elif confirm == 'n':
            clear_screen()
            print("Deletion Cancelled.")
            return
        else:
            clear_screen()
            print("Invalid Input.")
    else:
        clear_screen()
        print("Index out of range.")    


def describe_note():
    """List the available notes for user to pick from and show the content of a note based on number"""
    clear_screen()
    if not list_notes():
        return
    choice = prompt("Choose which Note to Open (By Number)", int)
    clear_screen()
    note = index_correction(choice)
    if note is None:
        return 
    print(note)


"""USER FUNCTIONS"""
def login():
    global is_logged_in
    global current_user

    clear_screen()
    if not users:
        print("No Users in List.")
        return
    print("""
        LOG-IN
""")
    us = find_user(prompt("User"))
    if us is None:
        clear_screen()
        print("User does not exist.")
        return
    pw = prompt("Password")
    if us.password != pw:
        clear_screen()
        print("Wrong Password.")
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
                    print("Invalid Input.")
    else:
        match choice:
            case '0':
                return True
            case '1':
                login()
            case '2':
                register()
            case _:
                print("Invalid Input.")


"""MAIN LOOP"""
def main():
    clear_screen()
    while True:
        print(f'\nCurrent User: {current_user}')
        show_menu(is_logged_in)
        choice = prompt("Choice")
        clear_screen()
        y = match_choice(choice, is_logged_in)
        if y is True:
            break

                
if __name__ == "__main__":
    main() 