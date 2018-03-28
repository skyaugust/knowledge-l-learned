import java.util.concurrent.CountDownLatch;
public class AlwaysDeadLock{
    private static Object lockA = new Object();
    private static Object lockB = new Object();
    
    private static Object waitThreadA_hold_lockB = new Object();
    private static volatile Boolean  threadA_has_held_lockB = false;
    private static Object waitThreadB_hold_lockA = new Object();
    private static volatile Boolean threadB_has_held_lockA = false;

    static class TaskA implements Runnable {
        public void run(){
            synchronized(lockB){
           
                System.out.println("TaskA hold lockB and ready requires lockA");
                 
                synchronized(waitThreadA_hold_lockB){
                    try {
                        threadA_has_held_lockB = true;
                        waitThreadA_hold_lockB.notify();
                        
                    } catch (Exception e) {
                        //TODO: handle exception
                    }
                }
                                      
                synchronized(waitThreadB_hold_lockA){
                    while(!threadB_has_held_lockA){
                        try {
                            waitThreadB_hold_lockA.wait();
                            
                        } catch (Exception e) {
                            //TODO: handle exception
                        }
                    }
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
          
                synchronized(waitThreadB_hold_lockA){
                    try {
                        threadB_has_held_lockA = true;
                        waitThreadB_hold_lockA.notify();
                    } catch (Exception e) {
                        //TODO: handle exception
                    }
                }
                
                synchronized(lockB){
                    System.out.println("TaskA hold lockA and lockB");
                }
            }
        }
    }

    public static void main(String[] args) {
        Thread threadA = new Thread(new TaskA(), "ThreadA");
        Thread threadB = new Thread(new TaskB(), "ThreadB");

        
        // wait threadA hold lockB.
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
     
        threadB.start();

    }
}