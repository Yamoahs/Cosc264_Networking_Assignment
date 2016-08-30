#!/bin/sh
gnome-terminal -e reciever_basic.py 1234 1235 sender.txt
gnome-terminal -e sender_basic.py 1234 1235 input.txt

