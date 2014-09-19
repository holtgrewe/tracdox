Assignment 3
------------

Task
~~~~

Write a program that iterates over all nodes of the suffix tree of the
string "tobeornottobe" in preorder DFS. Use seqan:Function.goDown,
seqan:Function.goRight and seqan:Function.goUp to iterate instead of
seqan:Function.goNext or the operator++. Output the representatives.

Solution
~~~~~~~~

First we create an index of the string ``tobeornottobe`` and an
seqan:"Function.TopDownHistory Iterator" that supports
seqan:Function.goDown, seqan:Function.goRight and seqan:Function.goUp.
.. includefrags:: core/demos/tutorial/index/index_assignment3.cpp
   :fragment: initialization

One iteration step of a preorder DFS can be described as follows:

-

   -  if possible, go down one node
   -  if not

      -

         -  if possible, go to the next sibling
         -  if not

            -  go up until it is possible to go to a next sibling
            -  stop the whole iteration after reaching the root node

Thus, the DFS walk can be implemented in the following way:
.. includefrags:: core/demos/tutorial/index/index_assignment3.cpp
   :fragment: iteration

Program output:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">

    be
    beornottobe
    e
    eornottobe
    nottobe
    o
    obe
    obeornottobe
    ornottobe
    ottobe
    rnottobe
    t
    tobe
    tobeornottobe
    ttobe

.. raw:: html

   </pre>

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
