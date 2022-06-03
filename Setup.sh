#!/bin/bash

echo "===== FraUAS Notes Setup ====="
echo 
echo "This setup will install IntelliJ IDEA,"
echo "JRE, python and PyCharm Community for you."
echo
echo "===== FraUAS Notes Setup ====="
echo 

read -p "Are you sure you want to continue? [Y/n] " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
	echo "Exiting.."
	exit 1
fi

if [[ $USER == "root" ]]
then
    echo "Please do NOT run as root!"
    exit 1
fi

# System update
sudo apt update
sudo apt install git -y
git clone https://github.com/meowosaurus/FraUASNotes /home/$USER/Documents/FraUASNotes
sudo chown $USER:$USER /home/$USER/Documents/FraUASNotes -R

# Java/IntelliJ/Server
sudo apt install default-jre -y
read -p "Do you want to install IntelliJ IDEA (Community)? [Y/n] " -n 1 -r
echo 
if [[ $REPLY =~ ^[Yy]$ ]]
then
	echo "Installing IntelliJ IDEA.."
	snap install intellij-idea-community --classic
fi

# Python/PyCharm/Client
sudo apt install software-properties-common build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev -y
sudo apt install python3 -y
sudo apt install pip -y
read -p "Do you want to install PyCharm IDE (Community)? [Y/n] " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
	echo "Installing PyCharm IDE.."
	sudo snap install pycharm-community --classic
fi

# Installing python packages
python3 -m pip install requests
python3 -m pip install pyside6

echo "Installation complete, exiting.."
exit 1
