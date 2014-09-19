Tutorial Indices
~~~~~~~~~~~~~~~~

TOC

| ``Learning Objective ::``
| `` You will get an overview of the different kinds of indices in SeqAn and how they are used.``
| ``Difficulty ::``
| `` Average``
| ``Duration ::``
| `` 1h``
| ``Prerequisites ::``
| `` ``\ ```Tutorial/Sequences`` <Tutorial/Sequences>`__

Indices in SeqAn
^^^^^^^^^^^^^^^^

Indices in SeqAn are substring indices, meaning that they allow
efficient pattern queries in strings or sets of strings. In contrast to
e.g. online-search algorithms that search through the text in O(n),
substring indices find a pattern in sublinear time o(n).

You can find the following indices in SeqAn:

+---------------------------------------------------------+-------------------------------------------------------------------------------------+
| **Specialization**                                      | **Description**                                                                     |
+=========================================================+=====================================================================================+
| :dox:`IndexEsa IndexEsa | Abouelhoda et al., 2004`])                                                          |
+---------------------------------------------------------+-------------------------------------------------------------------------------------+
| :dox:`IndexWotd`                               | Giegerich et al., 2003]])                                                           |
+---------------------------------------------------------+-------------------------------------------------------------------------------------+
| :dox:`IndexDfi`                                 | Weese, Schulz, 2008]])                                                              |
+---------------------------------------------------------+-------------------------------------------------------------------------------------+
| :dox:`IndexQGram`                             | q-gram index                                                                        |
+---------------------------------------------------------+-------------------------------------------------------------------------------------+
| :dox:`PizzaChiliIndex Pizza & Chili Index` PizzaChili]   | An adapter for the `Pizza & Chili <http://pizzachili.dcc.uchile.cl/>`__ index API   |
+---------------------------------------------------------+-------------------------------------------------------------------------------------+
| :dox:`FMIndex`                                   | Ferragina., Manzini 2001]])                                                         |
+---------------------------------------------------------+-------------------------------------------------------------------------------------+

Index Construction
^^^^^^^^^^^^^^^^^^

We will now show how we can create the different indices in SeqAn before
we show how they are used for pattern search.

All the mentioned indices belong to the generic :dox:`Index` class.
A SeqAn index needs two pieces of information: the type of the
:dox:`String` or :dox:`StringSet` to be indexed and the
index specialization, such as :dox:`IndexEsa` or [dox:FMIndex
FMIndex].

Example: The following code snippet creates an enhanced suffix array
index of a string of type Dox:Dna5 Dna5].

::

    #c++
    String<Dna5> genome = "ACGTACGTACGTN";
    Index<String<Dna5>, IndexEsa<> > esaIndex(genome);

In contrast, the next code snipped creates a FM index over a set of
amino acid sequences:

::

    #c++
    StringSet<String<AminoAcid> > protein;
    appendValue(protein,  "VXLAGZ");
    appendValue(protein,  "GKTVXL");
    appendValue(protein,  "XLZ");

    Index<StringSet<String<AminoAcid> >, FMIndex> fmIndex(protein);

Assignment 1
^^^^^^^^^^^^

::

    #AssignmentBox

     Type :: Review
     Objective :: Copy the code below and
    ##change it to build an :dox:`IndexEsa` over a string of type :dox:`Dna`,
    ##add an :dox:`IndexEsa` over a :dox:`StringSet` of :dox:`String Strings` of type :dox:`Dna`.

    <pre>
    #c++
    #include <seqan/sequence.h>
    #include <seqan/index.h>

    using namespace seqan;

    int main()
    {
        String<char> text = "This is the first example";
        Index<String<char>, FMIndex<> > index(text);

        return 0;
    }

``Solution ::``

::

    #FoldOut
    ----
    [[Include(source:trunk/core/demos/tutorial/index/indices_assignment_1.cpp)]]

.. raw:: html

   </pre>

Index Based Pattern Search (Strings)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SeqAn provides two methods for searching for a pattern in index
structures. One method uses iterators and is similar to traversing
search trees or tries. The tutorial `Index
Iterators <Tutorial/IndicesDraft>`__ explains this method in more
detail. In this section you will learn how to find a pattern with the
:dox:`Finder` interface.

The :dox:`Finder` is an object that stores all necessary
information for searching for a pattern using an index. The following
line of code shows how the :dox:`Finder` is initialized:

::

    #c++
    String<Dna5> genome = "ACGTACGTACGTN";
    Index<String<Dna5>, IndexEsa<> > esaIndex(genome);
    Finder<Index<String<Dna5>, IndexEsa<> > > esaFinder(esaIndex);

