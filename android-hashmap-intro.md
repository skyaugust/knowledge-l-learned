# Android中的HashMap实现
在Android N版本以下开发使用的java标准库，使用的是Apache Harmony的实现版本，与我们常见sun公司的OpenJDK 实现是不同的。在Android N及其以后版本，将使用Open JDK。这里我们先分析Apache Harmony版本的实现。
## HashMap的基本结构
HashMap的基础操作是放入<Key, Value>以及给定Key，取出指定的Value。
Hashmap中持有一个HashMapEntry[] table, 每一个table中存放一个链表，相同hashcode的key放在同一个链表中。table当前长度成为`capacity`,；当前HashMap最多能存放<Key, Value> pair的个数为`threshold`。一般，`threshold / capacity = 0.75`。

如果将HashMap看做一组桶，每个桶内可以放多个元素，那么所有元素的个数，最多是桶个数的3/4。

           +---------------------------------+
    table  |HashMapEntry|... ...|HashMapEntry|
           +-----|--------------------|------+
                 |                    |
                 V                    V
           +------------+       +------------+
           |HashMapEntry|       |HashMapEntry|
           +-----|------+       +-----|------+   
                 |                    |
                 V                    V
           +------------+            Null
           |HashMapEntry|   
           +-----|------+ 
				 |
                 V
                Null

     
##  Map的创建
对于默认的构造器`HashMap()`，最初的table长度为4 >>> 1，为2

    new HashMap()
    	table = EMPTY_TABLE
    		EMPTY_TABLE = new HashMapEntry[MINIMUM_CAPACITY >>> 1]
				MINIMUM_CAPACITY = 4

对于带capacity的构造器`HashMap(int capacity)`,

- 若capacity < 0 抛出 `IllegalArgumentException("Capacity: " + capacity)`
- 若capacity == 0， 同默认构造器，table长度为2
- 其他则确保在MINIMUM_CAPACITY(4) 与 MAXIMUM_CAPACITY(1M)之间选取一个与capacity最为接近的2^k做为table的长度。同时`threshold`设置为`3 / 4 * capacity`
