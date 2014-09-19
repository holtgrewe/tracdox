Sequences
---------

TOC

Sequences are at the core of SeqAn. This tutorial gives an overview of
the available sequence types and introduces alphabets. We also briefly
present how to manipulate sequences. Finally, we introduce the class
seqan:Class.StringSet for storing multiple strings.

Sequence Types
~~~~~~~~~~~~~~

In SeqAn, there are three kinds of sequences: Strings, Sequence
Adaptions and Segments.

Overview Of Strings And Alphabets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Strings are objects of the class [seqan:Class.String String] (or rather,
its specializations). Strings are [seqan:Concept.Container containers]
that store a sequence of values. For example, a string can store a
sequence of ``char``, nucleotides, or amino acids.

You can independently choose from several types of strings and
alphabets. The choice of the string type is independent of the choice of
the alphabet/contained type.

With the string, you choose *how* the data is stored. With the alphabet,
you choose *what kind* of data is stored.

Let's first have a look at some different alphabets and strings of
strings.

::

    #cpp
    // Each, a string of characters, of nucleotides and of amino acids.
    String<char> myText;
    String<Dna> myGenome;
    String<AminoAcid> myProteine;

    // More exotic: A string of character strings!
    String<String<char> > myStringList;

SeqAn also provides the common C++ operators for strings. You can use
them like STL strings, for example:

::

    #cpp
    String<char> str = "this is ";
    str += "a test.";
    std::cout << str << std::endl;
    std::cout << length(str) << std::endl;

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    this is a test.
    15

.. raw:: html

   </pre>

The default function in SeqAn for appending values to containers is
seqan:Function.appendValue. The function for appending a container to
another container is seqan:Function.append.

::

    #cpp
    String<char> str1 = "this is ";
    String<char> str2 = "a test.";
    appendValue(str1, 'j');
    append(str1, "ust ");
    append(str1, str2);

    std::cout << str1 << std::endl;

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    this is just a test.

.. raw:: html

   </pre>

There are [seqan:Indexpage.Shortcut shortcuts] to commonly used string
parametrizations, e.g. seqan:Shortcut.DnaString.

Alphabets / Contained Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Any type that provides a default constructor, a copy constructor and an
assignment operator can be used as the alphabet / contained type of a
seqan:Class.String. This includes the C++
[http://www.parashift.com/c\ ++-faq-lite/intrinsic-types.html#faq-26.7
POD types], e.g. ``char``, ``int``, ``double`` etc., but you can use
[seqan:Class.String Strings], too, for example.

SeqAn also provides the following types that are useful in
bioinformatics. Each of them is a specialization of the class
seqan:Class.SimpleType.

+------------------------+-----------------------------------------------------------+
| **Specialization**     | **Description**                                           |
+========================+===========================================================+
| seqan:Spec.AminoAcid   | Amino Acid Alphabet                                       |
+------------------------+-----------------------------------------------------------+
| seqan:Spec.Dna         | DNA alphabet                                              |
+------------------------+-----------------------------------------------------------+
| seqan:Spec.Dna5        | DNA alphabet including *N* character                      |
+------------------------+-----------------------------------------------------------+
| seqan:Spec.DnaQ        | DNA alphabet plus phred quality                           |
+------------------------+-----------------------------------------------------------+
| seqan:Spec.Dna5Q       | DNA alphabet plus phred quality including "N" character   |
+------------------------+-----------------------------------------------------------+
| seqan:Spec.Finite      | Finite alphabet of fixed size.                            |
+------------------------+-----------------------------------------------------------+
| seqan:Spec.Iupac       | DNA Iupac code.                                           |
+------------------------+-----------------------------------------------------------+
| seqan:Spec.Rna         | RNA alphabet                                              |
+------------------------+-----------------------------------------------------------+
| seqan:Spec.Rna5        | RNA alphabet including *N* character                      |
+------------------------+-----------------------------------------------------------+

See each specialization's documentation for the ordering of the
alphabet's values.

seqan:Spec.Finite is provided for storage efficiency reasons.
seqan:"Spec.Packed String" (see below) will pack as many values of your
Finite characters into one machine word, thus saving memory at a
slightly higher computational cost.

Assignments
^^^^^^^^^^^

