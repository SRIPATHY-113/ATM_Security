from ultralytics import YOLO

# Load YOLO model
model = YOLO("./yolov8n.pt")

def detect_persons(frame):

    results = model(frame)

    persons = []
    boxes_draw = []

    for r in results:
        boxes = r.boxes

        for box in boxes:

            cls = int(box.cls[0])

            # class 0 = person
            if cls == 0:

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                persons.append((x1, y1, x2, y2))
                boxes_draw.append((x1, y1, x2, y2))

    return persons, boxes_draw
