# Port_Scanner.py
This is a basic Port Scanner written in python 3 that does the job and looks like it was written in the 90's for a website.
Port_Scanner.py is for educational purposes only 
DO NOT USE FOR MALICIOUS ACTIVITY!!!!
I WILL NOT BE HELD RESPONSIBLE FOR ANY DAMAGE CAUSED.

+Description+
Port_Scanner.py is meant to either be luanched from a terminal/command prompt or from $PATH
Port_Scanner.py is used to check open ports of ip address remotely

Dependencies
Port_Scanner.py uses the following modules 
os
sys
socket
colored
datetime
RUN "pip3 install socket, colored, datetime"in the terminal to make sure you have the latest versions.


LUANCH FROM TERMINAL
To luanch Port_Scanner.py from terminal go to the directory that's called 'Port_Scanner'
Then use the command "python3 Port-Scanner.py"

$Path(Linux)
to add Port_Scanner to PATH add the folder labeled 'Port_ScannerPATH'to your home directory
then open the terminal in the home directory and use 'sudo vi ~/.bashrc' or 'sudo vi ~/.zhsrc'
NOTE Kali Linux users use 'sudo vi ~/.bashrc'
then press "i" once the file opens in the terminal
then type in the following line underneath "# some more ls aliases" section the line underneath the last 'alias l='
export PATH="$PATH:/home/YOURUSERNAMEHERE/Port_ScannerPATH"
replace YOURUSERNAME with the username you use for your usr in linux
then go all the way to the bottom and click a line with no characters
ahd hit the following in order
"Esc" key (followed by) :wq 
do this to save the modified file 
now open a new terminal and repeat for root usr if on kali by first doing sudo su
now to check if it was done correctly type "echo $PATH" INTO A NEW TERMINAL WINDOW 
if somewhere you see /home/YOURUSERNAME/Port_ScannerPATH it is correct
Finally inside the code on line 23 of Port_Scanner.py change YOURUSERNAME to your username
now you can luanch Port_Scanner.py just by typing Port_Scanner.py

**I DID NOT CREATE PYTHON NOR ANY OF THE MODULES**
