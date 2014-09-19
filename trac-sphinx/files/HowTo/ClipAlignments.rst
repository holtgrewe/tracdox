How To: Compute Positions In Clipped Alignments
-----------------------------------------------

This page describes how to compute view and source positions in an
unclipped and clipped seqan:class.Align object.

TOC

Position Computation Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are four coordinate systems related to each gap object. One can
consider the positions with and without gaps, both with and without
clipping. The following picture and list show the easiest
transformations between the coordinate systems.

`Image(gaps\_transformations.png, align=center,
width=300px) <Image(gaps_transformations.png, align=center, width=300px)>`__

#. Translate between view (gapped clipped) position and source (ungaped
   unclipped) position using the functions
   seqan:Function.toSourcePosition and seqan:Function.toViewPosition.

| ``2. Translate between clipped and unclipped gapped position by adding/subtracting seqan:Function.clippedBeginPosition of the gaps object.``
| ``3. Translate between clipped ungapped and unclipped ungapped position by adding/subtracing seqan:Function.beginPosition of the gaps object.``

All other transformations are most easily done following one of the
paths from the picture above.

An Example
~~~~~~~~~~

The following extensive example shows how to practically translate
between the coordinate systems.

Include(source:/trunk/core/demos/align_gaps_clipping.cpp)

Submit a Comment
^^^^^^^^^^^^^^^^

[/newticket?component=Documentation&description=Tutorial+Enhancement+for+page+http://trac.seqan.de/wiki/HowTo/ClipAlignments&type=enhancement
Submit your comment] If you found a mistake, or have suggestions about
an improvement of this page:

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
