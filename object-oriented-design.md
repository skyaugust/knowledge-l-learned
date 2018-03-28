# Object Oriented 面向对象设计讨论
## 基本原则

 * 单一职责：类、方法、模块有且只有一个原因能能被修改。
   
   即每次修改此处的源码，都是一种



## 单例模式

### 饥饿模式

在类的加载时期就创建实例

  	class Singleton{
    	private static instance = new Singleton();
    	private Singleton(){}
    	private static Singleton getSingleton(){
      	return instance;
    	}
  	}

优点：线程安全，类加载期间只有一个线程参与；

缺点：过早创建，造成资源浪费

### 饱汉模式

在客户端第一次需要实例时创建


    class Singleton{
      private static instance = null;
      private Singleton(){}
      private static Singleton getSingleton(){
          if(instance == null) {
            return instace;
          }
      };
    }

  优点：延迟创建，节省资源；

  缺点：当前实现，线程不安全。

### 线程安全的饱汉模式实现一

使用synchronized对关键方法加锁

    class Singleton{
      private static instance = null;
      private Singleton(){}
      private static synchronized Singleton getSingleton(){
          if(instance == null) {
            return instace;
          }
      };
    }

    优点：延迟创建，节省资源，线程安全实现简单明了；

    缺点: 每个线程在调用getSingleton之前都会尝试获取锁，获取锁需要切换上下文，有固定开销。假设有N个线程，获取锁的开销是c, 总开销就是N*c。如果还有其他synchronized块，那这个开销会更高。

### 线程安全的饱汉模式实现二

  通过减少synchronized的区域，只将创建实例的过程加锁，免去不必要的锁申请。
  
  double check：当一个线程在锁区将要改变instance取值，另一个线程已经通过了第一个if(instance == null)的判断条件，前者改变instance取值离开锁区，后者进入锁区后，又重新改变instance，违背了单例模式，因此在进入锁区，需要重新检查instance。

    class Singleton{
      private static instance = null;
      private Singleton(){}
      private static Singleton getSingleton(){
          if(instance == null) {
            synchronized(Singleton.class){
              if(instance == null) {
                  instance = new Singleton();
              }
            }
            return instace;
          }
      };
    }

  这样存在两个假设：

  1. if(instance == null) 判断对于多个线程是确信的，也就是当一个线程改变了instance的时候，另一个线程在执行此判断能立即获取到instance的最新值；
  2. instance = new Singleton()语句，在分解为jvm指令执行时，先执行new Singelton，创建好实例了，然后在赋值给instance，这样根据假设1，其他线程会立即看到此变化，逻辑上是完备的。

  但实际上并非如此，假设1是不存在的，instance在一个线程中修改，其他的线程并不一定第一时间导这个修改；假设2也不存在，因为有指令重排优化机制，instance = new Singleton()这条语句并不保证先创建实例还是先修改instance取值。

  为了满足这两个假设，在java 1.5以后引入了volatile关键字，来起到线程间数据强制同步、禁止重排序的作用。

  只需在instance增加volatile声明即可。

### 使用volatile关键字的线程安全的饱汉模式实现三 
  
    class Singleton{
      private static volatile instance = null;
      private Singleton(){}
      private static Singleton getSingleton(){
          if(instance == null) {
            synchronized(Singleton.class){
              if(instance == null) {
                  instance = new Singleton();
              }
            }
            return instace;
          }
      };
    }

### 使用静态内部类的实现四

饥饿模式借用类加载机制，线程是安全，但在类加载的同时就创建了实例，造成资源浪费，那么能否即使用类加载机制，又能延迟创建对象呢？可以使用静态内部类，静态内部类只在需要的时候加载，同时在其加载的时候再创建实例。这里利用外部类可以访问静态内部类的私有变量，将创建语句包在静态内部类中即可。

    class Singleton{
      private static class Instance{
        private static Singleton instance = new Singleton();
      }
    
      private Singleton(){}
      private static Singleton getSingleton(){
          return Instance.instance;
      };
    }


### 使用枚举类

    enum Singleton{
      instace;
      private int count = 0;
      void doSomething(){
        count ++
      }
    }

    Singleton.instace.doSomething();