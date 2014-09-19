Assignment 2
------------

Task
~~~~

Write a program that outputs all maximal unique matches (MUMs) between
"CDFGHC" and "CDEFGAHC".

Solution
~~~~~~~~

Again we start to create a seqan:Class.StringSet of
seqan:Shortcut.CharString and append the 2 strings.
.. includefrags:: core/demos/tutorial/index/index_assignment2.cpp
   :fragment: initialization

After that we simply use the predefined iterator for searching MUMs, the
seqan:Spec."MUMs Iterator". Its constructor expects the index and
optionally a minimum MUM length as a second parameter. The set of all
MUMs can be represented by a subset of suffix tree nodes. The iterator
will halt in every node that is a MUM of the minimum length. The
corresponding match is the node's seqan:Function.representative.
.. includefrags:: core/demos/tutorial/index/index_assignment2.cpp
   :fragment: iteration

Program output:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    CD
    FG
    HC

.. raw:: html

   </pre>

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
