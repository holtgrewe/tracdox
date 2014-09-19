Assignment 4
------------

Task
~~~~

Modify the program to efficiently skip nodes with representatives longer
than 3. Move the whole program into a template function whose argument
specifies the index type and call this function twice, once for the
seqan:Spec.Index\_ESA and once for the seqan:Spec.Index\_Wotd index.

Solution
~~~~~~~~

We modify the DFS traversal to skip the descent if we walk into a node
whose representative is longer than 3. We then proceed to the right and
up as long as the representative is longer than 3.

.. includefrags:: core/demos/tutorial/index/index_assignment4.cpp
   :fragment: iteration

Program output:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">

    be
    e
    o
    obe
    t


    be
    e
    o
    obe
    t

.. raw:: html

   </pre>

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
