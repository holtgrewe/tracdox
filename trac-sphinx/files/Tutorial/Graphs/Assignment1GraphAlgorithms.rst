Task 4 (Graph Algorithms)
-------------------------

Task
~~~~

Write a program which calculates the connected components of the graph
defined in task 1. Output the component for each vertex.

Solution
~~~~~~~~

Seqan provides the function seqan:Function.stronglyConnectedComponents
to compute the connected components of a directed graph. The first
parameter of this function is of course the graph. The second parameter
is an output parameter. It is a vertex map that will map a component id
to each vertex. Vertices that share the same id are in the same
component.

.. includefrags:: core/demos/tutorial/graph/graph_algo_scc.cpp
   :fragment: connected-components

Now, the only thing left to do is to walk through our graph and ouput
each vertex and the corresponding component using the function
seqan:Function.getProperty. One way of doing so is to define a
seqan:"Spec.Vertex Iterator".

.. includefrags:: core/demos/tutorial/graph/graph_algo_scc.cpp
   :fragment: output-connected-components

The output for the graph defined in the Graph Basics task 1 looks as
follows:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    Strongly Connected Components:
    Vertex a: Component = 3
    Vertex b: Component = 3
    Vertex c: Component = 2
    Vertex d: Component = 2
    Vertex e: Component = 3
    Vertex f: Component = 1
    Vertex g: Component = 1
    Vertex h: Component = 0

.. raw:: html

   </pre>

The graph consists of four components: The first contains vertex ``a``,
``b``, and ``e``, the second contains vertex ``c`` and ``d``, the third
contains vertex ``f`` and ``g`` and the last contains only vertex ``h``.

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
