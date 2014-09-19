File I/O
--------

TOC

::

    #WarningBox
    '''Caution''':
    The old I/O system will be replaced by the new I/O system.
    Consider using the new I/O system for sequence files as described [[Tutorial/BasicSequenceIO| here]].

Raw Data
~~~~~~~~

SeqAn supports the input and output of files in different
[seqan:"Tag.File Format" file formats]. The most simple file format is
``Raw`` that is used to load a file "as is" into a string or vice versa.

::

    #cpp
    // Loading.
    ::std::fstream fstrm;
    fstrm.open("input.txt", ::std::ios_base::in | ::std::ios_base::binary);

    String<char> str;
    read(fstrm, str, Raw());
    ::std::cout << str << ::std::endl;
    fstrm.close();

In this example, the tag ``Raw()`` can also be omitted, since ``Raw`` is
the default file format. Instead of using seqan:Function.read and
seqan:Function.write to read and write raw data, one can also use the
operators ``<<`` and ``>>``.

Files can either be instances of a [seqan:Adaption.std::iostream
standard stream class], or a C-style stream (i.e. ``FILE *``) or a
[seqan:Class.File SeqAn ``File`` object] (see below). Note that the
files should always be opened in binary mode.

File Formats for Bioinformatics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Apart from ``Raw``, SeqAn offers [seqan:"Tag.File Format" other file
formats] relevant in bioinformatics such as ``Fasta``, ``Embl``, or
``Genbank``. These file formats consist of one or more data records.
Multiple records in a file can be loaded by iteratively calling the
function seqan:Function.read.

::

    #cpp
    ::std::fstream fstrm;
    fstrm.open("est.fasta", ::std::ios_base::in | ::std::ios_base::binary);
    String<Dna> est;
    while (! fstrm.eof()) {
     read(fstrm, est, Fasta());
     ::std::cout << est << ::std::endl;
    }

The function seqan:Function.goNext skips the current record and proceeds
to the next record.

Each record contains a piece of data (i.e. a sequence or an alignment)
and optional some additional metadata. One can load these metadata
before loading the actual data using seqan:Function.readMeta. The
function fills a string with the unparsed metadata.

::

    #cpp
    ::std::fstream fstrm;
    fstrm.open("est.fasta", ::std::ios_base::in | ::std::ios_base::binary);
    String<Dna> est;
    String<char> meta;
    while (! fstrm.eof())
    {
     readMeta(fstrm, meta, Fasta());
     ::std::cout << meta << ::std::endl;
     read(fstrm, est, Fasta());
     ::std::cout << est << ::std::endl;
    }

seqan:Function.write is used to write a record into a file. Depending on
the file format, a suitable metadata string must be passed to
seqan:Function.write.

::

    #cpp
    FILE * cstrm = fopen("genomic_data.fa", "w");
    write(cstrm, "acgt", "the metadata", Fasta());
    fclose(cstrm);

This code creates the following file "genomic\_data.fa".

::

    >the metadata
    ACGT

File Reader Strings
~~~~~~~~~~~~~~~~~~~

The easiest way for a read-only access of sequence data stored in a file
is a [seqan:"Spec.File Reader String" file reader string]. A file reader
string implements the [seqan:Concept.Container container concept], i.e.
it implements common functions like seqan:Function.length or
seqan:Function.begin. It has minimal memory consumption, because each
part of the sequence data is not loaded before it is needed.

::

    #cpp
    String<Dna, FileReader<Fasta> > fr("ests.fa");
    //Print the length of the first sequence.
    ::std::cout << length(fr);

The constructor of the file reader string can also take a file from
which the sequences will be loaded. For example, the following code will
read the second sequence in the file:

::

    #cpp
    FILE * cstrm = fopen("est.fasta", "r");
    goNext(cstrm, Fasta());
    //Read the meta data of the second record.
    String<char> meta_data;
    readMeta(cstrm, meta_data, Fasta());
    ::std::cout << meta_data << ::std::endl;
    //Read the sequence data of the second record.
    String<Dna, FileReader<Fasta> > fr(cstrm);
    ::std::cout << fr << ::std::endl;
    fclose(cstrm);

Submit a comment
^^^^^^^^^^^^^^^^

If you found a mistake, or have suggestions about an improvement of this
page press:
[/newticket?component=Documentation&description=Tutorial+Enhancement+for+page+http://trac.seqan.de/wiki/Tutorial/FileIO&type=enhancement
submit your comment]

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
