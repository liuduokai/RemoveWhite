# 裁切图片白边
用于裁切CAD打印出图片的白边
## 原理
遍历检测最先出现黑色像素的范围，对图像进行裁切
## 说明
* single.py功能的实现
* test.py功能测试文件
* multi_thread_test.py多进程实现
* creatJpg.py生成测试图片