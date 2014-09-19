Task 2 (Graph Basics)
---------------------

Task
~~~~

Write a program which defines an HMM for DNA sequences:

#. Define an exon, splice, and intron state.
#. Consider to use the type ``LogProb<>`` from
   ``seqan/basic/basic_logvalue.h`` for the transition probabilities.

| ``   Sequences always start in the exon state.``
| ``   The probability to stay in an exon or intron state is 0.9.``
| ``   There is exactly one switch from exon to intron.``
| ``   Between the switch from exon to intron state, the HMM generates exactly one letter in the splice state.``
| ``   The sequence ends in the intron state with a probability of 0.1.``

#. Output the HMM to the screen.
#. Use the follwing emission probabilities:

+----+-----+-----+-----+-----+
|    | A   | C   | G   | T   |
+====+=====+=====+=====+=====+
+----+-----+-----+-----+-----+

+--------------+--------+--------+--------+--------+
| exon state   | 0.25   | 0.25   | 0.25   | 0.25   |
+==============+========+========+========+========+
+--------------+--------+--------+--------+--------+

+----------------+--------+-------+--------+-------+
| splice state   | 0.05   | 0.0   | 0.95   | 0.0   |
+================+========+=======+========+=======+
+----------------+--------+-------+--------+-------+

+----------------+-------+-------+-------+-------+
| intron state   | 0.4   | 0.1   | 0.1   | 0.4   |
+================+=======+=======+=======+=======+
+----------------+-------+-------+-------+-------+

Solution
~~~~~~~~

The program starts with the inclusion of ``seqan/graph_algorithms.h``
and ``seqan/basic/basic_logvalue.h``. In this example you could include
``seqan/graph_types.h`` instead of the algorithms header file. However,
it is likely that if you define a graph, you will call a graph algorithm
as well.

.. includefrags:: core/demos/tutorial/graph/graph_hmm.cpp
   :fragment: includes

Next, we define our types. The most interesting type here is ``THmm``.
It is a seqan:Class.Graph with the specialization seqan:Spec.Hmm. The
specialization takes itself three template arguments: The
`alphabet <Tutorial/Basics#Alphabets>`__ of the sequence that the HMM
generates, the type of the transitions, and again a specialization. In
our case, we define the transitions to be the logarithm of the
probilities (seqan:Class.LogProb) and hereby simplify multiplications to
summations. For the specialization we explicitly use the
seqan:Tag.Default tag.

.. includefrags:: core/demos/tutorial/graph/graph_hmm.cpp
   :fragment: typedefs

After that, we define some variables, especially one of our type
``THmm``.

.. includefrags:: core/demos/tutorial/graph/graph_hmm.cpp
   :fragment: variables

Now we can start with defining the states. States are represented by the
vertices of the HMM-specialized graph.

The initial and terminating states of an HMM in Seqan are always silent,
i.e. they do not generate characters. That is why we have to define an
extra begin state and tell the program that this is the initial state of
the HMM. The latter is done by calling the function
seqan:Function.assignBeginState.

.. includefrags:: core/demos/tutorial/graph/graph_hmm.cpp
   :fragment: begin-state

For our three main states we also add a vertex to the HMM with
seqan:Function.addVertex. Additionally, we assign the emission
probabilities for all possible characters of our alphabet using
seqan:Function.emissionProbability.

.. includefrags:: core/demos/tutorial/graph/graph_hmm.cpp
   :fragment: main-states-emissions

Finally, we need to define the end state and call
seqan:Function.assignEndState.

.. includefrags:: core/demos/tutorial/graph/graph_hmm.cpp
   :fragment: end-state

For the HMM, only the transition probabilities are still missing. A
transition is represented by an edge of our HMM graph type. The cargo on
these edges correspond to the transition probabilities.

Since the sequences always start with an exon, we set the transition
probability from the begin state to the exon state to 1.0 calling the
already well-known function seqan:Function.addEdge. And also the other
transitions can be defined in the same way.

.. includefrags:: core/demos/tutorial/graph/graph_hmm.cpp
   :fragment: transitions

To check the HMM we can simply output it to the screen:

::

        ::std::cout << hmm << ::std::endl;

This should yield the following:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    Alphabet:
    {A,C,G,T}
    States:
    {0 (Silent),1,2,3,4 (Silent)}
    Begin state: 0
    End state: 4
    Transition probabilities:
    0 -> 1 (1.000000)
    1 -> 2 (0.100000) ,1 (0.900000)
    2 -> 3 (1.000000)
    3 -> 4 (0.100000) ,3 (0.900000)
    4 ->
    Emission probabilities:
    1: A (0.250000) ,C (0.250000) ,G (0.250000) ,T (0.250000)
    2: A (0.050000) ,C (0.000000) ,G (0.950000) ,T (0.000000)
    3: A (0.400000) ,C (0.100000) ,G (0.100000) ,T (0.400000)

.. raw:: html

   </pre>

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
