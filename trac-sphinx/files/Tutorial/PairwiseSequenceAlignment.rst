Pairwise Sequence Alignment
---------------------------

TOC

| ``Learning Objective ::``
| `` You will learn how to compute global and local alignments, how you can use different scoring schemes, and how you can customize the alignments to fulfill your needs.``
| ``Difficulty ::``
| `` Average``
| ``Duration ::``
| `` 1h``
| ``Prerequisites ::``
| `` ``\ ```Basics`` <Tutorial/Basics>`__\ ``, ``\ ```Iterators`` <Tutorial/Iterators>`__\ ``, ``\ ```Alphabets`` <Tutorial/Alphabets>`__\ ``, ``\ ```Sequences`` <Tutorial/Sequences>`__\ ``, ``\ ```Alignment``
``Representation`` <Tutorial/AlignmentRepresentation>`__

Alignments are one of the most basic and important ways to measure
similarity between two or more sequences. In general, a pairwise
sequence alignment is an optimization problem which determines the best
transcript of how one sequence was derived from the other. In order to
give an optimal solution to this problem, all possible alignments
between two sequences are computed using a **Dynamic Programming**
approach. Scoring schemes allow the comparison of the alignments such
that the one with the best score can be picked. Despite of the common
strategy to compute an alignment, there are different variations of the
standard DP algorithm laid out for special purposes.

We will first introduce you to the scoring schemes followed by the
global alignments. Subsequent, you will learn how to compute local
alignments. Finally, we will demonstrate how you can reduce the search
space using a band.

Scoring Schemes
~~~~~~~~~~~~~~~

Scoring schemes define the score for aligning two characters of a given
alphabet and the score for gaps within alignments. Given an alignment
between two sequences and a scoring scheme, the score of the alignment
can be computed as the sum of the scores for aligned character pairs
plus the sum of the scores for all gaps.

An example for a scoring scheme is the Levenshtein distance, for which
each mismatch between two aligned characters costs 1 and each character
that is aligned with a gap costs 1. Translated into scores instead of
costs, misalignments get a score of -1 and gaps a score of -1 per
character, while matches costs nothing. This scoring scheme is the
default for :dox:`SimpleScore Simple Score`.

SeqAn offers two kinds of scoring scheme:

+----------------------------------+--------------------+
| :dox:`SimpleScore Simple Score`   | Scoring matrices   |
| ==============================   | ================   |

+==================================+====================+
+----------------------------------+--------------------+

::

    #td valign=top width=350
    This scoring scheme differentiates between "match" (the two aligned characters are the same), "mismatch" (the two aligned characters are different), and gaps. The score for a gap of length <tt>k</tt> is <tt>gap open + (k - 1) * gap extend</tt>. If <tt>gap open</tt> equals <tt>gap extend</tt> the score scheme uses linear gap costs, otherwise it uses affine gap costs.
    The functions :dox:`SimpleScore#scoreMatch scoreMatch` and :dox:`SimpleScore#scoreMismatch scoreMismatch` access values for match and mismatch. The function :dox:`SimpleScore#scoreGap scoreGap`, or :dox:`SimpleScore#scoreGapExtend scoreGapExtend` and :dox:`SimpleScore#scoreGapOpen scoreGapOpen` access values for gaps.

::

    #td valign=top width=350
    These scoring schemes store a score value for each pair of characters. This value can be accessed using :dox:`Score#score score`. Examples for this kind of scoring scheme are :dox:`Pam120` and :dox:`Blosum62`. The class :dox:`MatrixScore Matrix Score`" can be used to store arbitrary scoring matrices. Also see the [[HowTo/WorkWithCustomScoreMatrices| HowTo on custom scoring matrices]].

::

    #InfoBox
    The order of the different costs in the scoring scheme is <tt>match</tt>, <tt>mismatch</tt>, <tt>gap extend</tt> and <tt>gap open</tt>. If you want to use linear gap costs you could also omit the last parameter <tt>gap open</tt> and the scoring scheme would automatically choose the linear gap cost function.

Global Alignments
~~~~~~~~~~~~~~~~~

In this section, we want to compute a global alignment using the
Needleman-Wunsch algorithm. We will use the Levenshtein distance as our
scoring scheme.

A program always starts with including the headers that contain the
components (data structures and algorithms) we want to use. To gain
access to the alignment algorithms we need to include the ``align.h``
header file. We tell the program that it has to use the ``seqan``
namespace and write the ``main`` function with an empty body.

