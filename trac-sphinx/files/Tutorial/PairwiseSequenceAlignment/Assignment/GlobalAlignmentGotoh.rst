Assignment 1: Gotoh Algorithm
-----------------------------

Objective
^^^^^^^^^

Compute a global alignment between the DNA sequences "AAATGACGGATTG"
"AGTCGGATCTACTG" using the Gotoh algorithm with the following scoring
parameters: match = 4, mismatch = -2, gap open = -4 and gap extend = -2.
Store the alignment in an Align object and and print it together with
the score.

Solution
^^^^^^^^

First we have to define the body of our program. This includes the
definition of the library headers that we want to use. In this case it
is the ``iostream`` from the STL and the ``seqan\align.h`` header file
defining all algorithms and data structures we want to use. After we
added the namespace and opened the ``main`` body we define our types we
want to use in this function. We use an seqan:Class.String with the
seqan:Spec.Dna alphabet, since we know that we work with DNA sequences.
The second type is our seqan:Class.Align object storing the alignment
later on.

.. includefrags:: core/demos/tutorial/alignments/alignment_global_assignment1.cpp
   :fragment: main

In the next step we initialize our objects. This includes the both input
sequences ``seq1`` and ``seq2`` and ``align``. We resize the underlying
set of ``align`` that manages the separate seqan:Class.Gaps data
structures. Finally, we assign the input sequences as sources to the
corresponding row of ``align``.

.. includefrags:: core/demos/tutorial/alignments/alignment_global_assignment1.cpp
   :fragment: init

Now we compute the alignment using a scoring scheme with affine gap
costs. The first parameter corresponds to the ``match`` value, the
second to the ``mismatch`` value, the third to the ``gap extend`` value
and the last one to the ``gap open`` value. We store the computed score
of the best alignment in the equally named variable ``score``. In the
end we print the score and the alignment using print methods provided by
the ``iostream`` module of the STL.

.. includefrags:: core/demos/tutorial/alignments/alignment_global_assignment1.cpp
   :fragment: alignment

Congratulation! You have computed an alignment using affine gap costs.
Here the result of the program:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    Score: 16
          0     .    :    .
            AAATGACGGAT----TG
    {|
    !
    !/
    !
    |}

            A---GTCGGATCTACTG

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
