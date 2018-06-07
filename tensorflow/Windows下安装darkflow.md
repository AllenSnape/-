# 在Windows上编译安装darkflow

## 安装Python的OpenCV支持
1. 在[Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy)中下载自己对应的Python版本的whl文件. 电脑是64位的，安装的是python3.5，opencv_python-3.2.0+contrib-cp35-cp35m-win_amd64.whl就合适, [参考](https://blog.csdn.net/qxconverse/article/details/59704906)
2. 然后 pip install opencv_python-3.2.0+contrib-cp35-cp35m-win_amd64.whl, 或者python -m pip install 下载的whl文件(没有pip的[参考这个](https://github.com/AllenSnape/notes/blob/master/tensorflow/darkflow.md#%E5%AE%89%E8%A3%85pip-%E5%9B%A0%E4%B8%BA%E9%BB%98%E8%AE%A4%E7%9A%84python3%E6%98%AF%E6%B2%A1%E6%9C%89pip%E7%9A%84-%E5%BC%95%E7%94%A8%E5%9C%B0%E5%9D%80)即可)

----------------------------

## 安装Visual Studio 2017 Community
### 勾选上"工作负载 → Windows → 通用 Windows 平台开发"即可

----------------------------

## 安装Windows编译器(需要Node.js的npm) (下面编译那步出错时再弄这个)
### 安装Node.js, 已经安装了的可以跳过
1. 在[Node.js官网](http://nodejs.cn/download/)下载安装对应版本即可
2. 安装[Windows-Build-Tools](https://www.npmjs.com/package/windows-build-tools), npm install --global --production windows-build-tools

----------------------------

## 编译
```
# 克隆代码
git clone https://github.com/thtrieu/darkflow.git
cd darkflow
# 开始安装
python3 setup.py build_ext --inplace # 这句可能会报错, 错误参考FAQ
pip install .
```

----------------------------

## FAQ

> ... link.exe failed with exit status 1158 [参考](https://stackoverflow.com/questions/43858836/python-installing-clarifai-vs14-0-link-exe-failed-with-exit-status-1158)
>> 复制 C:\Program Files (x86)\Windows Kits\10\bin\10.0.17134.0\x64 下的 rc.ex e和 rcdll.dll 至C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\下所有的文件夹内 (也可根据编译报错内容选择文件夹)

> error: Unable to find vcvarsall.bat
>> 很有可能是npm安装windows-build-tools失败了, 可以尝试重新安装或者在vs2017中安装对python的依赖
