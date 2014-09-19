Task 2: Semi-global alignment
-----------------------------

Task
~~~~

Compute a semi-global alignment of the sequences "blablablu" and "abab"
using edit distance and an alignment algorithm of your choice. Print
distance and alignment

Hint: When using the Alignment Graph data structure, one can compute
more sophisticated alignments, so called end-space free alignments.
These alignments can be computed by using the regular global alignment
algorithms, but initializing the DP matrix with zeros in the first row
and/or column, and/or by searching for the best score in the last row
and/or column. This can be achieved by using an AlignConfig object that
specifies which end spaces are free from penalty (see also
seqan:Page.Alignments).

Solution
~~~~~~~~

As usual, first the necessary includes and typedefs. Our sequence type
is ``String<char>``.
.. includefrags:: core/demos/tutorial/alignments/alignment_pairwise_global_assignment2.cpp
   :fragment: main

A seqan:Class.StringSet with the sequences to be aligned is created, and
the seqan:"Spec.Alignment Graph" is initialized.
.. includefrags:: core/demos/tutorial/alignments/alignment_pairwise_global_assignment2.cpp
   :fragment: init

Now we use an seqan:Class.AlignConfig to configure our alignment to be
semi-global (the second sequence being contained in the first sequence).
The signature is ``AlignConfig<TTop, TLeft, TRight, TBottom>``. ``TTop``
is true meaning that the first row of the DP matrix is initialized with
zeros (gaps before the start of the second sequence are free), ``TLeft``
and ``TRight`` to false meaning that all gaps in the first sequence
receive a penalty, and ``TBottom`` to true, leaving gaps at the end of
the second sequence unpunished.
.. includefrags:: core/demos/tutorial/alignments/alignment_pairwise_global_assignment2.cpp
   :fragment: alignment

.. includefrags:: core/demos/tutorial/alignments/alignment_pairwise_global_assignment2.cpp
   :fragment: iterate

And the output:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    Score = 3
    Alignment matrix:
          0     .
            blablablu
    {|
    !
    |}

            --ab-ab--


.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
