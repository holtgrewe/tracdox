Task 5 (Graph Algorithms)
-------------------------

Task
~~~~

Extend the program from task 2. Given the sequence
``s``\ ="CTTCATGTGAAAGCAGACGTAAGTCA".

#. Calculate the Viterbi path of ``s`` and output the path as well as
   the probability of the path.

``b. Calculate the probability that the HMM generated ``\ ``s``\ `` with the forward and backward algorithm.``

Solution
~~~~~~~~

In the Graph Basics Assignment 2 we defined an HMM with three states -
exon, splice, and intron.

The Viterbi path is the sequence of states that is most likely to
produce a given output. In SeqAn, it can be calculated with the function
seqan:Function.viterbiAlgorithm. The produced output for this assignment
is the DNA sequence ``s``.

The first parameter of the function seqan:Function.viterbiAlgorithm is
of course the HMM, and the second parameter is the sequence ``s``. The
third parameter is an output parameter that will be filled by the
function. Since we want to compute a sequence of states, this third
parameter is a seqan:Class.String of
([seqan:Metafunction.VertexDescriptor vertex descriptors]) which assigns
a state to each character of the sequence ``s``.

The return value of the function seqan:Function.viterbiAlgorithm is the
overall probability of this sequence of states, the Viterbi path.

The only thing left is to output the path. The path is usually longer
than the given sequence. This is because the HMM may have silent states,
e.g. the begin and end state. To check if a state is silent SeqAn
provides the function seqan:Function.isSilent.

.. includefrags:: core/demos/tutorial/graph/graph_hmm.cpp
   :fragment: viterbi

The output of the above piece of code is:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    Viterbi algorithm
    Probability of best path: 1.25465e-18
    Sequence:
    C,T,T,C,A,T,G,T,G,A,A,A,G,C,A,G,A,C,G,T,A,A,G,T,C,A,
    State path:
    0 (Silent),1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,3,3,3,3,3,3,3,4 (Silent)

.. raw:: html

   </pre>

It is even simpler to use the forward algorithm in SeqAn since it needs
only the HMM and the sequence as parameters and returns a single
probability. This is the probability of the HMM to generate the given
sequence. The corresponding function is named
seqan:Function.forwardAlgorithm.

.. includefrags:: core/demos/tutorial/graph/graph_hmm.cpp
   :fragment: forward-algorithm

Analogously, the function seqan:Function.backwardAlgorithm implements
the backward algorithm in SeqAn.

.. includefrags:: core/demos/tutorial/graph/graph_hmm.cpp
   :fragment: backward-algorithm

The output of these two code fragments is:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    Forward algorithm
    Probability that the HMM generated the sequence: 2.71585e-18
    Backward algorithm
    Probability that the HMM generated the sequence: 2.71585e-18

.. raw:: html

   </pre>

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
