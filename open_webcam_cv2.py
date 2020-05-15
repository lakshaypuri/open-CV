import cv2
v=cv2.VideoCapture(0)
while True:
    r,i=v.read()
    #data will be stored in i
   #status of image will be stored in r
    print(r)
    if(r==True):
        cv2.imshow('My Image',i)
    k=cv2.waitKey(5)
    if(k==ord('q')):
        cv2.destroyAllWindows()
        break


