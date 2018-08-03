# Create DLL using Visual Studio 2017

References:

1. [walkthrough-creating-and-using-a-dynamic-link-library-cpp](https://docs.microsoft.com/zh-cn/cpp/build/walkthrough-creating-and-using-a-dynamic-link-library-cpp)
23.
2. [
解决_CRT_SECURE_NO_WARNINGS 警告](https://blog.csdn.net/iesneaker/article/details/63282780)

## Create Empty DLL Project

Guided with Ref1, we create a empty project named AggregationSDK. 
It includes those baisc files:

    AggregationSDK
        -AggregationSDK.sln #Microsoft Visual Studio Solution File
        -AggregationSDK
            -AggregationSDK.cpp #Defines the exported functions for the DLL application.
            -AggregationSDK.vcxproj #Project Properties.
            -AggregationSDK.vcxproj.filters #Project Properties.
            -AggregationSDK.vcxproj.user #Project Properties.
            -dllmain.cpp # Defines the entry point for the DLL application
            -stdafx.cpp # source file that includes just the standard includes
            -stdafx.h #include file for standard system include files or frequency files.
            -targetver.h #Including SDKDDKVer.h defines the highest available Windows platform.

### add source file and head file into project

### add include files hcicloudsdk to project
o
### add binx