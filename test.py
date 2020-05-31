import time
import os
import Stream as St
import threading

unused_notes = ["Do homeor"]
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

queue = Queue_of_records()
while True:
    file = open("essential.txt")
    for record in file:
        info_date_list = record.split(":")
        name_of_note = info_date_list[0]
        if (name_of_note in unused_notes):
            date = info_date_list[2].split(" ")
            current_date = time.ctime().split(" ")
            print(current_date[2] == date[0])
            print(current_date[3][0:2] == date[1])
            print(current_date[3][3:5] == date[2])
            print(current_date[4] == date[3])
            if (current_date[2] == date[0])&(
            current_date[3][0:2] == date[1])&(
            current_date[3][3:5] == date[2])&(
            str(current_date[4]) == str(date[3]).strip()):
                print("Done")
                queue.add_record(str(name_of_note))
                unused_notes.remove(name_of_note)
    file.close()
    time.sleep(1)
    print(queue.queue)
