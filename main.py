# Importing modules
import Hand_tracking_module as htm
import cv2
import time
import os
import image_handling as ih
from pathlib import Path

def main(images_save_path: str, 
         video_save_path: str, 
         video_name: str, 
         del_images_after: bool):

    # creating image path object
    img_path = images_save_path

    # creating video path object
    vid_path = video_save_path

    # creating video name object
    vid_name = video_name

    # capturing image from the front camera
    cap = cv2.VideoCapture(0)

    # creating file handling object
    handler = ih.file_handling()

    # creating counter object for keeping track of file names
    counter = 0

    # setting up run condition
    run = True

    # defining height and width
    new_width, new_height = 500, 700

    # setting up time values for FPS
    pTime, cTime = 0, 0

    # setting up hand tracker object
    tracker = htm.hand_detector()

    # defining points to track
    tracker_points = [2,4,6,8,10,12,14,16,18,20]

    # defining some colors
    color_green = (0,255,0)
    color_black = (0,0,0)

    # looping till conditions meet
    while run and cap.read():

        ret, img = cap.read() # reading the image captured from camera

        if ret:

            # img = img[100:500, 100:600] # cropping the image
            img = cv2.resize(img, (new_height, new_width))
            
            # img = cv2.flip(img, 1) # flipping the captured image
            img, detected_hand = tracker.find_hands(img, draw= False) # detecting the hand and points on the hand
            datapoints = tracker.track_pos(img, tracker_points) # getting datapoints for points being tracked
            
            detections = tracker.finger_count(img, datapoints, detected_hand) # counting fingers
            
            # calculating FPS
            cTime = time.time()
            fps = f'FPS: {int(1/(cTime-pTime))}'
            pTime = cTime

            detection_text = f'Fingers: {len(detections[0])} | Thumb: {len(detections[1])}' # text to show count

            # drawing on image
            cv2.rectangle(img, (0, 0), (150, 30), color_black, -1)
            cv2.rectangle(img, (800, 0), (250, 30), color_black, -1)
            cv2.putText(img, fps, (5, 25), cv2.FONT_HERSHEY_PLAIN, 2, color_green, 2)        
            cv2.putText(img, detection_text, (260, 25), cv2.FONT_HERSHEY_PLAIN, 2, color_green, 2)

            handler.save_images(img_path, img, counter) # saving images
            
            cv2.imshow('feed', img) # showing image

            counter += 1 # updating the counter value

        # ending the loop
        k = cv2.waitKey(1)

        if k == ord('q') or ret== False:

            handler.img_to_video(img_path, vid_path, vid_name) # converting images into video

            if del_images_after:
                
                # getting individual image path
                images = Path(img_path)
                images = list(images.glob('*.jpg'))

                # deleting the images
                for image in images:
                    os.remove(image)

                print('Images deleted')

            run = False

main(images_save_path=r'D:\software\mediapipe\target', 
     video_save_path=r'D:\software\mediapipe\target\video',
     video_name='test_video',
     del_images_after=True)