| *``Task`` ``1`` ``(Character`` ``Counting)``*\ `` ::``
| ``  Write a function ``\ ``countOneMers(str)``\ `` that accepts a seqan:Shortcut.CharString of lower case characters and then prints a list of pairs.``
| ``  Each of this pair gives a character and the number of occurences of this character in the string.``
| ``  A pair should only be printed if the occurence count is greater than 0.``
| ``  Call this function with the strings ``\ ``"helloworld"``\ ``, ``\ ``"banana"``\ `` and ``\ ``"mississippi"``\ ``.``
| *``Difficulty``*\ `` :: 2``
| *``Solution``*\ `` :: can be found ``\ ```here`` <Tutorial/Sequences/Assignment1CharacterCounting>`__\ ``.``

| *``Task`` ``1`` ``Bis`` ``(Generic`` ``Character``
``Counting)``*\ `` ::``
| ``  Rewrite the function ``\ ``countOneMers(str)``\ `` to accept a generic seqan:Shortcut.String.``
| ``  Call this function with the seqan:Shortcut.CharString ``\ ``"Hello world!"``\ ``, seqan:Shortcut.DnaString ``\ ``"TATACGCTA"``\ `` and seqan:Shortcut.Peptide ``\ ``"MQDRVKRPMNAFIVWSRDQRRKMALEN"``\ ``.``
| *``Difficulty``*\ `` :: 4``
| *``Solution``*\ `` :: can be found ``\ ```here`` <Tutorial/Sequences/Assignment1BisCharacterCounting>`__\ ``.``

| *``Task`` ``2`` ``(All`` ``Strings`` ``Of`` ``A`` ``Given``
``Length)``*\ `` ::``
| ``  Write a function ``\ ``printPermutations(len)``\ `` which, given a parameter ``\ ``len``\ ``, prints all strings consisting of ``\ ``len``\ `` lower case letters to ``\ ``std::cout``\ ``.``
| `` Call this function with the parameter 3 in your ``\ ``main(...)``\ `` function.``
| *``Difficulty``*\ `` :: 4 (getting the right idea is harder than the implementation)``
| *``Hints``*\ `` ::``

#. You will need to ``#include`` the headers ``<iostream>`` and
   ``<seqan/sequence.h>``.
#. Remember that in C++ ``'a' + 1 == 'b'``, ..., ``'y' + 1 == 'z'``.
#. In this case, a recursive solution is more elegant than an iterative
   one.
#. You can get the length of a string ``str`` with ``length(str)``.
#. It might be simpler to consider the binary alphabet {'a', 'b'}, where
   'a' represents 0 and 'b' represents '1'.

| ``   You could start out with building a "binary counter" of length ``\ ``len``\ `` over this alphabet and then replace the border 'b' by 'z'.``
| *``Solution``*\ `` :: can be found ``\ ```here`` <Tutorial/Sequences/Assignment2AllStringsOfAGivenLength>`__\ ``.``

String Types
^^^^^^^^^^^^

The user can specify the kind of string that should be used in an
optional second template argument of seqan:Class.String. String has the
following specializations.

In most cases, the implementation seqan:"Spec.Alloc String" (the default
when using a ``String<T>``) is the best choice. Exceptions are when you
want to process extremely large strings that are a bit larger than the
available memory (consider seqan:"Spec.Alloc String") or much larger so
most of them are stored on the hard disk and only parts of them are
loaded in main memory (consider seqan:"Spec.External String").

+--------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| **Specialization**             | **Description**                                                        | **Applications**                                                                                                                                   | **Limitations**                                                                                                       |
+================================+========================================================================+====================================================================================================================================================+=======================================================================================================================+
| seqan:"Spec.Alloc String"      | Expandable string that is stored on the heap.                          | The default string implementation that can be used for general purposes.                                                                           | Changing the seqan:Function.capacity can be very costly since all values must be copied.                              |
+--------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| seqan:"Spec.Array String"      | Fast but non-expandable string.                                        | Fast storing of fixed-size sequences.                                                                                                              | [seqan:Function.capacity Capacity] must already be known at compile time. Not suitable for storing large sequences.   |
+--------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| seqan:"Spec.Block String"      | String that stores its sequence characters in blocks                   | The [seqan:Function.capacity capacity] of the string can quickly be increased. Good choice for growing strings or stacks.                          | Iteration and random access to values is slightly slower than for [seqan:"Spec.Alloc String" Alloc Strings].          |
+--------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| seqan:"Spec.Packed String"     | A string that stores as many values in one machine word as possible.   | Suitable for storing large strings in memory.                                                                                                      | Slower than other in-memory strings.                                                                                  |
+--------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| seqan:"Spec.External String"   | String that is stored in secondary memory.                             | Suitable for storing very large strings (>2GB). Parts of the string are automatically loaded from secondary memory on demand.                      | Slower than other string classes.                                                                                     |
+--------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| seqan:"Spec.CStyle String"     | Allows adaption of strings to C-style strings.                         | Used for transforming other String classes into C-style strings (i.e. null terminated char arrays). Useful for calling functions of C-libraries.   | Only reasonable if value type is char or wchar\_t.                                                                    |
+--------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+

