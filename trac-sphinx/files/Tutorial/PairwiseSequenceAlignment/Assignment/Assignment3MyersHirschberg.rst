Assignment 3: MyersHirschberg
-----------------------------

Objective
^^^^^^^^^

Write a program that computes a fast global alignment between the RNA
sequences ``AAGUGACUUAUUG" and ``\ AGUCGGAUCUACUG\` using the Align data
structure and the Levenshtein distance. Print the score and the
alignment. Additionally, output for each row of the Align object the
view positions of the gaps.

Solution
^^^^^^^^

As usual, first the necessary includes and typedefs. Our sequence type
is String. TAlign and TRow are defined as in the previous example
program. The type Iterator::Type will be used to iterate over the rows
of the alignment.

.. includefrags:: core/demos/tutorial/alignments/alignment_global_assignment3.cpp
   :fragment: main

In the next step we initialize our input StringSet ``strings`` and pass
it as argument to the constructor of the AlignmentGraph ``alignG``.

.. includefrags:: core/demos/tutorial/alignments/alignment_global_assignment3.cpp
   :fragment: init

Now we compute the alignment using the levenshtein distance and a
AlignConfig object to set the correct free end-gaps. In this example we
put the shorter sequence on the vertical axis of our alignment matrix.
Hence, we have to use free end-gaps in the first and last row, which
corresponds to the first and the last parameter in the AlignConfig
object. If you add the shorter sequence at first to ``strings``, then
you simply have to flip the ``bool`` values of the AlignConfig object.

.. includefrags:: core/demos/tutorial/alignments/alignment_global_assignment3.cpp
   :fragment: alignment

.. includefrags:: core/demos/tutorial/alignments/alignment_global_assignment3.cpp
   :fragment: view

Here the result of the program:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    Score: -6
          0     .    :    .
            AAGU--GA-CUUAUUG
    {|
    !
    !
    ! /
    !
    |}

            A-GUCGGAUCU-ACUG



    Row 0 contains gaps at positions:
    4
    5
    8
    Row 1 contains gaps at positions:
    1
    11

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
