import PySimpleGUI as sg
import cv2
import numpy as np
import sys
from sys import exit as exit
from datetime import datetime
import requests
import pandas as pd
from tkinter import messagebox
import csv

# Parametros
max_num_plate=10 # maximo numero de placas a almacenar en el fichero .csv

sg.ChangeLookAndFeel('Black')

# define the window layout
layout = [[sg.Text('PLATE by Luis Sanchez', size=(40, 1), justification='center', font='Helvetica 20')],
          [sg.Image(filename='', key='image')],
          [sg.Button('Read plate', size=(10, 1), font='Helvetica 14'),
           sg.Button('Map', size=(10, 1), font='Any 14'),
          sg.Button('Exit', size=(10, 1), font='Helvetica 14'),]]
# create the window and show it without the plot
window = sg.Window('Demo Application - Read Plate v1.1', layout,
                   location=(800,400))
######## ciclo para que la ventana se ejecute constantemente #######

    
cap = cv2.VideoCapture(0)
recording = True
while True:
    event, values = window.Read(timeout=20)
    if event == 'Exit' or event is None:
        break
    elif event == 'Read plate':
        break
    elif event == 'Map':
        break
    if recording:
        ret, frame = cap.read()            
        imgbytes=cv2.imencode('.png', frame)[1].tobytes() #ditto
        window.FindElement('image').Update(data=imgbytes)
window.close() #cerrar todo


exit()