Examples:

::

    #cpp
    // String with maximum length 100.
    String<char, Array<100> > myArrayString;
    // String that takes only 2 bits per nucleotide.
    String<Dna, Packed<> > myPackedString;

Assignments: Thinking About Strings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following tasks do not have exactly one solution. Rather, they are
meant to be an incentive to think about how SeqAn strings are/should be
implemented.

| *``Task`` ``3``*\ `` ::``
| ``  Only consider the DNA alphabet {G, C, A, T}.``
| ``  How would you represent a string of these characters for a very space-efficient representation?``
| ``  How many characters can you pack in a byte of 8 bits and thus in a machine word of 32/64 bits?``
| *``Difficulty``*\ `` :: 2``

| *``Task`` ``4``*\ `` ::``
| ``  Given an alphabet of the ``\ ``int``\ `` values.``
| ``  How would you implement a string that supports access to the ``\ *``i``*\ ``-th character and efficient appending and ``\ *``popping``*\ `` of characters to/from its end?``
| ``  What is the asymptotic running time?``
| *``Difficulty``*\ `` :: 3 (1-5, depending on previous knowledge)``

| *``Task`` ``5``*\ `` ::``
| ``  How fast can you implement the following operations on C style strings?``

-

   -  Length
   -  Access of *i*-th character
   -  Appending data to it end
   -  Deleting data from its end

| ``  You might search Google for an explanation of C style strings and discussion of advantages and disadvantages of C style strings over "Pascal style" strings.``
| *``Difficulty``*\ `` :: 3``

Sequence Adaptions
^^^^^^^^^^^^^^^^^^

SeqAn offers an interface for accessing standard library strings and
c-style char arrays. Hence those built-in types can be handled in a
similar way as SeqAn strings, for example with the seqan:Function.length
function.

::

    #cpp
    std::string str1 = "a standard library string";
    std::cout << length(str1);

    char str2[] = "this is a char array";
    std::cout << length(str2);

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    25
    20

.. raw:: html

   </pre>

Note that the assignment operator cannot be easily overwritten.

Segments
^^^^^^^^

Segments are contiguous subsequences that represent parts of other
sequences. There are three kinds of segments in SeqAn:
[seqan:Spec.InfixSegment Infixes], [seqan:Spec.PrefixSegment prefixes],
and [seqan:Spec.SuffixSegment suffixes]. The metafunctions
seqan:Metafunction.Infix, seqan:Metafunction.Prefix, and
seqan:Metafunction.Suffix, respectively, return the appropriate segment
data type for a given sequence type.

For suffixes, the second parameter of the function denotes the starting
position of the suffix:

::

    #cpp
    String<AminoAcid> prot = "AAADDDEEE";
    Suffix<String<AminoAcid> >::Type suf = suffix(prot, 3);
    std::cout << suf;

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    DDDEEE

.. raw:: html

   </pre>

Segments store a pointer on the underlying sequence object, the *host*,
and an start and/or end position, depending on the type of segment.

The segment is *not* a copy of the sequence segment. That is, changing
the segment implies changing the host sequence.

::

    String<char> str = "start_middle_end";
    // We overwrite "middle"
    infix(str, 6, 12) = "overwrite";
    std::cout << str;

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    start_overwrite_end

.. raw:: html

   </pre>

If this effect is undesirable, one has to explicitly make a copy of the
string.

Working With Sequences
~~~~~~~~~~~~~~~~~~~~~~

This describes iterators on strings (including an extensive demo),
string comparison, string expansion and conversion.

Iterators
^^^^^^^^^

[seqan:Concept.Iterator Iterators] are objects that can be used to
iterate over containers such as strings or segments. For a given
container class, the metafunction seqan:Metafunction.Iterator returns
the appropriate iterator type. An iterator always points to one value of
the container. The function seqan:Function.value, which is equivalent to
the ``operator*``, can be used to access this value. Functions like
seqan:Function.goNext or seqan:Function.goPrevious, which are equivalent
to ``operator++`` and ``operator--`` respectively, can be used to move
the iterator to other values within the container.