A good programming practice is to define all types that shall be used by
the function at the beginning of the function body. In our case, we
define a ``TSequence`` type for our input sequences and an [dox:Align
Align] object (``TAlign``) type to store the alignment. For more
information on the Align datastructure, please read the tutorial
`Alignment Representation <Tutorial/AlignmentRepresentation>`__.

.. includefrags:: core/demos/tutorial/alignments/alignment_global_standard.cpp
   :fragment: main

After we defined the types, we can define the variables and objects.
First, we create two input sequences ``seq1 = "CDFGHC"`` and
``seq2 = "CDEFGAHC"``. We then define an 'align' object where we want to
put the sequences into, we resize it to manage two :dox:`Gaps`
objects, and then assign the sequences to it.

.. includefrags:: core/demos/tutorial/alignments/alignment_global_standard.cpp
   :fragment: init

Now, we can compute our first alignment. To do so, we simply call the
function :dox:`globalAlignment globalAlignment()` and give as input
parameters the ``align`` object and the scoring scheme representing the
Levenshtein distance. The globalAlignment function returns the score of
the best alignment, which we store in the ``score`` variable.
Afterwards, we print the computed score and the corresponding alignment.

.. includefrags:: core/demos/tutorial/alignments/alignment_global_standard.cpp
   :fragment: alignment

Here the output.

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    Score: -2
          0     .
            CD-FG-HC
    {|
    !
    !
    |}

            CDEFGAHC

Assignment 1
^^^^^^^^^^^^

::

    #AssignmentBox

     Type :: Review
     Objective :: Compute a global alignment between the DNA sequences "AAATGACGGATTG"
       "AGTCGGATCTACTG" using the Gotoh algorithm with the following scoring parameters: <tt>match = 4</tt>, <tt>mismatch = -2</tt>, <tt>gap open = -4</tt> and <tt>gap extend = -2</tt>. Store the alignment in an Align object and and print it together with the score.

     Hints ::
    <pre>
    #FoldOut
    ----
    The Gotoh algorithm uses an affine gap function. In SeqAn you can switch between linear and affine gap functions using the scoring scheme by setting different parameters for <tt>gap open</tt> and <tt>gap extend</tt>. Note, the order of the scoring parameters is important. Have a look on the scoring scheme section above if you are not sure about the correct ordering.

``Solution ::``

::

    #FoldOut
    ----
    You can find a complete solution with some more explanations
    [[Tutorial/PairwiseSequenceAlignment/Assignment/GlobalAlignmentGotoh| here]].

.. raw:: html

   </pre>

Overlap Alignments
^^^^^^^^^^^^^^^^^^

`Image(alignment\_AlignConfig.png, 40%,
align=right) <Image(alignment_AlignConfig.png, 40%, align=right)>`__ In
contrast to the global alignment, an overlap alignment does not penalize
gaps at the beginning and at the end of the sequences. This is referred
to as **free end-gaps**. It basically means that overlap alignments can
be shifted such that the end of the one sequence matches the beginning
of the other sequence, while the respective other ends are gapped.

We use the :dox:`AlignConfig` object to tell the algorithm
which gaps are free. The AlignConfig object takes four explicitly
defined bool arguments. The first argument stands for ``initial gaps``
in the vertical sequence of the alignment matrix (first row) and the
second argument stands for ``initial gaps`` in the horizontal sequence
(first column). The third parameter stands for ``end`` gaps in the
horizontal sequence (last column) and the fourth parameter stands for
``end gaps`` in the vertical sequence (last row). Per default the
arguments of AlignConfig are set to ``false`` indicating a standard
global alignment as you have seen above. In an overlap alignment all
arguments are set to ``true``. This means the first row and first column
are initialized with zeros and the maximal score is searched in the last
column and in the last row.

Just let us compute an overlap alignment to see how it works. We will
also make use of the :dox:`AlignmentGraph Alignment Graph` to store the
alignment this time. We start again with including the necessary headers
and defining all types that we need. We define the ``TStringSet`` type
to store our input sequences in a StringSet and we define the
``TDepStringSet`` which is an [dox:DependentStringSet Dependent
StringSet] used internally by the AlignmentGraph.

.. includefrags:: core/demos/tutorial/alignments/alignment_global_overlap.cpp
   :fragment: main

Before we can initialize the AlignmentGraph we append the input
sequences to the StringSet ``strings``. Then we simply pass ``strings``
as an argument to the constructor of the AlignmentGraph ``alignG``.

.. includefrags:: core/demos/tutorial/alignments/alignment_global_overlap.cpp
   :fragment: init

