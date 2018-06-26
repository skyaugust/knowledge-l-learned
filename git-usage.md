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
 * Linux/UNIX/Android系统采用LF表示下一行
 * MAC系统采用CR表示下一行

### 本地仓库分支push到远程仓库

    git push <repository> <local banch name>:<branchname for remote repo>
    git push origin branch4Sth:branch4Sth 
    
### 挑选某些commit提交到目标分支上

    branchA> git log to display commit info
    
    commit 816f5313da9931643ddebe52b5eea92af2dbee69 (HEAD -> master, origin/master, origin/HEAD)
    Author: zhangguanjun <zhangguanjun@sinovoice.com.cn>
    Date:   Wed Feb 7 15:43:12 2018 +0800
    
    [CHG] 修改开发指南文档
    
    commit 565376ee22be35632f4b03a3d6d0718c11b224af
    Author: zhangguanjun <zhangguanjun@sinovoice.com.cn>
    Date:   Wed Feb 7 10:42:25 2018 +0800
    
    [CHG] MusicControl领域添加换一首歌的情景，并处理多个未处理的分支结尾。
    
    commit b151622a89a1d66193b792257547b816724f4125
    Author: zhangguanjun <zhangguanjun@sinovoice.com.cn>
    Date:   Tue Feb 6 11:44:07 2018 +0800
    
    [CHG] 添加集成文档 IntroductionOfHciBox。
    
    Pick commit b151622a 816f531 to branchB
    
    barnchB>git cherry-pick b151622a 816f531
    
若有冲突，使用git mergetool 解决


### 删除本地缓存的远程分支

本地会显示远程已被删除的分支，需要删除：

显示所有分支：

<p>

    aiot@aiot MINGW64 /e/workspace/studio_workspace/Git-Voice-Assistant-1.1 (branch4nearfield-dev)
    $ git branch -a
      branch4_wake9.0
      branch4huawei
      branch4huawei-wake9.0
      branch4nearfield
    * branch4nearfield-dev
      branch4nearfield_dianxin
      master
      remotes/origin/HEAD -> origin/master
      remotes/origin/branch4_wake9.0
      remotes/origin/branch4huawei
      remotes/origin/branch4nearfield
      remotes/origin/branch4nearfield-AIOT-50
      remotes/origin/branch4nearfield-AIOT-51
      remotes/origin/branch4nearfield-dev
      remotes/origin/branch4nearfield_dianxin
      remotes/origin/master
  
查看可以清理的远程分支，`*AIOT-50`,`*AIOT-51`,`*dev`三个分支在远程的orgin仓库中已删，本地可以清理：

 <p>

    aiot@aiot MINGW64 /e/workspace/studio_workspace/Git-Voice-Assistant-1.1 (branch4nearfield-dev)
    $ git remote prune origin --dry-run
    Username for 'http://10.1.0.11': aiot
    Pruning origin
    URL: http://10.1.0.11/android-app/voice-assistant/voice-assistant-tv.git
     * [would prune] origin/branch4nearfield-AIOT-50
     * [would prune] origin/branch4nearfield-AIOT-51
     * [would prune] origin/branch4nearfield-dev
     
清理：

<p>

    aiot@aiot MINGW64 /e/workspace/studio_workspace/Git-Voice-Assistant-1.1 (branch4nearfield-dev)
    $ git remote prune origin
    Username for 'http://10.1.0.11': aiot
    Pruning origin
    URL: http://10.1.0.11/android-app/voice-assistant/voice-assistant-tv.git
     * [pruned] origin/branch4nearfield-AIOT-50
     * [pruned] origin/branch4nearfield-AIOT-51
     * [pruned] origin/branch4nearfield-dev
     

再次查看

<p>

    aiot@aiot MINGW64 /e/workspace/studio_workspace/Git-Voice-Assistant-1.1 (branch4nearfield-dev)
    $ git branch -a
      branch4_wake9.0
      branch4huawei
      branch4huawei-wake9.0
      branch4nearfield
    * branch4nearfield-dev
      branch4nearfield_dianxin
      master
      remotes/origin/HEAD -> origin/master
      remotes/origin/branch4_wake9.0
      remotes/origin/branch4huawei
      remotes/origin/branch4nearfield
      remotes/origin/branch4nearfield_dianxin
      remotes/origin/master
      
### git恢复分支状态

    # 恢复
    git checkout .
    # 删除 untracked files
    git clean -f
     
    # 连 untracked 的目录也一起删掉
    git clean -fd
     
    # 连 gitignore 的untrack 文件/目录也一起删掉 （慎用，一般这个是用来删掉编译出来的 .o之类的文件用的）
    git clean -xfd
     
    # 在用上述 git clean 前，墙裂建议加上 -n 参数来先看看会删掉哪些文件，防止重要文件被误删
    git clean -nxfd
    git clean -nf
    git clean -nfd
    
### 修改commit message

重写最近一次提交的commit信息,[更详细](https://stackoverflow.com/questions/179123/how-to-modify-existing-unpushed-commits)
    
    git commit --amend -m "your new message"

### git status显示中文

中文路径或文件名显示为"\344\272\345"类似，修改如下配置：

    git config --global core.quotepath false

这些数字是八进制下的utf码。当字符编码值超过0x80（双字节以上的），都会显示为utf码。设置为false，则会正常显示
