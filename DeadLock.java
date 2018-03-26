import java.util.concurrent.CountDownLatch;
public class DeadLock{
    private static Object lockA = new Object();
    private static Object lockB = new Object();
    private static Boolean condition = false;
    private static CountDownLatch waitThreadA_hold_lockB = new CountDownLatch(1);
    private static CountDownLatch waitThreadB_hold_lockA = new CountDownLatch(1);

    static class TaskA implements Runnable {
        public void run(){
            synchronized(lockB){

                System.out.println("TaskA hold lockB and ready requires lockA");
                waitThreadA_hold_lockB.countDown();
                try {
                    waitThreadB_hold_lockA.await();
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
                waitThreadB_hold_lockA.countDown();
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
            waitThreadA_hold_lockB.await();
        } catch (Exception e) {
            //TODO: handle exception
        }
        threadB.start();

    }
}