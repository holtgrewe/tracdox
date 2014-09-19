Task 1 (Graph Basics)
---------------------

Task
~~~~

Write a program which creates a directed graph with the following edges:

(1,0), (0,4), (2,1), (4,1), (5,1), (6,2), (3,2), (2,3), (7,3), (5,4),
(6,5), (5,6), (7,6), (7,7)

Use the function seqan:Function.addEdges instead of adding each edge
separately.

Output the graph to the screen.

Solution
~~~~~~~~

We first have to include the corresponding header file for graphs.
Instead of ``seqan/graph_types.h`` we can also include
``seqan/graph_algorithms.h`` as it already includes
``seqan/graph_types.h``.

.. includefrags:: core/demos/tutorial/graph/graph_algo_scc.cpp
   :fragment: includes

This time we define a seqan:"Spec.Directed Graph" without cargo at the
edges.

.. includefrags:: core/demos/tutorial/graph/graph_algo_scc.cpp
   :fragment: typedefs

The function seqan:Function.addEdges takes as parameters an array of
vertex descriptors and the number of edges. The array of vertex
descriptors is sorted in the way predecessor1, successor1, predecessor2,
successor2, ...

.. includefrags:: core/demos/tutorial/graph/graph_algo_scc.cpp
   :fragment: main-graph-construction

The screen output of the graph consists of an adjacency list for the
vertices and an edge list:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    Adjacency list:
    0 -> 4,
    1 -> 0,
    2 -> 3,1,
    3 -> 2,
    4 -> 1,
    5 -> 6,4,1,
    6 -> 5,2,
    7 -> 7,6,3,
    Edge list:
    Source: 0,Target: 4 (Id: 1)
    Source: 1,Target: 0 (Id: 0)
    Source: 2,Target: 3 (Id: 7)
    Source: 2,Target: 1 (Id: 2)
    Source: 3,Target: 2 (Id: 6)
    Source: 4,Target: 1 (Id: 3)
    Source: 5,Target: 6 (Id: 11)
    Source: 5,Target: 4 (Id: 9)
    Source: 5,Target: 1 (Id: 4)
    Source: 6,Target: 5 (Id: 10)
    Source: 6,Target: 2 (Id: 5)
    Source: 7,Target: 7 (Id: 13)
    Source: 7,Target: 6 (Id: 12)
    Source: 7,Target: 3 (Id: 8)

.. raw:: html

   </pre>

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
