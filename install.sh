#!/bin/bash
clear
echo "Hello,"
echo "please be sure you are connected to the internet..."
sleep 3
clear
read -p "Do you run install.sh as root?(y/n): " answer
if [ "$answer" == "n" ];then
	echo -e "\nI'll exit, run me again as root!"
	sleep 2
	exit
elif [ "$answer" == "y" ];then
	echo "Good!"
	sleep 1
	clear
else
	echo -e "[!] Wrong Input,\n Enter y for Yes or n for No!"
	echo "I will exit, but run me as root to resume installation"
	sleep 1
	read -p "press any key to continue..." null
	exit
fi
clear
echo "installing python modules."
pip3 install -r requirements.txt
clear
sleep 1
echo "Instalation Completed!"
sleep 1
clear
echo "Bye!"
sleep 1 
exit
