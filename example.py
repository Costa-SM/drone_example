# -*- coding: UTF-8 -*-

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








