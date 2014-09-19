Assignment 2: Semi-Global Alignment
-----------------------------------

Objective
^^^^^^^^^

Compute a semi-global alignment between the sequences AAATGACGGATTG and
TGGGA using the Levenshtein distance and using an AlignmentGraph to
store the alignment. Print the score and the resulting alignment to the
standard output.

Solution
^^^^^^^^

First we have to define the body of our program. This includes the
definition of the library headers that we want to use. In this case we
include the ``iostream`` header from the STL and the ``seqan\align.h``
header, which defines all algorithms and data structures we want to use.
After we added the namespace and opened the ``main``\ function body we
define our types we want to use in this function. We use an
seqan:Class.String with the seqan:Spec.Dna alphabet, since we know that
we work with DNA sequences. We use an additional seqan:Class.StringSet
to store the input sequences. In this scenario we use an
seqan:"Spec.Alignment Graph" to store the alignment. Remember, that the
AlignmentGraph uses an seqan:Spec.Dependent StringSet to map the
vertices to the correct input sequences.

.. includefrags:: core/demos/tutorial/alignments/alignment_global_assignment2.cpp
   :fragment: main

In the next step we initialize our input StringSet ``strings`` and pass
it as argument to the constructor of the AlignmentGraph ``alignG``.

.. includefrags:: core/demos/tutorial/alignments/alignment_global_assignment2.cpp
   :fragment: init

Now we compute the alignment using the Levenshtein distance and a
AlignConfig object to set the correct free end-gaps. In this example we
put the shorter sequence on the vertical axis of our alignment matrix.
Hence, we have to use free end-gaps in the first and last row, which
corresponds to the first and the last parameter in the AlignConfig
object. If you add the shorter sequence at first to ``strings``, then
you simply have to flip the ``bool`` values of the AlignConfig object.

Here the output of our program:
.. includefrags:: core/demos/tutorial/alignments/alignment_global_assignment2.cpp
   :fragment: alignment

Here the result of the program:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    Score: 3
    Alignment matrix:
          0     .    :
            AAATGACGGATTG
    {|
    !
    !/
    |}

            ---TG--GGA---

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
