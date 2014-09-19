Basics
------

TOC

Alphabets
~~~~~~~~~

In SeqAn, alphabets are value types that can take a limited number of
values and which hence can be mapped to a range of natural numbers. We
can retrieve the number of different values of an alphabet, the alphabet
size, by the metafunction seqan:Metafunction.ValueSize. Another useful
metafunction called seqan:Metafunction.BitsPerValue can be used to
determine the number of bits needed to store a value of a given
alphabet. The order of a character in the alphabet (i.e. its
corresponding natural number) can be retrieved by calling the function
seqan:Function.ordValue. In SeqAn, several standard alphabets are
already predefined, for example seqan:Spec.Dna, seqan:Spec.Dna5,
seqan:Spec.Rna, seqan:Spec.Rna5, seqan:Spec.Iupac, seqan:Spec.AminoAcid,
....

Let's start with a simple task. We want to write a program that outputs
all letters of the predefined seqan:Spec.AminoAcid alphabet. First we
include the corresponding header files and specify that we are using the
namespace ``seqan``.
.. includefrags:: core/demos/tutorial/basics/show_alphabets.cpp
   :fragment: includes

Next, we will define a template function
``template<typename TAlphabet> void showAllLettersOfMyAlphabet(TAlphabet const&)``
which will iterate over all the characters of the alphabet and outputs
them. For this, we need to determine the alphabet size using the
metafunction [seqan:Metafunction.ValueSize ValueSize::VALUE]. Then we
increment a counter from 0 to the alphabet size minus one and output the
counter as well as the corresponding letter of the alphabet using a
conversion constructor.
.. includefrags:: core/demos/tutorial/basics/show_alphabets.cpp
   :fragment: showAllLettersOfMyAlphabet

In the main program we simply call the above function using a number of
alphabets that are predefined in SeqAn.
.. includefrags:: core/demos/tutorial/basics/show_alphabets.cpp
   :fragment: main

This program produces the following output:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
     darwin10.0 : ./show_alphabets
    0,A  1,R  2,N  3,D  4,C  5,Q  6,E  7,G  8,H  9,I  10,L  11,K  12,M  13,F  14,P  15,S  16,T  17,W  18,Y  19,V  20,B  21,Z  22,X  23,*
    0,A  1,C  2,G  3,T
    0,A  1,C  2,G  3,T  4,N

Iterators
~~~~~~~~~