After initialization it is possible to use the :dox:`Finder#find find`
function in order to trigger a search for all occurrences of a given
pattern in the underlying :dox:`String` or [dox:StringSet
StringSet]. In this example, we search for the pattern ``ACGT``:

::

    #c++
    String<Dna5> genome = "ACGTACGTACGTN";
    Index<String<Dna5>, IndexEsa<> > esaIndex(genome);
    Finder<Index<String<Dna5>, IndexEsa<> > > esaFinder(esaIndex);

    find(esaFinder, "ACGT");

Calling the function :dox:`Finder#find find` invokes the localization of
all occurrences of a given pattern. It works by modifying pointers of
the ``Finder`` to tables of the index. For example, the [dox:Finder
Finder] of ``esaIndex`` stores two pointers, pointing to the first and
last suffix array entry that stores an occurrence of the pattern.

The return value of the :dox:`Finder#find find` function tells us whether
or not a given pattern occurs in the text. Furthermore, if there are
several instances of a pattern, consecutive calls of [dox:Finder#find
find] will modify the :dox:`Finder` such that it points to the
next occurrence after each call:

::

    #c++
    #include <seqan/sequence.h>
    #include <seqan/index.h>

    using namespace seqan;

    int main()
    {
        String<Dna5> genome = "ACGTACGTACGTN";
        Index<String<Dna5>, IndexEsa<> > esaIndex(genome);
        Finder<Index<String<Dna5>, IndexEsa<> > > esaFinder(esaIndex);

        find(esaFinder, "ACGT"); // first occurrence of "ACGT"
        find(esaFinder, "ACGT"); // second occurrence of "ACGT"
        find(esaFinder, "ACGT"); // third occurrence of "ACGT"
    }

The above code is not very useful, since we do not know the locations of
the first, second or third pattern occurrence. The function
:dox:`Finder#position position` will help here. [dox:Finder#position
position] called on a finder returns the location of the
``<tt>x``\ ``th pattern, where ``\ ``x``\  can be the first, second, or
any other occurrence of the pattern.

::

    #c++
    #include <seqan/sequence.h>
    #include <seqan/index.h>

    using namespace seqan;

    int main()
    {
        String<Dna5> genome = "ACGTACGTACGTN";
        Index<String<Dna5>, IndexEsa<> > esaIndex(genome);
        Finder<Index<String<Dna5>, IndexEsa<> > > esaFinder(esaIndex);

        find(esaFinder, "ACGT"); // first occurrence of "ACGT"
        position(esaFinder); // -> 0
        find(esaFinder, "ACGT"); // second occurrence of "ACGT"
        position(esaFinder); // -> 4
        find(esaFinder, "ACGT"); // third occurrence of "ACGT"
        position(esaFinder); // -> 8
    }

::

    #InfoBox
    Indices in SeqAn are build on demand. That means that the index tables are not build when the constructor is called, but when we search for a pattern for the first time.

Assignment 2
^^^^^^^^^^^^

::

    #AssignmentBox

     Type :: Application
     Objective :: Write a small program that prints the locations of all occurrences of "TATAA" in "TTATTAAGCGTATAGCCCTATAAATATAA".
     Hints ::
    <pre>
    #FoldOut
    ----
    Use the :dox:`Finder#find find` function as the conditional instruction of a <tt>while</tt> loop.

``Solution ::``

::

    #FoldOut
    ----
    [[Include(source:trunk/core/demos/tutorial/index/indices_assignment_2.cpp)]]

.. raw:: html

   </pre>

You might have noticed that we only applied the :dox:`FMIndex`
and :dox:`IndexEsa` in the examples. The reason for this is that
even though everything stated so far is true for the other indices as
well, :dox:`IndexWotd` and :dox:`IndexDfi` are more
usefull when used with iterators as explained in `Index
Iterators <Tutorial/IndexIterators>`__ and the [dox:IndexQGram
IndexQGram] uses :dox:`Shape Shapes` which is also explained in another
tutorial.

One last remark is necessary:

::

    #ImportantBox
    If you search for two different patterns with the same :dox:`Finder` object, you have to call the :dox:`Finder#clear clear` function of the finder between the search for the two patterns. Otherwise the behavior is undefined.

Handling Multiple Sequences (StringSets)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The previous sections already described how an index of a set of strings
can be instantiated. A character position of a :dox:`StringSet`
can be one of the following:

