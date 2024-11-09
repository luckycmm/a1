from ultralytics import YOLOv10  
  
# 加载模型  
model = YOLOv10("runs/detect/train2/weights/best.pt")  
  
# 进行预测  
results = model.predict("ultralytics/assets/1.jpg")  
  
# 显示结果  
results[0].show()