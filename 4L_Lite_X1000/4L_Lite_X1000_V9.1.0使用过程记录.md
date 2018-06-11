## 连线

主要接口：line in,line out, usb debug, usb&host

1. 使用1分2音频线，一头接pc耳机，一端分两头供下面的步骤使用；
2. 使用公对公音频线，一头接1分2音频线A口，一头接音箱，作为外放输出；
3. 使用公对公音频线，一头接1分2音频线B口，一头接line in,作为参考音输入；
4. 使用公对公音频线，一头接pc麦克孔，一头接line out,作为最终音频输出；
5. 使用usb线，一头接usb debug口，一头接pc usb口，可作为串口调试；
6. 使用usb线，一头接usb&host口，一头接pc usb口，作为电源；

最后一步完成后，系统将自动启动。通过下一步的adb操作，验证系统启动。

## 进入Adb shell

adb确认连接后,使用`putty_adb.exe`连接设备

1. 打开`putty_adb.exe`
2. Session Host Name 填写`transport-usb`，端口填写`5037`
3. Connection Type 选择`Adb`
4. 点击Open, 进入adb shell
5. 在shell中运行`ps | grep hci_sma`，若有`./bin/hci_sma_service`的信息，说明灵云麦克风阵列服务(Sinovoice Mic Array Service)已正常运行

## PC端运行`灵云麦克风阵列远讲演示V2.0软件`体验麦阵服务

1. 需要PC环境可访问互联网，用来做云端识别；
2. 运行`MicArrayTools.exe`
3. 点击`启动服务`,正常则弹出`启动服务成功`, 当用户在不同角度说话时，演示软件界面上将有对应的声源角度指示；
4. 点击开始录音，演示软件将录制来自line out的音频；
5. 可体验在正向90度和其他方向的识别情况；
6. 正向90±15度有拾音，因此在这个方向说话会识别出来；
7. 正向90±15度外抑制，因此在这个方向说话不会别识别出来；
8. PC播放音乐，体验AEC消除效果；
9. 可通过移动音箱的位置，来体验不同方向上AEC效果；

## 获取灵云麦克风阵列服务中间数据

1. 由于FL设备存储空间有限，需插入外部SD卡
2. 
3. 进入`adb shell`；
4. 进入`/usr/data`目录；
5. 修改`hci_micarray.ini`中的LogDataMask参数为0xffff,可在运行中保存所有数据
6. 修改`hci_micarray.ini`中的LogDataPath为/mnt/sdcard/
7. 修改`jt.sh`,新增mount /dev/mmcblk0p1 /mnt/sdcard/
8. reboot
9. 数据默认保存在`tmp`目录下，改目录大小可空间在13M左右，可保存一小段音频
10. reboot设备

取出tmp下的数据

1. *mic.pcm 4路原始音 16K 16BIT
2. *ref.pcm 1路参考音 16K16BIT
3. *aec.pcm 对应mic - ref的输出 4路 16k 16Bit
4. *ns.pcm  对aec.pcm做NS处理后,得到 4路 16k 16Bit；
5. *out.pcm 对aec数据 DBF/ICE，NS之后的1路输出 16K 16BIT

## TstVQEEngine.exe的使用
输入数据：
test/mic.pcm
test/mic.pcm.ref
TstVQEEngine.exe --AEC_pcm_multi_channel 4 1 100 128 2048 test
TstVQEEngine.exe --AEC_pcm_multi_channel 1 1 100 128 2048 test

TstVQEEngine.exe --DEN_pcm 6 6 160 1 3 ./test/


## SD卡的格式化

若micro SDCard被烧过linux镜像，再使用读卡器插到windows设备上，是读取不到的，需要以下步骤：

1. 使用读卡器插到windows设备上（工作电脑是linux的，可以忽略）
2. 在linux虚拟机中可识别到该设备，使用fdisk格式化
3. 在windows的设备管理中，管理磁盘，格式化目标磁盘；