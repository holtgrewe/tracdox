.. sidebar:: ToC

   .. contents::


.. _how-to-use-latest-clang-in-xcode:

How To: Use the latest LLVM/Clang in Xcode
------------------------------------------

Foreword
~~~~~~~~

Unfortunately, Apple still ships LLVM/Clang 2.0 with Xcode 4 which doesn't support the current C++11 standard (a.k.a. C++0x).
To equip Xcode 3 or 4 with a newer version of Clang, you can install it via MacPorts and enable it in Xcode with a plugin.

Install Clang
~~~~~~~~~~~~~

Clang can be compiled either by hand (as described `here <http://shapeof.com/archives/2010/01/using_the_latest_llvm_with_xcode.html>`__) or simply via MacPorts.
For the latter download and install `MacPorts <http://www.macports.org/install.php>`__.
Then open Terminal in Applications->Utilities->Terminal and type in a Terminal window:

.. code-block:: console

    sudo port install clang

If you want the unreleased developer version of clang, execute the following:

.. code-block:: console

    sudo port install clang-devel

If the installation was successful, there is an executable
/opt/local/bin/clang.

Install the Xcode plugins
~~~~~~~~~~~~~~~~~~~~~~~~~

.. todo:: Upload somewhere else.

To enable the installed compiler in Xcode you need to download a prepared `Xcode plugin <http://trac.mi.fu-berlin.de/seqan/export/10384/trunk/util/xcode/Clang%20LLVM%20MacPorts.xcplugin.zip>`__, unzip it and copy it in /Developer/Library/Xcode/Plug-ins or ~/Library/Application Support/Developer/Shared/Xcode/Plug-ins.
Restart Xcode and voila, you should be able to choose "LLVM-Clang from MacPorts" under C/C++ Compiler Version.

Remarks
~~~~~~~

We adapted our Cmake scripts to automatically choose "LLVM-Clang from
MacPorts" as default compiler. To use the new standard in your projects
you have to add **-std=c++0x** to your compiler flags. If you get errors
like:

.. code-block:: console

   Undefined symbols for architecture x86_64: "std::ios_base::Init::~Init()",

add ``-lstdc++`` to your linker flags.
