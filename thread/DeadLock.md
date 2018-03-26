# 死锁示例

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