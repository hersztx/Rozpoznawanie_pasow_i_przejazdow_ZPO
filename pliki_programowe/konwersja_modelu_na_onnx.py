from ultralytics import YOLO

# Załaduj wytrenowany model
model = YOLO('runs/segment/train11/weights/best.pt')

# Eksportuj model do formatu ONNX
model.export(format='onnx')
