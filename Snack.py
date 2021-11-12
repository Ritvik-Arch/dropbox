from os import access
import cv2
import dropbox
import time
import random

Starttime=time.time()

def take_snapshot():
    number=random.randint(0,100)
    videocaptureobject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videocaptureobject.read()
        imgname="img"+str(number)+".png"
        cv2.imwrite(imgname,frame)
        Starttime=time.time
        result=False
    return imgname
    print("snapshot taken")
    videocaptureobject.release()
    cv2.destroyAllWindows()
take_snapshot()

def upload_files(imgname):
    access_token="sl.A8FDrrWKUi5kJVyqyujBs-iSSj_kK_kVnpFp04GunOncXCu3pfkE5I-9NgeY8gfDvaavRHkzDhgCP2RNNWIGBrwFN5RsRP8Dyf3i_P96zVKNnGs0DnpN7qaZ9T7P84trPP0MXT0"
    file=file=imgname
    filefrom=file
    fileto="/newfolder/"+(imgname)
    dbx=dropbox.Dropbox(access_token)

    with open(filefrom, 'rb') as f:
         dbx.filesupload(f.read(), fileto, mode=dropbox.files.WriteMode.overwrite)
         print("File Uploaded")

def main():
     while(True):
          if((time.time() - Starttime)>= 300):
               name=take_snapshot()
               upload_files(name) 
main()