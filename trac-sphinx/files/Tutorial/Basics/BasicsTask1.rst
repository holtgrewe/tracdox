Task 1: Alphabets, Iterators, and Metafunctions
-----------------------------------------------

Task
~~~~

Write a program which does the following:

#.

   #. Create an amino acid string of the following sequence:
      "MQDRVKRPMNAFIVWSRDQRRKMALEN".
   #. Iterate through the sequence and replace all ‘R’ with ‘A’.
   #. Create a second string where you count the number of occurrences
      of each amino acid.
   #. Iterate through the latter string and output the frequency table.

Solution
~~~~~~~~

In this assignment we practice the use of alphabets, iterators and
metafunctions in SeqAn. We start by including the seqan basic header and
enter the namespace ``seqan`` to avoid writing it as a prefix (as we do
with the namespace ``std`` in this example). In the ``main`` function we
first define a a type ``TAmincoAcidString`` which is a
``String<AminoAcid>`` (Note the SeqAn naming conventions). Then we
define a variable ``sourceSeq`` of this type and initialize it with a
string constant.

::

    #comment
    Add link to naming conventions

.. includefrags:: core/demos/tutorial/basics/strings.cpp
   :fragment: create-string

Then we define an iterator type using the Seqan metafunction
seqan:Metafunction.Iterator. Using the correct iterator we iterate over
our amino acid string using the Seqan functions seqan:Function.begin,
seqan:Function.end, and seqan:Function.goNext. In the body of the while
loop we use the SeqAn function seqan:Function.value to access the value
the iterator is pointing to. Note that this function returns a reference
which allows us to replace the occurrence of all ``R``'s with ``A``'s.
So at this point we have solved parts a) and b) of the assignment.
.. includefrags:: core/demos/tutorial/basics/strings.cpp
   :fragment: iterate-and-replace

In the next part of the code we want to count, how often a specific
letter of the alphabet occurs in the string. To obtain the size type of
the used alphabet we call the SeqAn metafunction seqan:Metafunction.Size
and define a seqan:Class.String of that type to hold the counters. The
seqan:Class.String has here basically the same functionality as a STL
``vector``. Since alphabets are mapped to a contiguous interval of the
natural numbers, we can initialize the counter up to the size of the
alphabet which we obtain by a call to the SeqAn metafunction
seqan:Metafunction.ValueSize. We then iterate over the amino acid string
and increment the counter for the corresponding letter of the alphabet.
In order to know the corresponding natural number of an alphabet letter,
we use the SeqAn function seqan:function.ordValue. Note the use of the
seqan:Function.value function. In this example one could also use the
``operator[]`` to write ``counter[ordValue(value(it))]++``.
.. includefrags:: core/demos/tutorial/basics/strings.cpp
   :fragment: count-occurrences

Finally we iterate through the counter String and output the i-th amino
acid (by calling a constructor with the letter's ordinal value) ad its
frequency. .. includefrags:: core/demos/tutorial/basics/strings.cpp
   :fragment: frequency-table

The result looks like this:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
     darwin10.0 : basics//strings
    M,Q,D,A,V,K,A,P,M,N,A,F,I,V,W,S,A,D,Q,A,A,K,M,A,L,E,N,
    A:7
    R:0
    N:2
    D:2
    C:0
    Q:2
    E:1
    G:0
    H:0
    I:1
    L:1
    K:2
    M:3
    F:1
    P:1
    S:1
    T:0
    W:1
    Y:0
    V:2
    B:0
    Z:0
    X:0
    *:0

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
