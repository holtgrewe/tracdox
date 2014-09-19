Assignment 5: Complete Solution
-------------------------------

Now we want to replace the brute force methods with some cool pattern
matching algorithms. Therefor we include the header ``seqan/finder.h``.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_finder.cpp
   :fragment: include

Now we can use the seqan:Class.Finder interface of SeqAn. One cool thing
of the usage of the Finder class is that we don't have to check for the
borders anymore. This will do the Finder for us. We only have to specify
the correct infix over which the Finder should iterate to find the
pattern. We first compute the positions that enclose the search region.
Afterwards, we get an infix for this region and pass it to the Finder's
constructor. We also have to define the seqan:Class.Pattern object which
gets the pattern we are searching for. Then we can simply call the
function seqan:Function.find until we there is no more match. Be careful
when storing the position that the Finder is returning. We have to
recompute the correct virtual position since we used an infix of the
original search text.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_finder.cpp
   :fragment: searchAtBorder

So the biggest change is done. We simply repeat the changes from above
and watch to get the correct virtual position.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_finder.cpp
   :fragment: findInPatchNodePart1

Of course we don't need to change anything for the original nodes.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_finder.cpp
   :fragment: findInOriginalNode

Also the function ``findPatternInJournalString`` remains the same.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_finder.cpp
   :fragment: findPatternInJournalString

We will switch to the Finder concept for the function
``findPatternInReference`` too. This is done quickly, since we have the
basis already laid down in the previous functions.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_finder.cpp
   :fragment: findPatternInReference

From here on, we don't have to change anything.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_finder.cpp
   :fragment: searchPatternPart1

We write the same main body ...

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_finder.cpp
   :fragment: laodAndJoin

and finally print the results.

.. includefrags:: extras/demos/tutorial/data_journaling/solution_online_search_finder.cpp
   :fragment: main

And here is the result using the Finder and Pattern concept of SeqAn.

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
