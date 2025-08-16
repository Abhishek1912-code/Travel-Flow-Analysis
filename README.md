# Travel-Flow-Analysis

A computer vision project that detects, tracks, and counts vehicles in **three distinct lanes** from a traffic video, using YOLOv8 for object detection and the SORT algorithm for tracking.  
It outputs:
- **Real-time overlay video** with lane boundaries and live counts  
- **CSV file** containing vehicle IDs, lane numbers, frame counts, and timestamps  
- **Final summary** of total vehicle counts per lane  

---

## 📌 Features
- **Vehicle Detection** using YOLOv8 pretrained on COCO dataset
- **Tracking** with SORT (Simple Online and Realtime Tracking) to avoid duplicate counts
- **Three distinct lanes** with independent counters
- **Real-time or near real-time processing**
- **CSV export** with detailed tracking data
- **Visual overlays** for lanes, IDs, and counts
- **Final count summary** at the end of processing

---

## Traffic_flow_analysis

data

├── video.mp4   # Downloaded traffic video

└── output.csv   # Generated vehicle count data

models

└── yolov8n.pt   # YOLOv8 model (auto-downloaded if not found)

src

├── main.py   # Main execution script

├── detector.py   # YOLO-based vehicle detection

├── tracker.py   # SORT tracking wrapper

├── lane_counter.py   # Lane definition and counting

├── sort.py   # SORT algorithm implementation

└── utils.py   # Video downloading and helpers

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository




