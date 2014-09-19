Tutorial q-gram Index
---------------------

TOC

| ``Learning Objective ::``
| ``You will know the features of the q-gram Index, how it can be used for searching and how to access the different fibres.``
| ``Difficulty ::``
| `` Average``
| ``Duration ::``
| `` 1h``
| ``Prerequisites ::``
| `` ``\ ```Tutorial/Sequences`` <Tutorial/Sequences>`__\ ``, ``\ ```Tutorial/Iterators`` <Tutorial/Iterators>`__

The q-gram Index
~~~~~~~~~~~~~~~~

A q-gram index can be used to efficiently retrieve all occurrences of a
certain q-gram in the text. It consists of various tables, called fibres
(see `HowTo <HowTo/AccessIndexFibres>`__), to retrieve q-gram positions,
q-gram counts, etc. However, it has no support for suffix tree
iterators. A q-gram index must be specialized with a :dox:`Shape`
type. A :dox:`Shape` defines q, the number of characters in a
q-gram and possibly gaps between these characters. There are different
specializations of :dox:`Shape` available:

+---------------------------------------+--------------------+----------------------+
| **Specialization**                    | **Modifiable\***   | **Number of Gaps**   |
+=======================================+====================+======================+
| :dox:`UngappedShape`     | -                  | 0                    |
+---------------------------------------+--------------------+----------------------+
| :dox:`SimpleShape`         | +                  | 0                    |
+---------------------------------------+--------------------+----------------------+
| :dox:`OneGappedShape`   | +                  | 0/1                  |
+---------------------------------------+--------------------+----------------------+
| :dox:`GappedShape`         | -                  | any                  |
+---------------------------------------+--------------------+----------------------+
| :dox:`GenericShape`      | +                  | any                  |
+---------------------------------------+--------------------+----------------------+

-  - *fixed at compile time*, + *can be changed at runtime*

Each shape evaluates a gapped or ungapped sequence of q characters to a
hash value by the Functions :dox:`Shape#hash hash`, [dox:Shape#hash
hash]Next, etc. For example, the shape 1101 represents a 3-gram with one
gap of length 1. This shape overlayed with the :dox:`Dna` text
"GATTACA" at the third position corresponds to "TT-C". The function
:dox:`Shape#hash hash` converts this 3-gram into
61=((\ **3**\ \*4+\ **3**)\*4+\ **1**. 4 is the alphabet size in this
example (see :dox:`ValueSize`).

With :dox:`Shape#hash hash` / :dox:`Shape#hash hash`Next we can compute
the hash values of arbitrary / adjacent q-grams and a loop that outputs
the hash values of all overlapping ungapped 3-grams could look as
follows:
.. includefrags:: core/demos/tutorial/index/index_qgram_hash.cpp
   :fragment: hash_loop1

Note that the shape not only stores the length and gaps of a q-gram
shape but also stores the hash value returned by the last hash/hashNext
call. This hash value can be retrieved by calling [dox:Shape#value
value] on the shape. However, one drawback of the example loop above is
that the first hash value must be computed with :dox:`Shape#hash hash`
while the hash values of the following overlapping q-grams can more
efficiently be computed by :dox:`Shape#hashNext hashNext`. This
complicates the structure of algorithms that need to iterate all hash
values, as they have to handle this first hash differently. As a remedy,
the :dox:`Shape#hashInit hashInit` function can be used first and then
:dox:`Shape#hashNext hashNext` on the first and all following text
positions in the same way:
.. includefrags:: core/demos/tutorial/index/index_qgram_hash.cpp
   :fragment: hash_loop2

The q-gram index offers different functions to search or count
occurrences of q-grams in an indexed text, see [dox:Index#getOccurrences
getOccurrences], :dox:`Index#countOccurrences countOccurrences`. A q-gram
index over a :dox:`StringSet` stores occurrence positions in
the same way as the ESA index and in the same fibre (FibreSA). If only
the number of q-grams per sequence are needed the QGramCounts and
QGramCountsDir fibres can be used. They store pairs ``(seqNo, count)``,
``count``>0, for each q-gram that occurs ``counts`` times in sequence
number ``seqNo``.

To efficiently retrieve all occurrence positions or all pairs
``(seqNo, count)`` for a given q-gram, these positions or pairs are
stored in contiguous blocks (in QGramSA, QGramCounts fibres), called
buckets. The begin position of bucket i is stored in directory fibres
(QGramDir, QGramCountsDir) at position i, the end position is the begin
positions of the bucket i+1. The default implementation of the
:dox:`IndexQGram` index maps q-gram hash values 1-to-1 to
bucket numbers. For large q or large alphabets the
:dox:`OpenAddressingQGramIndex Open Adressing QGram Index` can be more
appropriate as its directories are additionally bound by the text
length. This is realized by a non-trivial mapping from q-gram hashes to
bucket numbers that requires an additional fibre (QGramBucketMap).

For more details on q-gram index fibres see the
`HowTo <HowTo/AccessIndexFibres>`__ or [dox:QGramIndexFibres QGram Index
Fibres].

Example
~~~~~~~

We want to construct the q-gram index of the string "CATGATTACATA" and
output the occurrences of the ungapped 3-gram "CAT". As 3 is fixed at
compile-time and the shape has no gaps we can use a [dox:UngappedShape
UngappedShape] which is the first template argument of [dox:IndexQGram
IndexQGram], the second template argument of :dox:`Index`. Next we
create the string "CATGATTACATA" and specialize the first index template
argument with the type of this string. The string can be given to the
index constructor.
.. includefrags:: core/demos/tutorial/index/index_qgram.cpp
   :fragment: initialization

To get all occurrences of a q-gram, we first have to hash it with a
shape of the same type as the index shape (we can even use the index
shape returned by :dox:`IndexQGram#indexShape indexShape`). The hash
value returned by :dox:`Shape#hash hash` or :dox:`Shape#hashNext hashNext`
is also stored in the shape and is used by the function
:dox:`Index#getOccurrences getOccurrences` to retrieve all occurrences of
our 3-gram.
.. includefrags:: core/demos/tutorial/index/index_qgram.cpp
   :fragment: output

Program output:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    0
    8

.. raw:: html

   </pre>

Assignment 1
^^^^^^^^^^^^

::

    #AssignmentBox
     Type ::
     Review
     Objective ::
     Write a program that outputs all occurrences of the gapped q-gram "AT-A" in "CATGATTACATA".
     Solution ::
     Click [[Tutorial/Indices/Assignment5| more]]

Assignment 2
^^^^^^^^^^^^

::

    #AssignmentBox
      Type ::
     Review
     Objective ::
     Create and output a matrix M where M(i,j) is the number of common ungapped 5-grams between sequence i and sequence j for 3 random :dox:`Dna` sequences, each not longer than 200 characters. Optional: Run the matrix calculation twice, once for an :dox:`IndexQGram` and once for an :dox:`OpenAddressingQGramIndex Open Adressing QGram Index` and output the directory sizes (QGram_Dir, QGram_CountsDir fibre).
     Hint :: A common g-gram that occurs a times in one and b times in the other sequence counts for min(a,b).
     Solution ::
     Click [[Tutorial/Indices/Assignment6| more]]

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
