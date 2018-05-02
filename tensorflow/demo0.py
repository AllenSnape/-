from darkflow.net.build import TFNet
import cv2
import numpy as np

# 初始化参数
options = {
    "model": "cfg/yolo.cfg", 
    # https://pjreddie.com/media/files/yolo.weights
    "load": "/home/as/Documents/AI/ML/darkflow/bin/yolo.weights", 
    "threshold": 0.1
}
# 载入参数, 初始化变量
tfnet = TFNet(options)

# 通过opencv读取图片
imgcv = cv2.imread("/home/as/Desktop/1.jpg")

# 预测图片结果
result = tfnet.return_predict(imgcv)
# 根据预测机率倒序排列
result.sort(key=lambda x: x['confidence'], reverse=True)

# 输出预测内容
#print(result)

black = (0, 0, 0)

for obj in result:
    if obj['confidence'] > 0.5:
        cv2.line(imgcv, (obj['topleft']['x'], obj['topleft']['y']), (obj['bottomright']['x'], obj['topleft']['y']), black, 3)
        cv2.line(imgcv, (obj['topleft']['x'], obj['topleft']['y']), (obj['topleft']['x'], obj['bottomright']['y']), black, 3)
        cv2.line(imgcv, (obj['bottomright']['x'], obj['bottomright']['y']), (obj['bottomright']['x'], obj['topleft']['y']), black, 3)
        cv2.line(imgcv, (obj['bottomright']['x'], obj['bottomright']['y']), (obj['topleft']['x'], obj['bottomright']['y']), black, 3)

# opencv展示图片
cv2.imshow('WindowOne', imgcv)
cv2.waitKey()
cv2.destroyAllWindows()

# 裁剪图片; 裁剪参数为[y1: y2, x1: x2], 1为离原点最近的点
cv2.imshow('WindowOne', imgcv[
    result[0]['topleft']['y']:result[0]['bottomright']['y'], 
    result[0]['topleft']['x']:result[0]['bottomright']['x']
])
cv2.waitKey()
cv2.destroyAllWindows()
