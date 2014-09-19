Task 3: compute suboptimal alignments
-------------------------------------

Task
~~~~

#. Write a program which computes the 3 best local alignments of the two
   seqan:Spec.AminoAcid sequences "PNCFDAKQRTASRPL" and
   "CFDKQKNNRTATRDTA" using the following scoring parameters: match = 3,
   mismatch = -2, gapopen = -5, gapextension = -1.

Solution
~~~~~~~~

The usual includes:
.. includefrags:: core/demos/tutorial/alignments/alignment_pairwise_local_assignment1.cpp
   :fragment: main

The initialization of the seqan:Class.Align object:
.. includefrags:: core/demos/tutorial/alignments/alignment_pairwise_local_assignment1.cpp
   :fragment: init

Computing the three best alignments with the desired scoring parameters:
.. includefrags:: core/demos/tutorial/alignments/alignment_pairwise_local_assignment1.cpp
   :fragment: ali

The output:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    Score = 21
          0     .    :
            CFDAKQ---RTASR
    {|
    !/
    !
    !/ |
    |}

            CFD-KQKNNRTATR


    Score = 8
          0     .
            AKQR-TA
    {|
    !
    |}

            AT-RDTA


    Score = 5
          0
            D-A
            | |
            DTA

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
