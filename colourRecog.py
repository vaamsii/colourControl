import cv2
import numpy as np
import pyautogui



cap = cv2.VideoCapture(0)

prev_y = 0
prev_x = 0


while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Range for lower red
    lower_blue = np.array([78, 158, 124])
    upper_blue = np.array([138, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    contours, heirarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        area = cv2.contourArea(c)
        if area > 300:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            #cv2.drawContours(frame, c, -1, (0, 255, 0), 2)
            #print(area)
            if y < prev_y:
                pyautogui.press('space')
                #print('moving down')
            prev_y = y
            #if x < prev_x:
                #pyautogui.press('left')
                #print('moving down')
            #prev_x = x

    cv2.imshow('Video Control', frame)
    #cv2.imshow('mask', mask1)
    if cv2.waitKey(10) == ord('e'):
        break


cap.release()
cv2.destroyAllWindows()