from sort import Sort
import numpy as np

class VehicleTracker:
    def __init__(self):
        self.tracker = Sort()

    def update(self, detections):
        dets = np.array(detections)
        return self.tracker.update(dets)
