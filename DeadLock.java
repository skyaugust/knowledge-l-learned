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