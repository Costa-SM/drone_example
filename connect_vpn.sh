#!/bin/bash

echo "Connecting to the VPN Server, please insert your credentials."
sudo -H gnome-terminal -- sudo openvpn --config client.ovpn --auth-user-pass credentials