The functions seqan:Function.begin and seqan:Function.end, applied to a
container, return iterators to the begin and to the end of the
container. Note that similar to C++ standard library iterators, the
iterator returned by seqan:Function.end does not point to the last value
of the container but to the value behind the last one. If the container
``s`` is empty then ``end(s) == begin(s)``.

The following code prints out a sequence and demonstrates how to iterate
over a string.

::

    #cpp
    String<char> str = "acgt";
    typedef Iterator<String<char> >::Type TIterator;
    for (TIterator it = begin(str); it != end(str); ++it)
    {
        std::cout << value(it);
    }

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    acgt

.. raw:: html

   </pre>

Iterator Demo
^^^^^^^^^^^^^

The program
[source:trunk/core/demos/tutorial/sequence/sequence\_iterator\_demo.cpp
sequence\_iterator\_demo.cpp] demonstrates the usage of iterators:

.. includefrags:: core/demos/tutorial/sequence/sequence_iterator_demo.cpp
   :fragment: includes

The metafunction seqan:Metafunction.Iterator returns the iterator type
for a given container type.

.. includefrags:: core/demos/tutorial/sequence/sequence_iterator_demo.cpp
   :fragment: metafunctions

We can use iterators to iterate over the elements of a container.

.. includefrags:: core/demos/tutorial/sequence/sequence_iterator_demo.cpp
   :fragment: iterators

[seqan:"Concept.Rooted Iterator" Rooted iterators] know their container
(also see the `Basics Tutorial on
iterators <Tutorial/Basics#Iterators>`__). Hence, the functions
seqan:Function.goBegin and seqan:Function.atEnd do not get ``str`` as an
argument. The following loop increments each character in ``str``:

.. includefrags:: core/demos/tutorial/sequence/sequence_iterator_demo.cpp
   :fragment: rooted-iterators

Some iterators support an iteration in reverse order with
seqan:Function.goPrevious. Note that seqan:Function.goPrevious is called
before the value of ``it2`` is accessed. Remember that the end position
of a container is always the position behind the last item in the
container.

.. includefrags:: core/demos/tutorial/sequence/sequence_iterator_demo.cpp
   :fragment: iterator-reverse

seqan:Function.assignValue can be used to change the value of an
iterator.

.. includefrags:: core/demos/tutorial/sequence/sequence_iterator_demo.cpp
   :fragment: assign-value

The output of the program is:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    admn
    oneb
    Xeno

.. raw:: html

   </pre>

Assignments
^^^^^^^^^^^

| *``Task`` ``6`` ``(Using`` ``Iterators)``*\ `` ::``
| ``  Write a function ``\ ``replaceAs``\ `` that accepts a seqan:Shortcut.CharString and replaces all occurences of ``\ ``'a'``\ `` by an ``\ ``'X'``\ ``.``
| ``  Run it on the strings ``\ ``"abcdefghijklmnopqrstuvxyz"``\ ``, ``\ ``"Hello SeqAn!"``\ `` and ``\ ``"Hello Seqan!"``\ ``.``
| *``Difficulty``*\ `` :: 1``
| *``Solution``*\ `` :: can be found ``\ ```here`` <Tutorial/Sequences/Assignment6UsingIterators>`__\ ``.``

Comparisons
^^^^^^^^^^^

Two sequences can be lexicographically compared using standard operators
such as < or >=.

::

    #cpp
    String<char> a = "beta";
    String<char> b = "alpha";

    std::cout << (a != b) << std::endl;
    std::cout << (a < b) << std::endl;
    std::cout << (a > b) << std::endl;

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    1
    0
    1

.. raw:: html

   </pre>

Each comparison involves a scan of the two sequences for searching the
first mismatch between the strings. This could be costly if the two
sequences share a long common prefix. Suppose we want to branch in a
program depending on whether a < b, a == b, or a > b.

::

    #cpp
    if (a < b)      { /* code for case "a < b"  */ }
    else if (a > b) { /* code for case "a > b"  */ }
    else            { /* code for case "a == b" */ }

In this case, although only one scan would be enough to decide what case
is to be applied, each operator > and < performs a new comparison. SeqAn
offers the class seqan:Class.Lexical to avoid unnecessary sequence
scans. Lexicals can store the result of a comparison, for example:

