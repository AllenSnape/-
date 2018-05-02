# -- coding: utf-8 -- 
import RPi.GPIO as GPIO 
import time 

# BOARD编号方式，基于插座引脚编号 
GPIO.setmode(GPIO.BOARD)

# 定义每个笔画
LETF_BELOW = 3
LEFT_ABOVE = 11
BELOW = 5
ABOVE = 8
CENTER = 7
RIGHT_ABOVE = 10
RIGHT_BELOW = 16
DOT = 12

# 所有笔画的元组
ALL_DRAW_SET = (LETF_BELOW, LEFT_ABOVE, BELOW, ABOVE, CENTER, RIGHT_ABOVE, RIGHT_BELOW, DOT)
# 数组元组, 根据下标获取数字的笔画
NUMBER_SET = (
	(LEFT_ABOVE, LETF_BELOW, BELOW, RIGHT_BELOW, RIGHT_ABOVE, ABOVE), 
	(RIGHT_ABOVE, RIGHT_BELOW), 
	(ABOVE, RIGHT_ABOVE, CENTER, LETF_BELOW, BELOW), 
	(ABOVE, RIGHT_ABOVE, CENTER, RIGHT_BELOW, BELOW), 
	(LEFT_ABOVE, CENTER, RIGHT_ABOVE, RIGHT_BELOW), 
	(ABOVE, LEFT_ABOVE, CENTER, RIGHT_BELOW, BELOW), 
	(ABOVE, LEFT_ABOVE, CENTER, RIGHT_BELOW, BELOW, LETF_BELOW), 
	(ABOVE, RIGHT_ABOVE, RIGHT_BELOW), 
	(LETF_BELOW, LEFT_ABOVE, BELOW, ABOVE, CENTER, RIGHT_ABOVE, RIGHT_BELOW), 
	(LEFT_ABOVE, BELOW, ABOVE, CENTER, RIGHT_ABOVE, RIGHT_BELOW), 
)

# 输出模式 
GPIO.setup(LETF_BELOW, GPIO.OUT)
GPIO.setup(BELOW, GPIO.OUT)
GPIO.setup(CENTER, GPIO.OUT)
GPIO.setup(LEFT_ABOVE, GPIO.OUT)

GPIO.setup(ABOVE, GPIO.OUT)
GPIO.setup(RIGHT_ABOVE, GPIO.OUT)
GPIO.setup(DOT, GPIO.OUT)
GPIO.setup(RIGHT_BELOW, GPIO.OUT)

def allLights(on = 0):
	for d in ALL_DRAW_SET:
		GPIO.output(d, GPIO.HIGH if on else GPIO.LOW) 

def drawNumber(index = 0):
	allLights()
	for d in NUMBER_SET[index]:
		GPIO.output(d, GPIO.HIGH) 
	
count = 7
while True: 
	# 绘制个位数字
	drawNumber(count % 10)
	# 大于10时显示点
	if count > 9:
		GPIO.output(DOT, GPIO.HIGH)
	else:
		GPIO.output(DOT, GPIO.LOW)
	# 计时减少
	count -= 1
	# 如果计时为-1则退出循环并闪烁
	if count < 0:
		break
	# 延时1秒
	time.sleep(1)
	
while True:
	allLights(1)
	time.sleep(0.05)
	allLights(0)
	time.sleep(0.05)