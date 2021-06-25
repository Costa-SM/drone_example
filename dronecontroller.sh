#!/bin/bash

./connect_vpn.sh
sleep 5
python3 ./example.py
sleep 5
sudo killall openvpn -9
