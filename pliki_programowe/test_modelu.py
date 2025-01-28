from ultralytics import YOLO

# Załaduj wytrenowany model
model = YOLO('runs/segment/train11/weights/best.pt')  # Upewnij się, że ścieżka do modelu jest poprawna

# Testowanie na zbiorze testowym (użyjemy metody val() z parametrem split='test')
results = model.val(data='/Users/jakubczyszewski/PycharmProjects/obrazy_zpo/dataset.yaml', imgsz=512, split='test')

# Wyświetlenie wyników
print(results)
