#!/bin/sh
gnome-terminal -e python3 "reciever_basic.py 1234 1235 sender.txt"
gnome-terminal -e python3 "sender_basic.py 1234 1235 input.txt"