Now we are ready to compute the alignment. This time we change two
things when calling the ``globalAlignment`` function. First, we use an
AlignmentGraph to store the computed alignment and second we use the
AlignConfig object to compute the overlap alignment.

.. includefrags:: core/demos/tutorial/alignments/alignment_global_overlap.cpp
   :fragment: alignment

Here the output.

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    Score: 2
    Alignment matrix:
          0     .    :
            blablubalu
    {|
    !
    |}

            --ab--ba--

Assignment 2
^^^^^^^^^^^^

::

    #AssignmentBox

     Type :: Review
     Objective :: Compute a semi-global alignment between the sequences <tt>AAATGACGGATTG</tt> and <tt>TGGGA</tt> using the costs 1, -1, -1 for match, mismatch and gap, respectively. Use an AlignmentGraph to store the alignment. Print the score and the resulting alignment to the standard output.

     Hint ::
    <pre>
    #FoldOut
    ----
    A semi-global alignment is a special form of an overlap alignment often used when aligning short sequences again a long sequence. Here we only allow free free end-gaps at the beginning and the end of the shorter sequence.

``Solution ::``

::

    #FoldOut
    ----
    You can find a complete solution with some more explanations
    [[Tutorial/PairwiseSequenceAlignment/Assignment/SemiGlobalAlignment| here]].

.. raw:: html

   </pre>

Specialized Alignments
^^^^^^^^^^^^^^^^^^^^^^

SeqAn offers specialized algorithms that can be selected using a tag.
Note that often these specializations are restricted in some manner. The
following table lists the different specialized alignments and how they
are restricted.

+-----------------+---------------+
| Alignment Tag   | Description   |
| =============   | ===========   |

+=================+===============+
+-----------------+---------------+

::

    #td valign=top width=150
    Hirschberg

::

    #td valign=top width=550
    The Hirschberg algorithm computes an alignment between two sequences in linear space. The algorithm can only be used with an Align object (or Gaps). It uses only linear gap costs and does no overlap alignments.

::

    #td valign=top width=150
    MyersBitVector

::

    #td valign=top width=550
    The MyersBitVector is a fast alignment specialization using bit parallelism. It only works with the Levenshtein distance and outputs no alignments.

::

    #td valign=top width=150
    MyersHirschberg

::

    #td valign=top width=550
    The MyersHirschberg is an combination of the rapid MyersBitVector and the space efficient Hirschberg algorithm, which additionally enables the computation of an alignment. It only works with the Levenshtein distance and for Align objects.

::

    #InfoBox
    In SeqAn you can omit the computation of the traceback to get only the score by using the function :dox:`globalAlignmentScore globalAlignmentScore()`. This way you can use the alignment algorithms for verification purposes, etc..

In the following example, we want to compute a global alignment of two
sequences using the Hirschberg algorithm. We are setting the ``match``
score to ``1``, and ``mismatch`` as well as ``gap`` penalty to ``-1``.
We print the alignment and the score.

First the necessary includes and typedefs:

.. includefrags:: core/demos/tutorial/alignments/alignment_global_specialised.cpp
   :fragment: main

In addition to the previous examined examples we tell the
globalAlignment function to use the desired Hirschberg algorithm by
explicitly passing the tag ``Hirschberg`` as last parameter (for an
overview of available alignment algorithms see
:dox:`PairwiseAlignmentAlgorithms Pairwise Alignment Algorithms`). The
resulting alignment and score are then printed.

.. includefrags:: core/demos/tutorial/alignments/alignment_global_specialised.cpp
   :fragment: alignment

Here the output:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    Score: 11
          0     .    :    .
            GARFIELDTHE---CAT
    {|
    !
    !
    !
    !
    !/
    !/
    |}

            GARFIELDTHEBIGCAT

Assignment 3
^^^^^^^^^^^^

::

    #AssignmentBox

     Type :: Application
     Objective :: Write a program that computes a fast global alignment between the :dox:`Rna` sequences <tt>AAGUGACUUAUUG</tt> and <tt>AGUCGGAUCUACUG</tt> using the Align data structure and the Levenshtein distance. Print the score and the alignment. Additionally, output for each row of the Align object the view positions of the gaps.

     Hint ::
    <pre>
    #FoldOut
    ----
    You can use an iterator to iterate over a row. Use the metafunction :dox:`Align#Row Row` to get the type of the row used by the Align object.

``Hint ::``

