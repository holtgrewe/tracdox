How To: Accessing Index Fibres Directly
---------------------------------------

TOC

Overview
~~~~~~~~

Basically each index consists of a set of tables, called fibres. The set
of available fibres of an index ``Index<TText, TSpec>`` depends on the
index specialization ``TSpec``.

+----------------------------------+-----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| **seqan:Spec.IndexEsa Fibres**   | **Description**                                                                                                       | **Type**                                                                                                 |
+==================================+=======================================================================================================================+==========================================================================================================+
| EsaText                          | The original text the index should be based on.                                                                       | First template argument of the seqan:Class.Index. Can be either a sequence or a seqan:Class.StringSet.   |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| EsaSA                            | The suffix array stores the begin positions of all suffixes in lexicographical order.                                 | String over the seqan:Metafunction.SAValue type of the index.                                            |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| EsaLcp                           | The lcp table stores at position i the length of the longest common prefix between suffix with rank i and rank i+1.   | String over the seqan:Metafunction.Size type of the index.                                               |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| EsaChildtab                      | Abouelhoda et al., 2004]]).                                                                                           | String over the seqan:Metafunction.Size type of the index.                                               |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| EsaBwt                           | The Burrows-Wheeler table stores at position i the character left of the suffix with rank i.                          | String over the alphabet of the text.                                                                    |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| EsaRawText                       | Virtually concatenates all strings of the EsaText fibre.                                                              | seqan:Concept.Container over the alphabet of the text.                                                   |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| EsaRawSA                         | Virtually transforms all positions of EsaSA fibre to global positions (see [seqan:Metafunction.SAValue here])         | seqan:Concept.Container over seqan:Metafunction.Size type of the index.                                  |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+

+-----------------------------------+------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| **seqan:Spec.IndexWotd Fibres**   | **Description**                                                                                                  | **Type**                                                                                                 |
+===================================+==================================================================================================================+==========================================================================================================+
| WotdText                          | The original text the index should be based on.                                                                  | First template argument of the seqan:Class.Index. Can be either a sequence or a seqan:Class.StringSet.   |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| WotdSA                            | The suffix array stores the begin positions of all suffixes in lexicographical order.                            | String over the seqan:Metafunction.SAValue type of the index.                                            |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| WotdDir                           | Giegerich et al., 2003]]).                                                                                       | String over the seqan:Metafunction.Size type of the index.                                               |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| WotdRawText                       | Virtually concatenates all strings of the WotdText fibre.                                                        | seqan:Concept.Container over the alphabet of the text.                                                   |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| WotdRawSA                         | Virtually transforms all positions of WotdSA fibre to global positions (see [seqan:Metafunction.SAValue here])   | seqan:Concept.Container over seqan:Metafunction.Size type of the index.                                  |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+

The seqan:Spec.Dfi index contains the same fibres as the
seqan:Spec.IndexWotd index:

+-----------------------------+-----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| **seqan:Spec.Dfi Fibres**   | **Description**                                                                                                 | **Type**                                                                                                 |
+=============================+=================================================================================================================+==========================================================================================================+
| DfiText                     | The original text the index should be based on.                                                                 | First template argument of the seqan:Class.Index. Can be either a sequence or a seqan:Class.StringSet.   |
+-----------------------------+-----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| DfiSA                       | The suffix array stores the begin positions of all suffixes in lexicographical order.                           | String over the seqan:Metafunction.SAValue type of the index.                                            |
+-----------------------------+-----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| DfiDir                      | Giegerich et al., 2003]]).                                                                                      | String over the seqan:Metafunction.Size type of the index.                                               |
+-----------------------------+-----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| DfiRawText                  | Virtually concatenates all strings of the DfiText fibre.                                                        | seqan:Concept.Container over the alphabet of the text.                                                   |
+-----------------------------+-----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| DfiRawSA                    | Virtually transforms all positions of DfiSA fibre to global positions (see [seqan:Metafunction.SAValue here])   | seqan:Concept.Container over seqan:Metafunction.Size type of the index.                                  |
+-----------------------------+-----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+

