from tkinter import *
from tkinter import messagebox

import cv2
import playsound
import threading
from tkinter import *

# create a tkinter window
root = Tk()

# Open window having dimension 100x100
root.geometry('100x100')

Alarm_Status = False
face_detected = 0
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def play_alarm_sound_function():
    while True:
        playsound.playsound('Danger Alarm Sound Effect.mp3',True)

cap = cv2.VideoCapture(0)
while True:
    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow('img', img)

        if faces.all():
            face_detected = face_detected + 1

        #cv2.imshow('img', img)

        if face_detected >= 1:

            if Alarm_Status == False:
                threading.Thread(target=play_alarm_sound_function).start()
                Alarm_Status = True
        if cv2.waitKey(1) & 0xFF:
            break

cap.release()

