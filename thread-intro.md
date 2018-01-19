#Android中的线程
Android中的线程按其工作内容，可为两类：主线程与子线程。前者负责UI相关操作以及重要组件的生命周期控制，由系统创建；后者执行主线程职责之外工作，一般为耗时的操作，由开发者创建。

## 主线程
主线程在andorid.jar源码的android.app.ActivityThread类中，其中的main方法，正如一个普通的java程序入口，应用进程从这里开始。该类负责：
> This manages the execution of the main thread in an application process, scheduling and executing activities, broadcasts, and other operations on it as the activity manager requests.
> 
>执行主线程；调度与执行activities, broadcasts；由activity manager请求的操作。

在main方法中，创建一个MainLooper，所有希望由主线程执行的工作，都必须通过这个handler发消息给main thread来执行。

    public final class ActivityThread{
       ... ...
       public static final main(String[] args) {
           ... ...
           Looper.prepareMainLooper();
           ... ...
           
           Looper.loop();
       } 
    }


## 子线程
除了main方法所在的线程之外，由开发者创建的线程，都是子线程。可分为以下几类：

### Java Thread类
这是java基础的类，所有java层面的线程均由此类开始创建并执行。在初学Android的时候，经常会有这样的代码出现。

    new Thread(new Runnable(){
            @Override
            public void run(){
                // do something in the thread.
            }
        }).start;

这种做法的缺点：

1. 创建随意，破坏代码的整体风格
2. 没有指定线程的名称，在debug的过程中难以排查
3. 无法持有该Thread的引用，并通过引用控制线程
4. 缺乏抽象，导致到处都是类似代码
5. 可能影响基本组件的生命周期，导致内存泄露等问题


### AsyncTask
此类将一类问题做了一个抽象：
准备工作->工作执行->执行状态->任务结束。一般只在工作执行时需要运行在子线程，其他都会直接由主线程执行。

	class MyTask extends AsyncTask<String, Integer, Boolean>{

	    @Override protected void onPreExecute() {
			// run on mainThread
        }
        
	    @Override protected void onPostExecute(Boolean result) {
			// run on mainThread
        }

	    @Override protected void onProgressUpdate(Integer... values) {
			// run on mainThread
        }
        
	    @Override protected void onCancelled(Boolean result) {
			// run on mainThread
        }

	    @Override protected void onCancelled() {
			// run on mainThread
        }
        
	    @Override protected Boolean doInBackground(String... params) { 
			// run on non-mainThread        
            return null;
        }
	    
	}


优点：

1. 对通用问题建立通用的处理模板，便于业务处理
2. 隐式的线程切换，无需关心线程见如何通信。Android中不允许子线程直接修改UI，如果按照Java Thread这样的写法，需要在子线程run方法中**显示地**通过mainHandler与main thread交互

在AsyncTask有一个mainHandler，用来切换线程执行。注意这里是mainHandler，意味着这这个mainHandler必须在主线程中创建。尽管在Android 4.1 （API16）开始，系统在ActivityThread的main方法中会主动地触发AsyncTask中mainHandler的创建，这样就可以在任意的线程中创建asynctask,但鉴于asyntask的使用场景以及版本的兼容性，还是在主线程中创建为好。

缺点：
主要体现在生命周期，特别是如何停止正在执行的任务，释放资源。

AsyncTask的核心实现是将一个FutureTask提交到SerialExecutor中执行，并通过mainHandler实现代码执行环境的切换。当调用AsyncTask的cancel方法时，会调用FutureTask的cancel，之后再调用Future的isCanceled方法，就会告诉你这个FutureTask以及处于cancel状态了，但FutureTask中的call方法并不会提前结束。之后FutureTask正常结束后，AsyncTask会通过isCanceled方法决定调用onCanceled(Result)还是onPostExecute(Result)。

总而言之，cancel方法并不会直接打断doInBackgroud方法，而是等待其正常执行结束之后，再决定调onCanceled(Result)还是onPostExecute(Result)。


我们注意到AsyncTask的cancel方法还有一个boolean入参，若参入cancel(true), 会将FurtureTask所在线程的中断标志设置为true，向线程发个“通知”，你需要在run/call方法中响应这个标记来决定是否提前结束线程中的任务。这个有一定帮助，但碰到一些无法响应中断的情况，比如一些网络IO，就没办法了。

###HandlerThread

