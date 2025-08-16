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

## 
