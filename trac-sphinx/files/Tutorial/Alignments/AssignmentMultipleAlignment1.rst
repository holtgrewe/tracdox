Assignment 1: Multiple Sequence Alignment
-----------------------------------------

Objective
^^^^^^^^^

Compute a multiple sequence alignments between the four protein
sequences

-

   -  ``DPKKPRGKMSSYAFFVQTSREEHKKKHPDASVNFSEFSKKCSERWKTMSAKEKGKFEDMAKADKARYEREMKTYIPPKGE``
   -  ``RVKRPMNAFIVWSRDQRRKMALENPRMRNSEISKQLGYQWKMLTEAEKWPFFQEAQKLQAMHREKYPNYKYRPRRKAKMLPK``
   -  ``FPKKPLTPYFRFFMEKRAKYAKLHPEMSNLDLTKILSKKYKELPEKKKMKYIQDFQREKQEFERNLARFREDHPDLIQNAKK``
   -  ``HIKKPLNAFMLYMKEMRANVVAESTLKESAAINQILGRRWHALSREEQAKYYELARKERQLHMQLYPGWSARDNYGKKKKRKREK``

using a seqan:class.Align object and the [seqan:"Spec.Score Matrix"
Blossum80] score matrix.

Repeat the above example using the Align data structure and the Blosum80
scoring matrix.

Solution
^^^^^^^^

After the usual includes, the seqan:Class.Align object ``align`` is
initialized and the four sequences are appended as rows.
.. includefrags:: core/demos/tutorial/alignments/alignment_msa_assignment1.cpp
   :fragment: main

Now the MSA is computed, using the seqan:Spec.Blosum80 matrix for
scoring.
.. includefrags:: core/demos/tutorial/alignments/alignment_msa_assignment1.cpp
   :fragment: alignment

And here is the output:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
          0     .    :    .    :    .    :    .    :    .    :
            DPKKPRGKMSSYAFFVQTSREEHKKKHPDASVNFSEFSKKCSERWKTMSA
    {|
    !
    !
    |}

            RVKRP---MNAFIVWSRDQRRKMALENPRMR-NS-EISKQLGYQWKMLTE
              | |              | | |   | |  |     | |    | | |
            FPKKP---LTPYFRFFMEKRAKYAKLHPEMS-NL-DLTKILSKKYKELPE
    {|
    !/   |        |
    !
    !      /
    |}

            HIKKP---LNAFMLYMKEMRANVVAESTLKE-SA-AINQILGRRWHALSR

         50     .    :    .    :    .    :    .    :    .    :
            KEKGKFEDMAKADKARYEREMKTY---------------IP--PKG---E
    {|
    !  /   |    |
    ! /                  |
    |}

            AEKWPFFQEAQKLQAMH-RE-K-----YP------NYKYRPRRKAKMLPK
    {|
    !   /
    |}

            KKKMKYIQDFQREKQEFERNLARFREDHP------DL--IQ--NAK---K
    {|
    !      / |             |                    |
    |}

            EEQAKYYELARKERQLH-MQ-L-----YPGWSARDNYGKKKKRKRE---K

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
