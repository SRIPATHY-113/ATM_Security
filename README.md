# Suspicious Behavior Detection in ATM Enclosures using YOLOv8

An automated computer vision surveillance system designed to monitor ATM booths in real-time. By leveraging deep learning and temporal logic, this system detects anomalies such as loitering and unauthorized multi-person booth entry to prevent theft and vandalism.

---

## 📌 Project Overview
Traditional security systems rely on manual monitoring, which is prone to human error and fatigue. This project introduces an intelligent monitoring layer using YOLOv8 and OpenCV to automatically flag suspicious activities:
1. Multi-Person Detection: Triggers an immediate alert if more than one individual enters the restricted single-user ATM zone.
2. Loitering Detection: Tracks individual dwell time and flags any person staying inside the zone longer than a defined threshold (e.g., 3 minutes).

---

## 🛠️ Technologies Required
* Python (v3.8 or higher)
* YOLOv8 (Ultralytics)
* OpenCV (Image & Video Processing)
* NumPy (Array Manipulation)
* Streamlit (Optional Dashboard Visualization)

---
