from ultralytics import YOLOv10

model = YOLOv10('yolov10s.pt')
model.train(data='E:\shenduxuexi\yolov\yolov10\datasets\data.yaml', epochs=100, batch=4, imgsz=640)