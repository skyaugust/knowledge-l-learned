## Git常用操作

### 从svn迁到git

已存在的svn项目:
`http://cvs:8080/svn/smartappdev/hcicloudextensionsdk/voiceui/Tv-Voice-Assitant/Tv-Voice-Assitant-1.0/trunk/code/TvVoiceAssistant`

	mkdir tvvoiceassistant
	cd tvvoiceassistant
	git svn clone http://cvs:8080/svn/smartappdev/hcicloudextensionsdk/voiceui/Tv-Voice-Assitant/Tv-Voice-Assitant-1.0/trunk/code/TvVoiceAssistant
	git remote add origin git@10.1.0.11:android-app/voice-assistant/tv-voice-assistant.git
	git push -u origin --all
	
	
### 从服务器仓库做类似svn的update操作

git fetch方式，手动merge

    git fetch origin master:tmp
    git diff tmp 
    git merge tmp
    
或者 git pull, 自动merge

    git pull origin master
    
### Gitlab 重命名仓库

1. Gitlab设置界面修改仓库信息
 在项目的设置-常规-高级设置中重命名版本库。生效后，项目主页已生效
 
2. 修改本地仓库信息
 远场已修改，本地记录的远程仓库名称也要更新
 * git remote -v
 
    列出本地记录的远程仓库url, 比如有origin的
 * git remote set-url origin git@github.com:username/newrepo.git

    完成修改

### 换行符的问题。Windows和Android的区别

大家在使用Git时，最好配置一下如下指令，禁用windows环境和Linux环境下换行符不同的智能检测转换， 因为我们都是用的windows开发的，所以执行了下面的指令关闭Git的这个转换，不然一些文件可能会出问题。
git config --global core.autocrlf false

 * CR(Carriage Return) 代表回车，对应字符 '\r'
 * LF(Line Feed) 代表换行，对应字符 '\n'
 * DOS/Windows系统采用CRLF(即回车+换行)表示下一行
 * Linux/UNIX系统采用LF表示下一行
 * MAC系统采用CR表示下一行
