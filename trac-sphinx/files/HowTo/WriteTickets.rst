TOC

How To: Write Tickets
---------------------

Also see: wiki:HowTo/SubmitPatches

Properties Of Good Tickets
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Good tickets clearly describe what you did, what you expected to
   happen and what happens instead.
-  Provide a minimal example on which a program fails.

| ``  A minimal example does not contain Megabytes of input, thousand lines of codes, incomplete programs or infinitely nested types.``
| ``  Rather, they boil down the input to the smallest problematic set and provide a succinct complete program that is well-formatted.``

-  Give the version of SeqAn for which the program fail.
-  Have the right component associated (see below).
-  Show the program's output and/or compiler output, depending where the
   problem is.
-  Wrap their program and output into ``<tt>`` and ````\ .

Components
~~~~~~~~~~

+------------------+--------------------------------------------------------------------------------------+
| **Name**         | **Description**                                                                      |
+==================+======================================================================================+
| Alignments       | alignment algorithms, alignment graph, multiple sequence alignment                   |
+------------------+--------------------------------------------------------------------------------------+
| Applications     | any of the programs in *apps*                                                        |
+------------------+--------------------------------------------------------------------------------------+
| Build System     | problems with CMake system, generated makefiles and forwards building                |
+------------------+--------------------------------------------------------------------------------------+
| Documentation    | incorrect and missing documentation in the API reference, the Tutorials or How-Tos   |
+------------------+--------------------------------------------------------------------------------------+
| Fragment Store   | FragmentStore, Annotation score and related programs                                 |
+------------------+--------------------------------------------------------------------------------------+
| Graph Library    | graph datastructures and algorithms                                                  |
+------------------+--------------------------------------------------------------------------------------+
| Indices          | index datastructures, algorithms for their construction, module pipe                 |
+------------------+--------------------------------------------------------------------------------------+
| Modifiers        | modified strings, alphabets and modifying iterators                                  |
+------------------+--------------------------------------------------------------------------------------+
| Seeds            | module seeds, chaining                                                               |
+------------------+--------------------------------------------------------------------------------------+
| Unspecified      | anything does not fit into another category, should be used rarely                   |
+------------------+--------------------------------------------------------------------------------------+
| Websites         | technical, not content related problems with seqan.de, trac, CDash                   |
+------------------+--------------------------------------------------------------------------------------+

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
