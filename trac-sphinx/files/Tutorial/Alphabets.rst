= Alphabets TOC()

| ``Learning Objective :: You will learn the details about the alphabets in SeqAn.``
| ``Difficulty :: Basic``
| ``Duration :: 15 min``
| ``Prerequisites :: ``\ ```Tutorial/FirstStepsInSeqAn`` <Tutorial/FirstStepsInSeqAn>`__

This tutorial will describe the different alphabets used in SeqAn, or in
other words, you will learn about the contained types of a SeqAn
:dox:`String`. To continue with the other tutorials, it would be
enough to know, that in SeqAn several standard alphabets are already
predefined, e.g. :dox:`Dna`, :dox:`Dna5`, :dox:`Rna`,
:dox:`Rna5`, :dox:`Iupac`, :dox:`AminoAcid`.

== Types

Any type that provides a default constructor, a copy constructor and an
assignment operator can be used as the alphabet / contained type of a
:dox:`String` (see also Tutorial/Sequences). This includes the C++
[http://www.parashift.com/c\ ++-faq-lite/intrinsic-types.html#faq-26.7
POD types], e.g. ``char``, ``int``, ``double`` etc.. In addition you can
use more complex types like :dox:`String Strings` as the contained type
of strings, e.g. *String >*.

SeqAn also provides the following types that are useful in
bioinformatics. Each of them is a specialization of the class
:dox:`SimpleType`.

+-----------------------------+-----------------------------------------------------------+
| **Specialization**          | **Description**                                           |
+=============================+===========================================================+
| :dox:`AminoAcid`   | Amino Acid Alphabet                                       |
+-----------------------------+-----------------------------------------------------------+
| :dox:`Dna`               | DNA alphabet                                              |
+-----------------------------+-----------------------------------------------------------+
| :dox:`Dna5`             | DNA alphabet including *N* character                      |
+-----------------------------+-----------------------------------------------------------+
| :dox:`DnaQ`             | DNA alphabet plus phred quality                           |
+-----------------------------+-----------------------------------------------------------+
| :dox:`Dna5Q`           | DNA alphabet plus phred quality including "N" character   |
+-----------------------------+-----------------------------------------------------------+
| :dox:`Finite`         | Finite alphabet of fixed size.                            |
+-----------------------------+-----------------------------------------------------------+
| :dox:`Iupac`           | DNA Iupac code.                                           |
+-----------------------------+-----------------------------------------------------------+
| :dox:`Rna`               | RNA alphabet                                              |
+-----------------------------+-----------------------------------------------------------+
| :dox:`Rna5`             | RNA alphabet including *N* character                      |
+-----------------------------+-----------------------------------------------------------+

::

    #comment
    Finite Info is not correlated to Packed.String
    <pre>#InfoBox
    :dox:`Finite` is provided for storage efficiency reasons.
    :dox:`PackedString Packed String` will pack as many values of your Finite characters into one machine word, thus saving memory at a slightly higher computational cost.

.. raw:: html

   </pre>

== Functionality

In SeqAn, alphabets are value types that can take a limited number of
values and which hence can be mapped to a range of natural numbers. We
can retrieve the number of different values of an alphabet, the alphabet
size, by the metafunction [dox:FiniteOrderedAlphabetConcept#ValueSize
ValueSize].

::

    #cpp
    typedef Dna TAlphabet;

    unsigned alphSize = ValueSize<TAlphabet>::VALUE;
    std::cout << "Alphabet size of Dna: " << alphSize << std::endl;

::

    #ShellBox
    Alphabet size of Dna: 4

Another useful metafunction called [dox:AlphabetConcept#BitsPerValue
BitsPerValue] can be used to determine the number of bits needed to
store a value of a given alphabet.

::

    #cpp
    unsigned bits = BitsPerValue<TAlphabet>::VALUE;
    std::cout << "Number of bits needed to store a value of type Dna: " << bits << std::endl;

::

    #ShellBox
    Number of bits needed to store a value of type Dna: 2

The order of a character in the alphabet (i.e. its corresponding natural
number) can be retrieved by calling the function
:dox:`FiniteOrderedAlphabetConcept#ordValue ordValue`. See each
specialization's documentation for the ordering of the alphabet's
values.

::

    #cpp
    Dna a = 'A';
    Dna c = 'C';
    Dna g = 'G';
    Dna t = 'T';

    std::cout <<"A: " << (unsigned)ordValue(a) << std::endl;
    std::cout <<"C: " << (unsigned)ordValue(c) << std::endl;
    std::cout <<"G: " << (unsigned)ordValue(g) << std::endl;
    std::cout <<"T: " << (unsigned)ordValue(t) << std::endl;

::

    #ShellBox
    A: 0
    C: 1
    G: 2
    T: 3

::

    #InfoBox
    '''Information:''' The return value of the :dox:`FiniteOrderedAlphabetConcept#ordValue ordValue` function is determined by the metafunction :dox:`FiniteOrderedAlphabetConcept#ValueSize ValueSize`.
    :dox:`FiniteOrderedAlphabetConcept#ValueSize ValueSize` returns the type which uses the least amount of memory while being able to represent all possible values. E.g. :dox:`FiniteOrderedAlphabetConcept#ValueSize ValueSize` of :dox:`Dna` returns an <tt>__uint8</tt> which is able to represent 256 different characters. However, note that <tt>std::cout</tt> has no visible symbol for printing all values on the screen, hence a cast to <tt>unsigned</tt> might be necessary.

::

    #AssignmentBox
    ==== Assignment 1 ====
     Type ::
      Application
     Objective ::
      In this task you will learn how to access all the letters of an alphabet.
      Use the piece of code from below and adjust the function <tt>showAllLettersOfMyAlphabet()</tt> to go through all the characters of the current alphabet and print them.
    <pre>#cpp
    #include <seqan/sequence.h>
    #include <seqan/basic.h>
    #include <iostream>

    using namespace seqan;

    // We want to define a function, which takes
    // the alphabet type as an argument
    template <typename TAlphabet>
    void showAllLettersOfMyAlphabet(TAlphabet const &)
    {
        // ...
    }

    int main()
    {
        showAllLettersOfMyAlphabet(AminoAcid());
        showAllLettersOfMyAlphabet(Dna());
        showAllLettersOfMyAlphabet(Dna5());
        return 0;
    }

| ``Hints ::``
| `` You will need the Metafunction :dox:`FiniteOrderedAlphabetConcept#ValueSize ValueSize`. ``
| ``Solution :: ``
| `` Click ``\ *``more...``*\ `` to see the solution. ``

::

    #FoldOut
    ----
    [[Include(source:trunk/core/demos/tutorial/alphabets/alphabet_assignment_1_solution.cpp)]]

.. raw:: html

   </pre>

Submit a comment
~~~~~~~~~~~~~~~~

If you found a mistake, or have suggestions about an improvement of this
page press:
[/newticket?component=Documentation&description=Tutorial+Enhancement+for+page+http://trac.seqan.de/wiki/Tutorial/Sequences&type=enhancement
submit your comment]

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
