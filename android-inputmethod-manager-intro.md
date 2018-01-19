# InputMethodManager

普通应用可通过此API与Android的**输入法框架(IME)**交互。
## IME架构

Android中的**输入法框架(IME)**主要包含三部分：

1.	**input method manager**：管理与所有应用的输入法交互接口。对于每个应用来说，这个类相当于输入法服务的client-side的api。
2.	**input method（IME）**：由输入法开发者遵循输入法服务开发接口所实现。比如灵云智能输入法，搜狗输入法。
3.	**client applications**

## 应用端
Android应用若使用标准的TextView及其子类来处理文本输入，基本上不用直接与IME发生交互，IME将自动监听TextView的输入情况来自动完成工作。也有需要直接交互的：

1. 为textview设置合适的inputType取值, 以提示IME应该弹出哪一种键盘，比如数字键盘，英文键盘。
2. 设置合适的windowSoftInputMode取值, 处理好输入法键盘区与当前应用显示区的屏幕占比关系。比如当输入法弹出的时候，指定当前界面是保持原样，还是被推上去，还是只显示编辑控件等。
3. 直接弹出或关闭键盘

## IME
IME本身继承于 InputMethodService来实现，是一个Service。同时要实现InputMethod 接口。

## 安全

通过IME可以收集或监控UI上的输入活动，存在安全问题。所以google在设计IME架构的时候，做了一些约束：

1. 只有系统才能访问某一个IME的InputMethod方法。可以防止第三方偷换输入法。
2. 后台可以存在多个输入法进程，但同时只能同一个交互
3. 切换输入法需要用户手动确认

# InputConection
开发输入法时，通过此接口向应用返回数据。主要有：

1. Read text around the cursor;
2. Commit the text to the textbox;
3. Send raw key events to the application.

在应用侧，开发着需要实现View.onCreateInputConnection来返回一个InputConnection的实例。这样，输入法与应用就串起来了。Android在TextView中已经实现了此方法，因此每创建一个TextView类型的对象，都会与输入法发生关联。






