Task 2: All Strings Of A Given Length
-------------------------------------

Task
~~~~

Write a function ``printPermutations(len)`` which, given a parameter
``len``, prints all strings consisting of ``len`` lower case letters to
``std::cout``. Call this function with the parameter 3 in your
``main(...)`` function.

Solution
~~~~~~~~

Start off by including the STL IO Streams and the SeqAn sequence module.

.. includefrags:: core/demos/tutorial/sequence/sequence_all_strings.cpp
   :fragment: includes

The recursive helper function that calls itself recursively.

.. includefrags:: core/demos/tutorial/sequence/sequence_all_strings.cpp
   :fragment: print-strings-rec

This function kicks off our recursion.

.. includefrags:: core/demos/tutorial/sequence/sequence_all_strings.cpp
   :fragment: print-strings

In our main function, we just call ``printString()``.

.. includefrags:: core/demos/tutorial/sequence/sequence_all_strings.cpp
   :fragment: main

Program Output
~~~~~~~~~~~~~~

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    aaa
    aab
    ...
    zzy
    zzz

.. raw:: html

   </pre>

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
