# 死锁

思路：
在同一时刻

ThreadA requires lockedA and holds lockedB;

ThreadB requires lockedB and holds lockedA;

以下代码运行后, 运行：

    >jps
    9232 GradleDaemon
    3508 DeadLock
    7012
    6668 Jps

查到DeadLock jvm进程号为3508, 运行`jstatck -l 3508`查看线程栈信息, 已自动分析出死锁。在windows下，可通过任务管理器杀死此进程。

    Found one Java-level deadlock:
    =============================
    "ThreadB":
      waiting to lock monitor 0x0000000057761768 (object 0x00000000d57b7b80, a java.lang.Object),
      which is held by "ThreadA"
    "ThreadA":
      waiting to lock monitor 0x0000000057764368 (object 0x00000000d57b7b70, a java.lang.Object),
      which is held by "ThreadB"

    Java stack information for the threads listed above:
    ===================================================
    "ThreadB":
    	at DeadLock$TaskB.run(DeadLock.java:28)
    	- waiting to lock <0x00000000d57b7b80> (a java.lang.Object)
    	- locked <0x00000000d57b7b70> (a java.lang.Object)
    	at java.lang.Thread.run(Thread.java:745)
    "ThreadA":
    	at DeadLock$TaskA.run(DeadLock.java:16)
    	- waiting to lock <0x00000000d57b7b70> (a java.lang.Object)
    	- locked <0x00000000d57b7b80> (a java.lang.Object)
    	at java.lang.Thread.run(Thread.java:745)

    Found 1 deadlock.


源码如下：

    public class DeadLock{
        private static Object lockA = new Object();
        private static Object lockB = new Object(); 

        static class TaskA implements Runnable {
            public void run(){
                synchronized(lockB){

                System.out.println("TaskA hold lockB and ready requires lockA");
                try {
                    Thread.sleep(4000); 
                } catch (Exception e) {
                    //TODO: handle exception
                }
                synchronized(lockA){
                    System.out.println("TaskA hold lockB and lockA");
                }
                }
            }
        }   

        static class TaskB implements Runnable {
            public void run(){
                synchronized(lockA){
                System.out.println("TaskB hold lockA and ready requires lockB");  
                System.out.println("TaskB' thread's state:"+Thread.currentThread().getState()); 
                synchronized(lockB){
                    System.out.println("TaskA hold lockA and lockB");
                }
                }
            }
        }   

        public static void main(String[] args) {
            Thread threadA = new Thread(new TaskA(), "ThreadA");
            Thread threadB = new Thread(new TaskB(), "ThreadB");    

            threadA.start();
            try {
                Thread.sleep(2000); 
            } catch (Exception e) {
                //TODO: handle exception
            }
            threadB.start();    

        }
    }

## 必死锁代码

上面的DeadLock类使用Thread.sleep来协调两个线程，故意产生死锁。这样做有一定的随机性，更好的办法是使用更好的线程协作机制来处理。如wait-notify机制，进一步可以使用CountDownLantch来简化，可查考Effective Java 2 第69条。

## wait-notify


就像一个团队中若干人员的协调一样，有的时候分开并行工作，某些时候需要停下来相互等待，大家一起做个同步等等。

wait notify为什么强制要求当前线程先获得monitor lock，然后在monitor lock上调用wait/notify？
两个原因：
* object.wait()会被任何一个线程调用object.notify() notifyAll() 所唤醒（所谓的虚假唤醒[Spurious wakeup](https://en.wikipedia.org/wiki/Spurious_wakeup) ）,这种情况并不合理，所以强烈推荐在while(condition){}中配合condition使用。condition作为一个临界数据，会在相配套的object.nofity的上下文修改，必须加锁。
* 线程和线程之间的协调，使用monitor lock本来就是自然的事情。


wait：

    synchronized(waitThreadA_hold_lockB){
                threadA.start();
                while(!threadA_has_held_lockB){
                    try {
                        waitThreadA_hold_lockB.wait();

                    } catch (Exception e) {
                        //TODO: handle exception
                    }
                }
            }

当前线程在进入等待状态，此时是持有waitThreadA_hold_lockB锁，
notify：

    synchronized(waitThreadB_hold_lockA){
                    try {
                        threadB_has_held_lockA = true;
                        waitThreadB_hold_lockA.notify();
                    } catch (Exception e) {
                        //TODO: handle exception
                    }
                }