#. A local position (default), i.e. a :dox:`Pair` (seqNo, seqOfs)
   where seqNo identifies the string within the [dox:StringSet
   StringSet] and the seqOfs identifies the position within this string.

``2. A global position, i.e. a single integer value between 0 and the sum of string lengths minus 1. This integer is the position in the gapless concatenation of all strings in the :dox:`StringSet StringSet` to a single string.``

For indices, the meta-function :dox:`SAValue` determines, which
position type (local or global) will be used for internal index tables
(suffix array, q-gram array) and what type of position is returned by
functions like :dox:`Finder#position position` of a :dox:`Finder`.
:dox:`SAValue` returns a :dox:`Pair` (local position) by
default, but could be specialized to return an integer type (global
position) for some applications. If you want to write algorithms for
both variants you should use the functions [dox:TextConcept#posLocalize
posLocalize], :dox:`TextConcept#posGlobalize posGlobalize`,
:dox:`TextConcept#getSeqNo getSeqNo`, and [dox:TextConcept#getSeqOffset
getSeqOffset].

Storing and Loading
^^^^^^^^^^^^^^^^^^^

Storing and loading an index can be done with:

::

    const char *fileName = "/home/user/myindex";
    save(index, fileName);

or

::

    const char *fileName = "/home/user/myindex";
    open(index, fileName);

If you have built your q-gram index with variable shapes (i.e.
seqan:Spec.SimpleShape or seqan:Spec.GenericShape), you have to keep in
mind that q or the shape is not stored or loaded. This must be done
manually directly before or after loading with seqan:Function.resize
(SimpleShape) oder seqan:Function.stringToShape (GenericShape).

**Hint:** A newly instantiated index is initially empty. If you assign a
text to be indexed, solely the text fibre is set. All other fibres are
empty and created on demand. Normally, a full created index should be
saved to disk. Therefore, you have to create the required fibres
explicitly by hand:

::

    const char *fileName = "/home/user/myindex";
    indexRequire(index, QGramSADir());
    save(index, fileName);

For the seqan:Spec.IndexEsa index you could do:

::

    const char *fileName = "/home/user/myindex";
    indexRequire(index, EsaSA());
    indexRequire(index, EsaLcp());
    indexRequire(index, EsaChildtab());  // for TopDown iterators
    indexRequire(index, EsaBwt());       // for (Super-)MaxRepeats iterators
    save(index, fileName);

**Hint:** Indexes based on external strings, e.g.
``Index<String<Dna,External<> >,IndexEsa<> >`` or
``Index<String<Dna,MMap<> >,IndexEsa<> >`` cannot be saved, as they are
persistent implicitly. The first thing after instantiating such an index
should be associating it to a file with:

::

    Index<String<Dna, External<> >, IndexEsa<> > index;
    const char *fileName = "/home/user/myindex";
    open(index, fileName);

The file association implies that any change on the index, e.g. fibre
construction, is synchronized to disk. When instantiating and
associating the index the next time, the index contains its previous
state and all yet constructed fibres.

Reducing the memory consumption
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One option is to change the data types used. This option to reduce the
memory consumption has no drawback concerning running time but one has
to make sure that the text to index does not exceed 4.29 billion
characters. The critical observation is that each suffix array entry
consumes 64 bit of memory per default where 32 bit would be sufficient
if the text size is appropriate. In order to change the size type of the
suffix array entry we simply have to overload the metafunction
``SAValue``.

::

    #c++

    template<>
    struct SAValue<String<Dna> >
    {
        typedef unsigned Type;
    }

If your text is a :dox:`StringSet` than ``SAValue`` will return
a :dox:`Pair` that can be overloaded in the same way.

::

    #c++
    template<>
    struct SAValue<StringSet<String<Dna> > >
    {
        typedef Pair<unsigned, unsigned> Type;
    }

The first type of the pair is used as the type for the index of a string
in the string set. So if you only have a few strings you could save even
more memory like this:

::

    #c++
    template<>
    struct SAValue<StringSet<String<Dna> > >
    {
        typedef Pair<unsigned char, unsigned> Type;
    }

How To: Accessing Index Fibres Directly
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See the [HowTo/AccessIndexFibres HowTo] page for more information.

Submit a comment
^^^^^^^^^^^^^^^^

If you found a mistake, or have suggestions about an improvement of this
page press:
[/newticket?component=Documentation&description=Tutorial+Enhancement+for+page+http://trac.seqan.de/wiki/Tutorial/Indices&type=enhancement
submit your comment]

{{TracNotice\|{{PAGENAME

.. raw:: html

   </pre>

}

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
