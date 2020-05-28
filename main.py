import os
import time
import Stream as St
import threading

notes = []
can_i_play = True

class Queue_of_records():
    def __init__(self):
        self.queue = []
        self._lock = threading.Lock()

    def add_record(self, name):
        with self._lock:
            self.queue.append(name)

    def get_record(self):
        with self._lock:
            return self.queue.pop(0)

    def is_empty(self):
        with self._lock:
            if (len(self.queue) == 0):
                return True
            else:
                return False

def daemon_adding(queue):

    while True:
        file = open("essential.txt")
        for record in file:
            info_date_list = record.split(":")
            name_of_note = info_date_list[0]
            if (name_of_note in unused_notes):
                date = info_date_list[2].split(" ")
                current_date = time.ctime().split(" ")
                if (current_date[2] == date[0])&(
                current_date[3][0:2] == date[1])&(
                current_date[3][3:5] == date[2])&(
                current_date[4] == date[3].strip()):
                    queue.add_record(str(name_of_note))
                    unused_notes.remove(name_of_note)
        file.close()

def daemon_playing(queue):
    while True:
        if (can_i_play):
            while (queue.is_empty() == False):
                record = queue.get_record()
                St.play_voice(str(record))


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
    can_i_play = False

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
    can_i_play = True

def delete_note():
    can_i_play = False
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
        can_i_play = True
    else:
        print("Incorrect name of note!")
        can_i_play = True

def main():
    queue_rec = Queue_of_records()
    daemon_add_notes = threading.Thread(target=daemon_adding, args=(queue_rec,), daemon=True)
    daemon_play_notes = threading.Thread(target=daemon_playing, args=(queue_rec,), daemon=True)
    daemon_add_notes.start()
    daemon_play_notes.start()
    while True:
        print_title()
        com = input("\n")

        if (com == "n"):
            add_note()
        elif (com == "d"):
            delete_note()
        elif (com == "q"):
            os.system("clear")
            exit(0)

try:
    open_notes()
    main()
except TypeError:
    exit(0)
