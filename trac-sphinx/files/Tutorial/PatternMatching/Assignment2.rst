Assignment 2
------------

Task
~~~~

Modify the example above to search with the seqan:Spec.Myers algorithm
for matches of "more" with an edit distance of at most 2.

Solution
~~~~~~~~

First we change the needle from "mo" to "more".
.. includefrags:: core/demos/tutorial/find/find_assignment2.cpp
   :fragment: initialization

We then change the specialization tag of the seqan:Class.Pattern to
seqan:Spec.Myers with default arguments. As seqan:Spec.Myers algorithm
is only applicable to edit distance searches it cannot be specialized or
initialized with a scoring scheme. In SeqAn, edit distance corresponds
to the scoring scheme (0,-1,-1) (match, mismatch, gap) and an edit
distance of 2 corresponds to a minimum score of -2 given to the
seqan:Function.find function.
.. includefrags:: core/demos/tutorial/find/find_assignment2.cpp
   :fragment: output

Program output:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    [2,4)   mo
    [2,5)   mon
    [2,6)   mon,
    [12,14) mo
    [12,15) mor
    [12,16) more
    [12,17) more
    [12,18) more m
    [17,19) mo
    [17,20) mon
    [17,21) mone
    [17,22) money

.. raw:: html

   </pre>

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
