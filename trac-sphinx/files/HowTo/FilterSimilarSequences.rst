How To: Filtering Similar Sequences
-----------------------------------

TOC

Using Swift
~~~~~~~~~~~

In the next example we are going to use the seqan:Spec.Swift filter to
efficiently find pairs of similar reads. The Swift algorithms searches
for so-called epsilon matches, local alignments, of two sequences with
an error rate below a certain epsilon threshold.

The Swift implementation in SeqAn provides a seqan:Function.find
interface and requires the seqan:Class.Finder and seqan:Class.Pattern to
be specialized with $Swift<..>$. Millions of sequences can be searched
simultaneously with one seqan:Class.Pattern in a Finder of a single
haystack sequence. The error rate of a local alignment is the number of
errors divided by the length of the needle sequence part of the match.
There are currently two version of the Swift algorithm implemented in
Seqan, seqan:Spec.SwiftSemiGlobal and seqan:Spec.SwiftLocal. Both can be
used to search epsilon-matches of a certain minimum length.
seqan:Spec.SwiftSemiGlobal should only be used for short needles
(sequenced reads) as it always returns potential epsilon matches
spanning a whole needle sequence. seqan:Spec.SwiftLocal should be
preferred for large needles as it returns needle sequences potentially
having an intersection with an epsilon match.

The following program searches for semi-global alignments between pairs
of reads with a maximal error rate of 10%.
.. includefrags:: core/demos/howto/filter_similar_sequences.cpp
   :fragment: includes

First we loads reads from a file into a seqan:Class.FragmentStore with
seqan:Function.loadReads.
.. includefrags:: core/demos/howto/filter_similar_sequences.cpp
   :fragment: load_reads

Swift uses a q-gram index of the needle sequences. Thus, we have to
specialize the seqan:Class.Pattern with a seqan:Spec.IndexQGram index of
the needle seqan:Class.StringSet in the first template argument, create
the index over the [seqan:Memvar.FragmentStore#readSeqStore
readSeqStore] and pass the index to the seqan:Class.Pattern constructor.
seqan:Class.Finder and seqan:Class.Pattern classes have to be
specialized with seqan:Spec.SwiftSemiGlobal in the second template
argument. The main loop iterates over all potential matches which can be
further processed, e.g. by a semi-global or overlap aligner.
.. includefrags:: core/demos/howto/filter_similar_sequences.cpp
   :fragment: filter

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
