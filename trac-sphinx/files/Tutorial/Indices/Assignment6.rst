Assignment 6
------------

Task
~~~~

Create and output a matrix M where M(i,j) is the number of common
ungapped 5-grams between sequence i and sequence j for 3 random
seqan:Spec.Dna sequences, each not longer than 200 characters. **Hint**:
A common g-gram that occurs a times in one and b times in the other
sequence counts for min(a,b). **Optional:** Run the matrix calculation
twice, once for an seqan:Spec.IndexQGram and once for an
seqan:Spec.OpenAddressing index and output the directory sizes
(QGram\_Dir, QGram\_CountsDir fibre).

Solution
~~~~~~~~

For generating random numbers we use the [seqan:"Spec.Mersenne Twister
Rng" Mersenne-Twister] which is a specialization of the random number
generator class seqan:Class.Rng. The random numbers returned by
seqan:Function.pickRandomNumber are arbitrary ``unsigned int`` values
which we downscale to values between 0 and 3 and convert into
seqan:Spec.Dna characters. The 3 generated strings are of random length
and appended to a seqan:Class.StringSet. The main algorithmus is
encapsulated in a template function ``qgramCounting`` to easily switch
between the two seqan:Spec.IndexQGram specializations.
.. includefrags:: core/demos/tutorial/index/index_assignment6.cpp
   :fragment: initialization

The main function expects the seqan:Class.StringSet and the
seqan:Class.Index specialization as a [seqan:Page.Glossary Tag]. First,
we define lots of types we need to iterate and access the fibres
directly. We then notify the index about the fibres we require. For
storing the common q-grams we use a 2-dimensional seqan:Class.Matrix
object whose lengths have to be set with ``<tt><tt>setLength``\  for
each dimension. The matrix is initialized with zeros by
seqan:Function.resize.
.. includefrags:: core/demos/tutorial/index/index_assignment6.cpp
   :fragment: matrix_init

The main part of the function iterates over the CountsDir fibre. Each
entry in this directory represents a q-gram bucket, a contiguous
interval in the Counts fibre storing for every sequence the q-gram
occurs in the number of occurrences in pairs (seqNo,count). The interval
begin of each bucket is stored in the directory and the interval end is
the begin of the next bucket. So the inner loops iterate over all
non-empty buckets and two pairs (seqNo1,count1) and (seqNo2,count2)
indicate that seqNo1 and seqNo2 have a common q-gram. At the end the
matrix can simply be output by shifting it to the ``cout`` stream.
.. includefrags:: core/demos/tutorial/index/index_assignment6.cpp
   :fragment: matrix_calculation

Please note that the seqan:Spec.OpenAddressing index directories are
smaller than the seqan:Spec.IndexQGram index directories. Program
output:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    >Seq0
    TCATTTTCTCGATGAAAGCGTTGACCCCACATATCGTTAGTACTCTTGTACCCT
    >Seq1
    TGATTGTGTAGAAACCGAACTACGGTACCTCCTGTTGGTAGTCACGATAGATTATAAAAGTATGTTCCCACCCTATCGACGAGACTGGCA
    >Seq2
    CCTAGGTGTTTGCGGTGTTGGTACGTGCG

    Length of the CountsDir fibre: 1025

    Common 5-mers for Seq_i, Seq_j
    50  4   0
    0   86  5
    0   0   25

    Length of the CountsDir fibre: 259

    Common 5-mers for Seq_i, Seq_j
    50  4   0
    0   86  5
    0   0   25

.. raw:: html

   </pre>

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
