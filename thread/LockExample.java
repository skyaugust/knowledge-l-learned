import java.util.concurrent.locks.Lock;
public class LockExample {
    private Lock lock = new Lock();
    private int count = 0;

    public int inc(){
        lock.lock();
        int newCount = ++count;
        lock.unlock();
        return newCount;
    }

    public int getCount(){
        return count;
    }

    public static void main(String[] args) {
        LockExample example = new LockExample();
        example.inc();
        System.out.println(example.getCount());
    }
    
}