+------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| **seqan:Spec.IndexQGram Fibres**   | **Description**                                                                                                   | **Type**                                                                                                 |
+====================================+===================================================================================================================+==========================================================================================================+
| QGramText                          | The original text the index should be based on.                                                                   | First template argument of the seqan:Class.Index. Can be either a sequence or a seqan:Class.StringSet.   |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| QGramShape                         | The q-gram seqan:Class.Shape.                                                                                     | Specified by the first template argument of seqan:Spec.IndexQGram.                                       |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| QGramSA                            | The suffix array stores the begin positions of all suffixes in lexicographical order.                             | String over the seqan:Metafunction.SAValue type of the index.                                            |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| QGramDir                           | The directory maps q-gram hash values to start indices in the QGramSA fibre.                                      | String over the seqan:Metafunction.Size type of the index.                                               |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| QGramCounts                        | Stores numbers of occurrences per sequence of each q-gram in pairs (seqNo,count), count>0.                        | String over seqan:Class.Pair of the seqan:Metafunction.Size type of the index.                           |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| QGramCountsDir                     | The counts directory maps q-gram hash values to start indices in the QGramCounts fibre.                           | String over the seqan:Metafunction.Size type of the index.                                               |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| QGramBucketMap                     | Used by the seqan:Spec.OpenAddressing index to store the hash value occupancy in the QGramDir fibre.              | String over the seqan:Metafunction.Value type of the shape.                                              |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| QGramRawText                       | Virtually concatenates all strings of the QGramText fibre.                                                        | seqan:Concept.Container over the alphabet of the text.                                                   |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| QGramRawSA                         | Virtually transforms all positions of QGramSA fibre to global positions (see [seqan:Metafunction.SAValue here])   | seqan:Concept.Container over seqan:Metafunction.Size type of the index.                                  |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+

+------------------------------------------------------------+--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| **[seqan:"Spec.Pizza & Chili Index" PizzaChili] Fibres**   | **Description**                                                          | **Type**                                                                                                       |
+============================================================+==========================================================================+================================================================================================================+
| PizzaChiliText                                             | The original text the index should be based on.                          | First template argument of the seqan:Class.Index. Must be a sequence (no support for seqan:Class.StringSet).   |
+------------------------------------------------------------+--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| PizzaChiliCompressed                                       | Specialization dependent data structure to store the compressed index.   | Depends on the compressed index.                                                                               |
+------------------------------------------------------------+--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+

The first column in each table above contains the tags to select the
corresponding fibre. Most of these tags are aliases for the same tag,
e.g. ``EsaSA``, ``QGramSA``, ... are aliases for ``FibreSA``. If you
write an algorithm that is generic in the type of index can use
``FibreText`` to specify the fibre that stores the index text.

Creation
~~~~~~~~

In most cases you don't need to create the fibres of an index by hand.
Most algorithms and data structures create them automatically, e.g.
seqan:Class.Finder or seqan:"Spec.VSTree Iterator". If you want to
specify a certain index construction algorithm, have to recreate a fibre
or manually access a fibre you can recreate or create on-demand a fibre
by seqan:Function.indexCreate and seqan:Function.indexRequire. If your
algorithm should behave differently depending on the presence or absence
of a fibre (and the fibre should then not be created), you can test for
presence by seqan:Function.indexSupplied.

Access
~~~~~~

The type of each fibre can be determined by the metafunction
seqan:Metafunction.Fibre. To access a fibre you can use the function
seqan:Function.getFibre whose return type is the result of
seqan:Metafunction.Fibre. The second argument of both functions is a tag
to select a specific fibre. See the first column in the tables above.
One fibre in every index is the text to be indexed itself. This fibre
can be assigned during the construction. For the ease of use, there
exist shortcuts to access frequently used fibres:

