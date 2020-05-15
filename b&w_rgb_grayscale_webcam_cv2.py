import cv2

v=cv2.VideoCapture(0)
while True:
    r,i=v.read()
    print(r)
    if(r==True):
        j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)   #gray color
        r,k=cv2.threshold(j,127,255,1)                          #(1 will be white and 0 will be black)
        cv2.imshow('Binary',k)
        cv2.imshow('My Image',i)                                 # basic color 
        cv2.imshow('My Gray Image',j)
    k=cv2.waitKey(5)
    if(k==ord('q')):
        cv2.destroyAllWindows()
        break
