# Android事件分发
View是单个“交互区域”，如TextView， EditText，Button，ImageView等控件。他们收到事件，自己处理完，给上层一个反馈，就完事了。

ViewGroup有一个或多个“交互区域”，是个树型结构，根节点是ViewGroup，叶子节点是单View。因此事件处理复杂一些。
## View中的MotionEvent事件处理

主要过程：View通过dispatchTouchEvent拿到MotionEvent，并调用onTounchEvent来处里，产生各种事件回调。boolean返回值告诉dispatchTouchEvent的直接者，这个View有无处理本次事件。

概要：

dispatchTouchEvent

	View.dispatchTouchEvent(MotionEvent event):
		拿到一个MotionEvent event
		第一个处理机会交给View.OnTouchListener.onTouch(View v, MotionEvent event), 开发者可以直接在此消费事件并返回true，结束事件分发。
		第二个处理机会交给View.onTouchEvent(event)。View本身有实现这个方法，同时这个方法是public的，意味着可以被子类重写。
		
		还有一个分支，是专门处理因安全原因不处理的情况

		以上分支，如果返回true，表明事件被消费了；否则没有被消费。（？？？上层拿到这个反馈有什么用？？？）
		
onTouchEvent，其返回值影响dispatchTouchEvent事件返回值。如果onTouchEvent返回false，dispatchTouchEvent一定返回false；如果前者返回true，后者在正常情况下，返回true。

	View.onTouchEvent(MotionEvent event):
		如果这个View是DISABLED，得到第一个处理机会，将会根据是否可点击表明是否已处理。
		如果这个View有TouchDelegate，将第二个得到处理机会。
		如果这个View CLICKABLE 或者 LONG_CLICKABLE，将第三个得到处理机会，此时会根据event的类型与View的属性产生具体的效果，比如调用performClick()来产生View.OnClickListener.onClick回调。

这里将onTouchEvent声明为pulic，是给View的继承者留了一个扩展的机会，可由继承者自行处理这个事件。

至于View的**事件从哪里来**(谁调的View.dispatchTouchEvent),**谁得到了View对事件的处理结果**（ dispatchTouchEvent的返回值），得到的**返回结果有什么影响**，需要再探索一下。

## ViewGroup中的MotionEven事件处理
ViewGroup是若干View类型的组合，保存在成员变量mChildren中：

	private View[] mChildren;

注意这里是View类型的组合，也就是可以包含View，View的子类，比如ViewGroup。

	@Override
	ViewGroup.dispatchTouchEvent(MotionEvent ev):
		intercepted = onInterceptTouchEvent(ev)
		if(not intercepted):
			for each child in mChildren:
				child.dispatchTouchEvent(event)
		else:
			
			
		
		



				
			