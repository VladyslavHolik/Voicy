import os

def print_title():
    os.system("clear")

    print("\t************ Your notes **************")
    for note in notes:
        print("\n" + str(note))


notes = ["Do tasks", "Having a meeting at 14:00"]

def main():
    print_title()

try:
    main()
except TypeError:
    exit(0)
