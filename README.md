# FraUASNotes

A python based qt application to write and sync notes to a java server via Rest API with [Spring](https://spring.io/)

## Content

- [Overview](#overview)
- [Getting started](#getting-started)
- [Usage](#usage)
- [Development team](#development-team)

## Getting started

### Prerequsites 

You should have the following things installed:
- Python 3.8
- Java JDK 1.7
- git

You also need the following IDEs:
- [PyCharm](https://www.jetbrains.com/pycharm/)
- [IntelliJ (Community)](https://www.jetbrains.com/idea/)

### Linux & Mac Installer
1. Run the installer script with: ```bash <(curl -fsSL https://raw.githubusercontent.com/meowosaurus/FraUASNotes/main/Setup.sh)``` (do NOT run as root!)
2. Setup [PyCharm IDE](#setup-pycharm-ide) and [IntelliJ IDE](#setup-intellij-ide-(community)) 

### Setup PyCharm IDE
1. Open folder ```client/``` as Project
2. Select Python 3.8 or higher as interpreter
3. Add new debug configuration -> Python
4. Set ```client/main.py``` as script path

### Setup IntelliJ IDE (Community)
1. Open folder ```server/``` as Project
2. Open file ```server/src/main/java/de/frauas/server/ServerApplication.java```in IntelliJ
3. Right click ```ServerApplication::main(String[] args)``` and click on Run

## Usage
1. Open ```client/``` with PyCharm IDE & open ```server/``` with IntelliJ IDE
2. First start the server, then the client

## Development team

### Active developers

- [Alicia Tichelaar](https://github.com/lizziti)
- [Hendrik Weichel](https://github.com/hendrikkwe)
- [Maximilian Rabe](https://github.com/Vynalys)
- [Björn Sonnen](https://github.com/meowosaurus)
