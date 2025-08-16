# Travel-Flow-Analysis

A computer vision project that detects, tracks, and counts vehicles in **three distinct lanes** from a traffic video, using YOLOv8 for object detection and the SORT algorithm for tracking.  
It outputs:
- **Real-time overlay video** with lane boundaries and live counts  
- **CSV file** containing vehicle IDs, lane numbers, frame counts, and timestamps  
- **Final summary** of total vehicle counts per lane  

---

##  Features
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

##  Setup Instructions

### 1️ Clone the Repository

### 2️ Install Dependencies
Ensure you have Python 3.8+ installed.
Then install required packages:
ultralytics==8.1.0
opencv-python
numpy
pandas
sort-tracker
yt-dlp

### 3️ Additional Dependency
The SORT tracker requires filterpy.

### 4️ Run the Project
src/main.py

---

###  Usage

The script automatically downloads the sample traffic video from YouTube on first run.

Press q anytime to stop the video early.

After processing:

data/output.csv → contains the vehicle tracking log

Console output → final vehicle counts per lane

Video window → shows lane boundaries & live counts during processing

---

###  Visual Output

The video display shows:

Lane boundaries (colored boxes)

Vehicle bounding boxes & IDs

Live lane-wise and total vehicle counts

---

## Approach Summary

- Detection: YOLOv8 detects vehicles in each frame

- Tracking: SORT tracks detected vehicles and assigns unique IDs

- Lane Mapping: Each vehicle is assigned a lane based on its center position

- Counting: Counts only new vehicle IDs per lane to avoid duplicates

- Export: Logs all events to CSV and displays real-time overlays




