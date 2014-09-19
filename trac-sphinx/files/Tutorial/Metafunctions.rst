.. _tutorial-metafunctions:

Metafunctions
~~~~~~~~~~~~~

Generic algorithms usually have to know certain types that correspond to
their arguments: An algorithm on containers may need to know which type
of values are stored in the string, or what kind of iterator we need to
access it. The usual way in the STL is to define the value type of a
class like ``vector`` as a *member typedef* of this class, so it can be
retrieved by ``vector::value_type``.

Unfortunately member typedef declarations have the same disadvantages as
any members: Since they are specified by the class definition, they
cannot be changed or added to the class without changing the code of the
class, and it is not possible in C++ to define members for built-in
types. What we need therefore is a mechanism that returns an output type
(e.g. the value type) given an input type (e.g. the string) and doing so
does not rely on members of the input type, but instead uses some kind
of global interface.

Such task can be performed by **metafunctions**, also known as **type
traits**. A metafunction is a construct to map some types or constants
to other entities like types, constants, functions, or objects at
compile time. The name metafunction comes from fact that they can be
regarded as part of a meta-programming language that is evaluated during
compilation.

In SeqAn we use class templates to implement metafunctions in C++.
Generic algorithms usually have to know certain types that correspond to
their arguments: An algorithm on strings may need to know which type of
characters are stored in the string, or what kind of iterator can be
used to browse it. SeqAn uses Metafunctions (also known as "traits") for
that purpose. For example: Assuming that we define a string of amino
acids:

::

    #cpp
    String<AminoAcid> str = "ARN";

Now lets define a function that exchanges the first two values in a
string:

::

    #cpp
    void exchangeFirstValues(String<AminoAcid> & str)
    {
        if (length(str) < 2) return;
        AminoAcid temp = str[0];
        str[0] = str[1];
        str[1] = temp;
    }

Since this function only works for instances of [dox:String
String<]:dox:`AminoAcid AminoAcid>`, we could try to make it more general
by making a template out of it:

::

    #cpp
    template <typename T>
    void exchangeFirstValues(T & str)
    {
        if (length(str) < 2) return;
        AminoAcid temp = str[0];
        str[0] = str[1];
        str[1] = temp;
    }

Now the function works for all sequence types ``T`` that store
``AminoAcid`` objects, but it will fail for other value types as soon as
the variable temp cannot store ``str[0]`` anymore. To overcome this
problem, we must redefine ``temp`` in a way that it can store a value of
the correct type. The question is:

"Given a arbitrary type ``T``, what is the value type of ``T``?"

The metafunction :dox:`ConatinerConcept#Value Value` anwers this
question: "The value type of ``T`` is given by ``Value<T>::Type``."

Hence, the final version of our function ``exchangeFirstValues`` reads
as follows:

::

    #cpp
    template <typename T>
    void exchangeFirstValues(T & str)
    {
        if (length(str) < 2) return;
        typename Value<T>::Type temp = str[0];
        str[0] = str[1];
        str[1] = temp;
    }

We can view ``Value`` as a kind of "function" that takes ``T`` as an
argument (in angle brackets) and returns the required value type of
``T``. In fact, ``Value`` is not implemented as a C++ function, but as a
class template. This class template is specialized for each sequence
type ``T`` in a way that the ``typedef Type`` provides the value type of
``T``. Unfortunately, the current C++ language standard does not allow
to write simply "``Value<T> temp``;", so we must select the return value
by appending "``::Type``\ ". The leading "``typename``\ " becomes
necessary since ``Value<T>::Type`` is a type that depends on a template
parameter of the surrounding function template.

Type Metafunctions
~~~~~~~~~~~~~~~~~~

The metafunction :dox:`ConatinerConcept#Value Value` is a type
metafunction, i.e. it is used to determine a type. Type metafunctions
have the form:

``typename TypeMetaFunc<T1, T2, ..., TN>::Type``

``TypeMetaFunc``: The name of the metafunction ``T1, T2, ..., TN``:
Arguments (types or constants) ``Type``: The resulting type

The keyword ``typename`` must be stated if one of the arguments
``T1, T2, ..., TN`` is or uses a template parameter. For example the
following piece of code uses the metafunction ``Iterator`` to determine
an iterator type for a string class:

::

    #cpp
    String<char> str = "I am a string";
    Iterator<String<char> >::Type it = begin(str);
    while (! atEnd(it, str))
    {
        ::std::cout << *it;
        ++it;
    }

Value Metafunctions
~~~~~~~~~~~~~~~~~~~

Metafunctions can also be used to determine constant values at compile
time. The general form of value metafunctions is:

``VALUE_META_FUNC<T1, T2, ..., TN>::VALUE``

``VALUE_META_FUNC``: The name of the metafunction ``T1, T2, ..., TN``:
Arguments (types or constants) ``VALUE``: The resulting constant value

For example the following function prints the length of a fixed sized
string using the value metafunction :dox:`LENGTH` :

::

    #cpp
    template <typename T>
    void printLenOfFixedSizeString(T const &)
    {
        ::std::cout << LENGTH<T>::VALUE;
    }

    String<char, Array<100> > my_str;
    printLenOfFixedSizeString(my_str);

SeqAn Metafunctions
~~~~~~~~~~~~~~~~~~~

If you want to search for metafunctions only you can do so by only
selecting the metafunction category to the left of the search window at
the online documentation.

Assignment
~~~~~~~~~~

| *``Task``
``1``*\ `` :: Write a generic program that swaps the value ranges ``\ ``[i,i+k)``\ `` and ``\ ``[j,j+k)``\ `` of a container ``\ ``str``\ ``. The container should be specified as a template argument ``\ ``T``\ ``.``
| `` ``\ *``Hint``*\ `` :: Use the Metafunctions :dox:`ContainerConcept#Value Value` to access the type of the elements in the container. Use the function :dox:`RandomAccessContainerConcept#value value` to assign the values.``
| *``Difficulty``*\ `` :: 2 ``
| *``Solution``*\ `` :: can be found ``\ ```here.`` <Tutorial/Basics/swap>`__

Submit a comment
^^^^^^^^^^^^^^^^

If you found a mistake, or have suggestions about an improvement of this
page press:
[/newticket?component=Documentation&description=Tutorial+Enhancement+for+page+http://trac.seqan.de/wiki/Tutorial/Metafunctions&type=enhancement
submit your comment]

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
