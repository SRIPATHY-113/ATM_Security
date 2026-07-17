import cv2

from person_detection import detect_persons
from loitering import LoiteringDetector
from alert import show_alert
from face_mask_detection import check_face

cap = cv2.VideoCapture("video/atm_test.mp4")

loiter_detector = LoiteringDetector()

while True:

    ret, frame = cap.read()

    if not ret or frame is None:
        break

    persons, boxes = detect_persons(frame)

    faces = check_face(frame)

    person_count = len(persons)

    # Draw person boxes
    for (x1,y1,x2,y2) in boxes:

        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)

    # Draw face boxes
    for (x,y,w,h) in faces:

        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    # ALERT: Multiple people
    if person_count > 1:
        show_alert(frame,"ALERT: MULTIPLE PEOPLE")

    # ALERT: Loitering
    if loiter_detector.check_loitering(person_count):
        show_alert(frame,"ALERT: LOITERING DETECTED")

    # ALERT: Face not visible (mask / helmet)
    if person_count > 0 and len(faces) == 0:
        show_alert(frame,"ALERT: FACE NOT VISIBLE")

    cv2.putText(frame,
                f"Persons: {person_count}",
                (10,30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,0,255),
                2)

    cv2.imshow("ATM Security System",frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
