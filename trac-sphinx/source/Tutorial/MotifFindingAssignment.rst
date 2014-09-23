.. sidebar:: ToC

   .. contents::


.. _tutorial-motif-finding-assignment:

Assingment (Motif Finding)
--------------------------

Task
~~~~

Write a program which finds all motifs of length three with exactly one mismatch in the sequences ``hatpins``, ``low-fat``, and ``habitat``.
Each sequence should have exactly one occurence of the motif. 
Use the randomized heuristic :dox:`Projection` algorithm.

Solution
~~~~~~~~

First of all, we include the header file ``seqan/find_motif.h``.

.. includefrags:: extras/demos/tutorial/find_motif.cpp
   :fragment: includes

This time we choose the :dox:`Projection` method as specified in the task. 
Instead of :dox:`DnaString` we use the more general :dox:`CharString`.

.. includefrags:: extras/demos/tutorial/find_motif.cpp
   :fragment: typedefs

Next, we append the sequences to a :dox:`String` object and store the number of sequences in a variable.

.. includefrags:: extras/demos/tutorial/find_motif.cpp
   :fragment: sequences

As the :dox:`Projection` algoirthm is a randomized heuristic we need to initialize the random number generator.

The parameter ``is_exact`` is in this case set to true in order to allow only motifs with exactly one mismatch.

The number of possible motif positions can be calculated from the number of sequences, sequence length, and motif length, and is a necessary parameter for this specialization of the class :dox:`MotifFinder`.

.. includefrags:: extras/demos/tutorial/find_motif.cpp
   :fragment: initialization

The function :dox:`findMotif` performs the search. 
Since we only want to find those motifs that occur exactly once per sequence, we use the :dox:`OOPS` tag.

.. includefrags:: extras/demos/tutorial/find_motif.cpp
   :fragment: search

The output of the program looks as follows:

.. raw:: html

    <pre class="wiki" style="background-color:black;color:lightgray">
    0: hat
   </pre>