::

    #FoldOut
    ----
    Use the function :dox:`Gaps#isGap isGap` to check whether the current value of the iterator is a gap or not.

``Hint ::``

::

    #FoldOut
    ----
    The gaps are already in the view space.

``Solution ::``

::

    #FoldOut
    ----
    You can find a complete solution with some more explanations
    [[Tutorial/PairwiseSequenceAlignment/Assignment/Assignment3MyersHirschberg| here]].

.. raw:: html

   </pre>

Local Alignments
~~~~~~~~~~~~~~~~

Now let's look at local pairwise alignments.

Seqan offers the classical Smith-Waterman algorithm that computes the
best local alignment with respect to a given scoring scheme, and the
Waterman-Eggert algorithm, which computes not only the best but also
suboptimal local alignments.

We are going to demonstrate the usage of both in the following example
where first the best local alignment of two character strings and then
all local alignments of two DNA sequences with a score greater than or
equal to 4 are computed.

.. includefrags:: core/demos/tutorial/alignments/alignment_pairwise_local.cpp
   :fragment: main

Let's start with initializing the :dox:`Align` object to contain
the two sequences.
.. includefrags:: core/demos/tutorial/alignments/alignment_pairwise_local.cpp
   :fragment: init1

Now the best alignment given the scoring parameters is computed by the
function :dox:`localAlignment`. The returned score value
is printed directly, and the alignment itself in the next line. The
functions :dox:`Gaps#clippedBeginPosition clippedBeginPosition`and
:dox:`Gaps#clippedEndPosition clippedEndPosition` can be used to retrieve
the begin and end position of the matching subsequences within the
original sequences.
.. includefrags:: core/demos/tutorial/alignments/alignment_pairwise_local.cpp
   :fragment: ali1

Next, several local alignments of the two given DNA sequences are going
to be computed. First, the :dox:`Align` object is created.
.. includefrags:: core/demos/tutorial/alignments/alignment_pairwise_local.cpp
   :fragment: init2

A :dox:`LocalAlignmentEnumerator` object needs
to be initialized on the :dox:`Align` object. In addition to the
Align object and the scoring scheme, we now also pass the ``finder`` and
a minimal score value, 4 in this case, to the localAlignment function.
The ``WatermanEggert`` tag specifies the desired Waterman-Eggert
algorithm. While the score of the local alignment satisfies the minimal
score cutoff, the alignments are printed with their scores and the
subsequence begin and end positions.
.. includefrags:: core/demos/tutorial/alignments/alignment_pairwise_local.cpp
   :fragment: ali2

Here is the output of the first part of our example program:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    Score = 19
          0     .    :
            a-philolog
    {|
    !/
    !
    !
    |}

            amphibolog


    Aligns Seq1[0:9] and Seq2[7:16]

The second part outputs two alignments:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    Score = 9
          0     .
            ATAAGCGT
    {|
    !/ |
    |}

            ATA-GAGT


    Aligns Seq1[0:7] and Seq2[2:9]

    Score = 5
          0     .
            TC-TCG
    {|
    ! / |
    |}

            TCATAG


    Aligns Seq1[7:12] and Seq2[0:5]

Assignment 4
^^^^^^^^^^^^

::

    #AssignmentBox

     Type :: Review
     Objective :: Write a program which computes the 3 best local alignments of the two :dox:`AminoAcid` sequences "<tt>PNCFDAKQRTASRPL</tt>" and "<tt>CFDKQKNNRTATRDTA</tt>" using the following scoring parameters: <tt>match = 3</tt>, <tt>mismatch = -2</tt>, <tt>gap open = -5</tt>, <tt>gap extension = -1</tt>.

     Hint ::
    <pre>
    #FoldOut
    ----
    Use an extra variable to enumerate the <tt>k</tt> best alignments.

``Solution ::``

::

    #FoldOut
    ----
    You can find a complete solution with some more explanations
    [[Tutorial/Alignments/AssignmentPairwiseLocalAlignment1| here]].

.. raw:: html

   </pre>

Banded Alignments
~~~~~~~~~~~~~~~~~

