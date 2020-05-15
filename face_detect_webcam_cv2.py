import cv2
v=cv2.VideoCapture(0)
fd=cv2.CascadeClassifier(r'C:\Users\LAKSHAY\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml')
while True:
    r,image=v.read()
    print(r)
    if(r==True):
        j=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        r,k=cv2.threshold(j,127,255,0)
        f=fd.detectMultiScale(image)
        for(x,y,w,h) in f:
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),5)
        cv2.imshow('Binary',k)
        cv2.imshow('My Image',image)               
        cv2.imshow('My Gray Image',j)
    k=cv2.waitKey(5)
    if(k==ord('q')):
        cv2.destroyAllWindows()
        break
