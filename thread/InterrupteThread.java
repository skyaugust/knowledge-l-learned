
public class InterrupteThread{
    static class MyTask implements Runnable{
        public MyTask(){}
        public void run(){
            try {
                System.out.println("thread sleeping ...");
                Thread.sleep(60*1000);
            } catch (Exception e) {
                //TODO: handle exception
            }
        }
    }
    public static void main(String[] args) {
        System.out.println("hello");
        Thread t = new Thread(new MyTask());
        t.start();

    }
}