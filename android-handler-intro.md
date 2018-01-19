# Android 中的Handler
Java Thread的生命周期，对于开发者而言，从run方法入口，表明该线程创建成功，然后在run方法中执行若干业务代码后，从run方法离开，表明该线程关闭。

如果启动的线程需要长时间运行, 一般的处理方式是使用一个while(isDoMoreThing)循环，往复执行，每次都检查isDoMoreThing来控制。

有了线程运行的方案，下面就看下线程间通信。一般有两种方式：

1. 共享内存。也就是两个线程通过读写同一个数据变量来保持通信。通常情况下，可能有多个共享的数据变量，且类型多种多样。带来的问题是条件竞争，锁的问题。同时还需要自行处理线程的状态问题，比如阻塞，挂起等。
2. 消息队列。共享同一个消息队列，本质上也算共享内存，但从消息队列这种生产-消费者模型，可以很好地处理竞争，锁的问题。

在代码中使用handler，可以发送Message或Runnable对象到与该handler相关关联线程的MessagesQueue中。如果messagesQeueu是一种阻塞队列，使用者还能避免使用低级的并发操作去挂起或唤醒线程。

Handler机制属于第二种，在线程中增加一个消息队列，外部线程使用handler用来发送消息（生产者），本线程使用handleMessage回调处理消息（消费者），同时该消息队列为阻塞队里，当消息队里中没有消息时，本线程（消费者）被自动阻塞，直到有消息插入或打断线程。


## Thread with Handler
一个普通的线程如何与Handler结合起来呢？

	class LooperThread extends Thread {
		public Handler mHandler;
		public void run() {
			Looper.prepare()
			mHandler = new Handler() {
				public void handleMessage(Message msg) {
					// process incoming messages here
				}
			}
			Looper.loop();
		}
	}

`Looper.prepare()` 为当前线程创建了一个Looper对象，Looper对象中创建一个消息队里，而Looper对象本身放在的ThreadLocal变量中。

`mHandler = new Handler(){}` 为当前线程创建了一个发送-接受消息的handler，一般这个handler的引用传给任意线程担当消息的生产者；当前线程中实现的handlerMessage,消费消息。

`Looper.loop()` 启动内部的looper对象进入内部的while循环，处理消息。注意这里只是进入一个循环执行的状态，若干调用looper对象的其他方法，比如quit(), quitSafely(), 仍然是可以响应的。

`mLooper.quit()` or `mLooper.quitSafely()` 时Looper.loop()结束，进而线程的run方法结束。