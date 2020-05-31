# Voicy 

Voicy is console program for organising your life using records that will be played at right time

## Dependencies

Program uses such libraries:
+ Pyaudio
+ wave
+ threading
+ time
+ os

Before using Voicy you should be confident that you have above modules

## Using Voicy

Download repository and go to the project folder
To launch program write:
    `python3 main.py`

There are such commands:
- n - means "new", press n to create new note
- w - means "watch", press w to see note description and play appropriate record
- d - means "delete", press d to delete note
- ? - press ? to see help    

## Repository structure

Repo has these files:
* main.py (main file of program, provides program interface and connections between all libraries)
* Stream.py (module that includes functions playvoice() and recordvoice())
* essential.txt (text file that helps to store data about records, so that program keeps your past notes)
* directory Records (This is a directory where all records are holding)
