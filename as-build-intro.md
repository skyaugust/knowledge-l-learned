# 构建的配置

Android编译系统将app resource, source code编译到一起，并打包成apk，进一步测试，部署，签名，分发.

Android studio使用Gradle提供的Android  plugin工具集来编译。

实际上gradle和Android plugin这套东西是独立于Android studio存在的。你可以通过命令行的方式编译。

## 构建过程

Gradle和Android plugin提供了非常丰富的工具将project转换为APK。构建过程简要如下：
![](https://developer.android.com/images/tools/studio/build-process_2x.png)

1. Compilers将源码与依赖资源转换为DEX文件，以及其他的Compiled Resources
2. APK Packager 将第一步的资源打成APK包。并签名。不签名是无法安装的设备上的。
3. 使用zipalign工具优化apk的体积。

最终得到一个debug版或release版的apk，下一步就测试，调试，部署，分发等工作。

## 自定义的构建配置

上面是一个最基本的流程。实际每一步都会有一个具体的命令来执行，那么每个命令都有参数和选项，不同的构建目的，命令的参数和选项都会有所不同。 Gradle以及Andorid plugin通过DSL的方式，将这种基于命令行的参数选项修改大为简化。

### Build Types
面向开发人员的一些参数。最常见的如debug type和release type，前者需要开启debug options, 使用debug key签名。后者需要shrink, 混淆，使用release key签名。这两套参数通过DSL的方式在build.gradle中配置生效。关于BuildType这个DSL对象的可以支持的构建参数，[参考这里](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.BuildType.html)。

### Product Flavors
面向最终用户的一些参数。比如免费版和收费版的应用是有区别的，这些区别我想在编译构建阶段使用参数控制，这类参数就是Product Flavors提供的。关于Product Flavors这个DSL对象的可以支持的构建参数，[参考这里](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.ProductFlavor.html)。

### Build Variants

这个其实是Product Flavors的一个扩展。Product Flavors有一个flavorDimensions属性，可以指定维度属性集合。Build Variants总的类型种类集合，就是每个flavorDimensions所参与Product Flavor 与Build Types的组合。

### Manifest Entries

### Dependencies
依赖管理。实际上上面的属于Gradle下的Android plugin, 这个属于gradle原生的功能。

### Signing
SigningConfig DSL对象，定义好之后，可以在Build Types中引用。

### ProGuard
proguardFiles 属性，在上述不同的DSL对象中是使用。可达到分场景混淆的目的。


### Multiple APK Support