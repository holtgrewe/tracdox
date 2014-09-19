How To: Read Compiler Errors
----------------------------

#. **Q:** I'm getting weird compiler errors using GCC/LLVM. I have tried
   quite long to understand it but I simply cannot find the problem.

``   ``\ **``A:``**\ `` Maybe the generated forwards are broken. Try to remove all such headers from your build directory (``\ ``find . -name '*generated_forwards.h' | xargs rm``\ `` on Linux or Os X. Another way to do this to create a fresh subdirectory of ``\ *``/build/``*\ `` and re-run CMake.``

| ``2. ``\ **``Q:``**\ `` When I try to compile under Linux, I get linker error messages like: ``\ **``undefined reference to `aio_suspend'``**\ ``.``
| ``   ``\ **``A:``**\ `` Have you linked your application against the ``\ ``librt``\ ``? Add ``\ ``-lrt``\ `` to the ``\ ``g++``\ `` or ``\ ``ld``\ `` command line.``

| ``3. ``\ **``Q:``**\ `` When I access files in SeqAn I get a warning: ``\ **``WARNING:``
``FilePtr`` ``is`` ``not`` ``64bit`` ``wide``**\ ``.``
| ``   ``\ **``A:``**\ `` Large file access is disabled. This is not a problem unless you access 4GB or larger files. To enable large files, you have to make sure to include all SeqAn headers before ``\ ``<fstream>``\ `` or ``\ ``<iostream>``\ ``. So reorder:``

::

    #include <iostream>
    #include <fstream>
    #include <seqan/index.h>

``   to:``

::

    #include <seqan/index.h>
    #include <iostream>
    #include <fstream>

``   Alternatively, you can add ``\ ``-D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64``\ `` to the ``\ ``g++``\ `` command line.``

Back to the `Developer's Corner <HowTo/GetStarted>`__

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
