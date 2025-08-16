from ultralytics import YOLO
import torch

class VehicleDetector:
    def __init__(self, model_path="models/yolov8n.pt"):
        self.model = YOLO(model_path)

    def detect(self, frame):
        results = self.model(frame)
        detections = []
        for r in results[0].boxes:
            cls = int(r.cls)
            if cls in [2, 3, 5, 7]:  # car, motorcycle, bus, truck
                x1, y1, x2, y2 = r.xyxy[0]
                conf = float(r.conf)
                detections.append([x1.item(), y1.item(), x2.item(), y2.item(), conf])
        return detections
