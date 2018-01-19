# InputService的生命周期
InputEasyService.onCreate() 输入法服务被创建时调用

	-super.onCreate()
		-父抽象类InputMethodService持有一个Dialog SoftInputWindow,用来放置输入法视图
		-iniViews()：该方法只在onCreate和onConfigurationChanged中调用
			-mRootView = mInflater.inflate(com.android.internal.R.layout.input_method, null);
				-布局文件R.layout.input_method描述了inputArea, candidatesArea等元素
			-mWindow.setContentView(mRootView);
	-注册广播，初始化KB jni， 初始化 hcicloud sdk, 初始化hwr 

InputEasyService.bindInput() 绑定输入法到新的应用环境上。一般只调用一次。

	-InputEasyService.initialize()
		-InputEasyService.onInitializeInterface() 被调用。每initViews一次，回调一次。
        	-Hcicloud实现onInitializeInterface()：从键盘xml描述中，实例化各种键盘。

View InputEasyService.onCreateInputView() 输入区域视图被第一次弹出来时被调用。

	-确定输入法视图view的大小，类型等，将view返回给输入法服务，最终与mRootView的R.id.inputArea绑定。
	-HciCloud的实现中，构建了一个ViewParent类，返回给输入法服务，这个ViewParent包含了inputArea与candidatesArea的功能。
	-如果后面的onStartInputView不做任何处理，这里将显示ViewParent中的默认键盘。

InputEasyService.onCreateCandidatesView()  候选字区域第一次显示时，被调用。
	
	-HciCloud没有单独创建CandidatesView	

InputEasyService.onStartInput(EditorInfo attribute, boolean restarting) 当应用中的某个editor开始需要文本输入时，该方法回调。比如editor获取到焦点。

	-HciCloud在这里做清除与上个eidtor交互过的数据。
InputEasyService.onStartInputView(EditorInfo attribute, boolean restarting) 当输入法键盘要弹出时，此方法回调。一般可在这里处理与一些特定view相关的处理，比如选择显示什么样的键盘
	
	-HciCloud重写此方法，主要按照attribute切换到同的键盘
	-如果HciCloud对此方法子类不重写，将使用ViewParent的默认键盘
	-以switch2En26为例：
		-mViewParent.switch2InputEasyView(): ViewParent的键盘区显示承载各种键盘的InputEasyView
		-mInputView.setKeyboard(mInputLastQwertyENKeyboard):设置InputEasyView为mInputLastQwertyENKeyboard
		-mInputView.update()
			-mInputView.invalidate()
				-mInputView.onDraw(Canvas canvas)
					-mCurKeyboard.draw(canvas)
						-mBackgroud.draw(canvas)
		-mInputView.requestLayout()
	
InputEasyService.onDestory() 输入法服务被销毁时调用
 -注销广播，释放hcicloud sdk以及反初始化个能力