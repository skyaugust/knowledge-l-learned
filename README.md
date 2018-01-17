##Git常用操作

###从svn迁到git

已存在的svn项目:
`http://cvs:8080/svn/smartappdev/hcicloudextensionsdk/voiceui/Tv-Voice-Assitant/Tv-Voice-Assitant-1.0/trunk/code/TvVoiceAssistant`

	mkdir tvvoiceassistant
	cd tvvoiceassistant
	git svn clone http://cvs:8080/svn/smartappdev/hcicloudextensionsdk/voiceui/Tv-Voice-Assitant/Tv-Voice-Assitant-1.0/trunk/code/TvVoiceAssistant
	git remote add origin git@10.1.0.11:android-app/voice-assistant/tv-voice-assistant.git
	git push -u origin --all