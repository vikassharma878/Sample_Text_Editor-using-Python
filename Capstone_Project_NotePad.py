'''
Text Editor - Notepad style application that can open, edit, and save text documents. 
'''


text_lines = []  # to hold the text content
filename = ""    # to track file name

def show_menu():
    print("\n===== Python Notepad =====")
    print("1. Open File")
    print("2. Create New File")
    print("3. Edit Text")
    print("4. Save File")
    print("5. View Current Content")
    print("6. Exit")



def file_open():
    global text_lines, filename
    filename = input("Enter file name to open: ")
    try:
        with open(filename,'r') as f:
            text_lines = f.readlines()
            print(f"✅ file {filename} opened succesfully")
    except FileNotFoundError:
        print(f"❌ file {filename} not found")



def create_new_file():
    global text_lines,filename
    filename = ""
    text_lines = []
    print(f"✅ file {filename} created succesfully")



def edit_text():
    global text_lines
    print("💬 Start typing your text. Type '::end' on a new line to stop editing.")
    while True:
        line = input()
        if line.strip() == '::end':
            break
        text_lines.append(line + "\n")
    print("✅ Editing complete")


def save_file():
    global text_lines,filename
    if not filename:
        filename = input("Save file as filename: ")
    with open(filename,'w') as f:
        f.writelines(text_lines)
    print(f"💾 File saved as '{filename}' successfully!")


def view_content():
    print("\n===== Current File Content =====")
    if not text_lines:
        print("Not any content")
    else:
        for i,line in enumerate(text_lines,1):
            print(f"{i} :{line}", end= " ")


while True:
    show_menu()
    choice = input("Enter choice: ")
    if choice == "1":
        file_open()
    elif choice =="2":
        create_new_file()
    elif choice == "3":
        edit_text()
    elif choice =="4":
        save_file()
    elif choice =="5":
        view_content()
    elif choice =="6":
        print("Exiting GoodBye!!...")
        break
    else:
        print("Invalid Choice")
        choice = input("Enter choice: ")

