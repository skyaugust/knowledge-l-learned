# Unicode编码系
## Unicode
unicode是一种字符编码的规范，其[官网](http://www.unicode.org/ )的介绍：

	Unicode provides a unique number for every character,
	no matter what the platform,
	no matter what the program,
	no matter what the language.

也就是说，unicode是一种抽象编码，将世界范围内的每个字符与一个数字一一对应起来。而且并没有指定如何存储。即给定一个01串，如何解析出unicode，再进一步转换为对应的字符，可以有很多不同的做法。

目前的范围：`0000~10FFFF`,一共包含了2^21 = 2097152个字符，即可表达两百万个字符。
其中`0000~FFFF`称为`基本平面`,`01 0000~10 FFFF`为辅助平面
例子：`Android开发`的unicode对照：

	字符串：      A      n     d       r     o       i      d      开    发 
	unicode码：u+0041 u+006e u+0064 u+0072 u+006f u+0069 u+0064 u+5f00 u+53d1

这些值在unicode.org网站上都可以查询到。

常用中文的范围是`u4e00-u9fa5`
##UTF-32
编码规则：使用4个字节表示1个unicode码。

即`0000 0000~FFFF FFFF`的前`0010 FFFF `与`0000~10FFFF`一一对应起来。比如某个UTF-32编码的16进制流如下：

	0000 0041 0000 006e 0000 0064 0000 0072 0000 006f 0000 0069 0000 0064 0000 5f00 0000 53d1

那么根据UTF-32的编码规则，从头开始，每四个字节认为是一个字符，比如第1个四字节`0000 0041`，转换为unicode为`u+0041`，进一步查到其对于的字符数据，便可以点阵形式显示在屏幕上。

使用UTF-32的优点很明显，转为unicode的复杂度为O(1)；缺点也很明显，直观就可以看出，浪费了很多空间。特别是纯英文字符文件中，比ASCII编码多3个字节。因此实际中很少使用。

## UTF-16
编码规则：使用2个字节表示基本平面上的字符，使用4个字节表示辅助平面上的字符。
解码规则：考察每两个字节，如果这两个字节大于U+D800，表明这两个字节开始，加上后面两个字节，一共四个字节，表示辅助平面上的字符；否则，这2个字节表示基本平面上的字符。

那如何区分2个字节究竟是表示基本平面上的1个字符，还是需要与另外两个2节合起来表示辅助平面上的字符呢？这里用了一个很trick的方法。辅助平面`01 0000~10 FFFF`一共可表示2^20 个字符，需要2^20 位个空间。正好unicode的U+D800到U+DFFF是空区间，用U+D800到U+DBFF这10位与U+DC00到U+DFFF这10位，可表示2^20 个字符，前10位用两个字节，后10用两个字节，一共四个字节。

那么，对于一个二进制流，我们考察每两个字节，如果这两个字节大于U+D800，表明这两个字节开始，加上后面两个字节，一共四个字节，表示辅助平面上的字符；否则，这2个字节表示基本平面上的字符。

那四个字节如何计算出其真实的unicode码呢？

## UTF-8
编码规则：

1. 对于unicode的`0000~007F`，可用1个字节表示。第1位为`0`，表示这是一个单字节的字符，后面7位为unicode值，实际中，与ASCII值正好相同，故能兼容ASCII；
2. 对于unicode的`0080~07FF`，可用2个字节表示。前3位为`110`，表示这是一个双字节的字符，后面13位可转换为`0080~07FF`中的unicode值；
3. 对于unicode的`0800~FFFF`，可用3个字节表示。前4位为`1110`，表示这是一个三字节的字符，后面20位可转换为`0800~FFFF`中的unicode值；
4. 对于unicode的`01 0000~10 FFFF`，可用4个字节表示。前5位为`11110`，表示这是一个四字节的字符，后面的27位可转换为`01 0000~10 FFFF`中的unicode值

转换关系如下：


Unicode符号范围      | UTF-8编码方式

(十六进制)           | （二进制）

--------------------+---------------------------------------------
0000 0000-0000 007F | 0xxxxxxx

0000 0080-0000 07FF | 110xxxxx 10xxxxxx

0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx

0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx


解码规则：从第一位向后查，直到0为止，得到一个包含该0在内的"头"，判读是上面4个规则中的哪一个，然后进一步将后面若干位转换为unicode码。

##Java中的编码
java使用什么编码呢？
下面这段代码声明两个char字符，
    package com.example.testforanything;
    public class test {
      public static void main(String[] args) {
          char c1 = 'a';
          char c2 = '好';
          String s1 = "abcd你";
      }
     }

javac命令得到的字节码文件，查看16进制文件, 常量 "abcd你" 以utf-8方式存储。"61 62 63 64 E4 BD A0"


![img](http://10.1.0.11/wanqiangxin/knowledge/raw/master/hex-javaclass.bmp)


再看char c2 = '好'，以utf-16方式存储。"4F 60"


![img](http://10.1.0.11/wanqiangxin/knowledge/raw/master/hex-javaclass.bmp)

当然这些对我们都是透明的，我们只关心从Java上层中得到的编码格式。






 


