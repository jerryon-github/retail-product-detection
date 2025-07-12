# More modular and project-aware
import os
import subprocess

YOLO_DIR = os.path.join(os.getcwd(), "yolov5")
if not os.path.exists(YOLO_DIR):
    subprocess.run(["git", "clone", "https://github.com/ultralytics/yolov5.git"])
    print("✅ YOLOv5 cloned successfully.")

subprocess.run(["pip", "install", "-r", os.path.join(YOLO_DIR, "requirements.txt")])

subprocess.run([
    "python", os.path.join(YOLO_DIR, "train.py"),
    "--img", "416",
    "--batch", "8",
    "--epochs", "5",
    "--data", "data.yaml",
    "--weights", "yolov5s.pt",
    "--project", "runs/train",
    "--name", "product-detector",
    "--cache"
])
