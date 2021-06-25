#!/bin/bash

#This is the script that handles the main objectives of this example. It first starts a connection to the VPN server, using the credentials provided, and then calls the program that controls the drone's flight.
#After the drone finishes it's routine, the script kills the VPN connection, and exits.

echo "Connecting to the VPN Server, please insert your credentials."
sudo -H gnome-terminal -- sudo openvpn --config client.ovpn --auth-user-pass credentials
sleep 5

python3 ./example.py
sleep 5
sudo killall openvpn -9
