Assignment 3: Intermediate Solution
-----------------------------------

Include the necessary headers.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_assignment3.cpp
   :fragment: include

We know implement the method to search for hits in an original node. We
only need to check if the current node covers a region of the reference
in which we've found a hit. We use the function
`::std::upper\_bound <http://www.cplusplus.com/reference/algorithm/upper_bound/>`__
to find the first element that is greater than the current physical
position. Since, we've found an upper bound we have to check
additionally if there exists a previous hit that lies directly on the
physical begin position of our current node. We then include all hits
that fit into this current node until we have found the first position
where the pattern would cross the border of this node or we have reached
the end of the reference hit set.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_assignment3.cpp
   :fragment: findInOriginalNode

Implementing the backbone to search for a pattern in the reference
string.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_assignment3.cpp
   :fragment: findPatternInJournalString

Implementing the search within the reference sequence.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_assignment3.cpp
   :fragment: findPatternInReference

Implementing the backbone of the search.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_assignment3.cpp
   :fragment: searchPattern

Implement the ``laodAndJoin`` method.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_assignment3.cpp
   :fragment: loadAndJoin

Implementing the main method.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_assignment3.cpp
   :fragment: main

Printing the hits of the reference sequence.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_assignment3.cpp
   :fragment: printResultReference

Printing the hits of the journaled sequences.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_assignment3.cpp
   :fragment: printResultJournalSequence

And here is the result.

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    Search for: GTGGT:
    Hit in reference  at 311: GTGGT 644: GTGGT
    Hit in sequence 0 at 312: GTGGT
    Hit in sequence 1 at 308: GTGGT
    Hit in sequence 2 at 311: GTGGT
    Hit in sequence 3 at 327: GTGGT
    Hit in sequence 4 at 317: GTGGT
    Hit in sequence 5 at 320: GTGGT

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
