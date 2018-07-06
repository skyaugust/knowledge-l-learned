# CMake

References:
1. [cmake.org](https://cmake.org)
2. [Cmake Intro](http://www.hahack.com/codes/cmake/)

## Single Source

    #include <stdio.h>
    #include <stdlib.h>
    /**
    * power - Calculate the power of number.
    * @param base: Base value.
    * @param exponent: Exponent value.
    *
    * @return base raised to the power exponent.
    */
    double power(double base, int exponent)
    {
        int result = base;
        int i;
        
        if (exponent == 0) {
            return 1;
        }
        
        for(i = 1; i < exponent; ++i){
            result = result * base;
        }
        return result;
    }
    int main(int argc, char *argv[])
    {
        if (argc < 3){
            printf("Usage: %s base exponent \n", argv[0]);
            return 1;
        }
        double base = atof(argv[1]);
        int exponent = atoi(argv[2]);
        double result = power(base, exponent);
        printf("%g ^ %d is %g\n", base, exponent, result);
        return 0;
    }


Write CMakeLists.txt for main.cc:

    cmake_minimum_required(VERSION 2.8)

    project(Demo1)

    add_executable(Demo main.cc)

Use cmake generate vs project

    E:\gitRepo\cmakelearn>cmake .
    -- Building for: Visual Studio 15 2017
    -- Selecting Windows SDK version 10.0.17134.0 to target Windows 6.1.7601.
    -- The C compiler identification is MSVC 19.14.26430.0
    -- The CXX compiler identification is MSVC 19.14.26430.0
    -- Check for working C compiler: E:/Program Files (x86)/Microsoft Visual    Studio/2017/Community/VC/Tools/MSVC/14.14.26428/bin/Hostx86/x86/cl.exe
    -- Check for working C compiler: E:/Program Files (x86)/Microsoft Visual    Studio/2017/Community/VC/Tools/MSVC/14.14.26428/bin/Hostx86/x86/cl.exe -- works
    -- Detecting C compiler ABI info
    -- Detecting C compiler ABI info - done
    -- Check for working CXX compiler: E:/Program Files (x86)/Microsoft Visual  Studio/2017/Community/VC/Tools/MSVC/14.14.26428/bin/Hostx86/x86/cl.exe
    -- Check for working CXX compiler: E:/Program Files (x86)/Microsoft Visual  Studio/2017/Community/VC/Tools/MSVC/14.14.26428/bin/Hostx86/x86/cl.exe -- works
    -- Detecting CXX compiler ABI info
    -- Detecting CXX compiler ABI info - done
    -- Detecting CXX compile features
    -- Detecting CXX compile features - done
    -- Configuring done
    -- Generating done
    -- Build files have been written to: E:/gitRepo/cmakelearn

Use Cmake-gui to chose vs 2008 verion.

