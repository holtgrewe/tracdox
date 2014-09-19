Task 3 (Property Maps)
----------------------

Task
~~~~

Add a vertex map to the program from task 1:

#. The map shall assigns a lower-case letter to each of the seven
   vertices.

``   Find a way to assign the properties to all vertices at once in a single function call (``\ *``without``*\ `` using the function seqan:Function.assignProperty for each vertex separately).``

#. Show that the graph is not connected by iterating through the graph
   in depth-first-search ordering.

``   Output the properties of the reached vertices.``

Solution
~~~~~~~~

Our aim is not to assign all properties at once to the vertices.
Therefore, we create an array containing all the properties, the letters
'a' through 'h'.

The function seqan:Function.assignVertexMap does not only resize the
vertex map (as seqan:Function.resizeVertexMap does) but also initializes
it. If we specify the optional parameter ``prop``, the values from the
array ``prop`` are assigned to the items in the property map.

.. includefrags:: core/demos/tutorial/graph/graph_algo_scc.cpp
   :fragment: vertex-map

To iterate through the graph in depth-first-search ordering we have to
define an seqan:Metafunction.Iterator with the specialization
seqan:"Spec.Dfs Preorder Iterator".

The vertex descriptor of the first vertex is ``0`` and we choose this
vertex as a starting point for the depth-first-search through our graph
``g`` with the iterator ``dfsIt``:

.. includefrags:: core/demos/tutorial/graph/graph_algo_scc.cpp
   :fragment: iterate-dfs

For the chosen starting point, only two other vertices can be reached:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    Iterate from 'a' in depth-first-search ordering: a, e, b,

.. raw:: html

   </pre>

So, the graph is not connected.

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
