import os
import time
import threading
import Stream as St


notes = []
can_i_play = True
unused_notes = []

class QueueOfRecords():

    """queue of records, that should be played at this time"""
    def __init__(self):
        self.queue = []
        self._lock = threading.Lock()

    def add_record(self, name):
        """adding record with name"""
        with self._lock:
            self.queue.append(name)

    def get_record(self):
        """returns name of record to play"""
        with self._lock:
            return self.queue.pop(0)

    def is_empty(self):
        """checks if queue is empty"""
        with self._lock:
            return len(self.queue) == 0

def make_list_from_string(line):
    """function for creating info list for daemon_adding"""
    result = []
    sub_string = ""
    for index in range(0, len(line)):
        if line[index] != " ":
            sub_string += line[index]
            if index == len(line) - 1:
                result.append(sub_string)
        elif sub_string != "":
            result.append(sub_string)
            sub_string = ""
    return result

def daemon_adding(queue):
    """daemon which adds records to play"""
    unused_notes.extend(notes)

    while True:
        file = open("essential.txt")
        for record in file:
            info_date_list = record.split(":")
            name_of_note = info_date_list[0]
            if name_of_note in unused_notes:
                date = info_date_list[2].split(" ")
                current_date = make_list_from_string(time.ctime())
                if (current_date[2] == date[1])& \
                    (current_date[1] == date[0])& \
                    (current_date[3][0:2] == date[2])& \
                    (current_date[3][3:5] == date[3])& \
                    (current_date[4] == date[4].strip()):
                    queue.add_record(str(name_of_note))
                    unused_notes.remove(name_of_note)
        file.close()

def daemon_playing(queue):
    """daemon which plays records in queue"""
    while True:
        if can_i_play:
            while not queue.is_empty():
                record = queue.get_record()
                St.play_voice(str(record))


def print_title():
    """function for displaying head of note board"""
    os.system("clear")

    print("\t************ Your notes **************")
    for note in notes:
        print("\n\t" + str(note))

def open_notes():
    """function for initialising list notes from cache"""
    file = open("essential.txt")
    for line in file:
        info = line.split(":")
        notes.append(info[0])
    file.close()

def add_note():
    """function for adding new note"""
    can_i_play = False

    os.system("clear")
    uncorrect = True
    name = None
    desc = None
    time = None

    while uncorrect:
        print("Add name of note\n")
        name = input("")
        os.system("clear")
        print("Write some description")
        desc = input("")
        os.system("clear")
        print("Write time in format [Month day hours minutes year]")
        time = input("")
        os.system("clear")
        print("Everything alright? [y,n]\n")
        print(name)
        print(desc)
        print(time)
        if input("") == 'y':
            uncorrect = False
    print("Hit enter to start recording")
    input("")
    St.record_voice(name)
    os.system("clear")
    print("\nPlay new voice message [y]\n")
    if input("") == "y":
        St.play_voice(str(name))
    file = open("essential.txt", "a")
    file.write(name + ":" + desc + ":" + time + "\n")
    file.close()
    notes.append(name)
    unused_notes.append(name)
    can_i_play = True

def delete_note():
    """function for invoking interface for deleting note"""
    can_i_play = False
    os.system("clear")
    print("Deleting note:\n")
    print("Enter full name of note to delete:")
    name = input("")
    if name in notes:
        del notes[notes.index(name)]

        file = open("essential.txt", "r")
        lines = []
        for line in file:
            if not line.startswith(name):
                lines.append(line)
        file.close()

        file = open("essential.txt", "w")
        for line in lines:
            file.write(line)
        file.close()

        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), \
        "./Records/" + name + ".wav")
        os.remove(path)
        can_i_play = True
    else:
        print("Incorrect name of note!")
        can_i_play = True

def see_note():
    """function for seeing note and its desctiption with opportunity to listen record"""
    os.system("clear")
    name = input("Write name of note to watch\n\n")
    if name not in notes:
        print("\nInvalid name of note")
        time.sleep(1)
        return

    desc = ""
    file = open("essential.txt", "r")
    for line in file:
        if line.startswith(name):
            desc = line.split(":")[1]
    os.system("clear")
    print("\t" + name)
    print("\n" + desc)
    if input("\nDo you want to play this record? [y]\n\n") == "y":
        St.play_voice(name)

def print_help():
    """function print user help info"""
    os.system("clear")
    print("For adding note press n")
    print("For watching note press w, then write name of note to see")
    print("For deleting note press d, then write name of note to delete")
    print("For quiting program press q")
    input("")

def main():
    """main function that employs behavior of program"""
    queue_rec = QueueOfRecords()
    daemon_add_notes = threading.Thread(target=daemon_adding, args=(queue_rec,), daemon=True)
    daemon_play_notes = threading.Thread(target=daemon_playing, args=(queue_rec,), daemon=True)
    daemon_add_notes.start()
    daemon_play_notes.start()
    while True:
        print_title()
        com = input("\n")

        if com == "n":
            add_note()
        elif com == "d":
            delete_note()
        elif com == "w":
            see_note()
        elif com == "?":
            print_help()
        elif com == "q":
            os.system("clear")
            exit(0)

try:
    open_notes()
    main()
except TypeError:
    exit(0)
