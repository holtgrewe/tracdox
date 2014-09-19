Task 1 Bis: Generic Character Counting
--------------------------------------

Task
~~~~

Rewrite the function ``countOneMers(str)`` to accept a generic
seqan:Shortcut.String. Call this function with the
seqan:Shortcut.CharString ``"Hello world!"``, seqan:Shortcut.DnaString
``"TATACGCTA"`` and seqan:Shortcut.Peptide
``"MQDRVKRPMNAFIVWSRDQRRKMALEN"``.

Solution
~~~~~~~~

We start off by including the IO steams library from the STL and the
sequence module from SeqAn.

.. includefrags:: core/demos/tutorial/sequence/count_generic_characters.cpp
   :fragment: includes

Then, define the ``countOneMers`` function.

.. includefrags:: core/demos/tutorial/sequence/count_generic_characters.cpp
   :fragment: count-one-mers-define-function

Define a table for counting characters and resize-and-initialize it
using seqan:Function.resize.

.. includefrags:: core/demos/tutorial/sequence/count_generic_characters.cpp
   :fragment: count-one-mers-initialize-table

Count the characters in the given string.

.. includefrags:: core/demos/tutorial/sequence/count_generic_characters.cpp
   :fragment: count-one-mers-count-chars

We print all pairs of characters and their counts if the ocunt is > 0.

.. includefrags:: core/demos/tutorial/sequence/count_generic_characters.cpp
   :fragment: count-one-mers-print-chars

In our ``main`` function, we call ``countOneMers`` with the strings from
the task.

.. includefrags:: core/demos/tutorial/sequence/count_generic_characters.cpp
   :fragment: main

Program Output
~~~~~~~~~~~~~~

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    ASCII String: Hello world!
     :1
    !:1
    H:1
    d:1
    e:1
    l:3
    o:2
    r:1
    w:1
    DNA String: TATACGCTA
    A:3
    C:2
    G:1
    T:3
    Peptide String: MQDRVKRPMNAFIVWSRDQRRKMALEN
    A:2
    R:5
    N:2
    D:2
    Q:2
    E:1
    I:1
    L:1
    K:2
    M:3
    F:1
    P:1
    S:1
    W:1
    V:2

.. raw:: html

   </pre>

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
