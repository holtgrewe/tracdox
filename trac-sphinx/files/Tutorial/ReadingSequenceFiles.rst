::

    #FoldOut
    Deprecated
    ----
    == Reading Sequence Files ==
    [[TOC()]]

    <pre>
    #html
    <div class="system-message">
    <strong>Caution</strong>:
    This tutorial and the described library contents are currently in <strong>beta state</strong>.
    They might change in the future.
    In this case, notice will be given.
    </div>

This chapter explains how to read sequence files. Currently, SeqAn
supports reading sequences (and qualities where it applies) in FASTA,
FASTQ, EMBL and GenBank format. There are three API types: (1) record
reading, (2) document/batch reading, and (3) indexed reading of sequence
files.

The first two API styles are also described in the `File I/O
2.0 <Tutorial/FileIO2>`__ chapter. To recap: Record reading is suitable
for reading many sequences when only one or few sequences are to be kept
in main memory at the same time. Document reading (especially the
double-pass variant) is suitable when all sequences are to be kept in
main memory and the "waste memory" in allocated but unused parts of
buffers is to be kept low at a cost of accessing each part of the file
twice. Indexed reading separates the double-pass reading into two steps:
(1) **splitting:** determining where the sequence identifiers, sequences
and qualities start and the lengths and (2) **loading** of the sequences
by their index in the file.

Record Reading API
~~~~~~~~~~~~~~~~~~

The sequence files are interpreted as a sequence of records, each with
an *id subrecord* and a *sequence subrecord*. The sequence subrecord
includes the residue qualities. For FASTA and FASTQ, both single- and
double-pass I/O have been implemented. For EMBL and GenBank, only
single-pass I/O is available at the moment.

The following example shows an example for reading sequences from a
FASTA file
([source:trunk/extras/demos/tutorial/stream/stream\_read\_record\_fasta.cpp
full source], [source:trunk/extras/demos/tutorial/stream/example.fasta
example.fasta]).

.. includefrags:: extras/demos/tutorial/stream/stream_read_record_fasta.cpp
   :fragment: read-sequences

An example run of this program:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    $ ./extras/demos/tutorial/stream/tutorial_stream_read_record_fasta ../../extras/demos/tutorial/stream/example.fasta
    first sequence  CGATCGATCGAT
    second sequence CCCAAATTTGGG

.. raw:: html

   </pre>

You can use seqan:Function.readRecord with the tag
seqan:Shortcut.AutoSeqStreamFormat for using automatic file detection
(full source:
[source:trunk/extras/demos/tutorial/stream/stream\_read\_record\_auto\_format.cpp
full source], [source:trunk/extras/demos/tutorial/stream/example.fasta
example.fasta]). You have to change the above program only slightly.
First, declare a variable of type seqan:Shortcut.AutoSeqStreamFormat.

.. includefrags:: extras/demos/tutorial/stream/stream_read_record_auto_format.cpp
   :fragment: file-format

We then call seqan:Function.checkStreamFormat here to determine the file
format, but this is optional. This is also automatically performed in
the seqan:Function.readRecord call in the part below.

.. includefrags:: extras/demos/tutorial/stream/stream_read_record_auto_format.cpp
   :fragment: read-sequences

And here is the program in action:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    $ ./extras/demos/tutorial/stream/tutorial_stream_read_record_auto_format ../../extras/demos/tutorial/stream/example.fasta
    File format is FASTA
    first sequence  CGATCGATCGAT
    second sequence CCCAAATTTGGG

.. raw:: html

   </pre>

Document Reading API
~~~~~~~~~~~~~~~~~~~~

We can also read whole FASTA and FASTQ files into seqan:Class.StringSet
objects using the seqan:Function.read2 function. (NB: This function is
called *read2* to avoid conflicts with the old I/O function *read*. In
the future, the old *read* function will be removed and *read2* will be
renamed to *read*).

The following example shows how to do this for FASTQ files using
single-pass with the default Owner [seqan:Class.StringSet StringSets]
and double-pass I/O with [seqan:Spec.ConcatDirect ConcatDirect
StringSets]. When the latter (double-pass with concat-direct) is used
together with reading from [seqan:"Spec.MMap String" memory mapped
strings], it yields a very compact representation after the sequences
are in main memory, at the cost of accessing each part of the input file
twice. Since [seqan:"Spec.MMap String" MMap Strings] are used, buffer
usage is minimized (the operating system will make the actual buffer
used for DMA I/O visible to your program).

