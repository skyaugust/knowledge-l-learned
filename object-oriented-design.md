# Object Oriented 面向对象设计讨论
## 基本原则

### 单一职责
类、方法、模块有且只有一个原因能能被修改。
   
   这个原因具体可以是业务原因，比如用户管理是一个业务，数据下载是一个业务，不会因为后者这个业务改变，而去修改用户管理的代码。

好处：

		a. 类的复杂性降低，实现什么职责都有理了清晰明确的定义。
		b. 可读性提高
		c. 可维护性提高。
		d. 类变更引起的风险变更


### 里氏替换原则 LSP
所有引用基类的地方必须能透明的使用子类对象。

		a. 子类完全实现父类
		b. 子类可以有自己的个性
		c. 子类中的父类方法参数可以被放大
		d. 子类中的父类方法结果可以被缩小
	

缺点:

		继承是侵入性的——只要继承，就必须拥有父类的属性和方法；
		降低代码的灵活性——子类必须拥有父类的属性和方法，让子类自由的世界多了些约束；
		增强了耦合性——当父类的属性和方法被修改时，必须要考虑子类的修改。
	
### 依赖倒置原则 DIP
面向接口编程	最重要

基本要求: 抽象
  所谓倒置，就是A的实现依赖的是A的接口，从更高层面来说，就是先规定抽象，然后实现按照抽象所定义的去做。而不是以前那种，A实现，B实现，C实现，然后直接相互依赖。

好处：降低类间耦合，提高系统稳定性，降低并行开发危险，提高阅读和维护性
  
	    a. 模块间依赖由接口产生,不存在直接依赖，最直接的影响就是可以功能并行开发。
	    b. 接口和抽像类不依赖实体类
	    c. 实现类依赖接口或抽象类
	
规则：

    每个类都尽量有抽象
    变量的表面类型尽量使抽象
    具体类尽量不派生
    尽量不覆写基类方法
    结合了LSP 使用

		
### 接口隔离原则 ISP
接口和类尽量使用原子接口和原子类进行组装

含义：

		a. 接口尽量小
		b. 接口高内聚
		c. 定制服务
		d. 接口设计有限度，过小、灵活但是会导致复杂、开发难度提升
		
### 迪米特法则 LOD
一个类因该对自己需要耦合或者调用的类知道的最少，
	核心观念 类间解耦
	缺点：产生大量中间类或者跳转类，复杂性提高，难维护
	
### 开闭原则 OCP
 对扩展开放，对修改关闭。	最基础的原则，其他五个原则都是具体实现

## 单例模式

### 实现一：饥饿模式

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

### 实现二：饱汉模式

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

### 实现三：线程安全的饱汉模式

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

### 实现四：线程安全的饱汉模式

  通过减少synchronized的区域，只将创建实例的过程加锁，免去不必要的锁申请。那么锁的开销主要就是前期创建，总开销N*c中的N，就是个位数，一旦示例创建，instance不为null，都不会进入锁区。
  
  double check：当一个线程在锁区将要改变instance取值，另一个线程已经通过了第一个if(instance == null)的判断条件，前者改变instance取值离开锁区，后者进入锁区后，又重新改变instance，违背了单例模式，因此在进入锁区，需要重新检查instance。

  >double check 在延迟初始化场景中是较为常用的多线程保护方式。

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


### 实现五：使用volatile关键字的线程安全的饱汉模式
  
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

### 实现六：使用静态内部类的

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


### 实现七：使用枚举类
以上实现基于的创建都是通过new关键字。如果有人恶意地通过反射并setAccessible(true)修改Singleton.class的私有构造方法，进而创建额外的对象。可通过对构造方法做标记来防止多次创建。（问题：该标记如何保护）。另外对于序列化返序列化这种场景，需要额外的代码去控制不被重复创建。
枚举类可以避免以上问题。

    enum Singleton{
      instace;
      private int count = 0;
      void doSomething(){
        count ++
      }
    }

    Singleton.instace.doSomething();