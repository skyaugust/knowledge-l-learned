# Activity's lifecycle

Activity是Android框架中的重要组件。所谓框架，即Android开发中，系统已经准备好了Activity的运行环境，控制了生命周期，开发者
只需要在指定的生命周期环节完成业务逻辑即可。本文主要考察系统是为Activity准备的运行环境以及如何控制其生命周期。

## ActivityThread

此类包含了main方法，是应用所在进程的入口，相当于mainThread的'run'方法。在这个方法中，系统将负责接受屏幕响应类（背后与具体的系统进程通信），负责控制组件与UI的manThread所在进程联系起来。


> 注意： android.app.ActivityThread在源码中被注解为`@hide`，在Android sdk编译时，在`android.jar`被删掉的，所以在正常发布的`android.jar`中是看不到的，进而在Android studio中也是找不到反编译源码的。可以在sourcecode下的android.app包找到。


`main`方法不长，且很重要，因此贴上所有代码：

	   1.  public static void main(String[] args) {
       2.    SamplingProfilerIntegration.start();
	   3.    
       4.    // CloseGuard defaults to true and can be quite spammy.  We
       5.    // disable it here, but selectively enable it later (via
       6.    // StrictMode) on debug builds, but using DropBox, not logs.
       7.    CloseGuard.setEnabled(false);
       8.    
       9.    Process.setArgV0("<pre-initialized>");
		
      10.    Looper.prepareMainLooper();
      11.    if (sMainThreadHandler == null) {
      12.        sMainThreadHandler = new Handler();
      13.    }
	  14.    
      15.    ActivityThread thread = new ActivityThread();
      16.    thread.attach(false);
	  17.    
      18.    if (false) {
      19.        Looper.myLooper().setMessageLogging(new
      20.                LogPrinter(Log.DEBUG, "ActivityThread"));
      21.    }
	  22.    
      23.    Looper.loop();
	  24.    
      25.    throw new RuntimeException("Main thread loop unexpectedly exited");
      26.  }


line2 与line7 的`SamplingProfilerIntegration`是系统性能分析类。其中`CloseGuard`与StrickMode有关，在开发阶段开启严苛模式可辅助检查一些性能、内存使用问题。

line9 的`Process`是与系统进程交互的工具，这里作用暂不分析。

line10~line13 给mainThread创建一个Looper，再通过line23 的Looper.loop()使mainThread进入一个"无限循环"的状态，在这个状态中，mainThread不断响应处理handler发来的消息，这就是所谓的UI单线程模型。

> UI单线程模型：几乎在所有的UI显示系统中，均采用这种单线程的模式。同时将任务(task)与执行(run)分离，task由业务侧实现，run由线程侧调度执行。

line15~line16 mainThread主动将ActivityThrad类与物理显示系统关联(`thread.attach(false)`)起来，物理显示系统的进程将通过ActivityThread的中的mHandler发消息给mainThread的looper，进一步驱动mainThread下运行的各种组件，如Activity。

因此下一步，我们分析下`ActivityThread`的attach方法。

attach接受boolean参数，若为false，表明

