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


if [[ $OSTYPE == "Darwin"* ]]
then
	echo "Detected MacOS"

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
	git clone https://github.com/meowosaurus/FraUASNotes /Users/$USER/Documents/FraUASNotes
	
	# Install requirements
	pip3 install -r /Users/$USER/Documents/FraUASNotes/requirements.txt
	
	echo "Installation complete, exiting.."
	exit 1	
	
# Is using apt repo manager? => Debian/Ubuntu/Pop?
elif command -v apt &> /dev/null
then
	echo "Detected Debian/Ubuntu"
	
	# Is the user running this script as root?
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

	# Java
	sudo apt install default-jre -y

	# Python
	sudo apt install software-properties-common build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev -y
	sudo apt install python3 -y
	sudo apt install pip -y
	
	# Check if snap store is installed
	if ! command -v snap &> /dev/null
	then
		# Should we install snapd?
		read -p "Do you want to install snap store (needed for automatic installation of IntelliJ IDEA and PyCharm IDE? [Y/n] " -n 1 -r
		echo 
		if [[ $REPLY =~ ^[Yy]$ ]]
		then
			echo "Installing snap store.."
			sudo apt install snapd
			echo "Please reboot or logout now and use the installer again!"
			exit 1
		fi
	else # if snap is available
		# Should we install IntelliJ IDEA?
		read -p "Do you want to install IntelliJ IDEA (Community)? [Y/n] " -n 1 -r
		echo 
		if [[ $REPLY =~ ^[Yy]$ ]]
		then
			echo "Installing IntelliJ IDEA.."
			snap install intellij-idea-community --classic
		fi
		
		# Should we install PyCharem IDE?
		read -p "Do you want to install PyCharm IDE (Community)? [Y/n] " -n 1 -r
		echo
		if [[ $REPLY =~ ^[Yy]$ ]]
		then
			echo "Installing PyCharm IDE.."
			sudo snap install pycharm-community --classic
		fi
	fi

	# Installing python packages
	pip3 install -r /home/$USER/Documents/FraUASNotes/requirements.txt

	echo "Installation complete, exiting.."
	exit 1

# Is using dnf repo manager? => RedHat/Fedora/CentOS
elif command -v dnf &> /dev/null
then
	echo "Detected RedHat/Fedora/CentOS"
	
	# Is the user running this script as root?
	if [[ $USER == "root" ]]
	then
    		echo "Please do NOT run as root!"
    		exit 1
	fi
	
	# Update system and install git
	sudo dnf update
	sudo dnf install git -y

	# Clone repo
	git clone https://github.com/meowosaurus/FraUASNotes /home/$USER/Documents/FraUASNotes
	sudo chown $USER:$USER /home/$USER/Documents/FraUASNotes -R
	
	sudo dnf install java-latest-openjdk -y 
	
	# Install python packages
	sudo dnf install g++ cmake python3 pip -y
	
	# Check if snap store is installed
	if ! command -v snap &> /dev/null
	then
		# Should we install snapd?
		read -p "Do you want to install snap store (needed for automatic installation of IntelliJ IDEA and PyCharm IDE? [Y/n] " -n 1 -r
		echo 
		if [[ $REPLY =~ ^[Yy]$ ]]
		then
			echo "Installing snap store.."
			sudo dnf install snapd
			sudo ln -s /var/lib/snapd/snap /snap
			echo "Please reboot or logout now and use the installer again!"
			exit 1
		fi
	else # if snap is available
		# Should we install IntelliJ IDEA?
		read -p "Do you want to install IntelliJ IDEA (Community)? [Y/n] " -n 1 -r
		echo 
		if [[ $REPLY =~ ^[Yy]$ ]]
		then
			echo "Installing IntelliJ IDEA.."
			snap install intellij-idea-community --classic
		fi
		
		# Should we install PyCharem IDE?
		read -p "Do you want to install PyCharm IDE (Community)? [Y/n] " -n 1 -r
		echo
		if [[ $REPLY =~ ^[Yy]$ ]]
		then
			echo "Installing PyCharm IDE.."
			sudo snap install pycharm-community --classic
		fi
	fi
	
	# Installing python packages
	pip3 install -r /home/$USER/Documents/FraUASNotes/requirements.txt
	
	echo "Installation complete, exiting.."
	exit 1
fi

