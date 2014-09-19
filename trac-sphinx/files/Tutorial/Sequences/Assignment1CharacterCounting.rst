Task 1: Character Counting
--------------------------

Task
~~~~

Write a function ``countOneMers(str)`` that accepts a
seqan:Shortcut.CharString of lower case characters and then prints a
list of pairs. Each of this pair gives a character and the number of
occurences of this character in the string. A pair should only be
printed if the occurence count is greater than 0. Call this function
with the strings ``"helloworld"``, ``"banana"`` and ``"mississippi"``.

Solution
~~~~~~~~

We start off by including the IO steams library from the STL and the
sequence module from SeqAn. Then, define the ``countOneMers`` function.
Note that it only works correctly for words that only consist of lower
case characters.

.. includefrags:: core/demos/tutorial/sequence/count_characters.cpp
   :fragment: includes

Define a table for counting characters and resize-and-initialize it
using seqan:Function.resize.

.. includefrags:: core/demos/tutorial/sequence/count_characters.cpp
   :fragment: count-one-mers-initialize-table

Count the characters in the given string.

.. includefrags:: core/demos/tutorial/sequence/count_characters.cpp
   :fragment: count-one-mers-count-chars

We print all pairs of characters and their counts if the ocunt is > 0.
Note that the explicit conversion to ``char`` from ``'a' + i`` is
required. Otherwise, the value would become an ``int``. The
``static_cast<>`` is prefered to bracket-casting (e.g.
``(char)('a' + i)`` in SeqAn).

.. includefrags:: core/demos/tutorial/sequence/count_characters.cpp
   :fragment: count-one-mers-print-chars

In our ``main`` function, we call ``countOneMers`` with the strings from
the task.

.. includefrags:: core/demos/tutorial/sequence/count_characters.cpp
   :fragment: main

Program Output
~~~~~~~~~~~~~~

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    String: helloworld
    d 1
    e 1
    h 1
    l 3
    o 2
    r 1
    w 1
    String: mississippi
    i 4
    m 1
    p 2
    s 4
    String: banana
    a 3
    b 1
    n 2

.. raw:: html

   </pre>

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