An iterator is an object that is used to browse through the values of a
container. The metafunction seqan:Metafunction.Iterator can be used to
determine an appropriate iterator type given a container. Some
containers offer several kinds of iterators, which can be selected by an
optional argument of Iterator. For example, the tag [seqan:"Tag.Iterator
Spec" Standard] can be used to get an iterator type that resembles the
C++ standard random access iterator. The more elaborated
seqan:"Concept.Rooted Iterator", i.e., an iterator that knows its
container, can be selected by specifying the [seqan:"Tag.Iterator Spec"
Rooted] tag.

Rooted iterators offer some convenience for the user: They offer
additional functions like seqan:Function.container for determining the
container on which the iterator works, and they simplify the interface
for other functions like seqan:Function.atEnd. Moreover, rooted
iterators may change the container’s length or capacity, which makes it
possible to implement a more intuitive variant of a remove algorithm.

While rooted iterators can usually be converted into standard iterators,
it is not always possible to convert standard iterators back into rooted
iterators, since standard iterators may lack the information about the
container they work on. Therefore, many functions that return iterators
like seqan:function.begin or seqan:function.end return rooted iterators
instead of standard iterators; this way, they can be used to set both
rooted and standard iterator variables. Alternatively it is possible to
specify the returned iterator type explicitly by passing the iterator
kind as a tag argument.

The following code piece shows examples for creating Iterators. If no
iterator kind is specified, the metafunction seqan:Metafunction.Iterator
assumes [seqan:"Tag.Iterator Spec" Standard] and the function
seqan:function.begin assumes [seqan:"Tag.Iterator Spec" Rooted]. Both
``it1`` and ``it2`` are standard iterators, whereas ``it3`` and ``it4``
are rooted iterators.

::

    #cpp
    String<char> str = "ACME";
    Iterator<String<char> >::Type it1 = begin(str); //a standard iterator
    Iterator<String<char>, Standard>::Type it2 = begin(str);  //same as above
    Iterator<String<char>, Rooted>::Type it3 = begin(str);  //a rooted iterator
    Iterator<String<char>, Rooted>::Type it4 = begin(str, Rooted());  //same as above

::

    #comment
    An iterator is stable if it stays valid even if its container is expanded, otherwise it is unstable. For example, the standard iterator of seqan:"Spec.Alloc String" – which is a simple pointer to a value in the string – is unstable, since during the expansion of an Alloc String, all values are moved to new memory addresses. A typical implementation of stable iterators for strings stores the position instead of a pointer to the current value. The seqan:Metafunction.Iterator  metafunction called with the [seqan:"Tag.Iterator Spec" Stable] tag returns a type for stable iterators.

    Stable tag does not appear in Doku. Clarify with Andreas.

Assignments
^^^^^^^^^^^

*``Task`` ``1``*\ `` :: Write a program which does the following:``

#.

   #. Create an amino acid string of the following sequence:
      "MQDRVKRPMNAFIVWSRDQRRKMALEN".

| ``     b. Iterate through the sequence and replace all ‘R’ with ‘A’.``
| ``     c. Create a second string where you count the number of occurrences of each amino acid.``
| ``     d. Iterate through the latter string and output the frequency table.``
| *``Difficulty``*\ `` :: 4 (after a few hours of browsing through the demos you should be able to solve this)``
| *``Solution``*\ `` :: can be found ``\ ```here`` <Tutorial/Basics/BasicsTask1>`__

Memory Allocation
~~~~~~~~~~~~~~~~~

Controlling memory allocation is one of the big advantages of C++
compared to other programming languages as for example Java. Depending
on the size of objects and the pattern they are allocated during the
program execution, certain memory allocation strategies have advantages
compared to others. SeqAn supports a variety of memory allocation
strategies.

The two functions seqan:Function.allocate and seqan:Function.deallocate
are used in SeqAn to allocate and deallocate dynamic memory. Both
functions take an allocator as an argument. An seqan:Class.Allocator is
an object that is responsible for allocated memory. The default
implementations of seqan:Function.allocate and seqan:Function.deallocate
completely ignore the allocator but simply call the basic operators
``new`` and ``delete``. Although in principle every kind of object can
be used as allocator, typically the object that stores the pointer to
the allocated memory is used as allocator. For example, if memory is
allocated for an [seqan:"Spec.Alloc String" Alloc String], this string
itself acts as allocator. A memory block should be deallocated using the
same allocator object as it was allocated for. The following allocators
are available in SeqAn and support the seqan:Function.clear function.
This function deallocates at once all memory blocks that were previously
allocated.

| ``seqan:"Spec.Simple Allocator"::``
| ``  General purpose allocator.``
| ``seqan:"Spec.Single Pool Allocator"::``
| ``  Allocator that pools memory blocks of specific size. Blocks of different sizes are not pooled.``
| ``seqan:"Spec.Multi Pool Allocator"::``
| ``  Allocator that pools memory blocks. Only blocks up to a certain size are pooled. The user can specify the size limit in a template argument.``
| ``seqan:"Spec.Chunk Pool Allocator"::``
| ``  Allocator that pools one or more consecutive memory blocks of a specific size.``

The function seqan:Function.allocate has an optional argument to specify
the intended allocator usage for the requested memory. The user can
thereby specialize seqan:Function.allocate for different allocator
applications. For example, the tag [seqan:"Tag.Allocator Usage"
TagAllocateTemp] specifies that the memory will only be used
temporarily, whereas [seqan:"Tag.Allocator Usage" TagAllocateStorage]
indicates that the memory will be used in the long run for storing
values of a container.

SeqAn also offers more complex allocators which support the function
seqan:Function.clear. The library predefines some allocator
specializations for different uses (see above). Most of these allocators
are pool allocators. A pool allocator implements its own memory
management. It reserves storage for multiple memory blocks at a time and
recycles deallocated blocks. This reduces the number of expensive
``new`` and ``delete`` calls and speeds up the allocation and
deallocation.

Assignments
^^^^^^^^^^^

| *``Task``
``2``*\ `` :: Write a program which compares the runtimes of the seqan:"Spec.Simple Allocator" and the seqan:"Spec.Multi Pool Allocator" for pool sizes (10,100,1000) for allocating and deallocating memory.``
| *``Difficulty``*\ `` :: 3 (given the hints)``
| *``Hint``*\ `` :: For timing the allocation you can use seqan:Function.sysTime.``
| *``Solution``*\ `` :: can be found ``\ ```here`` <Tutorial/Basics/BasicsTask2>`__

Submit a comment
^^^^^^^^^^^^^^^^

If you found a mistake, or have suggestions about an improvement of this
page press:
[/newticket?component=Documentation&description=Tutorial+Enhancement+for+page+http://trac.seqan.de/wiki/Tutorial/Basics&type=enhancement
submit your comment]

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
