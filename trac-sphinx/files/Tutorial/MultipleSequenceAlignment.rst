Multiple Sequence Alignment
---------------------------

TOC

| ``Learning Objective ::``
| `` You will learn how to compute a multiple sequence alignment using SeqAn's alignment data structures and algorithms.``
| ``Difficulty ::``
| `` Basic``
| ``Duration ::``
| `` 0:15h``
| ``Prerequisites ::``
| `` ``\ ```Basics`` <Tutorial/Basics>`__\ ``, ``\ ```Sequences`` <Tutorial/Sequences>`__\ ``, ``\ ```Alphabets`` <Tutorial/Alphabets>`__\ ``, ``\ ```Alignment``
``Representation`` <Tutorial/AlignmentRepresentation>`__

Apart from pairwise alignments, also multiple sequence alignments can be
computed in SeqAn. The easiest way to do this is by using the function
:dox:`globalMsaAlignment`. This function computes a
heuristic alignment based on a consistency-based progressive alignment
strategy as described in
`Seqan::TCoffee <http://bioinformatics.oxfordjournals.org/cgi/content/abstract/24/16/i187>`__
paper.

In the following example, we align four amino acid sequences using the
:dox:`AlignmentGraph` data structure and the [dox:Blosum62
Blosum62] scoring matrix with gap extension penalty -11 and gap open
penalty -1. The required header for multiple sequence alignments is
``seqan/graph_msa.h``.
.. includefrags:: core/demos/tutorial/alignments/alignment_msa.cpp
   :fragment: main

First, the sequence type ``TSequence`` is defined and a [dox:StringSet
StringSet] is declared. The four sequences to be aligned are appended to
the StringSet ``seq``.
.. includefrags:: core/demos/tutorial/alignments/alignment_msa.cpp
   :fragment: init

Now we initialize our :dox:`AlignmentGraph` with the
sequences. The graph and the :dox:`Blosum62` scoring matrix are
handed to the function :dox:`globalMsaAlignment` which
computes the desired alignment.
.. includefrags:: core/demos/tutorial/alignments/alignment_msa.cpp
   :fragment: alignment

And here is the output of this example program:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    Alignment matrix:
          0     .    :    .    :    .    :    .    :    .    :
            DPKKPRGKMSSYAFFVQTSREEHKKKHPDASVNFSEFSKKCSERWKTMSA
    {|
    !
    !
    !
    |}

            RVKRP---MNAFIVWSRDQRRKMALENP--RMRNSEISKQLGYQWKMLTE
              | |              | | |   |   | |    | |    | | |
            FPKKP---LTPYFRFFMEKRAKYAKLHP--EMSNLDLTKILSKKYKELPE
    {|
    !/   |        |
    !
    !      /
    |}

            HIKKP---LNAFMLYMKEMRANVVAEST--LKESAAINQILGRRWHALSR

         50     .    :    .    :    .    :    .    :
            KEKGKFEDMAKADKARYEREMKTY----------IPPKGE
    {|
    !  /   |    |        |
    |}

            AEKWPFFQEAQKLQAMHREKYPNYKYRP---RRKAKMLPK
              |    |  |                            |
            KKKMKYIQDFQREKQEFERNLARFREDH---PDLIQNAKK
    {|
    !      / |                        |
    |}

            EEQAKYYELARKERQLHMQLYPGWSARDNYGKKKKRKREK

Assignment 1
^^^^^^^^^^^^

::

    #AssignmentBox

     Type :: Review
     Objective :: Repeat the above example using the Align data structure and the Blosum80 scoring matrix.

     Solution ::
    <pre>
    #FoldOut
    ----
    A complete solution can be found [[Tutorial/Alignments/AssignmentMultipleAlignment1| here]].

.. raw:: html

   </pre>

Submit a comment
^^^^^^^^^^^^^^^^

If you found a mistake, or have suggestions about an improvement of this
page press:
[/newticket?component=Documentation&description=Tutorial+Enhancement+for+page+http://trac.seqan.de/wiki/Tutorial/Alignments&type=enhancement
submit your comment]

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
