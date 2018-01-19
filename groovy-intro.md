# Groovy入门
Groovy是运行在jvm上的一种脚本语言。是编写gradle的主要语言。
## 运行 Hello world
Android studio中按`ctrl+shift+a`，呼出快速指令查询窗口，输入`groovy console`, 进入groovy的脚本编辑器界面。

输入

	println 'Hello, world'

点击运行或`Ctrl+Enter`执行

## 基础 Basic 

### 简洁

    System.out.println("Hello, Java style")
    println("Hello, Java style");
    println("Hello, Java style")
    println "Hello, Groovy style"
    println 'Hello, Groovy style'
### 动态类型 Dynamic typing

	name = 1+2
	Sting name = 'sinovoice'
	// or
	def name = 'hcicloud'
    
### 字符串插值 String interpolation

	def name = 'aicloud'
	def greeting = "hello, $name"
	println greeting
	def name_size = "Your name has ${name.size()} chars"
### 方法 Methods
	public int square(int num) {
        return num * num
	}
	
	
	println square(2)
	def result = square 2
	println result
	
	def square2(def num) {
	    num++
	    num * num
	}
	
	println square2(2)

### 闭包 Clousures

	def square2(def num) {
	    num * num
	}
	
	def square = { num ->
	    num * num
	}
	
	square 8
	
	Closure square2 = {
	    it * it
	}
	
	square2 16

	Closure sqrt = {
		Math.sqrt(it)
	}

	sqrt 4

	def runClosure(Closure closure) {
	    closure()
	}
	
	runClosure({square2 5})
	runClosure(){square2 5}
	runClosure {square2 5}

	runClosure {
		squre2 5
		sqrt 4
	}

### 列表 Lists

    List list = [1,2,3,4,5]
    list.each {
        e -> println e
    }
    list.each {
        println it
    }

### 映射 Map

    Map map = [one:1, two:2, three:3]
    println map.get('one')
    println map['two']
    println map.three
    
    def print1(Map args, String message) {
        println args
        println message
    }
    
    print1(map, 'hello, print1(map, "msg")')
    print1 map, 'hello, print1 map, "msg"'
    print1 one:1, two:2, 'hello, print1 one:1 two:2, "msg"'



## 构建文件 The build file writen by Groovy

Example:

	
	apply plugin: 'com.android.application'
	// project.apply([])
	android {
	    compileSdkVersion 25
	    buildToolsVersion "25.0.2"
	
	    defaultConfig {
	        applicationId "com.sinovoice.hcicloudseed.devexample"
	        minSdkVersion 14
	        targetSdkVersion 25
	        versionCode 1
	        versionName "1.0"
	
	        testInstrumentationRunner "android.support.test.runner.AndroidJUnitRunner"
	
	    }
	    buildTypes {
	        release {
	            minifyEnabled false
	            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
	        }
	    }
	}

	Closure sqrt = {
    	println Math.sqrt(it)
	}
	
	dependencies {
		sqrt 2
	    compile fileTree(dir: 'libs', include: ['*.jar'])
	    androidTestCompile('com.android.support.test.espresso:espresso-core:2.2.2', {
	        exclude group: 'com.android.support', module: 'support-annotations'
	    })
	    compile 'com.android.support:appcompat-v7:25.1.0'
	    compile 'com.android.support.constraint:constraint-layout:1.0.0-alpha9'
	    testCompile 'junit:junit:4.12'
	}

