Graphs
------

TOC

| ``Learning Objective ::``
| `` This tutorials show how to use graphs in SeqAn and their functionality``
| ``Difficulty ::``
| `` Average``
| ``Duration ::``
| `` 1h``
| ``Prerequisites ::``
| `` ``\ ```Tutorial/Sequences`` <Tutorial/Sequences>`__\ ``,  ``\ ```Tutorial/Alignments`` <Tutorial/Alignments>`__
``A graph in computer science is an ordered pair G =(V,E) of a set of vertices V and a set of edges E.``
``SeqAn provides different :dox:`Graph Graph types of graphs` and the most well-known graph algorithms as well as some specialized alignment graph algorithms.``
``In this part of the tutorial, we demonstrate how to construct a graph in SeqAn and show the usage of some algorithms.``
``Alignment graphs are described in the ``\ ```Alignments`` <Tutorial/Alignments>`__\ `` part of this tutorial.``

Let us follow a simple example. We have given the following network of
five cities and in this network we want to compute the shortest path
from Hannover to any other city:

`Image(source:tags/seqan-1.4.0/core/demos/tutorial/graph/graph\_cities.jpg,
240px) <Image(source:tags/seqan-1.4.0/core/demos/tutorial/graph/graph_cities.jpg, 240px)>`__

In the section *Graph Basics*, we will create the network and write the
graph to a dot-file. The section *PropertyMaps* assigns city names to
the vertices and demonstrates the usage of a vertex iterator. Finally,
in *Graph Algorithms* we will compute the shortest path by calling a
single function.

After having worked through these sections you should be familiar with
the general usage of graphs in SeqAn. By the way, it is worth looking at
the [seqan:Indexpage.Demo examples] section of the documentation. You
will find examples for many of the graph algorithms implemented in
SeqAn.

Graph Basics
~~~~~~~~~~~~

The general header file for all types of graphs is
``seqan/graph_types.h``. It comprises the class :dox:`Graph` and
its specializations, all functions for basic graph operations, and
different iterators. Later, for computing the shortest path we will also
need ``seqan/graph_algorithms.h`` which includes the implementations of
most of SeqAn's graph algorithms.

.. includefrags:: eqan-1.4.0/core/demos/tutorial/graph/graph_dijkstra.cpp
   :fragment: includes

We want to model the network of cities as an undirected graph and label
the edges with distances. Before we start creating edges and vertices,
we need some typedefs to specify the graph type.

SeqAn offers different specializations of the class :dox:`Graph`:
:dox:`UndirectedGraph Undirected Graph`, [dox:DirectedGraph Directed
Graph], :dox:`Tree`, :dox:`Trie`, :dox:`Automaton`,
:dox:`Hmm`, and :dox:`AlignmentGraph Alignment Graph`. For our
example, an undirected graph will be sufficient, so we define our own
graph type ``TGraph`` with the specialization[dox:UndirectedGraph
Undirected Graph] of the class :dox:`Graph`. Luckily, this
specialization has an optional cargo template argument, which attaches
any kind of object to the edges of the graph. This enables us to store
the distances between the cities, our edge labels, using the cargo type
``TCargo`` defined as ``unsigned int``. Using the cargo argument, we
have to provide a distance when adding an edge. And when we remove an
edge we also remove the distance.

.. includefrags:: eqan-1.4.0/core/demos/tutorial/graph/graph_dijkstra.cpp
   :fragment: main-typedefs

Each vertex and each edge in a graph is identified by a so-called
descriptor. The type of the descriptors is returned by the metafunction
:dox:`VertexDescriptor`. In our example, we define a
type ``TVertexDescriptor`` by calling [dox:VertexDescriptor
VertexDescriptor] on our graph type. Analogously, there is the
metafunction :dox:`Graph#EdgeDescriptor Edge Descriptor` for edge
descriptors.

We can now create the graph ``g`` of our type ``TGraph``.

::

        TGraph g;

For our example, we add five vertices for the five cities, and six edges
connecting the cities.

Vertices can be added to ``g`` by a call to the function
:dox:`Graph#addVertex addVertex`. The function returns the descriptor of
the created vertex. These descriptors are needed to add the edges
afterwards.

.. includefrags:: eqan-1.4.0/core/demos/tutorial/graph/graph_dijkstra.cpp
   :fragment: create-vertices

