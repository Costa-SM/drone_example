# -*- coding: UTF-8 -*-

#This script handles the login GUI presented to the employee responsible for the drone, as well as the main routine for the drone's flight.
#The login routine uses unencrypted credentials, hard coded to the script in this example. In a real scenario, this would be substituted for a database managed by the company that offers the service.
#The routine for the drone was taken from the examples contained in the Olympe library.
#https://developer.parrot.com/docs/olympe/userguide.html


import olympe
import time
import subprocess
from olympe.messages.ardrone3.Piloting import TakeOff, Landing
from PySimpleGUI import PySimpleGUI as sg

DRONE_IP = "10.202.0.1"

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('User'), sg.Input(key='user')],
    [sg.Text('Password'),sg.Input(key='password', password_char='*')],
    [sg.Button('Login')]
]

def main():
    drone = olympe.Drone(DRONE_IP)
    drone.connect()
    assert drone(TakeOff()).wait().success()
    time.sleep(10)
    assert drone(Landing()).wait().success()
    drone.disconnect()


if __name__ == "__main__":
    # Janela
    window = sg.Window('Login to System', layout)
    
    # Ler os eventos
    while True:
        events, values = window.read()
        if events == sg.WINDOW_CLOSED:
            break
        if events == 'Login':
            if values['user'] == 'Admin' and values['password'] == 'admin':
                window.close()
                main()








