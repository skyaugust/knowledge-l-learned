public class Hello<P, E>{
    P p;
    E e;
    public Hello(P p, E e){
        this.p = p;
        this.e = e;
    }

    public void sayHello(){
        System.out.println(p+" say hello to " + e);
    }

    

    public static void main(String[] args) {
        Hello hello = new Hello<String, String>("Tom", "Jerry");
        hello.sayHello();
        hello = new Hello<Integer, Integer>(1,"2");
        hello.sayHello();
    }    
}