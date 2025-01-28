import os

from ultralytics import YOLO


model = YOLO('yolov8n-seg.pt')  # load a pretrained model (recommended for training)

model.train(data='/Users/jakubczyszewski/PycharmProjects/obrazy_zpo/dataset.yaml', epochs=10, imgsz=512)
