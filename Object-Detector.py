import cv2

def load_cascade():
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')
    if cascade.empty():
        raise IOError("Failed To Load cascade")
    print("Cascade loaded succesfully")
    return cascade

def detect_objects(cascade,frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    objects = cascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=5)
    for(x,y,w,h) in objects:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    return frame
    