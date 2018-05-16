import cv2  
import numpy as np
import matplotlib.pyplot as plot
import time

from darkflow.net.build import TFNet

# YOLO初始化参数
options = {
    "model": "cfg/yolo.cfg", 
    # https://pjreddie.com/media/files/yolo.weights
    "load": "yolo.weights", 
    "threshold": 0.1,
	"gpu":	1.0
}

# 黑色
black = (0, 0, 0)
# 标签字体
font = cv2.FONT_HERSHEY_SIMPLEX

# 载入YOLO参数, 初始化变量
tfnet = TFNet(options)

# 初始化摄像头
cap = cv2.VideoCapture(0)

while(1):
	# 获取帧
	ret, frame = cap.read()
	# 显示帧
	# cv2.imshow("capture", frame)
	
	frame = cv2.resize(frame, (320, 240), interpolation=cv2.INTER_AREA)
	
	# 预测图片结果
	result = tfnet.return_predict(frame)
	# 根据预测机率倒序排列
	result.sort(key=lambda x: x['confidence'], reverse=True)
	
	# 绘制线条
	for obj in result:
		if obj['confidence'] > 0.5:
			# 添加标签
			frame = cv2.putText(frame, obj['label'], (obj['topleft']['x']+8, obj['topleft']['y']+20), font, 0.5, (255, 255, 255))
			# 绘制线条
			cv2.line(frame, (obj['topleft']['x'], obj['topleft']['y']), (obj['bottomright']['x'], obj['topleft']['y']), black, 3)
			cv2.line(frame, (obj['topleft']['x'], obj['topleft']['y']), (obj['topleft']['x'], obj['bottomright']['y']), black, 3)
			cv2.line(frame, (obj['bottomright']['x'], obj['bottomright']['y']), (obj['bottomright']['x'], obj['topleft']['y']), black, 3)
			cv2.line(frame, (obj['bottomright']['x'], obj['bottomright']['y']), (obj['topleft']['x'], obj['bottomright']['y']), black, 3)

	# 展示图片
	cv2.imshow("capture", frame)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
		
cap.release()
cv2.destroyAllWindows()