::

    #cpp
    // Compare a and b and store the result in comp
    Lexical<> comp(a, b);

    if (isLess(comp))         { /* code for case "a < b"  */ }
    else if (isGreater(comp)) { /* code for case "a > b"  */ }
    else                      { /* code for case "a == b" */ }

Expansion
^^^^^^^^^

Each sequence object has a capacity, i.e. the maximum length of a
sequence that can be stored in this object. While some sequence types
like seqan:"Spec.Array String" or char arrays have a fixed capacity, the
capacity of other sequence classes like seqan:"Spec.Alloc String" or
std::basic\_string can be changed at runtime. The capacity can be set
explicitly by functions such as seqan:Function.reserve or
seqan:Function.resize. It can also bet set implicitly by functions like
seqan:Function.append or seqan:Function.replace if the operation's
result exceeds the length of the target string.

There are several overflow strategies that determine what actually
happens when a string should be expanded beyond its capacity. If no
overflow strategy is specified for a function call, a default overflow
strategy is selected depending on the type of the sequence.

::

    #cpp
    String<char> str;
    // Sets the capacity of str to 5.
    resize(str, 5, Exact());
    // Only "abcde" is assigned to str, since str is limited to 5.
    assign(str, "abcdefghijklmn", Limit());
    std::cout << str << std::endl;
    // Use the default expansion strategy.
    append(str, "ABCDEFG");
    std::cout << str;

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    abcde
    abcdeABCDEFG

.. raw:: html

   </pre>

The following overflow strategies exist:

+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Tag**                                    | **Description**                                                                                                                                                                                                                   |
+============================================+===================================================================================================================================================================================================================================+
| [seqan:"Tag.Overflow Strategy" Exact]      | Expand the sequence exactly as far as needed. The capacity is only changed if the current capacity is not large enough.                                                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [seqan:"Tag.Overflow Strategy" Generous]   | Whenever the capacity is exceeded, the new capacity is chosen somewhat larger than currently needed. This way, the number of capacity changes islimited in a way that resizing the sequence only takes amortized constant time.   |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [seqan:"Tag.Overflow Strategy" Limit]      | Instead of changing the capacity, the contents are limited to current capacity. All values that exceed the capacity are lost.                                                                                                     |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [seqan:"Tag.Overflow Strategy" Insist]     | No capacity check is performed, so the user has to ensure that the container's capacity is large enough.                                                                                                                          |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Conversion
^^^^^^^^^^

A sequence of type A values can be converted into a sequence of type B
values, if A can be converted into B. SeqAn offers three different
conversion alternatives.

**Copy conversion.** The source sequence is copied into the target
sequence. This can be done by assignment (``operator=``) or using the
function seqan:Function.assign.

::

    #cpp
    String<Dna> source = "acgtgcat";
    String<char> target;
    assign(target, source);
    std::cout << target;

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    acgtgcat

.. raw:: html

   </pre>

**Move conversion.** If the source sequence is not needed any more after
the conversion, it is always advisable to use seqan:Function.move
instead of seqan:Function.assign. The function seqan:Function.move does
not make a copy but can reuse the source sequence storage. In some
cases, seqan:Function.move can also perform an in-place conversion.

::

    #cpp
    String<char> source = "acgtgcat";
    String<Dna> target;
    //The in-place move conversion.
    move(target, source);
    std::cout << target;

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    acgtgcat

.. raw:: html

   </pre>

**Modifier conversion.** Instead of creating an actual target sequence,
use a `modifier <Tutorial/Modifiers>`__ to 'emulate' a sequence with a
different value type. The modifier target in the following example
behaves exactly like a char sequence:

::

    #cpp
    String<char> source = "acgtXgcat";
    typedef ModifiedString<String<char>, ModView<FunctorConvert<char, Dna5> > > TCharToDna5Modifier;
    //Create a sequence of dna5 characters that contains "acgtngcat".
    TCharToDna5Modifier target(source);
    std::cout << target;
    //Define a variable of type Dna5.
    Value<TCharToDna5Modifier>::Type c;

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    acgtngcat

.. raw:: html

   </pre>

Others
^^^^^^

SeqAn offers several ways for loading and saving sequences in different
formats. For more information, see seqan:"Demo.File Format I/O".

String Sets
~~~~~~~~~~~

A set of sequences can either be stored in a sequence of sequences, for
example in a ``String< String<char> >``, or in seqan:Class.StringSet.

