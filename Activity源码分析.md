# Activity 

Activity是Android应用中实现与用户直接交互的基本组件。开发者继承一个Activity，实现其定义的生命周期方法，即可展示一个显示在系统屏幕上的界面。

## ActivityThread类

类似jvm上运行的每一个进程从main方法开始，我们编写的Android应用从ActivityThread的main方法出发。
主要启动了一下工作：
1. 为主线程初始化了一个MainLooper。当运行到我们自己写的代码的时候，MainLooper已经就绪了，因此我们通过
Looper.getMainLooper()获取主线程的Looper，从而做到与主线程通信，比如通过主线程更新UI，将指定的接口方法在主线程中调用。
这里有几个面试点：
 * Handler与Looper机制：可另仔细分析；
 * Looper.loop()是个死循环，为什么不会卡死？目前猜测与线程的运行挂起阻塞等待等状态管理有关。对于主线程而言，只要应用有活动，基本都在运行，很难有消息队列为空的现象。如果消息处理不及时，从用户体验上看，就会产生卡顿，甚至ANR
 * ANR 的产生机制

 2. 在准备好MainLooper之后，创建一个ActivityThread对象，调用attach 在该方法中，做了
  * 为ViewRootImpl的sFirstDrawHandlers添加了一个小任务，用来开启jit。
  * 与AMS建立binder连接：
            RuntimeInit.setApplicationObject(mAppThread.asBinder());
            final IActivityManager mgr = ActivityManagerNative.getDefault();
            try {
                mgr.attachApplication(mAppThread);
                
  RuntimeInit在进入ActivityThread main
  之前，就已经开始运转了，关于从点击应用图标的启动过程，应该与此有关，可进一步分析了解ZygoteInit.java.这行代码创建了一个mAppThread.asBinder() IApplicationThread binder，并存放在RuntimeInit中，可用于与系统吧的AMS服务交互，比如由AMS服务发起启动一个新的Activity（scheduleLaunchActivity）或者由于屏幕事件或者其他用户操作，暂停一个Activity（schedulePauseActivity）
  * 监控heap使用限定检查，如果使用量超过总量的75%，就会通过IActivityManager mgr向AMS请求释放一些activitys。扩展知识点：系统为应用分配的heap大小，如何调节等
  
  到这里后，ActivityThread main 主线程就进入一个待响应状态，所有的任务都通过主 handler下发执行。
  3. 主Handler H的创建与使用：
   * main方法中，Looper.prepareMainLooper, 为当前线程（主线程）在Looper的类静态成员sThreadLocal下挂一个与该线程映射的Looper。该Looper持有一个MessageQueue与该线程引用。然后在任何线程的执行环境下，调用Looper.getMainLooper()，都可以得到主线程的Looper，进一步可通过此Looper向主线程发送message。
   * 在主线程创建完Looper后，紧接着ActivityThread thread = new ActivityThread();按照java类成员的初始化过程，此时执行H mH = new H();H集成的Handler的默认构造函数中获取当前执行线程(mainThread)的Looper以及MessageQueue。之后，便可以通过mH来send各类消息了。
   * 主Handler H处理的消息类型有54种（android-25）：控制Acitivy生命周期的（LAUNCH_ACTIVITY，PAUSE_ACTIVITY,...），控制Service生命周期的（CREATE_SERVICE,STOP_SERVICE, ... ）,控制window的（SHOW_WINDOW，HIDE_WINDOW, ...）, 通知环境变化的（CONFIGURATION_CHANGED，ACTIVITY_CONFIGURATION_CHANGED，LOW_MEMORY，...）;
   * 每种消息的发送，在ActivityThread的内部类ApplicationThread中都有一个public方法来处理，比如LAUNCH_ACTIVITY -> ApplicationThread.scheduleLaunchActivity.
   * ApplicationThread 继承实现binder，主要是IApplicationThread接口。即上面提到的与AMS通信的binder
 4. 总结：
   * 系统AMS事先已准备就绪；
   * 每个新创建的应用进程，通过ActivityThread与AMS使用binder通信，由AMS下发各类事件，ActivityThread作出响应；
   * 由ActivityThread中的ApplicationThread（ a binder） 与AMS通信；
   * 由ActivityThread中的H extends Handler响应ApplicationThread的binder调用；
   * 由ActivityThread中的MainLooper.handlerMessage处理AMS的消息，产生各种应用层的回调（Activity.onCreate, Service.onCreate）
   
  ## 最初的若干main handler处理

  
## 创建一个Activity的过程

Activity.startActivityForResult(intent, resquestCode)
  Activit.mParent.startActivityForResult(intent, resquestCode)
     mInstrumentation.execStartActivity(mMainThread.getApplicationThread, intent, resquestCode)
         ActivityManagerNative.getDefault().startActivities(applicationThread, intent, resquestCode)
             ActivityManagerProxy.startActivity(applicationThread, intent, requestCode)
                   encapsulate (applicationThread, intent, requestCode) into data
                   mRemote.transact(START_ACTIVITY_TRANSACTION, data, ...)
                   mRemote.onTransact(code, data)
                      onTransact中的代码在AMS进程中执行
                      ActivityManagerService.startActivity(applicationThread, intent, requestCode)
                         ActivityManagerService.startActivityAsUser(applicationThread, intent, requestCode）
                              ActivityStarter.startActivityMayWait(applicationThread, intent, requestCode)
                                  ActivityStarter.startActivityLocked(applicationThread, intent, requestCode)
                                  
                                  
                      
                   
                 
         
     
  
 

public static void main(String[] args) {
        SamplingProfilerIntegration.start();

        // CloseGuard defaults to true and can be quite spammy.  We
        // disable it here, but selectively enable it later (via
        // StrictMode) on debug builds, but using DropBox, not logs.
        CloseGuard.setEnabled(false);

        Environment.initForCurrentUser();

        // Set the reporter for event logging in libcore
        EventLogger.setReporter(new EventLoggingReporter());

        Security.addProvider(new AndroidKeyStoreProvider());

        // Make sure TrustedCertificateStore looks in the right place for CA certificates
        final File configDir = Environment.getUserConfigDirectory(UserHandle.myUserId());
        TrustedCertificateStore.setDefaultUserDirectory(configDir);

        Process.setArgV0("<pre-initialized>");

        Looper.prepareMainLooper();

        ActivityThread thread = new ActivityThread();
        thread.attach(false);

        if (sMainThreadHandler == null) {
            sMainThreadHandler = thread.getHandler();
        }

        if (false) {
            Looper.myLooper().setMessageLogging(new
                    LogPrinter(Log.DEBUG, "ActivityThread"));
        }

        Looper.loop();

        throw new RuntimeException("Main thread loop unexpectedly exited");
    }

