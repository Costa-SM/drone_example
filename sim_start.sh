#!/bin/bash
#This script starts up the drone simulation that will be used.

sudo -H gnome-terminal -- firmwared
sphinx /opt/parrot-sphinx/usr/share/sphinx/drones/anafi4k.drone::stolen_interface=eth0:eth0:192.168.42.1/24