First, we read the FASTQ file using Single-Pass I/O on an
``std::fstream`` object. We write the sequence ids, the sequences and
the qualities to stdout.

.. includefrags:: extras/demos/tutorial/stream/stream_read2_fastq.cpp
   :fragment: read-sequences-single-pass

Then, we do the same with double-pass I/O and a memory mapped string.

.. includefrags:: extras/demos/tutorial/stream/stream_read2_fastq.cpp
   :fragment: read-sequences-double-pass

Example run of the complete program
([source:trunk/extras/demos/tutorial/stream/stream\_read2\_fastq.cpp
full source], [source:trunk/extras/demos/tutorial/stream/example.fastq
example.fastq]):

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    $ ./extras/demos/tutorial/stream/tutorial_stream_read2_fastq ../../extras/demos/tutorial/stream/example.fastq
    Reading from std::fstream...

    first sequence  CGATCGATCGAT    !+!+!+!+!!+!
    second sequence CCCAAATTTGGG    +!+!+!+!!++!

    Reading from memory mapped string...

    first sequence  CGATCGATCGAT    !+!+!+!+!!+!
    second sequence CCCAAATTTGGG    +!+!+!+!!++!

.. raw:: html

   </pre>

Similar to the function seqan:Function.readRecord, the function
seqan:Function.read2 also supports seqan:Shortcut.AutoSeqStreamFormat:

::

    #cpp
    AutoSeqStreamFormat formatTag;
    if (read2(ids, seqs, reader, formatTag) != 0)
    {
        std::cerr << "ERROR reading FASTA." << std::endl;
        return 1;
    }

Indexed Reading API
~~~~~~~~~~~~~~~~~~~

Indexed reading can be done through seqan:Shortcut.MultiSeqFile which is
a shortcut to a memory mapped string set. We open the file using
seqan:Function.open on its ``concat`` member (which is a
seqan:"Spec.MMap String"). The function seqan:Function.split then parses
the file contents and sets the separating indexes of the
seqan:Class.StringSet. For this, we need the file format. We could give
a fixed format in the tag (e.g. ``Fastq()``) or use
seqan:Class.AutoSeqFormat together with seqan:Function.guessFormat.

.. includefrags:: extras/demos/tutorial/stream/stream_multi_seq_file.cpp
   :fragment: open-guess-split

Now, we can access the sequence, qualities and ids using the functions
seqan:Function.assignSeq, seqan:Function.assignQual, and
seqan:Function.assignSeqId. Note that these functions still have to do
some parsing of the input file. The number of sequences is the same as
the number of entries in the ``MultiSeqFile`` ``StringSet``.

.. includefrags:: extras/demos/tutorial/stream/stream_multi_seq_file.cpp
   :fragment: load

Finally, we print the result.

.. includefrags:: extras/demos/tutorial/stream/stream_multi_seq_file.cpp
   :fragment: output

The full example can be found
[source:trunk/extras/demos/tutorial/stream/stream\_multi\_seq\_file.cpp
here].

Indexed reading has multiple advantages:

-  Its performance is only slightly worse than when reading sequentially
   with a double-pass String RecordReader.
-  The input file is mapped into main memory and otherwise complicated
   page-wise memory management is done by the operating system and does
   not have to be implemented by the user: The user can access the file
   almost at random and only the used parts will be loaded into main
   memory. This is quite efficient when only few sequences are needed.

If you need to have fast random access to all sequences in a file then
loading it into a seqan:Spec.ConcatDirect StringSet with the
batch-reading API is faster than using seqan:Shortcut.MultiSeqFile.

Submit a comment
^^^^^^^^^^^^^^^^

If you found a mistake, or have suggestions about an improvement of this
page press:
[/newticket?component=Documentation&description=Tutorial+Enhancement+for+page+http://trac.seqan.de/wiki/Tutorial/ReadingSequenceFiles&type=enhancement
submit your comment]

.. raw:: html

   </pre>

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
