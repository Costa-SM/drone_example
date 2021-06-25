# Drone Remote Control Example
Simple project to control a drone while connecting to a VPN, using the Parrot platforms, specifically, Olympe for control, and Sphinx for simulation. 
Made for the CSC-03 2021 class of the Aeronautics Institute of Technology.
Requires the installation of Olympe and Sphinx, and the files in this repository should be put inside the "code" folder created when following the installation instructions for Olympe.

The file client.ovpn must be generated via the administrator side of a OpenVPN server.
The file credentials must have the login and password required for logging in to the OpenVPN server.

This example IS NOT SUITABLE for real world scenarios, as it has several unencrypted files that contain private information. 
Therefore, the files in this repository are strictly for academic uses.

Drone flight routine copied from:
https://developer.parrot.com/docs/olympe/userguide.html
