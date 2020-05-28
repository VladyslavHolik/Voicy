import os
import time
import Stream as St

notes = []

def print_title():
    os.system("clear")

    print("\t************ Your notes **************")
    for note in notes:
        print("\n\t" + str(note))

def open_notes():
    file = open("essential.txt")
    for line in file:
        info = line.split(":")
        notes.append(info[0])
    file.close()

def add_note():
    os.system("clear")
    bool = True
    name = None
    desc = None
    time = None

    while (bool):
         print("Add name of note\n")
         name = input("")
         os.system("clear")
         print("Write some description")
         desc = input("")
         os.system("clear")
         print("Write time in format [day hours minutes year]")
         time = input("")
         os.system("clear")
         print("Everything alright? [y,n]\n")
         print(name)
         print(desc)
         print(time)
         if (input("") == 'y'):
             bool = False
    print("Hit enter to start recording")
    input("")
    St.record_voice(name)
    os.system("clear")
    print("\nPlay new voice message [y]\n")
    if (input("") == "y"):
        St.play_voice(name)
    file = open("essential.txt", "a")
    file.write(name + ":" + desc + ":" + time + "\n")
    file.close()
    notes.append(name)

def delete_note():
    os.system("clear")
    print("Deleting note:\n")
    print("Enter full name of note to delete:")
    name = input("")
    if (name in notes):
        del notes[notes.index(name)]

        file = open("essential.txt", "r")
        lines = []
        for line in file:
            if (line.startswith(name) == False):
                lines.append(line)
        file.close()

        file = open("essential.txt", "w")
        for line in lines:
            file.write(line)
        file.close()

        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "./Records/" + name + ".wav")
        os.remove(path)
    else:
        print("Incorrect name of note!")

def main():
    while True:
        print_title()
        com = input("\n")

        if (com == "n"):
            add_note()
        elif (com == "d"):
            delete_note()
        elif (com == "q"):
            exit(0)
try:
    open_notes()
    main()
except TypeError:
    exit(0)
