Assignment 5
------------

Task
~~~~

Write a program that outputs all occurrences of the gapped q-gram "AT-A"
in "CATGATTACATA".

Solution
~~~~~~~~

Before we can create a seqan:Shortcut.DnaString index of "CATGATTACATA",
we have to choose an appropriate seqan:Class.Shape. Because our shape
``1101`` is known at compile-time and contains only one gap we could
choose seqan:Spec.OneGappedShape, seqan:Spec.GappedShape or
seqan:Spec.GenericShape (see the commented-out code). Although the
seqan:Spec.GenericShape could be used for every possible shape, it is a
good idea to choose a seqan:Class.Shape with restrictions as its
seqan:Function.hash functions are more efficient in general.

.. includefrags:: core/demos/tutorial/index/index_assignment5.cpp
   :fragment: initialization

Please note that the seqan:Class.Shape object that corresponds to the
seqan:Spec.IndexQGram index is empty initially and has to be set by
seqan:Function.stringToShape or seqan:Function.resize. This
initialization is not necessary for seqan:Class.Shape that are defined
at compile-time, i.e. seqan:Spec.UngappedShape and
seqan:Spec.GappedShape. To search for "AT-A" we first have to hash it
with the index shape or any other seqan:Class.Shape with the same
bitmap. The we can use seqan:Function.getOccurrences to output all
matches.
.. includefrags:: core/demos/tutorial/index/index_assignment5.cpp
   :fragment: output
**Hint:** Instead of ``length(getOccurrences(...))`` we could have used
seqan:Function.countOccurrences. But beware that
seqan:Function.countOccurrences requires only the ``QGram_Dir`` fibre,
whereas seqan:Function.getOccurrences requires both ``QGram_Dir`` and
``QGram_SA``, see `Index Fibre HowTo <HowTo/AccessIndexFibres>`__.
Because ``QGram_SA`` can be much more efficiently constructed during the
construction of ``QGram_Dir``, ``QGram_Dir`` would be constructed twice.

Program output:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    1
    4

.. raw:: html

   </pre>

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
