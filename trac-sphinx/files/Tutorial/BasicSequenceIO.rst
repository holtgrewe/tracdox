Basic Sequence I/O
------------------

TOC()

| ``Learning Objective ::``
| `` You will learn how to read and write sequence files (FASTA and FASTQ) using a simple, high-level API in the SeqAn library.``
| `` This includes reading and writing compressed files.``
| ``Difficulty ::``
| `` Basic``
| ``Duration ::``
| `` 30 min``
| ``Prerequisites ::``
| `` ``\ ```Tutorial/Sequences`` <Tutorial/Sequences>`__

This tutorial explains how to read and write sequence files using the
:dox:`SequenceStream` class.

The SeqAn library's I/O functionality (i.e. reading from and writing to
files) is organized in layers and :dox:`SequenceStream` is
in the highest layer: It provides an easy-to-use API for reading and
writing sequence files, automatically compressing and decompressing
data, and support for different sequence formats. This flexibility comes
at a slight cost of performance, compared to using the more low-level
APIs.

The lower layers are responsible for providing raw file I/O
functionality and adding parsing functionality. Their usage is not part
of this tutorial and is explainend in the Tutorials `File
I/O <Tutorial/FileIO>`__, `Reading Sequence
Files <Tutorial/ReadingSequenceFiles>`__, and
`Parsing <Tutorial/Parsing>`__.

After completing the tutorial, you will be able to read and write
sequence files in the formats supported by the [dox:SequenceStream
SequenceStream] class.

A First Working Example
~~~~~~~~~~~~~~~~~~~~~~~

Let us start out with a minimal working example. The following small
program will read the file ``example.fa`` (which we will create later)
from the current directory and print out the identifier and the sequence
of the first record.

Include(source:/trunk/extras/demos/tutorial/basic_sequence_io/example1.cpp)

We use the [dox:SequenceStream#SequenceStream SequenceStream
constructor] with one parameter, the path to the file we want to read.
This will open the file and guess the file format from the file
contents. The class will read the first some thousand characters and try
to guess what format the file is. Note that you can also pass ``"-"`` as
the file name. This will open the standard input when reading and the
standard output when writing.

After construction, the ``seqStream`` object is ready for reading. We
use the function :dox:`SequenceStream#readRecord readRecord` to read the
first record from the file. :dox:`SequenceStream#readRecord readRecord`
always reads the next record in the file.

::

    #InfoBox
    '''Information:''' FASTA/FASTQ and Record-Based Files

    Most files in Bioinformatics have a record-based structure.
    Often, a file format requires or allows for a header that contains information about the file format.
    Then, the file contains a list of records, one after another.

    The FASTA and FASTQ formats do not have a header but only contain lists of records.
    For example, a FASTQ record contains the sequence id, the sequence characters, and a quality value for each character.

Note that we do not have to close the file manually: The
:dox:`SequenceStream` object will automatically close any
open files when it goes out of scope and it is destructred. If you want
to force a file to be closed, you can use the function
:dox:`SequenceStream#close close`.

Adding Error Handling
~~~~~~~~~~~~~~~~~~~~~

Now, create a new FASTA file named ``example.fa`` in a directory of your
choice with the following content:

::

    >seq1
    CCCCCCCCCCCCCCC
    >seq2
    CGATCGATC
    >seq3
    TTTTTTT

Then, copy the program above into new application
``basic_seq_io_example``, adjust the path ``"example.fa"`` to the just
created FASTA file, compile the program, and run it. For example, if you
stored the file ``example.fa`` in ``/home/username/example.fa``, you
replace the line ``seqan::SequenceStream seqStream("example.fa");`` from
above with
``seqan::SequenceStream seqStream("/home/username/example.fa");``. You
should see the following output:

::

    #ShellBox
    # basic_seq_io
    seq1    CCCCCCCCCCCCCCC

::

    #AssignmentBox
    '''Assignment 1'''

     Type ::
      Review
     Objective ::
      Adjust the program above to use the first command line parameter <tt>argv[1]</tt>, i.e. the first argument.
      Check that there actually is such an argument (<tt>argc >= 2</tt>) and let <tt>main()</tt> return <tt>1</tt> otherwise.
     Solution ::
      Click ''more...'' to see the solution.

    <pre>#FoldOut
    ----
    [[Include(source:/trunk/extras/demos/tutorial/basic_sequence_io/solution1.cpp)]]

.. raw:: html

   </pre>

Our program is very simple but there is one large problem: Anything can
go wrong during file I/O and have not used any means to handle such
errors. Possible errors include: The file permissions forbid a certain
operations, the file does not exist, there is a disk reading error, a
file read from a remote location gets deleted while we are reading from
it, or there is a physical error in the hard disk.

