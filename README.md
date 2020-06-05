# Voicy 

Voicy is console program for organising your life using records that will be played at right time

## Table of Contents

- [Description](#description)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [Repo_structure](#repo_structure)
- [License](#license)

## Description

Voicy is used for saving records of your voice and corresponding text or warnings, records are recodred within Voicy and will be played at time which you set.

### Using Voicy

Download repository and go to the project folder
To launch program write:
    `python3 main.py`

There are such commands:
- n - means "new", press n to create new note
- w - means "watch", press w to see note description and play appropriate record
- d - means "delete", press d to delete note
- q - means "quit", press q to exit program
- ? - press ? to see help  

## Dependencies

Program uses such libraries:
- Pyaudio ~= 0.2.11
- wave ~= 0.0.2
- numpy ~= 1.18.4
- threading (standard lib)
- time (standard lib)
- os (standard lib)

Before using Voicy you should be confident that you have above modules

## Contributing

Feel free to contibute this project.
Text me your ideas and suggestions to develop Voicy

## Repo_structure

Repo has these files:
- main.py (main file of program, provides program interface and connections between all libraries)
- Stream.py (module that includes functions playvoice() and recordvoice())
- essential.txt (text file that helps to store data about records, so that program keeps your past notes)
- requirements.txt (file with dependecies)
- test.py (test for travis ci)
- LICENSE (MIT License for project)
- directory Records (This is a directory where all records are holding)

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- My telegram @Vladlinu
- Copyright 2020 © <a href="https://github.com/vladlinu" target="_blank">Vladlinu</a>.
