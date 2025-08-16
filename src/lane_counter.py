import cv2

class LaneCounter:
    def __init__(self):
        # Define lane boundaries (adjust based on video)
        self.lanes = [
            ((100, 0), (300, 720)),  # Lane 1
            ((300, 0), (600, 720)),  # Lane 2
            ((600, 0), (900, 720))   # Lane 3
        ]
        self.counts = {1: set(), 2: set(), 3: set()}

    def get_lane(self, x, y):
        for i, ((x1, y1), (x2, y2)) in enumerate(self.lanes, start=1):
            if x1 <= x <= x2:
                return i
        return None

    def update_counts(self, track_id, lane):
        if lane and track_id not in self.counts[lane]:
            self.counts[lane].add(track_id)

    def draw_lanes(self, frame):
        for ((x1, y1), (x2, y2)) in self.lanes:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
