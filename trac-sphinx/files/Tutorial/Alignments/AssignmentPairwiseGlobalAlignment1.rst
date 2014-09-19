Task 1: Pairwise global alignment
---------------------------------

Task
~~~~

``Write a program that computes a global alignment of the DNA sequences "acgtacgtact" and "actactacgt" using the Align data structure. Iterate through the rows of the aligment and for each row output the view positions of the gaps. ``
``Hint: Use the function seqan:Function.isGap. ``

Solution
~~~~~~~~

As usual, first the necessary includes and typedefs. Our sequence type
is ``String<Dna>``. ``TAlign`` and ``TRow`` are defined as in the
previous example program. The type ``Iterator<TRow>::Type`` will be used
to iterate over the rows of the alignment.
.. includefrags:: core/demos/tutorial/alignments/alignment_pairwise_global_assignment1.cpp
   :fragment: main

The seqan:Class.Align object ``align`` is intialized with the two
sequences to be aligned.
.. includefrags:: core/demos/tutorial/alignments/alignment_pairwise_global_assignment1.cpp
   :fragment: init

The alignment is computed by the Hirschberg algorithm. Score and
alignment are printed on screen.
.. includefrags:: core/demos/tutorial/alignments/alignment_pairwise_global_assignment1.cpp
   :fragment: alignment

Now we iterate over the rows, printing the view position whenever the
function seqan:Function.isGap returns true.
.. includefrags:: core/demos/tutorial/alignments/alignment_pairwise_global_assignment1.cpp
   :fragment: iterate

And the output:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    Score = 6
          0     .    :
            ACGTACGTAC-T
    {|
    !
    !/
    !/ |
    |}

            AC-TAC-TACGT


    Row 0 contains gaps at positions:
    10
    Row 1 contains gaps at positions:
    2
    6

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