The function :dox:`Graph#addEdge addEdge` adds an edge to the graph. The
arguments of this function are the graph to which the edge is added, the
vertices that it connects, and the cargo (which is in our case the
distance between the two cities).

.. includefrags:: eqan-1.4.0/core/demos/tutorial/graph/graph_dijkstra.cpp
   :fragment: create-edges

Once we have created the graph we may want to have a look at it. SeqAn
offers the possibility to write a graph to a dot file. With a tool like
`Graphviz <http://www.graphviz.org/>`__ you can then visualize the
graph.

The only thing that we have to do is to call the function
:dox:`Graph#write write` on a file stream with the tag ``DotDrawing()``
and pass over our graph ``g``.

.. includefrags:: eqan-1.4.0/core/demos/tutorial/graph/graph_dijkstra.cpp
   :fragment: main-graph-io

After executing this example, there should be a file ``graph.dot`` in
your directory.

Alternatively, you can use the standard output to print the graph to the
screen:

::

        ::std::cout << g << ::std::endl;

Assignment 1
^^^^^^^^^^^^

::

    #AssignmentBox
     Type ::
      Review
     Objective ::
      Copy the code from above and adjust it such that a road trip from Berlin via Hamburg and Hannover to Munich is simulated.
     Hints ::
      Use directed Edges
     Solution ::
    <pre>
    #FoldOut
    ----
    [[Include(source:/trunk/core/demos/tutorial/graph/solution_1.cpp)]]

.. raw:: html

   </pre>

Assignment 2
^^^^^^^^^^^^

::

    #AssignmentBox
     Type ::
      Application
     Objective ::
      Write a program which creates a directed graph with the following edges:
         (1,0), (0,4), (2,1), (4,1), (5,1), (6,2), (3,2), (2,3), (7,3), (5,4), (6,5), (5,6), (7,6), (7,7)
         Use the function :dox:`Graph#addEdges addEdges` instead of adding each edge separately.
         Output the graph to the screen.
     Solution ::
    <pre>
    #FoldOut
    ----
      ''Solution'' :: [wiki:Tutorial/Graphs/Assignment1GraphBasics
    can be found here]

.. raw:: html

   </pre>

Assignment 3
^^^^^^^^^^^^

::

    #AssignmentBox
     Type ::
      Transfer
     Objective ::
      Write a program which defines an HMM for DNA sequences:
    ###Define an exon, splice, and intron state.
    ###Consider to use the type <tt>LogProb<></tt> from <tt>seqan/basic/basic_logvalue.h</tt> for the transition probabilities.
            Sequences always start in the exon state.
            The probability to stay in an exon or intron state is 0.9.
            There is exactly one switch from exon to intron.
            Between the switch from exon to intron state, the HMM generates exactly one letter in the splice state.
            The sequence ends in the intron state with a probability of 0.1.
    ###Output the HMM to the screen.
    ###Use the follwing emission probabilities:

    {|
    !
    ! A
    ! C
    ! G
    ! T
    |}

    {|
    ! exon state
    ! 0.25
    ! 0.25
    ! 0.25
    ! 0.25
    |}

    {|
    ! splice state
    ! 0.05
    ! 0.0
    ! 0.95
    ! 0.0
    |}

    {|
    ! intron state
    ! 0.4
    ! 0.1
    ! 0.1
    ! 0.4
    |}


     Solution ::
    <pre>
    #FoldOut
    ----
    [[Tutorial/Graphs/Assignment2GraphBasics| can be found here]]

.. raw:: html

   </pre>

Property Maps And Iterators
~~~~~~~~~~~~~~~~~~~~~~~~~~~

So far, the vertices in our graph can only be distinguished by their
vertex descriptor. We will now see how to associate the city names with
the vertices.

SeqAn uses :dox:`ExternalPropertyMap External Property Map` Property
Maps] to attach auxiliary information to the vertices and edges of a
graph. The cargo parameter that we used above associated distances to
the edges. In most scenarios you should use an external property map to
attach information to a graph. Be aware that the word external is a hint
that the information is stored independently of the graph and functions
like :dox:`Graph#removeVertex removeVertex` do not affect the property
map. Property maps are simply :dox:`String Strings` of a property type
and are indexed via the already well-known vertex and edge descriptors.

Lets see how we can define a vertex property map for the city names. Our
property type is a :dox:`String` of a city name type, a char
string. We only have to create and :dox:`Graph#resizeVertexMap resize`
this map so that it can hold information on all vertices.

