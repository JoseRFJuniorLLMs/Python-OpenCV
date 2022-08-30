import cv2

import numpy as np

class RedPointDetector :
    def _init_(slef) :
        #creat mask for red color
        self.low_red = np.array ([160,169,192])
        self.high_red = np.array([179,255,255])

    def detect(self,frame) :
        hsv_img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        #creat mask with color range
        mask = cv2.inRange(hsv_img,self.low_red ,self.high_red)
        #find contoures
        contours,_ = cv2.findcontours(mask,cv2.PETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours,key = lambda x:cv2.contourArea(x),reverse=True)

        box = (-100,-100,0,0)
        for cnt in contours :
            (x,y,w,h) = cv2.boundingRect(cnt)
            if w*h > 300 :
                box = (x,y,x+w ,y+h )
                break
        return box



class KalmanFilter :
    kf =cv2.KalmanFilter(4,2)
    kf.measurementMatrix = np.array([[1,0,0,0],[0,1,0,0]],np.float32)
    kf.transitionMatrix = np.array([[1,0,1,0],[0,1,0,1],[0,0,1,0],[0,0,0,1]],np.float32)

    def predict (self,coordx,coordy) :
        # this function estimate the position of the object
        measured = np.array([[np.float32(coordx)],[np.float32(coordy)]])
        self.kf.correct(measured)
        predicted = self.kf.predict()
        x ,y = int(predicted[0]),int(predicted[1])
        return x,y
spW = 640
spH = 480
ip = 2


#load detector
od = RedPointDetector()

#load kalman filter to predict next point
kf = KalmanFilter()

outvid = cv2.VideoWriter("orangex.mp4",30,(640,480))


while True:
    ret ,frame = cap.read()
    frame = cv2.flip(frame,1)
    if ret is False :
        break


    redpoint_bbox = od.detect(frame)
    x,y,x2,y2 =redpoint_bbox
    cx =int((x+x2)/2)
    cy = int((y+y2)/2)

    predicted = kf.predict(cx,cy)
    cv2.circle(frame,(cx,cy),10,(0,255,255),-1)
    cv2.cirdle(frame,(predicted[0],predicted[1]),10,(255,0,0),4)

    cv2.imshow("Frame",frame)
    outvid.write(frame)
    key = cv2.waitkey(1)
    if key == 27 :
        break

    cap.release()
    outvid.release()
