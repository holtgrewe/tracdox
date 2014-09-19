KNIME Nodes
-----------

TOC()

| ``Learning Objective ::``
| `` You will learn how to import new applications written in SeqAn into the KNIME Eclipse plugin. After completing this tutorial, you will be able to use self made applications in KNIME workflows.``
| ``Difficulty ::``
| `` Basic``
| ``Duration ::``
| `` 1,5 h ``
| ``Prerequisites ::``
| `` Basic C or C++ knowledge, the ``\ ```First`` ``Steps`` ``in``
``SeqAn`` <Tutorial/FirstStepsInSeqAn>`__\ `` and the ``\ ```Parsing``
``Command`` ``Line``
``Arguments`` <Tutorial/ParsingCommandLineArguments>`__\ `` tutorial help.``

In this tutorial you will learn how to integrate new apps written in
SeqAn into a KNIME workflow. The first part consists of preparing a
dummy app such that it can be used in a KNIME workflow and in the second
part you are asked to adapt the app such that it becomes a simple
quality control tool.

::

    #ImportantBox
    The steps described here are necessary if you want to develop and test new SeqAn apps in KNIME. If you only want to use existing SeqAn apps in KNIME follow [HowTo/UseSeqAnNodesInKnime this howto].

Importing SeqAn apps into KNIME
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For the first part of the tutorial follow the instructions
`here <HowTo/GenerateSeqAnKnimeNodes>`__ and import a dummy SeqAn app
into KNIME

Create a useful KNIME workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the second part of the tutorial you are asked to modify the app you
imported into KNIME such that it becomes a quality control tool.

::

    #AssignmentBox
    ==== Assignment 1 ====
     Type ::
      Transfer
     Objective ::
       Create a simple read mapping workflow in KNIME using 'razers3' and map the attachment:reads.fastq to attachment:ref.fasta. Configure the node to use a [[MenuTrace(percent-identity)]] value of 99 and the output format could be 'razers', where the third to last and second to last column show the matching position in the reference (begin and end respectively) and the last one represents the number of matching characters in percent.

You probably observe that you do not find a lot of matches. The reason
for this are wrong bases at the end of the reads.

::

    #AssignmentBox
    ==== Assignment 2 ====
     Type ::
      Transfer
     Objective ::
      Modify the 'knime_node' app such that it becomes a quality trimmer. You might start by just deleting the last bases of the reads (say 4 or 5) and then make the cutting depending on the actual quality values. Include the node into you workflow and inspect if the results change.

::

    #InfoBox
    '''Information:''' KNIME needs to know the input and output ports of a node. Therefore we must specify them using ArgParseArgument::INPUTFILE or ArgParseArgument::OUTPUTFILE as can be seen in the 'knime_node' app. In addition, KNIME needs to know the valid file endings, which you can specify with :dox:`ArgParseArgument#setValidValues setValidValues`, which is also shown in the example.

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