Let us add some error handling. At the very least, we should detect
errors. If possible, we should try to recover from the error (sometimes
it is possible to return default values instead of loading values from a
file) or otherwise stop the current task in an organized fashion and
notify the user about the problem.

We can use the Function :dox:`SequenceStream#isGood isGood` to check
whether the :dox:`SequenceStream` object is ready for any
more reading. After the creation of the object, this function indicates
whether the file could be opened successfully by returning ``true``. The
function :dox:`SequenceStream#readRecord readRecord` returns an ``int``
that indicates whether the reading was successful. If everything went
fine, it returns ``0``, and a different value otherwise.

Note that :dox:`SequenceStream#isGood isGood` queries the state of the
stream and returns a ``bool`` indicating whether the stream is ready for
reading/writing (``true`` for "is good" and ``false`` for "is not
good"). :dox:`SequenceStream#readRecord readRecord`, on the other hand,
returns an ``int`` indicating whether there was any error (``0`` for "is
good" and a non-\ ``0`` value for "is not good", as it is customary in
Unix programming).

The program will now read as follows:

Include(source:/trunk/extras/demos/tutorial/basic_sequence_io/example2.cpp)

::

    #AssignmentBox
    '''Assignment 2'''

     Type ::
      Review
     Objective ::
      Change your program from above to perform these checks, too.
     Solution ::
      Click ''more...'' to see the solution.

    <pre>#FoldOut
    ----
    [[Include(source:/trunk/extras/demos/tutorial/basic_sequence_io/solution2.cpp)]]

.. raw:: html

   </pre>

::

    #AssignmentBox
    '''Assignment 3'''

     Type ::
      Application
     Objective ::
      Change your program from above to loop over all sequences and print them in the same fashion.
     Hint ::
      You can use the function :dox:`SequenceStream#atEnd atEnd` to check whether a :dox:`SequenceStream` object is at the end of the file.
     Solution ::
      Click ''more...'' to see the solution.

    <pre>#FoldOut
    ----
    [[Include(source:/trunk/extras/demos/tutorial/basic_sequence_io/solution3.cpp)]]

.. raw:: html

   </pre>

After completing Assignment 3, you should be able to run your program on
the example file we created above and see the following output:

::

    #ShellBox
    # basic_seq_io_example example.fa
    seq1    CCCCCCCCCCCCCCC
    seq2    CGATCGATC
    seq3    TTTTTTT

The Interface for Reading
~~~~~~~~~~~~~~~~~~~~~~~~~

There are three major usage patterns for sequence I/O:

#. We want to read **all records** from the file into memory, for
   example for building an index.

| ``2. We want to read the file into memory ``\ **``record`` ``by``
``record``**\ ``, so the memory usage is minimal.``
| ``   We could then perform some computation on each record, e.g. search it in an index.``
| ``3. We want to read a ``\ **``batch`` ``of``
``records``**\ `` into memory, e.g. 100k records at a time.``
| ``   Then, we perform some computation on the records, for example in parallel with 4 threads on 25k records each.``

These use cases are supported by the functions
:dox:`SequenceStream#readAll readAll`, [dox:SequenceStream#readRecord
readRecord], and :dox:`SequenceStream#readBatchreadBatch`.

Each of these functions is available in two variants: The first
accepting only the sequence identifier and sequence characters besides
the :dox:`SequenceStream` object and the second also
accepting the a :dox:`CharString` for the PHRED base
qualities. If a file does not contain any qualities and the function
variant with quality values is used then the quality strings are
returned as empty. When writing a file with qualities and the function
variant without quality values is used then the qualities are written
out as ``'I'``, i.e. PHRED score 40.

When :dox:`DnaQ` or :dox:`Dna5Q` are used, then you should use
the function variant without a parameter for qualities: The qualities
are simply stored directly in the sequence characters.

As to be expected, when there are characters in the file that are not
valid characters in the :dox:`String` then the alphabet-dependent
conversion is performed. For example, for :dox:`Dna` and [dox:Rna
Rna] this means a conversion of the invalid character to ``'A'``, and
for :dox:`Dna5 Dna5 and [dox:Rna5 Rna5` this means a conversion to
``'N'``.

Here is an example for using :dox:`SequenceStream#readRecord readRecord`:

::

    #cpp
    seqan::CharString id;
    seqan::Dna5String seq;
    seqan::CharString qual;
    int res = 0;

    seqan::SequenceStream seqStream("in.fq");

    res = readRecord(id, seq, seqStream);
    res = readRecord(id, seq, qual, seqStream);

The functions :dox:`SequenceStream#readAll readAll` and
:dox:`SequenceStream#readBatch readBatch` use :dox:`StringSet`
instead of :dox:`String`. The function
:dox:`SequenceStream#readBatch readBatch` reads up to the given number of
records. It is not an error if there are less records.

::

    #cpp
    seqan::StringSet<seqan::CharString> ids;
    seqan::StringSet<seqan::Dna5String> seqs;
    seqan::StringSet<seqan::CharString> quals;
    int res = 0;

    seqan::SequenceStream seqStream("in.fq");

    res = readAll(ids, seqs, seqStream);
    res = readAll(ids, seqs, quals, seqStream);

    res = readBatch(ids, seqs, seqStream, 10);
    res = readBatch(ids, seqs, quals, seqStream, 10);

::

    #AssignmentBox
    '''Assignment 4'''

     Type ::
      Application
     Objective ::
      Change your result of Assignment 3 to use the variant of :dox:`SequenceStream#readRecord readRecord` that also reads in the qualities and writes them next to the sequences.
      Create the following FASTQ file <tt>example.fq</tt>.

      <pre>
    @seq1
    CCCCCCCCCCCCCCC
    +
    IIIIIHIIIIIIIII
    @seq2
    CGATCGATC
    +
    IIIIIIIII
    @seq3
    TTTTTTT
    +
    IIIIHHG

`` When your program is called on this file, the result should look as follows.``

`` ``

::

    #ShellBox
    # basic_seq_io_example example.fq
    seq1    CCCCCCCCCCCCCCC    IIIIIHIIIIIIIII
    seq2    CGATCGATC    IIIIIIIII
    seq3    TTTTTTT      IIIIHHG

| ``Solution ::``
| `` Click ``\ *``more...``*\ `` to see the solution.``

::

    #FoldOut
    ----
    [[Include(source:/trunk/extras/demos/tutorial/basic_sequence_io/solution4.cpp)]]

.. raw:: html

   </pre>

The Interface for Writing
~~~~~~~~~~~~~~~~~~~~~~~~~

Now that you know how to read sequence files, writing them will come
easy to you. We can open files for writing by giving
``seqan::SequenceStream::WRITE`` as the second parameter to the
:dox:`SequenceStream#SequenceStream SequenceStream constructor`. Create a
new SeqAn app ``basic_seq_io_example2`` in your sandbox and change the
C++ file ``basic_seq_io_example2.cpp`` in this application to have the
content below. This program already has all the bells and whistles for
error checking.

Include(source:/trunk/extras/demos/tutorial/basic_sequence_io/example3.cpp)

The first lines are similar to those in the solution to Assignment 4.
However, instead of opening the file using
``seqan::SequenceStream seqStream(argv[1]);``, we use
``seqan::SequenceStream seqStream(argv[1], seqan::SequenceStream::WRITE);``.
this opens the file with the name in ``argv[1]`` for writing instead of
for reading. Also, instead of reading records, we write one record.

The program writes out one sequence with id "seq1" and the contents
"CGAT" to the file given on the command line. Note that
:dox:`SequenceStream` will guess the format from the file
name. A file ending in ``.fa`` and ``.fasta`` mean FASTA, ``.fq`` and
``.fastq`` means FASTQ. Optionally, you can force to use any file format
with the third parameter to the [dox:SequenceStream#SequenceStream
SequenceStream constructor].

Let us try out the program from above:

::

    #ShellBox
    # basic_seq_io_example2 out.fa
    # cat out.fa
    >seq1
    CGAT
    # basic_seq_io_example2 out.fq
    # cat out.fq
    @seq
    CGAT
    +
    IIII

::

    #AssignmentBox
    '''Assignment 5'''

     Type ::
      Reproduction
     Objective ::
      Change the program from above to write out a second sequence.
     Solution ::
      Click ''more...'' to see the solution.

    <pre>#FoldOut
    ----
    [[Include(source:/trunk/extras/demos/tutorial/basic_sequence_io/solution5.cpp)]]

.. raw:: html

   </pre>

There are two functions for writing to sequence files using
:dox:`SequenceStream`. One,
:dox:`SequenceStream#writeRecord writeRecord`, for writing one sequence
record from :dox:`String Strings`, and another one,
:dox:`SequenceStream#writeAll writeAll`, for writing all sequences from
:dox:`StringSet StringSets`.

Again, they come in one variant with and another variant without base
qualities. When writing to a FASTQ file using the function without
qualities, the PHRED score 40 is written for each character (``'I'``)
and when writing to a FASTA file with the variant with qualities, the
qualities are ignored. When using :dox:`DnaQ` or :dox:`Dna5Q`,
the variant without qualities parameter writes out the qualities stored
in the sequence characters themselves.

Here is an example for using [dox:SequenceStream#writeRecord
writeRecord]:

::

    #cpp
    seqan::CharString id;
    seqan::Dna5String seq;
    seqan::CharString qual;

    seqan::SequenceStream seqStream("out.fq", seqan::SequenceStream::WRITE);

    res = writeRecord(seqStream, id, seq);
    res = writeRecord(seqStream, id, seq, qual);

And here is an example for using :dox:`SequenceStream#writeAll writeAll`:

::

    #cpp
    seqan::StringSet<seqan::CharString> ids;
    seqan::StringSet<seqan::Dna5String> seqs;
    seqan::StringSet<seqan::CharString> quals;

    seqan::SequenceStream seqStream("out.fq", seqan::SequenceStream::WRITE);

    res = writeAll(seqStream, ids, seqs);
    res = writeAll(seqStream, ids, seqs, quals);

::

    #AssignmentBox
    '''Assignment 6'''

     Type ::
      Application
     Objective ::
      Change the result of Assignment 5 to store the data for the two records in :dox:`StringSet StringSets` and write them out using :dox:`SequenceStream#writeAll writeAll`.
     Solution ::
      Click ''more...'' to see the solution.

    <pre>#FoldOut
    ----
    [[Include(source:/trunk/extras/demos/tutorial/basic_sequence_io/solution6.cpp)]]

.. raw:: html

   </pre>

Compressed Files
~~~~~~~~~~~~~~~~

Using compressed files is simple: When opening a file for reading,
:dox:`SequenceStream` will automatically detect whether
the file is compressed or not, the same it detects the sequence file
format for you. If you run into problems here, make sure that you have
zlib and/or libbz2 installed (see box "Dependencies on Compression
Libraries" below).

When opening a file for writing, :dox:`SequenceStream`
will infer the compression type (gzip, bzip2, or plain text only) and
the file format (FASTA or FASTQ) from the file ending. First, the file
type is guessed: A file ending in ``.gz`` means "gzip-compressed", one
ending in ``.bz2`` means "bzip2-compressed". Then, the ``.gz`` or
``.bz2`` suffix is ignored when guessing the file format: A path ending
in ``.fa`` and ``.fasta`` mean FASTA, ``.fq`` and ``.fastq`` mean FASTQ.
Since the suffixes ``.gz`` and ``.bz2`` are ignored, ``.fa.gz``,
``.fa.bz2``, ... mean FASTA too and ``.fq.gz``, .\ ``fq.bz2``, ... mean
FASTQ.

File type detection from standard input is currently limited to either
gzip-compressed or plain-text data.

Note that you can also use additional parameters in the
:dox:`SequenceStream#SequenceStream SequenceStream constructor` to force
a certain file type and file format when writing. You can also force a
certain file type and format when reading but this is only helpful in
the few instances where the automatic detection fails.

This means that all the examples and your solutions to the assignments
from above **already have compression support built-in**, if the
compression libraries are available.

::

    #InfoBox
    '''Information:''' Dependencies on Compression Libraries

    For accessing compressed files, you need to have zlib installed for reading <tt>.gz</tt> files and libbz2 for reading <tt>.bz2</tt> files.

    If you are using Linux or Mac Os X and you followed the [[Tutorial/GettingStarted| Getting Started]] tutorial closely then you should have already installed the necessary libraries.
    On Windows, you will need to follow [[HowTo/InstallContribsWindows| How To: Install Contribs On Windows]] to get the necessary libraries.

    You can check whether you have installed the libraries to use zlib and libbz2 by running CMake again.
    Simply call <tt>cmake .</tt> in your build directory.
    At the end of the output, there will be a section "Seqan Features".
    If you can read <tt>ZLIB - FOUND</tt> and <tt>BZIP2 - FOUND</tt> then you can use zlib and libbz2 in your programs.

Congratulations, you have now learned to write simple and robust
sequence I/O code using SeqAn!

Next Steps
~~~~~~~~~~

-  Read the Wikipedia articles about the `FASTA file
   format <http://en.wikipedia.org/wiki/FASTA_format>`__ and the `FASTQ
   file format and quality
   values <http://en.wikipedia.org/wiki/FASTQ_format>`__ to refresh your
   knowledge.
-  Read the `Indexed FASTA I/O <Tutorial/IndexedFastaIO>`__ tutorial to
   learn how to read FASTA files efficiently in a random-access fashion.
-  Continue with the `remaining tutorials <Tutorial>`__.

Submit a Comment
~~~~~~~~~~~~~~~~

If you found a mistake, or have suggestions about an improvement of this
page press:
[/newticket?component=Documentation&description=Tutorial+Enhancement+for+page+http://trac.seqan.de/wiki/Tutorial/BasicSequenceIO&type=enhancement
submit your comment]

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
