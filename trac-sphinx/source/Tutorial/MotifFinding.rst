.. sidebar:: ToC

   .. contents::


.. _tutorial-motif-finding:

Motif Finding
-------------

.. warning::

    There are known issues with SeqAn's ``modif_finding`` module (also see `Ticket 95 <http://trac.seqan.de/ticket/95>`_).
    We are working on a solution to this problem.

In this part of the tutorial we demonstrate how to find sequence motifs
in *multiple* sequences.

Multiple Sequence Motifs
^^^^^^^^^^^^^^^^^^^^^^^^

Lets consider the following case: We are given three DNA sequences of equal length and want to find all motifs that fulfill certain criteria.
In our example, we assume that the motif is four nucleotides long, occurs at least once per sequence, and contains at most one mismatch.

There are several motif finding algorithms in Seqan. 
The header file ``seqan/find_motif.h`` includes all necessary data types and functions.

.. includefrags:: extras/demos/tutorial/find_motif_pms1.cpp
   :fragment: includes

For our example we choose the seqan:Spec.Pms1 method, which is an exhaustive enumeration algorithm, and therefore use this specialization for our seqan:Class.MotifFinder.

.. includefrags:: extras/demos/tutorial/find_motif_pms1.cpp
   :fragment: typedefs

Next, we append the sequences to a seqan:Class.String object.

.. includefrags:: extras/demos/tutorial/find_motif_pms1.cpp
   :fragment: sequences

Before we can construct an instance of the motif finder we have to specify the motif length (``motifLength``) and number of allowed mismatches (``mm``). 
The parameter ``is_exact`` determines whether an occurence of the motif must have exactly ``mm`` mismatches or if ``mm`` is an upper bound.

.. includefrags:: extras/demos/tutorial/find_motif_pms1.cpp
   :fragment: initialization

The function :dox:`findMotif` performs the search. 
Since we only want to find those motifs that occur at least once per sequence, we use the :dox:`Omops` tag.

The function :dox:`motifCount` returns the number of found motifs. 
The ``i``\ th motif can be accessed by calling the function :dox:`getMotif`.

.. includefrags:: extras/demos/tutorial/find_motif_pms1.cpp
   :fragment: search

The result of this example is:

.. raw:: html

    <pre class="wiki" style="background-color:black;color:lightgray">
    0: ACAG
    1: AGCC
    2: CCAG
    3: GCAG
    4: TCAG
   </pre>

Assignment 1
^^^^^^^^^^^^

.. container:: assignment

   Type
     Review

   Objective
     Write a program which finds motifs of length three with exactly one mismatch in the sequences ``hatpins``, ``low-fat``, and ``habitat``.
     Each sequence should have exactly one occurence of the motif. Use the randomized heuristic :dox:`Projection` algorithm.

   Solution
     Click on the following link for a detailed explanation\: :ref:`tutorial-motif-finding-assignment`.