+---------------------------------------------------------+---------------------------------------------------------------+
| **Shortcut**                                            | **Expands To ...**                                            |
+=========================================================+===============================================================+
| [seqan:Function.indexBucketMap indexBucketMap(index)]   | [seqan:Function.getFibre getFibre(index, FibreBucketMap())]   |
+---------------------------------------------------------+---------------------------------------------------------------+
| [seqan:Function.indexBwt indexBwt(index)]               | [seqan:Function.getFibre getFibre(index, FibreBwt())]         |
+---------------------------------------------------------+---------------------------------------------------------------+
| [seqan:Function.indexChildtab indexChildtab(index)]     | [seqan:Function.getFibre getFibre(index, FibreChildtab())]    |
+---------------------------------------------------------+---------------------------------------------------------------+
| [seqan:Function.indexCounts indexCounts(index)]         | [seqan:Function.getFibre getFibre(index, FibreCounts())]      |
+---------------------------------------------------------+---------------------------------------------------------------+
| [seqan:Function.indexCountsDir indexCountsDir(index)]   | [seqan:Function.getFibre getFibre(index, FibreCountsDir())]   |
+---------------------------------------------------------+---------------------------------------------------------------+
| [seqan:Function.indexLcp indexLcp(index)]               | [seqan:Function.getFibre getFibre(index, FibreLcp())]         |
+---------------------------------------------------------+---------------------------------------------------------------+
| [seqan:Function.indexRawSA indexRawSA(index)]           | [seqan:Function.getFibre getFibre(index, FibreRawSA())]       |
+---------------------------------------------------------+---------------------------------------------------------------+
| [seqan:Function.indexRawText indexRawText(index)]       | [seqan:Function.getFibre getFibre(index, FibreRawText())]     |
+---------------------------------------------------------+---------------------------------------------------------------+
| [seqan:Function.indexSA indexSA(index)]                 | [seqan:Function.getFibre getFibre(index, FibreSA())]          |
+---------------------------------------------------------+---------------------------------------------------------------+
| [seqan:Function.indexShape indexShape(index)]           | [seqan:Function.getFibre getFibre(index, FibreShape())]       |
+---------------------------------------------------------+---------------------------------------------------------------+
| [seqan:Function.indexText indexText(index)]             | [seqan:Function.getFibre getFibre(index, FibreText())]        |
+---------------------------------------------------------+---------------------------------------------------------------+

and to access a single values:

+----------------------------------------------------+--------------------------------------------------------------+
| **Shortcut**                                       | **Expands To ...**                                           |
+====================================================+==============================================================+
| [seqan:Function.bwtAt bwtAt(pos, index)]           | [seqan:Function.indexBwt "indexBwt[index](pos)"]             |
+----------------------------------------------------+--------------------------------------------------------------+
| [seqan:Function.childAt childAt(pos, index)]       | [seqan:Function.indexChildtab "indexChildtab[index](pos)"]   |
+----------------------------------------------------+--------------------------------------------------------------+
| [seqan:Function.dirAt dirAt(pos, index)]           | [seqan:Function.indexDir "indexDir[index](pos)"]             |
+----------------------------------------------------+--------------------------------------------------------------+
| [seqan:Function.lcpAt lcpAt(pos, index)]           | [seqan:Function.indexLCP "indexLcp[index](pos)"]             |
+----------------------------------------------------+--------------------------------------------------------------+
| rawsaAt(pos, index)                                | [seqan:Function.indexRawSA "indexRawSA[index](pos)"]         |
+----------------------------------------------------+--------------------------------------------------------------+
| [seqan:Function.rawtextAt rawtextAt(pos, index)]   | [seqan:Function.indexRawText "indexRawText[index](pos)"]     |
+----------------------------------------------------+--------------------------------------------------------------+
| [seqan:Function.saAt saAt(pos, index)]             | [seqan:Function.indexSA "indexSA[index](pos)"]               |
+----------------------------------------------------+--------------------------------------------------------------+
| [seqan:Function.textAt textAt(pos, index)]         | [seqan:Function.indexText "indexText[index](pos)"]           |
+----------------------------------------------------+--------------------------------------------------------------+

Please note that seqan:Function.textAt can also be used if the index
text is a seqan:Class.StringSet. ``pos`` can then be a
seqan:Metafunction.SAValue.

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
