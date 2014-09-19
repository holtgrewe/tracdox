Assignment 4: Complete Solution
-------------------------------

Include the necessary headers.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_assignment4.cpp
   :fragment: include

Search at the border the current node for the pattern.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_assignment4.cpp
   :fragment: searchAtBorder

Search for the pattern in the insertion region covered by the current
node.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_assignment4.cpp
   :fragment: findInPatchNode

Check if hit was reported for this region in the reference sequence.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_assignment4.cpp
   :fragment: findInOriginalNode

Implementing the backbone of the search for the Journaled String.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_assignment4.cpp
   :fragment: findPatternInJournalStringPart1

Implementing the search for the reference sequence.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_assignment4.cpp
   :fragment: findPatternInReference

The backbone of the search method.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_assignment4.cpp
   :fragment: searchPatternPart1

Loading and joining the sequences.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_assignment4.cpp
   :fragment: loadAndJoin

Implementing the main function.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_assignment4.cpp
   :fragment: main

Reporting the identified hits.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_assignment4.cpp
   :fragment: printResult

And here is the result.

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    Search for: GTGGT:
    Hit in reference  at 311: GTGGT 644: GTGGT
    Hit in sequence 0 at 151: GTGGT 312: GTGGT
    Hit in sequence 1 at 308: GTGGT
    Hit in sequence 2 at 311: GTGGT 507: GTGGT
    Hit in sequence 3 at 327: GTGGT
    Hit in sequence 4 at 307: GTGGT 312: GTGGT  317: GTGGT
    Hit in sequence 5 at 0: GTGGT   320: GTGGT  986: GTGGT

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
