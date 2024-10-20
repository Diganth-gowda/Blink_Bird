import cv2
import mediapipe as mp
import pyautogui as pag
import keyboard

import socket
import time

#UDP SETUP
UDP_IP = "127.0.0.1"  # Change this to the IP of the machine running Unity if not local
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# creates a video capturing interface
cam = cv2.VideoCapture(0)
# for face detection
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks= True)

screen_w, screen_h = pag.size()

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmarks_points = output.multi_face_landmarks
    frame_h,frame_w,_ = frame.shape

    # print(landmarks_points)
    if landmarks_points:
        landmarks = landmarks_points[0].landmark
        for id, landmark in enumerate(landmarks[474 :478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0 ))
            if id == 1:
                screen_x = screen_w / frame_w * x
                screen_y = screen_h / frame_h * y
                #pag.moveTo(screen_x, screen_y)
            # print(x, y)
            left = [landmarks[145], landmarks[159]]
            for landmark in left:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 255 ))
                #print(left[0].y - left[1].y)

                if (left[0].y - left[1].y) <0.013:
                    keyboard.press_and_release('space')
                    #print('click')
                #    pag.click()

    cv2.imshow('Eye controlled mouse', frame)
    cv2.waitKey(1)