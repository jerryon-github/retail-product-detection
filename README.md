# 🛒 Retail Product Detection (YOLOv5)
An object detection system built with YOLOv5 to identify retail products like Coke, Pepsi, and Sprite in real-time images.

## 🧠 Features
Trains YOLOv5 on custom labeled retail product dataset

Roboflow-based annotations (YOLO format)

Configurable training via data.yaml

Flask-ready backend and Streamlit support (optional)

Can be deployed for real-time shelf monitoring

## 📁 Folder Structure

retail-product-detection/
├── data.yaml                     # Dataset config file
├── images/
│   ├── train/
│   └── val/
├── notebooks/
│   └── labeling.ipynb            # Image and annotation preview
├── src/
│   └── train.py                  # YOLOv5 training trigger
├── README.md
├── LICENSE
├── requirements.txt

### 🚀 How to Train

```bash
    git clone https://github.com/ultralytics/yolov5.git
    cd yolov5
    pip install -r requirements.txt

```bash
    cd ..
    python src/train.py

### ⚙️ Tech Stack
Python, YOLOv5 (PyTorch), OpenCV, Matplotlib, Roboflow, Flask