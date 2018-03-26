# Java中的线程
可以认为JVM中的进程提供独享的内存空间，在这些空间上运转的是线程。其中主线程是进程创建后的创建的第一个线程，入口就是main方法，类似于普通线程的执行的run方法。从main方法开始，就可以不断创建子线程，子线程又可以创建子线程，这些线程共享内存空间，同时通过cpu时间片轮转的方式交替执行。指令执行的特点是线程内顺序执行，线程间交替执行。

为什么会有线程出现？一个本质的原因： cpu的执行速度大大高于io，而现实业务中涉及io又非常多。假如只有一个线程的话，由于是顺序执行，遇到IO类操作，cpu相当于空转，极为浪费效率。如果cpu执行可以在多个代码执行任务间来回执行，cpu就得到有效利用。相当于同时可以做多事情。

每个线程在其生命周期内，只会在一个处理器上运行。那么多处理器对于多线程也是理所应当的。

## 创建

通过继承线程Thread类来创建一个实例：

    Thread t2 = new Thread(){
        @override
        void run(){
            // called in this new thread.
        }
    }

或：

    class MyThread extends Thread {
        @override
        void run(){
            // called in this new thread.
        }
    }

推荐的方式是先实现Runnable接口，然后通过Thread(Runnable r)构造方法创建线程。这样将任务（Runnable）与执行者（Thread）分离，可以有效地管理任务与线程。毕竟线程在系统中属于宝贵的资源。进一步可以通过了解Java并发库中提供的线程池库。

给你的线程起个名字，这在开发调试、监控运行、性能分析时都能起到良好的作用。否则默认的线程名称为"Thread-<nums>"，难以区分。

## 运行
最基本的方式就是由创建者调用start方法：

    t.start()

不要与run方法混淆。run是Runnable中定义的方法，将任务封装为标准的任务，线程在被start之后，线程自身会调用run方法中的代码，从而达到在新开线程中执行任务的目的。

推荐的方式是结合Java并发库，可以选用并发库提供的Executor，也可以按照业务的实际需求实现Executor。通过Exector的submit方法提交任务，将任务提交到线程池中，由线程池分配的某个线程来执行。

## 生命周期

Thread.java定义了6中状态：

    public enum State {
        /**
         * Thread state for a thread which has not yet started.
         */
        NEW,

        /**
         * Thread state for a runnable thread.  A thread in the runnable
         * state is executing in the Java virtual machine but it may
         * be waiting for other resources from the operating system
         * such as processor.
         * 在jvm中执行代码或者等待processor的处理
         */
        RUNNABLE,

        /**
         * Thread state for a thread blocked waiting for a monitor lock.
         * A thread in the blocked state is waiting for a monitor lock
         * to enter a synchronized block/method or
         * reenter a synchronized block/method after calling
         * {@link Object#wait() Object.wait}.
         * 被锁状态，与monitor lock有关
         * monitor lock：在JVM中，每个对象和类在逻辑上都是和一个监视器相关联的，
         * 为了实现监视器的排他性监视能力，JVM为每一个对象和类都关联一个锁，
         * 锁住了一个对象，就是获得对象相关联的监视器。从线程的角度看，当它试图获取一个对象的monitor lock
         * 的时候，发现已经被别的线程占用了，那它就进入此状态，直到通过获取这个monitor lock
         */
        BLOCKED,

        /**
         * Thread state for a waiting thread.
         * A thread is in the waiting state due to calling one of the
         * following methods:
         * <ul>
         *   <li>{@link Object#wait() Object.wait} with no timeout</li>
         *   <li>{@link #join() Thread.join} with no timeout</li>
         *   <li>{@link LockSupport#park() LockSupport.park}</li>
         * </ul>
         *
         * <p>A thread in the waiting state is waiting for another thread to
         * perform a particular action.
         *
         * For example, a thread that has called <tt>Object.wait()</tt>
         * on an object is waiting for another thread to call
         * <tt>Object.notify()</tt> or <tt>Object.notifyAll()</tt> on
         * that object. A thread that has called <tt>Thread.join()</tt>
         * is waiting for a specified thread to terminate.
         * 等待唤醒机制中的等待状态
         */
        WAITING,

        /**
         * Thread state for a waiting thread with a specified waiting time.
         * A thread is in the timed waiting state due to calling one of
         * the following methods with a specified positive waiting time:
         * <ul>
         *   <li>{@link #sleep Thread.sleep}</li>
         *   <li>{@link Object#wait(long) Object.wait} with timeout</li>
         *   <li>{@link #join(long) Thread.join} with timeout</li>
         *   <li>{@link LockSupport#parkNanos LockSupport.parkNanos}</li>
         *   <li>{@link LockSupport#parkUntil LockSupport.parkUntil}</li>
         * </ul>
         * 带有超时机制的等待唤醒机制中的等待状态
         */
        TIMED_WAITING,

        /**
         * Thread state for a terminated thread.
         * The thread has completed execution.
         * run方法结束后的状态，这种状态再start呢？
         */
        TERMINATED;
    }