.. includefrags:: eqan-1.4.0/core/demos/tutorial/graph/graph_dijkstra.cpp
   :fragment: definition-property-map

Next, we can enter the city names for each vertex. Note that this is
completely independent from our graph object ``g``.

.. includefrags:: eqan-1.4.0/core/demos/tutorial/graph/graph_dijkstra.cpp
   :fragment: enter-properties

If we now want to output all vertices including their associated
information we can iterate through the graph and use the iterators value
to access the information in the property map.

But let us first have a quick look at iterators for graph types. SeqAn
provides six different specializations for graph iterators:
:dox:`VertexIterator Vertex Iterator`, [dox:AdjacencyIterator Adjacency
Iterator], :dox:`DfsPreorderIterator Dfs Preorder Iterator`, and
:dox:`BfsIterator Bfs Iterator` for traversing vertices, and
:dox:`EdgeIterator Edge Iterator` and [dox:OutEdgeIterator Out-edge
Iterator] for traversing edges. Except for the [dox:VertexIterator
Vertex Iterator] and the :dox:`EdgeIterator Edge Iterator` they depend
additionally to the graph on a specified edge or vertex.

To output all vertices of our graph in an arbitrary order, we can define
an iterator of the specialization :dox:`VertexIterator Vertex Iterator`
and determine its type with the metafunction
:dox:`ContainerConcept#Iterator Iterator`. The functions
:dox:`RootedIteratorConcept#atEnd atEnd` and
:dox:`InputIteratorConcept#goNext goNext` also work for graph iterators
as for all other iterators in SeqAn.

The :dox:`IteratorAssociatedTypesConcept#value value` of any type of
vertex iterator is the vertex descriptor. To print out all city names we
have to call the function :dox:`Graph#getProperty getProperty` on our
property map ``cityNames`` with the corresponding vertex descriptor that
is returned by the value function.

.. includefrags:: eqan-1.4.0/core/demos/tutorial/graph/graph_dijkstra.cpp
   :fragment: iterate-and-output-properties

The output of this piece of code should look as follows:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    0:Berlin
    1:Hamburg
    2:Hannover
    3:Mainz
    4:Munich

.. raw:: html

   </pre>

Assignments 4
^^^^^^^^^^^^^

::

    #AssignmentBox
     Type ::
      Application
     Objective ::
      Add a vertex map to the program from task 2:
    ###The map shall assign a lower-case letter to each of the seven vertices.
            Find a way to assign the properties to all vertices at once in a single function call (''without'' using the function :dox:`Graph#assignProperty assigProperty` for each vertex separately).
    ###Show that the graph is not connected by iterating through the graph in depth-first-search ordering.
            Output the properties of the reached vertices.

     Solution ::
    <pre>
    #FoldOut
    ----
    [[Tutorial/Graphs/Assignment1PropertyMaps| can be found here]]

.. raw:: html

   </pre>

Graph Algorithms
~~~~~~~~~~~~~~~~

Now that we completed creating the graph we can address the graph
algorithms. Here is an overview of some graph algorithms currently
available in SeqAn:

::

    #comment
    [[Image(source:tags/seqan-1.4.0/docs/img/contentGraph.png)]]

+-----------------------------------+------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                   | **Algorithm**                                                                                                    | **SeqAn function**                                                                                                                                                                                                                                |
+===================================+==================================================================================================================+===================================================================================================================================================================================================================================================+
| **Elementary Graph Algorithms**   | Breadth-First-Search Depth-First Search Topological Sort Strongly-Connected Components                           | :dox:`breadthFirstSearch` :dox:`depthFirstSearch` :dox:`topologicalSort` :dox:`stronglyConnectedComponents`                                                           |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Minimum Spanning Tree**         | Prim's Algorithm Kruskal's Algorithm                                                                             | :dox:`primsAlgorithm` :dox:`kruskalsAlgorithm`                                                                                                                                                                     |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Single-Source Shortest Path**   | DAG Shortest Path Bellman-Ford Dijkstra                                                                          | :dox:`dagShortestPath` :dox:`bellmanFordAlgorithm` :dox:`dijkstra`                                                                                                                                     |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **All-Pairs Shortest Path**       | All-Pairs Shortest Path Floyd Warshall                                                                           | :dox:`allPairsShortestPath` :dox:`floydWarshallAlgorithm`                                                                                                                                               |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Maximum Flow**                  | Ford-Fulkerson                                                                                                   | :dox:`fordFulkersonAlgorithm`                                                                                                                                                                                               |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Transitive Closure**            | Transitive Closure                                                                                               | :dox:`transitiveClosure`                                                                                                                                                                                                         |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Biologicals**                   | Needleman-Wunsch Gotoh Hirschberg with Gotoh Smith-Waterman Multiple Sequence Alignment UPGMA Neighbor Joining   | :dox:`globalAlignment` :dox:`globalAlignment` :dox:`globalAlignment` :dox:`localAlignment` :dox:`globalMsaAlignment` :dox:`upgmaTree` :dox:`njTree`   |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

