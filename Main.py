import cv2
from detectors.cat_face_detector import load_cascade, detect_objects

def start_detection():
    cascade = load_cascade()
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print(" cannot access camera")
        return
    
    print("Camera opened")
    print("Press 'Q' to quite")

    while True:
        ret, frame = cap,read()
        if not ret:
            print("Faild to read frame")
            break

        frame = detect_objects(cascade, frame)
        cv2.imshow("Cat face detection", frame)

        if cv2.waitkey(1) & 0xFF == ord('q'):
            break

        cap.release()
        cv2.destroyAllWindows()

        if __name__=="__main__":
            start_detection()

