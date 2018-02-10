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