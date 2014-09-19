Assignment 2: Intermediate Solution
-----------------------------------

Include the necessary headers.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_assignment2.cpp
   :fragment: include

Implementation of the ``findPatternInReference`` function.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_assignment2.cpp
   :fragment: findPatternInReference

Implementation of the ``searchPattern`` function. Note that we haven't
implemented the function ``findPatternInJournalString `` yet.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_assignment2.cpp
   :fragment: searchPattern

Implementation of the ``loadAndJoin`` function.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_assignment2.cpp
   :fragment: loadAndJoin

Implementation of the ``main`` function.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_assignment2.cpp
   :fragment: main

Printing the hits of the reference sequence.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_assignment2.cpp
   :fragment: printResult

And here is the result.

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    Search for: GTGGT:
    Hit in reference  at 311: GTGGT 644: GTGGT

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
