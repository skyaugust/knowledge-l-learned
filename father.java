import java.util.*;
public class father{
    public void doSomething(HashMap map){
        System.out.println("father doSomething using HashMap");
    }
    public static void invoke(){
        father son = new Son();
        Map<String, String> map = new HashMap();
        son.doSomething(map);
    }
    public static void main(String[] args) {
        invoke();
    }
}

class Son extends father{
    public void doSomething(Map map){
        System.out.println("Son doSomething using Map");
    }
}