`Image(alignment\_band.png, 50%,
align=right) <Image(alignment_band.png, 50%, align=right)>`__ Often it
is quite useful to reduce the search space in which the optimal
alignment can be found, e.g., if the sequences are very similar, or if
only a certain number of errors is allowed. To do so you can define a
band, whose intersection with the alignment matrix defines the search
space. To define a band we have to pass two additional parameters to the
alignment function. The first one specifies the position where the lower
diagonal of the band crosses the vertical axis. The second one specifies
the position where the upper diagonal of the band crosses the horizontal
axis. You can imagine the matrix as the fourth quadrant of the Cartesian
coordinate system. Then the main diagonal of an alignment matrix is
described by the function ``f(x) = -x`` and all diagonals that crosses
the vertical axis below this point are specified with negative values
and all diagonals that crosses the horizontal axis right of it are
specified with positive values (see image). A given band is valid as
long as the relation ``lower diagonal <= upper diagonal`` holds. In case
of equality, the alignment is equivalent to the hamming distance
problem, where only substitutions are considered.

::

    #ImportantBox
    The alignment algorithms return <tt>MinValue<ScoreValue>::VALUE</tt> if a correct alignment cannot be computed due to invalid compositions of the band and the specified alignment preferences. Assume, you compute a global alignment and the given band does not cover the last cell of the alignment matrix. In this case it is not possible to compute a correct alignment, hence <tt>MinValue<ScoreValue>::VALUE</tt> is returned, while no further alignment information are computed.

Let's compute a banded alignment. The first step is to write the
``main`` function body including the type definitions and the
initializations.
.. includefrags:: core/demos/tutorial/alignments/alignment_banded.cpp
   :fragment: main

After we initialized everything, we will compute the banded alignment.
We pass the values ``-2`` for the lower diagonal and ``2`` for the upper
diagonal.

.. includefrags:: core/demos/tutorial/alignments/alignment_banded.cpp
   :fragment: alignment

And here is the output:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    Score: -2
          0     .
            CD-FG-HC
    {|
    !
    !
    |}

            CDEFGAHC

Assignment 5
^^^^^^^^^^^^

::

    #AssignmentBox

     Type :: Transfer
     Objective :: Write an approximate pattern matching algorithm using alignment algorithms. Report the positions of all hits where the pattern matches the text with at most <tt>2</tt> errors. Output the number of total edits used to match the pattern and print the corresponding cigar string of the alignment without leading and trailing gaps in the pattern. Text: "<tt>MISSISSIPPIANDMISSOURI</tt>" Pattern: "<tt>SISSI</tt>"

     Hint ::
    <pre>
    #FoldOut
    ----
    The first step would be to verify at which positions in the text the pattern matches with at most 2 errors.

``Hint ::``

::

    #FoldOut
    ----
    Use the :dox:`SegmentableConcept#infix infix` function to return a subsequence of a string.

``Hint ::``

::

    #FoldOut
    ----
    A cigar string is a different representation of an alignment. It consists of a number followed by an operation. The number indicates how many consecutive operations of the same type are executed. Operations can be <tt>M</tt> for match, <tt>S</tt> for mismatch, <tt>I</tt> for insertion and <tt>D</tt> for deletion. Here is an example:
    <pre>
    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    ref: AC--GTCATTT
    r01: ACGTCTCA---
    Cigar of r01: 2M2I1S3M3D

.. raw:: html

   </pre>

``Solution Step 1 ::``

::

    #FoldOut
    ----
    [[Include(source:trunk/core/demos/tutorial/alignments/pairwise_sequence_alignment_assignment5_step1.cpp, fragment=main)]]

``Solution Step 2  ::``

::

    #FoldOut
    ----
    [[Include(source:trunk/core/demos/tutorial/alignments/pairwise_sequence_alignment_assignment5_step2.cpp, fragment=main)]]

``Solution Step 3 ::``

::

    #FoldOut
    ----
    [[Include(source:trunk/core/demos/tutorial/alignments/pairwise_sequence_alignment_assignment5_step3.cpp, fragment=main)]]

``Solution Step 4  ::``

::

    #FoldOut
    ----
    [[Include(source:trunk/core/demos/tutorial/alignments/pairwise_sequence_alignment_assignment5_step4.cpp, fragment=main)]]

``Solution Step 5 ::``

::

    #FoldOut
    ----
    [[Include(source:trunk/core/demos/tutorial/alignments/pairwise_sequence_alignment_assignment5_step5.cpp, fragment=main)]]

``Solution Step 6  ::``

::

    #FoldOut
    ----
    [[Include(source:trunk/core/demos/tutorial/alignments/pairwise_sequence_alignment_assignment5_step6.cpp, fragment=main)]]

``Complete Solution ::``

::

    #FoldOut
    ----
    You can find a complete solution with some more explanations
    [[Tutorial/PairwiseSequenceAlignment/Assignment/Assignment5ApproximatePatternMatching| here]].

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
