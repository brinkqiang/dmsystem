# Awesome CMake [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

[<img src="https://rawgit.com/onqtam/awesome-cmake/master/cmake-logo.svg" align="right" width="100">](https://cmake.org/)

> 关于 [CMake](https://cmake.org/) 脚本、模块、示例和其他资源的精选列表

## 目录

- [Awesome CMake ](#awesome-cmake-)
  - [目录](#目录)
  - [社区](#社区)
  - [资源](#资源)
  - [包管理 / 构建系统](#包管理--构建系统)
  - [模块](#模块)
  - [实用脚本](#实用脚本)
  - [工具链](#工具链)
  - [示例 / 模板](#示例--模板)
  - [License](#license)

## 社区

* [Freenode 上的 cmake](http://webchat.freenode.net/?channels=cmake)
* [Reddit 上的 cmake](https://www.reddit.com/r/cmake/)
* [Reddit 上的 cpp](https://www.reddit.com/r/cpp/)
* [邮件列表](https://cmake.org/mailing-lists/)
* [Stack Overflow](http://stackoverflow.com/questions/tagged/cmake)

## 资源

* [最新文档](https://cmake.org/cmake/help/latest/)
* [FAQ](https://cmake.org/Wiki/CMake_FAQ)
* [Wiki](https://cmake.org/Wiki/CMake)
* [网络研讨会](https://cmake.org/webinars/)
* [CGold](https://github.com/ruslo/CGold) - CMake 的[指南](https://cgold.readthedocs.io)。[```[BSD2]```][BSD-2-Clause]
* [Modern CMake](https://github.com/toeb/moderncmake) - 现代 CMake **PDF** 和示例，由 [cmakepp](https://github.com/toeb/cmakepp) 的创建者编写。[```[MIT]```][MIT]
* [文章 - 轻松支持 CMake 安装和 find_package()](http://foonathan.net/blog/2016/03/03/cmake-install.html)
* [文章 - 使用 CMake 和 Git 轻松管理 C++ 依赖](http://foonathan.net/blog/2016/07/07/cmake-dependency-handling.html)
* [文章 - 使用 CMake 选择加入仅头文件库](https://steveire.wordpress.com/2016/08/09/opt-in-header-only-libraries-with-cmake/)
* [文章 - 现代 CMake 终极指南](https://rix0r.nl/blog/2015/08/13/cmake-guide/)
* [文章 - 常见的 CMake 反模式列表（2013 年但仍相关）](http://voices.canonical.com/jussi.pakkanen/2013/03/26/a-list-of-common-cmake-antipatterns/)
* [文章 - 如何构建基于 CMake 的项目](http://preshing.com/20170511/how-to-build-a-cmake-based-project/)
* [文章 - 15 分钟学会 CMake 脚本语言](http://preshing.com/20170522/learn-cmakes-scripting-language-in-15-minutes/)
* [文章 - CMake 的架构](http://aosabook.org/en/cmake.html)
* [讲座 - Effective CMake - Daniel Pfeifer, C++Now 2017](https://www.youtube.com/watch?v=bsXLMQ6WgIk)
* [文章 - 使用 CMake 构建跨平台 CUDA 应用](https://devblogs.nvidia.com/parallelforall/building-cuda-applications-cmake/)
* [教程 - 逐步理解 CMake](https://github.com/Wigner-GPU-Lab/Teaching/tree/master/CMake)
* [文章 + 讲座 - 拥抱现代 CMake - Stephen Kelly](https://steveire.wordpress.com/2017/11/05/embracing-modern-cmake/)
* [讲座 - CppCon 2017: Mathieu Ropert "现代 CMake 模块化设计"](https://www.youtube.com/watch?v=eC9-iRN2b04)
* [文章 - 现代 C++ 持续集成（尽管使用了非现代 CMake 如 ```include_directories()```）](https://juan-medina.com/2017/07/01/moderncppci/)
* [文章 - 是时候正确使用 CMake 了](https://pabloariasal.github.io/2018/02/19/its-time-to-do-cmake-right/)（关于 CMake 的最佳文章之一）
* 文章系列 - CMake 系列 - Martin Hořeňovský
    * [基础 CMake 用法](https://codingnest.com/basic-cmake/)
    * [基础 CMake，第二部分：库](https://codingnest.com/basic-cmake-part-2/)
* [讲座 - CMake 简介 - Florent Castelli, C++ Sweden 2018](https://www.youtube.com/watch?v=jt3meXdP-QI)
* [文章 - 一些实用准确的 CMake 技巧](http://bastian.rieck.me/blog/posts/2018/cmake_tips/)
* [文章 - 面向库开发者的现代 CMake](http://unclejimbo.github.io/2018/06/08/Modern-CMake-for-Library-Developers/)
* [文章 - 有效的现代 CMake：良好实践的总结 - Manuel Binna](https://gist.github.com/mbinna/c61dbb39bca0e4fb7d1f73b0d66a4fd1)

## 包管理 / 构建系统

* [hunter](https://github.com/ruslo/hunter) - C++ 的跨平台包管理器（基于 CMake ExternalProject）。[```[BSD2]```][BSD-2-Clause]
* [cget](https://github.com/pfultz2/cget) - CMake 包检索工具，用于下载和安装 CMake 包。[```[BOOST]```][BOOST]
* [cppan](https://cppan.org/) - C++ 存档网络 - 基于 CMake 的 C++ 包管理器，使用 C++14 实现。[```[APACHE2]```][APACHE2]
* [cpm](https://github.com/iauns/cpm) - 基于 CMake 和 Git 的 C++ 包管理器。[```[MIT]```][MIT]
* [conan](https://github.com/conan-io/conan) - Conan C++ 包管理器，使用 Python 实现并集成 CMake 后端。[```[MIT]```][MIT]
* [fips](https://github.com/floooh/fips) - 高级构建系统/依赖管理，用于分布式、跨平台 C/C++ 项目。[```[MIT]```][MIT]
* [Ninja](https://github.com/ninja-build/ninja) - 构建系统，主要特点：输入文件由高级构建系统（如 CMake）生成，并以最快速度运行构建。[```[APACHE2]```][APACHE2]
* [vcpkg](https://github.com/Microsoft/vcpkg) - 获取和构建 C++ 开源库的工具，内部使用 CMake 作为构建脚本语言。[```[MIT]```][MIT]

## 模块

* [cmake-modules](https://github.com/rpavlik/cmake-modules) - Ryan Pavlik 的 CMake 模块集合，包含众多查找模块（尤其是虚拟现实和物理模拟）、实用模块和 CMake 补丁。[```[BOOST]```][BOOST]
* [cmake-modules](https://github.com/bilke/cmake-modules) - 额外的 CMake 模块集合，多数来自 Ryan Pavlik。[```[BOOST]```][BOOST]
* [CMake](https://github.com/Eyescale/CMake) - Eyescale 的通用 CMake 模块。[```[BSD3]```][BSD-3-Clause]
* [sdl2-cmake-scripts](https://github.com/tcbrindle/sdl2-cmake-scripts) - 查找 SDL2、SDL2_image 和 SDL2_ttf 库及头文件的 CMake 脚本。[```[BSD2]```][BSD-2-Clause]
* [vfxcmake](https://github.com/nerdvegas/vfxcmake) - 常见视觉效果软件的 CMake 查找模块和通用实用代码。[```[LGPL]```][LGPL]
* [cmake-modules](https://github.com/jedbrown/cmake-modules) - 科学计算库的 CMake 模块。[```[BSD2]```][BSD-2-Clause]
* [cgcmake](https://github.com/chadmv/cgcmake) - 计算机图形相关应用的 CMake 模块。[```[MIT]```][MIT]
* [FindMathematica](https://github.com/sakra/FindMathematica) - Mathematica 的 CMake 模块。[```[MIT]```][MIT]
* [extra-cmake-modules](https://github.com/KDE/extra-cmake-modules) - KDE 的额外 CMake 模块和脚本。[```[BSD3]```][BSD-3-Clause]
* [FindICU.cmake](https://github.com/julp/FindICU.cmake) - 查找 ICU 库的 CMake 模块。[```[BSD2]```][BSD-2-Clause]
* [FindTBB](https://github.com/justusc/FindTBB) - 查找 Intel TBB 的 CMake 模块。[```[MIT]```][MIT]
* [cmake-modules](https://github.com/hanjianwei/cmake-modules) - hanjianwei 的 CMake 模块集合。[```[MIT]```][MIT]
* [YCM](https://github.com/robotology/ycm) - 用于 Yet Another Robot Platform 及其伙伴的额外 CMake 模块。[```[BSD3]```][BSD-3-Clause]

## 实用脚本

* [cotire](https://github.com/sakra/cotire) - 通过预编译头和 unity 构建加速 CMake 项目的编译过程。[```[MIT]```][MIT]
* [ucm](https://github.com/onqtam/ucm) - 管理编译器/链接器标志、收集源文件、预编译头、unity 构建等。[```[MIT]```][MIT]
* [cmakepp](https://github.com/toeb/cmakepp) - CMake 构建系统的增强套件。[```[MIT]```][MIT]
* [sugar](https://github.com/ruslo/sugar) - CMake 工具和示例：收集源文件、抑制警告等。[```[BSD2]```][BSD-2-Clause]
* [DownloadProject](https://github.com/Crascit/DownloadProject) - 在配置时下载外部项目源代码的 CMake 模块。[```[MIT]```][MIT]
* [buildem](https://github.com/janelia-flyem/buildem) - 基于 ExternalProject 的模块化 CMake 系统，简化构建。[```[LICENSE]```](https://github.com/janelia-flyem/buildem/blob/master/LICENSE.txt)
* [coveralls-cmake](https://github.com/JoakimSoderberg/coveralls-cmake) - 生成并上传 Coveralls JSON 覆盖率报告的 CMake 工具。[```[MIT]```][MIT]
* [compatibility](https://github.com/foonathan/compatibility) - cmake-compile-features 的改进版。[```[LICENSE]```](https://github.com/foonathan/compatibility/blob/master/LICENSE)
* [cmake-modules](https://github.com/Tronic/cmake-modules) - LibFindMacros 开发库和其他 CMake 工具。[```[LICENSE]```](https://github.com/Tronic/cmake-modules/blob/master/LibFindMacros.cmake#L2)
* [GreatCMakeCookOff](https://github.com/UCL/GreatCMakeCookOff) - 实用和非实用的 CMake 配方集合。[```[MIT]```][MIT]
* [cppcheck-target-cmake](https://github.com/polysquare/cppcheck-target-cmake) - 为 CMake 目标添加 CPPCheck 检查。[```[MIT]```][MIT]
* [clang-tidy-target-cmake](https://github.com/polysquare/clang-tidy-target-cmake) - 为 CMake 目标添加 clang-tidy 检查。[```[MIT]```][MIT]
* [cmake-unit](https://github.com/polysquare/cmake-unit) - CMake 单元测试框架。[```[MIT]```][MIT]
* [cmake-header-language](https://github.com/polysquare/cmake-header-language) - 确定头文件语言的 CMake 宏。[```[MIT]```][MIT]
* [tooling-cmake-util](https://github.com/polysquare/tooling-cmake-util) - 所有 polysquare CMake 工具的通用库。[```[MIT]```][MIT]
* [iwyu-target-cmake](https://github.com/polysquare/iwyu-target-cmake) - include-what-you-use 的 CMake 集成。[```[MIT]```][MIT]
* [sanitizers-cmake](https://github.com/arsenm/sanitizers-cmake) - 为目标启用 sanitizers 的 CMake 模块。[```[MIT]```][MIT]
* [cmake-precompiled-header](https://github.com/larsch/cmake-precompiled-header) - Visual Studio 和 GCC 的预编译头宏。[```[LICENSE]```](https://github.com/larsch/cmake-precompiled-header/blob/master/PrecompiledHeader.cmake#L31)
* [CMakePCHCompiler](https://github.com/nanoant/CMakePCHCompiler) - 通过自定义编译器扩展支持预编译头复用。[```[MIT]```][MIT]
* [CMake-codecov](https://github.com/RWTH-ELP/CMake-codecov) - 启用代码覆盖率并生成覆盖率报告的 CMake 目标。[```[GPL]```][GPL]
* [leatherman](https://github.com/puppetlabs/leatherman) - C++ 和 CMake 实用库集合。[```[APACHE2]```][APACHE2]
* [cmake-get](https://github.com/pfultz2/cmake-get) - 在配置或脚本模式下获取依赖。[无许可证]

## 工具链

* [dockcross](https://github.com/dockcross/dockcross) - Docker 镜像中的交叉编译工具链。[```[MIT]```][MIT]
* [android-cmake](https://github.com/taka-no-me/android-cmake) - Android NDK 的 CMake 工具链文件及脚本。[```[BSD3]```][BSD-3-Clause]
* [ios-cmake](https://github.com/cristeab/ios-cmake) - iOS 开发的 CMake 工具链文件及示例。[```[BSD3]```][BSD-3-Clause]
* [qt-android-cmake](https://github.com/LaurentGomila/qt-android-cmake) - 无需 QtCreator 构建和部署 Android 上的 Qt 应用。[```[LICENSE]```](https://github.com/LaurentGomila/qt-android-cmake/blob/master/license.txt)
* [mingw-w64-cmake](https://github.com/lachs0r/mingw-w64-cmake) - 基于 CMake 的 MinGW-w64 交叉工具链，用于构建 mpv 的 Windows 二进制文件。[```[ISC]```][ISC]
* [cmake-avr](https://github.com/mkleemann/cmake-avr) - AVR 的 CMake 工具链。[```[LICENSE]```](https://github.com/mkleemann/cmake-avr/blob/master/LICENSE)
* [arduino-cmake](https://github.com/francoiscampbell/arduino-cmake) - Arduino 平台的 CMake 项目设置。[```[MPL]```][MPL]
* [polly](https://github.com/ruslo/polly) - 跨平台构建和 CI 测试的 CMake 工具链文件和脚本集合。[```[BSD2]```][BSD-2-Clause]
* [toolchains](https://github.com/mosra/toolchains) - 用于 CMake 交叉编译，主要在 ArchLinux 上使用。[无许可证]
* [cmake](https://github.com/staticlibs/cmake/tree/master/toolchains) - CMake 工具链文件集合，主要用于静态链接。[```[APACHE2]```][APACHE2]

## 示例 / 模板

* [cmake-init](https://github.com/cginternals/cmake-init) - 用于可靠的跨平台 C++ 项目设置的 CMake 模板。 [```[LICENSE]```](https://github.com/cginternals/cmake-init/blob/master/LICENSE)
* [learning-cmake](https://github.com/Akagi201/learning-cmake) - 一个简单的 CMake 实践项目，包含一些不同的场景。 [```[GPL2]```][GPL2]
* [cmake_test](https://github.com/skebanga/cmake_test) - 使用 CMake 的小示例项目。 ```[NO LICENSE]```
* [android-cmake](https://github.com/forexample/android-cmake) - 使用 [ruslo/hunter](https://github.com/ruslo/hunter) 包管理器为 Android 应用提供的示例。 [```[BSD2]```][BSD-2-Clause]
* [hunter-simple](https://github.com/forexample/hunter-simple) - 使用 [ruslo/hunter](https://github.com/ruslo/hunter) 包管理器下载/安装依赖项的示例。 [```[BSD2]```][BSD-2-Clause]
* [weather](https://github.com/ruslo/weather) - 使用 [Hunter](http://github.com/ruslo/hunter) 跨平台包管理器构建的示例，使用 Boost、CppNetlib.URI、GTest、JSON Spirit。平台：Windows (Visual Studio)、Linux、Mac OS X + iOS。 [```[BSD2]```][BSD-2-Clause]
* [package-example](https://github.com/forexample/package-example) - find_package 配置模式的示例（针对 [这个](http://stackoverflow.com/questions/20746936/cmake-of-what-use-is-find-package-if-you-need-to-specify-cmake-module-path-an) Stack Overflow 问题）。 ```[NO LICENSE]```
* [CMakeTemplates](https://github.com/OutOfOrder/CMakeTemplates) - 用于每个游戏移植的初始 CMake 模板集。 ```[NO LICENSE]```
* [minimal_cmake_example](https://github.com/krux02/minimal_cmake_example) - 最小化的 CMake 示例，涵盖依赖项和打包。 [```[CC0-1.0]```][CC0-1.0]
* [cmake-example](https://github.com/bast/cmake-example) - 展示各种 CMake 特性的示例项目。 [```[BSD3]```][BSD-3-Clause]
* [cmake-examples](https://github.com/ttroy50/cmake-examples) - 以教程格式提供的有用 CMake 示例。 [```[MIT]```][MIT]
* [cmake-templates](https://github.com/district10/cmake-templates) - 一些 CMake 模板，包含 Qt、Boost、OpenCV、C++11 等。 [```[MIT]```][MIT]
* [CppProjectTemplate](https://github.com/Barthelemy/CppProjectTemplate) - 基本但完整的 C++ 项目，使用 CMake、Boost 和 Doxygen。 [```[MIT]```][MIT]
* [mini-cmake-qt](https://github.com/euler0/mini-cmake-qt) - 用于 Qt 5 项目的最小化 CMake 模板。 [```[LICENSE]```](https://github.com/euler0/mini-cmake-qt/blob/master/LICENSE)
* [CMake-VisualStudio-Example](https://github.com/cognitivewaves/CMake-VisualStudio-Example) - Visual Studio 开发者的 CMake 示例 - [博客文章](http://cognitivewaves.wordpress.com/cmake-and-visual-studio/)。 ```[NO LICENSE]```
* [Cpp-Project-Template](https://github.com/NewProggie/Cpp-Project-Template) - 包含 CMake 构建系统的 C++ 启动项目模板。 [```[MIT]```][MIT]
* [BASIS](https://github.com/cmake-basis/BASIS) - CMake BASIS 使创建可以共享的、互相协作的软件和库变得简单。 [```[BSD2]```][BSD-2-Clause]
* [OpenGL_CMake_Skeleton](https://github.com/ArthurSonzogni/OpenGL_CMake_Skeleton) - 使用 GLFW、Glew 和 glm 的现成 CMake 骨架。 [```[MIT]```][MIT]
* [coveralls-cmake-example](https://github.com/JoakimSoderberg/coveralls-cmake-example) - 用于 [coveralls-cmake](https://github.com/JoakimSoderberg/coveralls-cmake) 的示例项目。 ```[NO LICENSE]```
* [cppbase](https://github.com/kartikkumar/cppbase) - 用于简单 CMake 基于 C++ 项目的模板。 [```[MIT]```][MIT]
* [Arduino-CMake-Template](https://github.com/maxbader/Arduino-CMake-Template) - 用于 Arduino 开发的 CMake 起始模板。 ```[NO LICENSE]```
* [c-template](https://github.com/fletcher/c-template) - 设置 C 项目的模板，包含 CuTest、CMake 构建设置。 [```[MIT]```][MIT]
* [cpp_project_template](https://github.com/duckie/cpp_project_template) - 一个简单的模板，用于快速启动由 CMake 管理的 C++ 项目。 [```[MIT]```][MIT]
* [cpp-boilerplate](https://github.com/Lectem/cpp-boilerplate) - 旨在成为现代 CMake 和 CI 的参考模板。 [```[MIT]```][MIT]
* [ci_helloworld](https://github.com/ainfosec/ci_helloworld) - 一个简单的示例，展示如何为 C 和 C++ 设置完整的 CI 环境。 [```[MIT]```][MIT]
* [how-to-export-cpp-library](https://github.com/robotology/how-to-export-cpp-library) - 一个跨平台的 C++ 库模板，包含 ctest 和 CI 支持，使用纯 CMake，并提供逐行指导评论。 [```[MIT]```][MIT]
* [ModernCppCI](https://github.com/LearningByExample/ModernCppCI) - 一个使用 CI 的现代 C++ 项目的示例（虽然它使用了非现代 CMake，如 ```include_directories()```）。 [```[MIT]```][MIT]
* [modern-cmake-sample](https://github.com/pabloariasal/modern-cmake-sample) - 使用 CMake 的最佳实践和正确用法，使用目标管理。 ```[NO LICENSE]```
* [CMakeInstallExample](https://github.com/DeveloperPaul123/CMakeInstallExample) - 使用 CMake 为 C++ 项目提供的安装示例（Windows）。 ```[NO LICENSE]```
* [cpp14-project-template](https://github.com/arnavb/cpp14-project-template) - 一个 C++14 模板，包含 CI、测试、代码覆盖、文档和静态分析集成。 [```[CC0-1.0]```][CC0-1.0]
* [cmake_templates](https://github.com/acdemiralp/cmake_templates) - 用于创建 C++ 库和可执行文件的模板（包括 conan）。 ```[NO LICENSE]```
* [cmake_snippets](https://github.com/adishavit/cmake_snippets) - 可复制的 CMake 片段。 [```[BSD3]```][BSD-3-Clause]
* [cmake-cookbook](https://github.com/dev-cafe/cmake-cookbook) - 一本包含大量 CMake 配方的大型 CMake 食谱书。 [```[MIT]```][MIT]
## License

This is released under the [**```Creative Commons Attribution 4.0 International```**](http://creativecommons.org/licenses/by/4.0/) License ```(CC BY 4.0)```.

[ISC]: https://opensource.org/licenses/ISC
[GPL]: https://www.gnu.org/licenses/gpl-3.0.html
[GPL2]: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
[LGPL]: https://www.gnu.org/licenses/lgpl-3.0.en.html
[MIT]: https://opensource.org/licenses/MIT
[BOOST]: http://www.boost.org/LICENSE_1_0.txt
[BSD-2-Clause]: https://opensource.org/licenses/BSD-2-Clause
[BSD-3-Clause]: https://opensource.org/licenses/BSD-3-Clause
[APACHE2]: http://www.apache.org/licenses/LICENSE-2.0
[CC0-1.0]: https://creativecommons.org/publicdomain/zero/1.0/
[MPL]: https://www.mozilla.org/en-US/MPL/2.0/
