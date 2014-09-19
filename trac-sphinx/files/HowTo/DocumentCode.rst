How To: Document Code
---------------------

TOC

Generally, the best way to learn how to document with dddoc is to look
at the existing well-documented code. Well-documented modules are
*sequence* and ''basic', for example.

We will document the =IntervalAndCargo= class:

::

    #cpp
    template <typename TValue = int, typename TCargo = int>
    class IntervalAndCargo
    {
    public:
          TValue i1;
          TValue i2;
          TCargo cargo;

          IntervalAndCargo(TValue i1, TValue i2, TCargo cargo):
                  i1(i1), i2(i2), cargo(cargo)
          {
    SEQAN_CHECKPOINT
          }
    };

Make sure you also comment any member functions!

Classes
~~~~~~~

First, we have to document the IntervalAndCargo class. Otherwise, it
will not appear in the documentation.

We place the following in front of =template <...= so it is close to the
class it describes. DDDoc itself does not enforce you to place it there,
it does not read the C++ code when generating the documentation.

Note that the lines beginning with dots have to be placed at the
beginning of the lines.

::

    #cpp
    /**
    .Class.IntervalAndCargo:
    ..cat:Miscellaneous
    ..summary:A simple record type that stores an interval and a cargo value.
    ..signature:IntervalAndCargo<TValue, TCargo>
    ..param.TValue:The value type, that is the type of the interval borders.
    ...default:int.
    ...metafunction:Metafunction.Value
    ..param.TCargo:The cargo type.
    ...default:int.
    ...metafunction:Metafunction.Cargo
    ..include:seqan/refinement.h
    */

Note that this text fragment is a tree: The strings "." represent nodes.
So ".ClassIntervalAndCargo" is a top level node. If a line begins with
more than one dot, the names of the nodes on the path to the previous
node are adopted, up to the number of dots minus one. In the first line,
for example, there are two leading dots. The first dot has no node
label, thus "Class.IntervalAndCargo" is used. The second dot is labeled
"cat". The labels have the following meaning (See =dddoc\_docu.txt= for
a comprehensive list):

| ``cat :: The category of the class.``
| ``summary :: A one-line summary of the class' functionality.``
| ``signature :: Signature of the class/class template.``
| ``param.``\ \ `` :: For each template parameter, there is a parame entry.``
| ``default :: Default for the template parameter.``
| ``metafunction :: Documentation path to Metafunction to retrieve the template parameter from the type.``
| ``include :: Name of the file to include to have access to this class.``

Member Functions (TODO)
~~~~~~~~~~~~~~~~~~~~~~~

Now, we have to document the member functions of the class.

In SeqAn, we use top level functions, so generally, our classes only
have constructors as member functions.

In this case, the construtor is an example of an overloaded function,
i.e. there are multiple functions with the same name but different
signatures. We start out with the documentation of the first
constructor.

::

    #cpp
    /**
    .Memfunc.IntervalAndCargo#IntervalAndCargo:
    ..class:Class.IntervalAndCargo
    ..summary:Constructor.
    ..signature:IntervalAndCargo(i1, i2, cargo)
    ..param.i1:The first element in the interval, of type TValue.
    ..param.i2:The last element in the interval of type TValue.
    ..param.cargo:The cargo value of type TCargo.
    */

The keys have the following meaning (again, *dddoc\_docu.txt*) has a
comprehensive list.

| ``class :: Path to the class this member function belongs to.``
| ``summary :: One-line description of the member function/parameter.``
| ``signature :: The signature to print in documentation.``
| ``param.``\ \ `` :: Description of the parameter ``\ \ ``.``

Functions (TODO)
~~~~~~~~~~~~~~~~

There are also some functions defined on the IntervalAndCargo class:

::

    #cpp
    template <typename TValue, typename TCargo>
    TValue &
    leftBoundary(IntervalAndCargo<TValue, TCargo> & interval)
    {
    SEQAN_CHECKPOINT
           return interval.i1;
    }

    template <typename TValue, typename TCargo>
    TValue &
    rightBoundary(IntervalAndCargo<TValue, TCargo> & interval)
    {
    SEQAN_CHECKPOINT
           return interval.i2;
    }

We document them as follows:

::

    #cpp
    /**
    .Function.leftBoundary:
    ..cat:Miscellaneous
    ..summary:Returns reference to left boundary of an interval.
    ..signature:leftBoundary(interval)
    ..param.object:The interval to return the left boundary for.
    ...type:Class.IntervalAndCargo
    ..returns:The reference to the left boundary of the interval of type TValue&.
    ..see:Function.getLeftBoundary
    ..see:Function.rightBoundary
    ..see:Function.getRightBoundary
    */

and

::

    #cpp
    /**
    .Function.rightBoundary:
    ..cat:Miscellaneous
    ..summary:Returns reference to right boundary of an interval.
    ..signature:leftBoundary(interval)
    ..param.object:The interval to return the left boundary for.
    ...type:Class.IntervalAndCargo
    ..returns:The reference to the right boundary of the interval of type TValue&.
    ..see:Function.getRightBoundary
    ..see:Function.leftBoundary
    ..see:Function.getLeftBoundary
    */

We use the following new keys

| ``returns :: Description of the returend value.``
| ``see :: A link to a page under "See Also".``

Tags (TODO)
~~~~~~~~~~~

Metafunctions
~~~~~~~~~~~~~

We also define the Metafunctions =Value= and =Cargo= for the
IntervalAndCargo class. We tell dddoc that they can also be used for
IntervalAndCargo:

::

    #cpp
    ///.Metafunction.Value.param.T.type:Class.IntervalAndCargo
    template <typename TValue, typename TCargo>
    struct Value<IntervalAndCargo<TValue, TCargo> >
    {
           typedef TValue Type;
    };


    ///.Metafunction.Cargo.param.T.type:Class.IntervalAndCargo
    template <typename TValue, typename TCargo>
    struct Cargo<IntervalAndCargo<TValue, TCargo> >
    {
           typedef TCargo Type;
    };

Example Code
~~~~~~~~~~~~

In order to simplify the usage of SeqAn we provide short code samples.
As a rule of thump, the code snippets should be short and include only
necessary information.

::

    #cpp
    /**
    .Function.goDown
    ..signature:bool goDown(iterator)
    ..example.code:
    String<Dna5> genome = "ACGTACGT";
    WaveletTreeStructure<Dna5> waveletTreeStructure(genome);

    Iterator<WaveletTreeStructure<Dna5>, TopDown<> >::Type it;
    it = begin(waveletTreeStructure); // go to root node

    goDown(it); // go to left child of root node
    */

In addition, we provide links to example pages that contain a functional
program using the function we document. The example pages are located in
``xxx/demos``, where xxx=core or xxx=extras, and can be included with
the code word ``demfor``. For example,

::

    .Demo.Global Alignments:
    ..cat:Basics
    ..order:Alignments 1
    ..summary:Computing an optimal global alignment between two sequences.
    ..file:../core/demos/alignment.cpp
    ..demofor:Function.globalAlignment

creates a example page for global alignments, where the code is
contained in ``alignment.cpp`` and the html pages describing the
function ``globalAlignment`` has a link to the demo page.

Building The API Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Building the API documentation for the current trunk is easy:

#. Check out the current trunk of SeqAn.

| ``2. ``\ ``cd docs``
| ``3. ``\ ``./make.sh``\ `` or ``\ ``make.bat``

Remarks
~~~~~~~

If you want to include your sandbox, step 3 becomes

3. ``./make.sh {path to sandbox}`` or ``make.bat {path to sandbox}``

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
