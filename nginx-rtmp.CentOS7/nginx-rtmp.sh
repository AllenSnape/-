# 进入下载目录
downloadPath="./downloads/"
# 检查目录是否存在
if [ ! -f "$downloadPath" ];then  
# 不存在则创建
mkdir "$downloadPath"  
fi

# 复制当前目录的nginx.conf到下载目录, 后面要直接复制到配置目录
cp ./nginx.conf "$downloadPath" 

cd "$downloadPath"

# 安装gcc
yum install gcc gcc-c++ -y
# 安装PCRE和pcre-devel
yum install pcre pcre-devel -y
# 安装zlib
yum install zlib zlib-devel -y
# 安装OpenSSL
yum install openssl openssl-devel -y
# 安装解压
yum install unzip -y

# 下载nginx
wget https://nginx.org/download/nginx-1.15.3.tar.gz
# 解压nginx
tar -zxvf nginx-1.15.3.tar.gz

# 下载nginx的rtmp模块
wget https://github.com/arut/nginx-rtmp-module/archive/master.zip
# 解压
unzip master.zip
# 更改文件名称
mv nginx-rtmp-module-master nginx-rtmp-module

# 进入nginx目录
cd nginx-1.15.3
# 配置
./configure --prefix=/usr/local/nginx  --add-module=../nginx-rtmp-module  --with-http_ssl_module
# 编译与安装
make & make install

# 移动配置文件
mv ../nginx.conf /usr/local/nginx/conf/
# 设置应用软链接
ln -s /usr/local/nginx/sbin/nginx /usr/local/bin/nginx
# 配置文件软链接
ln -s /usr/local/nginx/conf/nginx.conf /etc/

# 启动
nginx -t
nginx
