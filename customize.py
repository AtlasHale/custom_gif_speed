import os, shutil
import cv2
import imageio
from PIL import Image, GifImagePlugin


def getFrames(gif, outFolder):
    files = os.listdir(".")
    if gif+"_custom_speed" in files:
        os.remove(gif+"_custom_speed")
    os.mkdir(outFolder)
    cap = cv2.VideoCapture(gif)
    i = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == 0:
            break
        cv2.imwrite(outFolder+'/'+str(i)+'.jpg', frame)

        i+=1
    cap.release()
    cv2.destroyAllWindows() 

def custom_speed(gif, image_folder, dur):
    frames = []
    files = os.listdir(image_folder)
    temp = {}
    for x in files:
        temp[int(x[:-4])]=x
    for frame in sorted (temp.keys()):
        frames.append(imageio.imread(image_folder+'/'+temp[frame]))
    imageio.mimwrite(gif+"_custom_speed", frames, format="gif" ,duration=dur)
    shutil.rmtree(gif+'_frames')



s = input("file name: ")
dur = input("duration of each frame (.01 fastest): ")
getFrames(s, s+'_frames')
custom_speed(s, s+'_frames', dur)

