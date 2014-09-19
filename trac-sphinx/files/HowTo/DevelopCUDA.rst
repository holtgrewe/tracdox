How To: Getting Started with CUDA
---------------------------------

Requirements
~~~~~~~~~~~~

In order to follow this HowTo, you need:

-

   -  git to download the sources
   -  cmake to build the projects
   -  the CUDA toolkit >= v5.0 to compile the CUDA demos
   -  a CUDA-capable GPU with SM architecture >= 2.0 to run the CUDA
      demos

Refer to Tutorial/GettingStarted for detailed SeqAn installation
instructions.

Getting the source code
~~~~~~~~~~~~~~~~~~~~~~~

CUDA acceleration resides in the develop branch of SeqAn, hosted on
`GitHub <http://github.com/seqan/>`__. Execute the following command to
get the last sources:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    $ git clone -b develop https://github.com/seqan/seqan.git SeqAn

Compiling the demos
~~~~~~~~~~~~~~~~~~~

Hello CUDA
^^^^^^^^^^

Let us first setup the build system:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    $ mkdir SeqAn-Builds && cd SeqAn-Builds
    $ cmake ../SeqAn -DCMAKE_BUILD_TYPE=Release

Now we can compile and execute our `CUDA hello
world <http://github.com/seqan/seqan/blob/develop/extras/demos/cuda/hello.cu>`__:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    $ make demo_cuda_hello
    $ bin/demo_cuda_hello
    Hello CUDA!

::

    #ImportantBox
    Some users experienced compilation problems on Mac OS X. If the compilation fails with:
    '''clang: error: unsupported option '-dumpspecs'''

    then you need to manually create links to gcc 4.4 in the nvcc directory. If you for example installed gcc44 via MacPorts in <tt>/opt/local/bin</tt> you can create these links as follows:
    <pre>#ShellBox
    $ ln -s /opt/local/bin/gcc-mp-4.4 /usr/local/cuda/bin/gcc
    $ ln -s /opt/local/bin/g++-mp-4.4 /usr/local/cuda/bin/g++

.. raw:: html

   </pre>

MMap String
^^^^^^^^^^^

Now let's try the `MMap String
demo <http://github.com/seqan/seqan/blob/develop/extras/demos/cuda/mmap.cu>`__.
This demo maps a text file in memory, copies it on the device and uses
Thrust to count the number of occurrences of a given character into the
file.

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    $ make demo_cuda_mmap
    $ echo "THIS IS A TEST" > test.txt
    $ bin/demo_cuda_mmap test.txt T
    3

FM-index counting
^^^^^^^^^^^^^^^^^

The `FM-index counting
demo <http://github.com/seqan/seqan/blob/develop/extras/demos/cuda/count.cu>`__
builds an FM-index over a static text. Given a set of patterns, the
program counts - both on the host and on the device - the total number
of occurrences of all patterns in the text.

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    $ make demo_cuda_count
    $ bin/demo_cuda_count ACGTACGTACGTACGT ACGT GTA
    CPU Occurrences: 7
    GPU Occurrences: 7

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
