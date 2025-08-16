import cv2
import pandas as pd
from utils import download_video
from detector import VehicleDetector
from tracker import VehicleTracker
from lane_counter import LaneCounter

VIDEO_PATH = "data/video.mp4"
CSV_PATH = "data/output.csv"
VIDEO_URL = "https://www.youtube.com/watch?v=MNn9qKG2UFI"

def main():
    download_video(VIDEO_URL, VIDEO_PATH)

    cap = cv2.VideoCapture(VIDEO_PATH)
    detector = VehicleDetector()
    tracker = VehicleTracker()
    lane_counter = LaneCounter()

    output_data = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detections = detector.detect(frame)
        tracked_objects = tracker.update(detections)

        for obj in tracked_objects:
            x1, y1, x2, y2, track_id = map(int, obj)
            cx = int((x1 + x2) / 2)
            cy = int((y1 + y2) / 2)

            lane = lane_counter.get_lane(cx, cy)
            lane_counter.update_counts(track_id, lane)

            cv2.putText(frame, f"ID:{track_id} L:{lane}", (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255,0,0), 2)

            output_data.append({
                "Vehicle_ID": track_id,
                "Lane": lane,
                "Frame": int(cap.get(cv2.CAP_PROP_POS_FRAMES)),
                "Timestamp": cap.get(cv2.CAP_PROP_POS_MSEC)/1000
            })

        lane_counter.draw_lanes(frame)

        # Draw real-time vehicle count overlay
        y_offset = 30
        for lane in sorted(lane_counter.counts.keys()):
            count = len(lane_counter.counts[lane])
            cv2.putText(frame, f"Lane {lane}: {count}",
                        (10, y_offset),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.9, (255, 255, 255), 2)
            y_offset += 30

        total_count = sum(len(ids) for ids in lane_counter.counts.values())
        cv2.putText(frame, f"Total: {total_count}",
                    (10, y_offset),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, (0, 255, 255), 2)

        cv2.imshow("Traffic Analysis", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    df = pd.DataFrame(output_data)
    df.to_csv(CSV_PATH, index=False)
    print("\n✅ Data saved to:", CSV_PATH)

    # Display summary counts
    print("\n📊 Total Vehicle Count per Lane:")
    for lane, ids in lane_counter.counts.items():
        print(f"  Lane {lane}: {len(ids)} vehicles")

    total = sum(len(ids) for ids in lane_counter.counts.values())
    print(f"\n🚗 Total Vehicles Counted: {total}")

if __name__ == "__main__":
    main()
