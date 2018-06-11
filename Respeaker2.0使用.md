# Respeaker2.0 上手过程

## Image Installation

1. 下载[image文件](https://bfaceafsieduau-my.sharepoint.com/personal/miaojg22_off365_cn/_layouts/15/guestaccess.aspx?folderid=0bb3c4f3f122d4c2bb0f65eee2b5938f8&authkey=AfLSkcE8QeeUHTQ8GGfrrsU)
2. 选用respeaker-debian-9-lxqt-sd-[date]-4gb.img.xz
3. 下载安装[etcher](https://etcher.io/)准备sd卡镜像
4. 准备一个4G以上的sd卡
5. 打开etcher，将respeaker-debian-9-lxqt-sd-[date]-4gb.img.xz烧录到SD卡上
6. SD卡插入设备，插上usb电源PWD_IN,
7. USER1和USER2灯闪，说明启动OK

## 设置WIFI

1. `sudo nmtui` 打开wifi设置 ，按提示连接wifi
2. `ip address` 查看io

## SSH从PC访问设备

1. xshell 建立ssh连接到respeaker@ip:22 密码respeaker
2. 在respeaker上安装rz（上传）、sz（下载）工具`sudo apt-get install lrzsz`
3. 在respeaker上执行`sz testfile`，传输到pc上

