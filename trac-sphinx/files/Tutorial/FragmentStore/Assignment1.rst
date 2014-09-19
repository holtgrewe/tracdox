Task 1: Fragment Store
----------------------

Task
~~~~

Modify the example that output pairwise alignments of aligned reads,
such that reads that align to the reverse strand are displayed in
lower-case letters.

Solution
~~~~~~~~

As we copy the read sequence, it suffices to change the type of the
target string readSeq and the sequence type of the read seqan:Class.Gaps
object into CharString, i.e. a seqan:Class.String of ``char``.
.. includefrags:: core/demos/tutorial/store/store_access_aligned_reads2.cpp
   :fragment: typedefs

Then we not only need to reverse-complement readSeq if the read aligns
to the reverse strand (endPos

#. html

::

    ALIGNMENT 140
        contig 0:   CTGTGTTTAGTGCCTTTGTTCA-----ACCCCCTTGCAAC        [266..306[
        read 149:   ctgtgtttagtgcctttgttca-----acccccttgcaac

    ALIGNMENT 144
        contig 0:   AGTGCCTTTGTTCA-----ACCCCCTTGCAACAACC        [274..310[
        read 153:   AGTGCCTTTGTTCACATAGACCCCCTTGCAACAACC

    ALIGNMENT 148
        contig 0:   TTCA-----ACCCCCTTGCAACAACCTTGAGAACCCCAGG        [284..324[
        read 157:   ATAG-----ACCCCCTTGCAACAACCTTGAGAACCCCAGG

    ALIGNMENT 152
        contig 0:   CA-----ACCCCCTTGCAACAACCTTGAGAACCCCAGGGA        [286..326[
        read 161:   CA-----ACCCCCTTGCAACAACCTTGCGAACCCCAGGGA

    ALIGNMENT 156
        contig 0:   CCCCCTTGCAACAACCTTGAGAACCCCAGGGAATT         [294..329[
        read 165:   cccccttgcaacaaccttgagaaccccagggaatt

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
