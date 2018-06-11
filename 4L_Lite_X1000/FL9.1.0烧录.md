# FL9.1.0 固件升级烧录

## 所需材料：

1. 捷通华声拾音模块开发板烧录说明书
2. cloner-2.2.3-windows_release.zip：带界面的烧录工具
3. cloner-win32-driver.zip：烧录时烧录工具与设备之间的驱动程序
4. 固件
    1. appfs
    2. configs
    3. kernel
    4. uboot
    5. udata
    6. updater

## 配置烧录工具

1. 解压cloner-2.2.3-windows_release.zip
2. 打开cloner.exe
    1. pc上若有类似亿赛通加密安全工具，可能会发生报错，可多尝试几次
3. 点击"配置"->"POLICY"
4. 按照图中所示，将固件下的相关文件依次配置进来；注意：只修改属性1列，其他列不要修改。
    1. uboot/u-boot-with-spl.bin
    2. configs/nv.img
    3. udata/usrdata.jffs2
    4. kernel/zImage
    5. updater/updater.cramfs
    6. appfs/appfs.cramfs

1. 确认所选正确后，点击"保存"->"Yes", 回到cloner主界面，点击"开始",改按钮文字变为"停止"。注意这里点击开始，不会开始烧录，等待设备进入烧录模式后，会真正开始。

## 连接FL设备，使其进入烧录模式

1. usb&host（adb/电源接口）用usb-micro usb 线与电脑连接，此时power LED上电指示灯亮起，则表示上电成功
2. 进入烧录模式: 依次按住BOOT_SEL0、RESE手真T按键，不要松开，再依次松开RESET、BOOT_SEL0按键。
3. 如果是第一次烧录，windows一般会自动安装驱动，等待一会之后，提示安装失败。我们自行安装cloner-win32-driver.
    1. 解压cloner-win32-driver.zip
    2. 在"计算机"-"设备管理器"中找到问题设备
    3. 选择在磁盘上选择驱动安装cloner-win32-driver
4. 若安装成功，处于开始等待状态的cloner检测到此设备，开始烧录
5. 进度条变为100%，绿色后，表明烧录成功
6. 重启设备，`cat /usr/fs/usr/jt/VERSION`版本号，确定版本，开始使用。





## FAQ

1. 检查FL设备usb debug是否正常连接,adb devices是否能看到FL设备`Ingenic online`;如果显示`Ingenic offline`，运行`adb kill-server`,`adb start-server`，重启adb服务。


THE PEOPLE'S REPUBLIC OF CHINA is a country with a long history and ancient civilization. As early as 4,000 BC, there were settlements in the range of Yellow River. Chinese always tell their history from the Xia Dynasty, which began in the 21st century BC and was followed by all the ddynasties until 1911 when Sun Yat-sen was proclaimed the president of the Republic of China. In 1921, the Communist Party of China was founded. After this, the communist cooperated with Sun Yat-sen's Nationalists, but broke with the Nationalist after Sun died. Then the Communist Party began to establish its army, called as Red Army. Shortly  before  the Anti-Japanese War (1936-1945) the Red Army formally established Through protracted and arduous struggle under the leadership of the party and her chairman, Mao Zedong, the Chinese people founded the People's Republic of China in 1949. After 1949, The People's Republic  of China (also called as New China locally) experienced the Korea Wall with Americans, and about 10 years rapid growing period, and then suffered a 3-year long hard time because of natural disasters and withdraw of Soviet Union's aid. From 1966-1976 China had its "Cultural Revolution", a nation-wide movement against feudalism  (also including  religion) and capitalism. As a result, China's economy was stopped. After 1978, when Mr. Deng Xiaoping came into the top leader, China began a reform and opening program, and has enjoyed a 20 years of rapid development. 
你是男是女香蕉用英语怎么说？你加入式怎么做？鱼香肉丝怎么做？北京西二旗附近有什么快餐店。你哦！她你嗯你听三年定期，这个存款利率是多少？你啊嗯什么？嗯你别你我明天嗯嘻嘻我嗯等你好，你好嗯天气怎么样？上一首你好！北京天气怎么样？你好，你好哦！哦！你你哦！嗯亿你天气怎么样？网络IPTV广东IPTV你输出正在连接你你要你好没有我们随便聊事，我们你说这都是什么呀？他们随便儿聊天儿肯定效果不好。这个说话就那特别真你走路角度，这个是不是又死啦？你挂掉了吗？你好，你好你行那行红就得认真说话龙哥他们客户是一个我觉得那样他们是什么哈行业背然后我们给他们发什么产品的时候最，然后我们给他们发什你这个这次就是带几个这个例那他你他们是做自助公安的多这个我想去取钱银行卡怎么办如果是这个电费的那他们是做在扣过一口也画的这么闲聊天儿的不，聊牙疼的不行就说你说呢我？我说确实不好嗯哼你你哦！嗯你好，你好上一首1234567嗯重病患者你每分钟呼吸18次美分血压，血压13715mm汞柱。全身皮肤未见黄染临表未触及肿大气管剧，气管哦！爱的开始空港医院，不是三产品实施