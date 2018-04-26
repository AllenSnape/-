# 安装OpenCV (在Ubuntu 16.04上) [引用的教程](https://blog.csdn.net/yudiemiaomiao/article/details/72780790) [Ubuntu更改至阿里云源](https://github.com/AllenSnape/notes/Ubuntu.md)

## 1.必要包

>GCC 4.4.x or later

>CMake 2.6 or higher

>Git

>GTK+2.x or higher, including headers (libgtk2.0-dev) # 控制opencv GUI

>pkg-config

>Python 2.6 or later and Numpy 1.5 or later with developer packages (python-dev, python-numpy)

>ffmpeg or libav development packages: libavcodec-dev, libavformat-dev, libswscale-dev

>[optional] libtbb2 libtbb-dev

>[optional] libdc1394 2.x

>[optional] libjpeg-dev, libpng-dev, libtiff-dev, libjasper-dev, libdc1394-22-dev

```
sudo apt-get install build-essential
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
# 处理图像所需的包
sudo apt-get install python-dev python3-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
# 处理视频所需的包
sudo apt-get install libxvidcore-dev libx264-dev
# 优化opencv功能
sudo apt-get install libatlas-base-dev gfortran
sudo apt-get install ffmpeg
```

## 2.下载OpenCV (或者直接clone[OpenCV项目](https://github.com/opencv) [Git代理设置](https://github.com/AllenSnape/notes/git.md)) (自行选择版本)
```
wget https://github.com/opencv/opencv/archive/3.2.0.zip
wget https://github.com/opencv/opencv_contrib/archive/3.2.0.zip
# 解压, 自己补全代码
# unzip ...
```

## 3.编译&安装
```
cd opencv3.2.0
mkdir build
cd build
sudo cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local ..
# j4表示使用4核进行编译, 可根据自己电脑的配置进行修改j后面的数字
sudo make -j4
sudo make install
```

# 其他

## 修正python默认引用版本
```
# 因为Ubuntu 16.04默认的python引用的是python2, 所以更改至python3
cd /usr/bin
sudo rm -f python
sudo ln -s python3 python
```

## 安装pip, 因为默认的python3是没有pip的 [引用地址](https://pip.pypa.io/en/stable/installing/)
```
sudo apt-get install curl
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python get-pip.py
```

## 安装依赖
```
# 安装Python3的opencv包
sudo pip install opencv-python
# 安装tensorflow
sudo pip install tensorflow
```

# 安装darkflow
```
# 克隆代码
git clone https://github.com/thtrieu/darkflow.git
cd darkflow
# 开始安装
python3 setup.py build_ext --inplace
pip install .
```

# 使用
```
./flow --h
```
## 应该会有如下内容
```
Instructions for updating:
Use the retry module or similar alternatives.

Example usage: flow --imgdir sample_img/ --model cfg/yolo.cfg --load bin/yolo.weights

Arguments:
  --json           Outputs bounding box information in json format.
  --momentum       applicable for rmsprop and momentum optimizers
  --batch          batch size
  --summary        path to TensorBoard summaries directory
  --help, --h, -h  show this super helpful message and exit
  --lr             learning rate
  --train          train the whole net
  --labels         path to labels file
  --epoch          number of epoch
  --verbalise      say out loud while building graph
  --imgdir         path to testing directory with images
  --trainer        training algorithm
  --demo           demo on webcam
  --saveVideo      Records video from input video or camera
  --keep           Number of most recent training results to save
  --save           save checkpoint every ? training examples
  --backup         path to backup folder
  --binary         path to .weights directory
  --queue          process demo in batch
  --dataset        path to dataset directory
  --annotation     path to annotation directory
  --gpuName        GPU device name
  --savepb         save net and weight to a .pb file
  --config         path to .cfg directory
  --gpu            how much gpu (from 0.0 to 1.0)
  --pbLoad         path to .pb protobuf file (metaLoad must also be specified)
  --model          configuration of choice
  --load           how to initialize the net? Either from .weights or a checkpoint, or even from scratch
  --metaLoad       path to .meta file generated during --savepb that corresponds to .pb file
```