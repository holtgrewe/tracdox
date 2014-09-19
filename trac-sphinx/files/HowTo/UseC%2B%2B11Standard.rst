**Note: this page is deprecated and refers to our old build system. If
you want to use C++11 with our `new build
system <BuildManual/UsingTheSeqAnBuildSystem>`__ or in your own external
projects, follow the steps described on
`StackOverflow <http://stackoverflow.com/questions/10984442/how-to-detect-c11-support-of-a-compiler-with-cmake>`__.**

How To: Use the C++11 Standard for Compilation
----------------------------------------------

Currently the new standard is partially supported on all of the major 3
platforms, `read
more <http://wiki.apache.org/stdcxx/C%2B%2B0xCompilerSupport>`__.
Compilation with the new C++11 (a.k.a. C++0x) standard can easily be
enabled via cmake if the following prerequisites are fulfilled:

Prerequisites
~~~~~~~~~~~~~

Windows
^^^^^^^

On Windows the new standard is only supported by `Visual Studio
10 <http://www.microsoft.com/visualstudio/en-us/products/2010-editions/visual-cpp-express>`__
and later or `MinGW <http://www.mingw.org/>`__ with GCC 4.5 or later.
After successful installation follow the steps of the next section.

Mac OS X
^^^^^^^^

On Mac OS X the new standard is supported by GCC 4.5 and later of
LLVM/Clang 2.9 and later. If you use Xcode you need to install the
latest Clang and an Xcode plugin, [HowTo/UseLatestClangInXcode described
here]. If you use Makefiles or Eclipse, install the latest GCC compiler
via `MacPorts <http://www.macports.org/>`__ by:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    sudo port install gcc46

.. raw:: html

   </pre>

Linux
^^^^^

On Linux install the latest GCC. On a Ubuntu or Debian system this can
be done with the following command:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    sudo aptitude install g++-4.6

.. raw:: html

   </pre>

Enable C++11 support in cmake
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After installing a compiler supporting the new standard, you need to
enable the appropriate flags during compilation. Typically this is
"-std=c++0x" (for GCC and LLVM/Clang). Visual Studio 10 uses the new
standard by default and needs no extra flags. If you use cmake to
compile your SeqAn projects, you need to activate the option
``SEQAN_C++11_STANDARD`` either via ccmake or command line defines and
if the compiler installed in the previous section is not the default
compiler, you may need to set the compiler variable
CMAKE\_CXX\_COMPILER.

Windows
^^^^^^^

The new standard is enabled by default for Visual Studio 10 and later,
i.e. you only need to create an appropriate project file. For MinGW,
cmake must be called with the additional option
``-DSEQAN_C++11_STANDARD=ON``.

Mac OS X
^^^^^^^^

If your build directory is build/Debug and you use XCode, you can set
the corresponding variables by the following

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    cd seqan-trunk/build/Debug
    rm CMakeCache.txt
    cmake ../.. -DSEQAN_C++11_STANDARD=ON -G Xcode

For Makefiles and GCC 4.6 use:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    cd seqan-trunk/build/Debug
    rm CMakeCache.txt
    cmake ../.. -DCMAKE_CXX_COMPILER=g++-mp-4.6 -DSEQAN_C++11_STANDARD=ON

Linux
^^^^^

For Makefiles and GCC 4.6 use:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    cd seqan-trunk/build/Debug
    rm CMakeCache.txt
    cmake ../.. -DCMAKE_CXX_COMPILER=g++-4.6 -DSEQAN_C++11_STANDARD=ON

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
