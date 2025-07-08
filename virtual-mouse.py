import cv2
import mediapipe as mp
import pyautogui

cap=cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

index_y=0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_h, frame_w, _ = frame.shape
    screen_w, screen_h = pyautogui.size()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            # drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                if id == 8:
                    index_x = int(landmark.x * frame_w)
                    index_y = int(landmark.y * frame_h)
                    cv2.circle(img=frame, center= (index_x,index_y), radius=20, color=(0,255,255))
                    screen_x = int(landmark.x * screen_w)
                    screen_y = int(landmark.y * screen_h)
                    pyautogui.moveTo(screen_x,screen_y)
                if id == 4:
                    thumb_x = int(landmark.x * frame_w)
                    thumb_y = int(landmark.y * frame_h)
                    cv2.circle(img=frame, center = (thumb_x, thumb_y), radius=10, color=(255,0,0))
                    if abs(index_y - thumb_y) < 20:
                        pyautogui.click()
                        pyautogui.sleep(1)
    cv2.imshow('VirtualMouse', frame)
    cv2.waitKey(1)