There are two kinds of seqan:Class.StringSet specializations in SeqAn:
seqan:Spec.Owner and seqan:Spec.Dependent; see the table below.
seqan:Spec.Owner string sets actually store the sequences, whereas
seqan:Spec.Dependent string set just refer to sequences that are stored
outside of the string set.

One advantage of using seqan:Class.StringSet is that it supports the
function seqan:Function.concat that returns a *concatenator* of all
sequences in the string set. A *concatenator* is an object that
represents the concatenation of a set of strings. This way it is
possible to build up index data structures for multiple sequences by
using the same construction methods as for single sequences. The
specialization [seqan:Spec.ConcatDirect Owner] already stores the
sequences in a concatenation. The concatenators for all other
specializations of seqan:Class.StringSet are **virtual** sequences, that
means their interface **simulates** a concatenation of the sequences,
but they do not literally concatenate the sequences into a single
sequence. Hence in any case the sequences need not to be copied when a
concatenator is created.

One string can be an element of several seqan:Spec.Dependent string
sets. Typical tasks are therefore to find a specific string in a string
set, or to test whether the strings in two string sets are the same.
Therefore a mechanism to identify the strings in the string set is
needed, and, for performance reasons, this identification should not
involve string comparisons. SeqAn solves this problem by introducing
*ids*, which are by default ``unsigned int`` values. There are two ways
for accessing the sequences in a string set: (1) the function
seqan:Function.value returns a reference to the sequence at a specific
*position* within the sequence of sequences, and (2)
seqan:Function.valueById accesses a sequence given its *id*. In the case
of seqan:Spec.Owner string sets, id and position of a string are always
the same, but for seqan:Spec.Dependent string sets, the ids can differ
from the positions. For example, if a seqan:Spec.Dependent string set is
used to represent subsets of strings that are stored in seqan:Spec.Owner
string sets, one can use the position of the string within the
seqan:Spec.Owner string set as id of the strings.

+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Specialization**        | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+===========================+================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| ``Owner``                 | The default specialization of seqan:Class.StringSet. The sequences in this string set are stored in a string of string data structure. seqan:Function.concat returns a special *concatenator* object that simulates the concatenation of all these strings.                                                                                                                                                                                                                                                                                                                                                                                                                    |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``Owner<ConcatDirect>``   | The sequences are stored as parts of a long string. Since the sequences are already concatenated, seqan:Function.concat just needs to return this string. The string set also stores lengths and starting positions of the strings. Inserting new strings into the set or removing strings from the set is more expensive than for the default seqan:Spec.Owner specialization, since this involves moving all subsequent sequences in memory.                                                                                                                                                                                                                                 |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``Dependent<Tight>``      | This specialization stores sequence pointers consecutively in an array. Another array stores an id value for each sequence. That means that accessing given an id needs a search through the id array.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``Dependent<Generous>``   | The sequence pointers are stored in an array at the position of their ids. If a specific id is not present, the array stores a zero at this position. The advantage of this specialization is that accessing the sequence given its id is very fast. On the other hand, accessing a sequence given its position ``i`` can be expensive, since this means we have to find the *i*-th non-zero value in the array of sequence pointers. The space requirements of a string set object depends on the largest id rather than the number of sequences stored in the set. This could be inefficient for string sets that store a small subset out of a large number of sequences.   |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Building String Sets
^^^^^^^^^^^^^^^^^^^^

Use the function seqan:Function.appendValue to append strings to string
sets:

::

    #cpp
    StringSet<CharString> stringSet;
    CharString str1 = "foo";
    CharString str2 = "bar";

    appendValue(stringSet, str1);
    appendValue(stringSet, str2);

Also see [HowTo/EfficientlyImportMillionsOfSequences HowTo: Efficiently
import millions of sequences] for remarks on seqan:Spec.ConcatDirect
StringSets.

Iterating Over String Sets
^^^^^^^^^^^^^^^^^^^^^^^^^^

Of course, StringSets also have iterators:

::

    #cpp
    typedef Iterator<StringSet<CharString> > TStringSetIterator;
    for (TStringSetIterator it = begin(stringSet); it != end(stringSet); ++it) {
      std::cout << value(it) << std::endl;
    }

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    foo
    bar

.. raw:: html

   </pre>

Submit a comment
^^^^^^^^^^^^^^^^

If you found a mistake, or have suggestions about an improvement of this
page press:
[/newticket?component=Documentation&description=Tutorial+Enhancement+for+page+http://trac.seqan.de/wiki/Tutorial/Sequences&type=enhancement
submit your comment]

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
