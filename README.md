# a1
深度学习yolov10
可以运行xunlian.py文件开始训练，也可以在终端输入下面指令进行训练
yolo detect train data=E:\shenduxuexi\yolov\yolov10\datasets\data.yaml model=yolov10s.yaml epochs=100 batch=4 imgsz=640 device=cpu

运行predict.py文件时对assets文件夹中的图片进行预测

jiekou.py文件是在虚拟机中进行运行，在终端输入指令，示例python3 /home/jiekou.py -dir/home/images -model /home/best.pt -out /home/outputjieguo
注意：在运行该文件时要新建一个文件夹来储存生成的xml文件，dir后面写需要检测的图片文件夹的地址，model后面写模型地址，out后面写储存结果的文件夹地址

在验证模型时使用的时指令
yolo val model=E:\shenduxuexi\yolov\yolov10\runs\detect\train\weights\best.pt data=E:\shenduxuexi\yolov\yolov10\datasets\data.yaml batch=4