::

    #comment
    {|
    ! '''Matching'''
    ! Path Growing Algorithm
    ! seqan:Function.weightedBipartiteMatching
    |}

The biological algorithms use heavily the alignment graph. Most of them
are covered in the `Alignments section <Tutorial/Alignments>`__. All
others use the appropriate standard graph. All algorithms require some
kind of additional input, e.g., the Dijkstra algorithm requires a
distance property map, alignment algorithms sequences and a score type
and the network flow algorithm capacities on the edges.

Generally, only a single function call is sufficient to carry out all
the calculations of a graph algorithm. In most cases you will have to
define containers that store the algorithms results prior to the
function call.

In our example, we apply the shortest-path algorithm of Dijkstra. It is
implemented in the function :dox:`dijkstra`.

Let's have a look at the input parameters: The first parameter is of
course the graph, ``g``. Second, you will have to specify a vertex
descriptor. The function will compute the distance from this vertex to
all vertices in the graph. The last input parameter is an edge map
containing the distances between the vertices. One may think that the
distance map is already contained in the graph. Indeed this is the case
for our graph type but it is not in general. The cargo of a graph might
as well be a string of characters or any other type. So, we first have
to find out how to access our internal edge map. We do not need to copy
the information to a new map. Instead we can define an object of the
type :dox:`InternalMap` of our type ``TCargo``. It will
automatically find the edge labels in the graph when the function
:dox:`Graph#property property` or :dox:`Graph#getProperty getProperty` is
called on it with the corresponding edge descriptor.

The output containers of the shortest-path algorithm are two property
maps, ``predMap`` and ``distMap``. The ``predMap`` is a vertex map that
determines a shortest-paths-tree by mapping the predecessor to each
vertex. Even though we are not interested in this information, we have
to define it and pass it to the function. The ``distMap`` indicates the
length of the shortest path to each vertex.

.. includefrags:: eqan-1.4.0/core/demos/tutorial/graph/graph_dijkstra.cpp
   :fragment: dijkstra-containers

Having defined all these property maps, we can then call the function
:dox:`dijkstra`:

::

        dijkstra(g,vertHannover,cargoMap,predMap,distMap);

Finally, we have to output the result. Therefore, we define a second
vertex iterator ``itV2`` and access the distances just like the city
names with the function :dox:`Graph#property property` on the
corresponding property map.

.. includefrags:: eqan-1.4.0/core/demos/tutorial/graph/graph_dijkstra.cpp
   :fragment: dijkstra-output

Assignments 5
^^^^^^^^^^^^^

::

    #AssignmentBox
     Type ::
      Application
     Objective ::
      Write a program which calculates the connected components of the graph defined in task 1. Output the component for each vertex.

     Solution ::
    <pre>
    #FoldOut
    ----
    [[Tutorial/Graphs/Assignment1GraphAlgorithms| can be found here]]

.. raw:: html

   </pre>

Assignments 6
^^^^^^^^^^^^^

::

    #AssignmentBox
     Type ::
      Application
     Objective ::
      xtend the program from the task 2. Given the sequence <tt>s</tt>="CTTCATGTGAAAGCAGACGTAAGTCA"
    ###calculate the Viterbi path of <tt>s</tt> and output the path as well as the probability of the path and
    ###calculate the probability that the HMM generated <tt>s</tt> with the forward and backward algorithm.

     Solution ::
    <pre>
    #FoldOut
    ----
    [[Tutorial/Graphs/Assignment2GraphAlgorithms| can be found here]]

.. raw:: html

   </pre>

Submit a comment
^^^^^^^^^^^^^^^^

If you found a mistake, or have suggestions about an improvement of this
page press:
[/newticket?component=Documentation&description=Tutorial+Enhancement+for+page+http://trac.seqan.de/wiki/Tutorial/Graphs&type=enhancement
submit your comment]

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
