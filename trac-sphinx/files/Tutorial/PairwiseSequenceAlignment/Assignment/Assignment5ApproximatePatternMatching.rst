= Assignment 5: Approximate String Matching.

Objective
^^^^^^^^^

Write an approximate pattern matching algorithm using alignment
algorithms. Report the positions of all hits where the pattern matches
the text with at most ``2`` errors. Output the number of total edits
used to match the pattern and print the corresponding cigar string of
the alignment without leading and trailing gaps in the pattern. Text:
``MISSISSIPPIANDMISSOURI`` Pattern: ``SISSI``

Solution
^^^^^^^^

Write the ``main`` body of the program with type definition and
initalization of the used data structures.
.. includefrags:: core/demos/tutorial/alignments/pairwise_sequence_alignment_assignment5.cpp
   :fragment: main

In the first part of the algorithm we implement am alignment based
verification process to identify positions in the ``database`` at which
we can find our pattern with at most ``2`` errors. We slide the ``5*5``
alignment matrix position by position over the ``database`` and use the
``MeyersBitVector`` to verify the hits. If the score is greater or equal
than ``-2``, then we have found a hit. We store the begin position of
the hit in ``locations``.

.. includefrags:: core/demos/tutorial/alignments/pairwise_sequence_alignment_assignment5.cpp
   :fragment: verfication

In the second part of the algorithm we iterate over all reported
locations. This time we compute a semi-global alignment since we won't
penalize gaps at the beginning and at the end of our pattern. We also
compute a band allowing at most ``2`` errors in either direction. Don't
forget to clear the gaps in each iteration, otherwise we might encounter
wrong alignments.

.. includefrags:: core/demos/tutorial/alignments/pairwise_sequence_alignment_assignment5.cpp
   :fragment: alignment

In the next part we determine the cigar string for the matched pattern.
We have to remove leading and trailing gaps in the ``gapsPattern``
object using the functions seqan:Function.setClippedBeginPosition and
seqan:Function.setClippedEndPosition. We also need to set the clipped
begin position for the ``gapsText`` object such that both Gaps begin at
the same position.
.. includefrags:: core/demos/tutorial/alignments/pairwise_sequence_alignment_assignment5.cpp
   :fragment: cigar

First, we identify insertions using the functions seqan:Function.isGap
and seqan:Function.countGaps.
.. includefrags:: core/demos/tutorial/alignments/pairwise_sequence_alignment_assignment5.cpp
   :fragment: cigarInsertion

We do the same to identify deletions.
.. includefrags:: core/demos/tutorial/alignments/pairwise_sequence_alignment_assignment5.cpp
   :fragment: cigarDeletion

If there is neither an insertion nor a deletion, then there must be a
match or a mismatch. As long as we encounter matches we move forward in
the Gaps structures and count the number of consecutive matches. When we
are done we report the match count.
.. includefrags:: core/demos/tutorial/alignments/pairwise_sequence_alignment_assignment5.cpp
   :fragment: cigarMatch

In a similar procedure we determine the consecutive substitutions.
Finally we print out the position of the hit, its total number of edits
and the corresponding cigar string.
.. includefrags:: core/demos/tutorial/alignments/pairwise_sequence_alignment_assignment5.cpp
   :fragment: cigarMismatch

Here is the output of this program.

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    Text: MISSISSIPPIANDMISSOURI    Pattern: SISSI
    Hit at position  0  total edits: 1  cigar: 1S4M
    Hit at position  1  total edits: 1  cigar: 1I4M
    Hit at position  2  total edits: 1  cigar: 4M1I
    Hit at position  3  total edits: 0  cigar: 5M
    Hit at position  4  total edits: 1  cigar: 1I4M
    Hit at position  6  total edits: 2  cigar: 2M2S1M
    Hit at position  14 total edits: 2  cigar: 1S3M1S

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
