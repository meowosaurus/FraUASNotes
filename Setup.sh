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

# Check if OS is Linux or Mac
case $(uname -s) in
	####################### Linux #######################
	Linux) 
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
	pip3 install -r /home/$USER/Documents/FraUASNotes/requirements.txt

	echo "Installation complete, exiting.."
	exit 1;;
	
	####################### MAC #######################
	Darwin) 
	if ! command -v brew &> /dev/null
	then
		echo "Homebrew in not installed! Please install it here: https://brew.sh/"
		exit 1
	fi
	
	# Update system and download basic packages
	brew update
	brew install git
	brew install gcc 
	brew install python
	brew install openjdk
	
	# Clone github repo
	git clone https://github.com/meowosaurus/FraUASNotes /home/$USER/Documents/FraUASNotes
	chown $USER:$USER /home/$USER/Documents/FraUASNotes
	
	# Install requirements
	pip3 install -r /home/$USER/Documents/FraUASNotes/requirements.txt
	
	echo "Installation complete, exiting.."
	exit 1;;
	
	####################### Unsupported OS #######################
	*) 
	echo "Unsupported operating system, please refer to the manual installation guide!"
	exit 1;;
esac

