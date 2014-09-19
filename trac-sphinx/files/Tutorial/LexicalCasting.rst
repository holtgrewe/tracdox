Tutorial: Lexical Casting
-------------------------

TOC

| ``Learning Objective ::``
| `` In this tutorial, you will learn about the lexical casting functionality in SeqAn.``
| `` Lexical casting allows you to convert numbers stored as strings to their numeric values.``
| ``Difficulty ::``
| `` Basic``
| ``Duration ::``
| `` 15 min``
| ``Prerequisites ::``
| `` Tutorial Basics,``
| `` Tutorial Sequences``

Lexical Casting
~~~~~~~~~~~~~~~

When reading data from text files all data is usually first stored as
strings. For example, a genomic location is often described as a pair of
the chromosome name and the position on the chromosome, e.g. ``"chr1"``
and ``"1000"``. To really make use of the the ``"1000"`` we have to cast
it to an integer.

For this purpose, SeqAn provides the :dox:`lexicalCast` and
:dox:`lexicalCast2` functions. These functions do not cast a
value into a related type but convert a :dox:`CharString` into
its numeric value.

The function is located in the ``stream`` module so we have to include
``seqan/stream.h``.

::

    #cpp
    #include <seqan/stream.h>

The function :dox:`lexicalCast` converts a string into the
type given in the template argument and returns the value after
conversion. In case of errors, the result is undefined. This is mainly
useful if you know that the value can be converted (e.g. you accepted a
sequence of 1-4 digits and want to cast it to ``int``).

::

    #cpp
    seqan::CharString valueAsStr = "1000";
    int valueAsInt = lexicalCast<int>(valueAsStr);
    // => valueAsInt == 1000

The function :dox:`lexicalCast2` has two parameters: A
reference to the numeric destination and the string source. The result
is a ``bool`` and ``true`` indicates success.

::

    #cpp
    seqan::CharString valueAsStr = "1000";
    bool success = lexicalCast2<int>(valueAsInt, valueAsStr);
    // => success == true
    // => valueAsInt == 1000

::

    #InfoBox
    '''Information:''' Strictness of Lexical Casting

    A string such as <tt>"123XX"</tt> will be successfully cast into the <tt>int</tt> 123.
    The string <tt>-123</tt> can be converted into an <tt>int</tt> using :dox:`lexicalCast` but it might not be converted correctly into an <tt>unsigned</tt> value.

    Lexical casting in SeqAn uses the standard <tt><sstring></tt> library.
    The exact implementation of casting is library-dependent.

A Full Example
~~~~~~~~~~~~~~

The example program
[source:trunk/extras/demos/tutorial/stream/lexical\_cast\_example.cpp
lexical\_cast\_example.cpp] demonstrates the usage of both interfaces:

Include(source:trunk/extras/demos/tutorial/stream/lexical_cast_example.cpp)

This is the program's output:

::

    #ShellBox
    lexicalCast<int>("123")   --> 123
    lexicalCast<int>("123XX") --> 123
    lexicalCast2<int>("-123") --> (1, -123)
    lexicalCast2<double>("-123") --> (1, -123)

::

    #AssignmentBox
    '''Assignment 1:''' Using Lexical Casting
     Type ::
      Application
     Objective ::
      Based on the example above, create a small program that takes one argument.
      This argument is then converted into an <tt>int</tt>, <tt>unsigned</tt>, and <tt>double</tt>.
      The program should display the results of :dox:`lexicalCast` and :dox:`lexicalCast2` as in the example above.
     Hints ::
      The following shows an example session:
      <pre>#ShellBox
    # tutorial_lexical_casting_solution1 10.3
    lexicalCast<int>(10.3) ==      10
    lexicalCast<unsinged>(10.3) == 10
    lexicalCast<double>(10.3) ==   10
    lexicalCast2<int>(10.3) ==      (1, 10)
    lexicalCast2<unsigned>(10.3) == (1, 10)
    lexicalCast2<double>(10.3) ==   (1, 10.3)
    # tutorial_lexical_casting_solution1 10
    lexicalCast<int>(10) ==      10
    lexicalCast<unsinged>(10) == 10
    lexicalCast<double>(10) ==   10
    lexicalCast2<int>(10) ==      (1, 10)
    lexicalCast2<unsigned>(10) == (1, 10)
    lexicalCast2<double>(10) ==   (1, 10)
    # tutorial_lexical_casting_solution1 TEXT
    lexicalCast<int>(TEXT) ==      0
    lexicalCast<unsinged>(TEXT) == 0
    lexicalCast<double>(TEXT) ==   0
    lexicalCast2<int>(TEXT) ==      (0, 0)
    lexicalCast2<unsigned>(TEXT) == (0, 0)
    lexicalCast2<double>(TEXT) ==   (0, 0)


| ``Solution ::``
| `` Click ``\ *``more...``*\ `` to see the full solution.``

::

    #FoldOut
    ----
    [[Include(source:trunk/core/demos/tutorial/lexical_casting/solution1.cpp)]]
    [source:trunk/core/demos/tutorial/lexical_casting/solution1.cpp File in repository.]

.. raw:: html

   </pre>

Next Steps
~~~~~~~~~~

-  Continue with the `rest of the tutorials <Tutorial>`__.

Submit a Comment
~~~~~~~~~~~~~~~~

If you found a mistake, or have suggestions about an improvement of this
page press:
[/newticket?component=Documentation&description=Tutorial+Enhancement+for+page+http://trac.seqan.de/wiki/Tutorial/LexicalCasting&type=enhancement
submit your comment]

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
