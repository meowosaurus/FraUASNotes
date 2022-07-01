@ECHO OFF

:: ### MAIN ###

:: Check if Python is installed
python --version 2>NULL
if errorlevel 1 goto errNoPython

pip --version 2>NULL
if errorlevel 1 goto errNoPip

java 2>NULL
if errorlevel 1 goto errNoJDK

:: Install dependencies with pip
pip install -r ./requirements.txt
PAUSE
EXIT

:: ### MAIN END ###

:: Python not installed
:errNoPython
echo.
echo Error^: Python not installed. You can download it here: https://www.python.org/downloads/
PAUSE
EXIT

:: Pip not installed
:errNoPip
echo.
echo Error^: Pip not installed. Pip is included with Python, you might want to reinstall Python.
PAUSE 
EXIT

:: Java Developer Kit not installed
:errNoJDK
echo Error^: Java Developer Kit (JDK) not installed. You can download it here: https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html
PAUSE 
EXIT
