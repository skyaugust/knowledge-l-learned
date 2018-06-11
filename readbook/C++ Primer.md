# C++ Primer

## 开始

与java运行在虚拟机上不同，C++运行在真实操作系统上的高级语言，不同操作系统之上的应用开发者，为了适应操作系统的环境，写出的C++程序千差万别。


### 名称空间

using 编译指令

### 函数

函数原型与函数定义。原型类似java中的方法签名，定义指实现部分。

using namespaces的作用域：与函数范围有关

1. using namespace std 在函数定义之前，文件中所有函数均可用std中的元素
2. using namespace std 在函数定义中，函数定义范围之内均可用std中的元素
3. using std::cout, 在函数定义范围内使用cout
4. 不使用using，可加前缀，在需要cout的地方使用std::cout,

## 处理数据

### 简单变量

从语言层面看，数据与信息存储在某个一个变量之中。这个变量实际就是内存指针的别名。操作符 `&` 作用到变量上，就可以拿到内存的地址

### 命名

使用字母数字下划线 && 数字不开头 && 不建议下划线开头

### 整型

int ,short, long, char

在`limits.h`中有以上四种数据的范围以及char的位数

可使用sizeof(int/short/long)获取到 int/short/long占据的字节数

char：字符，和小整数

bool：true or false，C++中非零值为true，0为false

### const限定符

`const int MONTHS = 12;`

### 浮点数

指数取值范围和有效数字取值范围的平衡
`+5.37E+16`

## 第四章 复合类型

## 数组

有其他类型创建的，都是复合类型。

`float loads[20]`

1. loads 的类型不是数组；
2. 是float数组
3. 强调此数组是由float类型创建的
4. 下标计数是不检查范围的

## 字符串

### char 数组

1. C-style string: 以'\0'结尾的char数组。
2. 很多库函数依赖于'\0'结尾这个信息。比如计数，比如计算长度。
3. char bird[10] = "012345678"; vs上，只能存9个可用字符，必须留一个给'\0'，否则编译器报错；
4. char bird[] = "0123456789"; 推荐这种做法，让编译器自己算。
5. (sizeof (bird) 为11 包括了'\0'
6. strlen(bird) 为10，将其作为字符串处理，长度不包含'\0'

### string

`#include<cstring>`

1. char数组是定长的字符串序列，而string是一个字符串实体。
2. 和java中的string属于同一概念
3. 比起char数组，在复杂操作上，string更简单，操作手段更直接简单

### 结构体

数组是同构的数据集合；结构体是异构的数据集合。

    struct inflatable
    {
        char name[20];
        float volume;
        double price;
    }

inflatable 成为新类型的名称

    inflatable hat;
    inflatable mainframe;

    hat.name来使用


#### 声明位置

在函数内部声明，成为局部声明，只为本函数使用；反之，称为外部说明，可供声明位置之后的所有函数使用。

#### 赋值

inflatable hat2 = hat// 复制一份，而非引用复制。


### 共用体（union），匿名共用体