## 内存布局

## Java并发库中的线程池

## 性能

# Android中的线程
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

### HandlerThread

### Object Locking
As mentioned in earlier chapters, some of the Java virtual machine's runtime data areas are shared by all threads, others are private to individual threads. Because the heap and method area are shared by all threads, Java programs need to coordinate multi-threaded access to two kinds of data: o instance variables, which are stored on the heap o class variables, which are stored in the method area Programs never need to coordinate access to local variables, which reside on Java stacks, because data on the Java stack is private to the thread to which the Java stack belongs.

In the Java virtual machine, every object and class is logically associated with a monitor. For objects, the associated monitor protects the object's instance variables. For classes, the monitor protects the class's class variables. If an object has no instance variables, or a class has no class variables, the associated monitor protects no data.

To implement the mutual exclusion capability of monitors, the Java virtual machine associates a lock (sometimes called a mutex) with each object and class. A lock is like a privilege that only one thread can "own" at any one time. Threads need not obtain a lock to access instance or class variables. If a thread does obtain a lock, however, no other thread can obtain a lock on the same data until the thread that owns the lock releases it. (To "lock an object" is to acquire the monitor associated with that object.)

Class locks are actually implemented as object locks. As mentioned in earlier chapters, when the Java virtual machine loads a class file, it creates an instance of class java.lang.Class. When you lock a class, you are actually locking that class's Class object.

A single thread is allowed to lock the same object multiple times. For each object, the Java virtual machine maintains a count of the number of times the object has been locked. An unlocked object has a count of zero. When a thread acquires the lock for the first time, the count is again incremented to one. Each time the thread acquires a lock on the same object, the count is again incremented. (Only the thread that already owns an object's lock is allowed to lock it again. As mentioned previously, no other thread can lock the object until the owning thread releases the lock.) Each time the thread releases the lock, the count is decremented. When the count reaches zero, the lock is released and made available to other threads.

A thread in the Java virtual machine requests a lock when it arrives at the beginning of a monitor region. In Java, there are two kinds of monitor regions: synchronized statements and synchronized methods. (These are described in detail later in this chapter.) Each monitor region in a Java program is associated with an object reference. When a thread arrives at the first instruction in a monitor region, the thread must obtain a lock on the referenced object. The thread is not allowed to execute the code until it obtains the lock. Once it has obtained the lock, the thread enters the block of protected code. When the thread leaves the block, no matter how it leaves the block, it releases the lock on the associated object.

Note that as a Java programmer, you never explicitly lock an object. Object locks are internal to the Java virtual machine. In your Java programs, you identify the monitor regions of your program by writing synchronized statements and methods. As the Java virtual machine runs your program, it automatically locks an object or class every time it encounters a monitor region.