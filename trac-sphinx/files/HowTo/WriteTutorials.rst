How To: Write a Tutorial
------------------------

TOC

 

::

     #ImportantBox
    Please only use this how-to in conjunction with the [Tutorial/Template tutorial template].
     

Conventions
~~~~~~~~~~~

Wiki Conventions
^^^^^^^^^^^^^^^^

-

   -  Use only one line per sentence. This increases the readability of
      the sources.\\\\

::

    #FoldOut
    ----
    Besprechung Manuel, Jochen, Sabrina, Björn: One line per sentence (easier diff traceability), Easier to see how long a sentence actually is.

Naming Conventions
^^^^^^^^^^^^^^^^^^

-

   -  Use `headline
      capitalization <http://www.newsletterfillers.com/archives/grammar/capitalization_headline.htm>`__
      for headlines.\\\\

::

    #FoldOut
    ----
    tutorial_guide_old; Besprechung Manuel, Jochen, Sabrina, Björn: Formatierung von Dateinamen, Code, Output

-

   -  Use the tutorial‘s title as the last part in the wiki url (e.g.
      /wiki/Tutorial/NameOfYourTutorial).\\\\

::

    #FoldOut
    ----
    tutorial_guide_old

-

   -  Assignments are numbered in the order they appear in a tutorial
      (e.g. Assignment 5). Do not use a section relative numbering but
      an absolute one. (e.g. If the last assignment of section 1 was
      assignment 3, the first assignment of section 2 is assignment
      4).\\\\

::

    #FoldOut
    ----
    tutorial_guide_old

-

   -  Place the assignment‘s complete solution on
      ``/wiki/Tutorial/NameOfYourTutorial/Assignment/NameOfYourAssignment``
      (e.g.
      ``/wiki/Tutorial/Sequences/Assignment/CharacterCounting``).\\\\

::

    #FoldOut
    ----
    tutorial_guide_old

Design & Layout Conventions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

-

   -  Use back ticks (``<tt>``) to denote names of variables, functions,
      etc. (e.g. ````\ append\ ``<tt>`` results in append\`). \\\\

::

    #FoldOut
    ----
    tutorial_guide_old

-

   -  Use bold font (‘‘‘word‘‘‘) to denote key concepts.\\\\

::

    #FoldOut
    ----
    Besprechung Manuel, Jochen, Sabrina, Björn: Hervorhebung key concepts

-

   -  Use ``[[MenuTrace(Project Explorer)]]`` to denote menu entries in
      a graphical user interface. (e.g. `MenuTrace(Project
      Explorer) <MenuTrace(Project Explorer)>`__)

-

   -  Use the following markup to include source code\\\\

::

    [[Include(source:trunk/extras/demos/tutorial/find_motif_pms1.cpp, fragment=search)]]  

| ``where ``\ ``extras/demos/tutorial/find_motif_pms1.cpp``\ `` locates the source code file in the subversion repository and ``\ ``search``\ `` the segment to include in the tutorial.  ``
| ``This results in: ￼   ``\ ```Include(source:trunk/extras/demos/tutorial/find_motif_pms1.cpp,``
``fragment=search)`` <Include(source:trunk/extras/demos/tutorial/find_motif_pms1.cpp, fragment=search)>`__\ ``  ``
| ``The corresponding source code file ``\ ``extras/demos/tutorial/find_motif_pms1.cpp``\ `` looks like this:``

::

    [...]

    // FRAGMENT(includes)
    #include <iostream>
    #include <seqan/find_motif.h>

    using namespace seqan;

    [...]

    // FRAGMENT(search)
        findMotif(finder_pms1, dataset, Omops());

        for (int i = 0; i < (int) motifCount(finder_pms1); ++i)
            std::cout << i << ": " << getMotif(finder_pms1, i) << ::std::endl;

        return 0;
    }

-

   -  You should always build and test the tutorials code snippets
      before using them:

::

    #ShellBox
    make targets

-

   -  Use the following markup to format screen output:

::

     <pre> #ShellBox
    # Hello World! 

.. raw:: html

   </pre>

 

::

     #ShellBox
    # Hello World! 

-

   -   

Use the following markup to inform about **important bugs** or other
relevant issues. The content (and thereby the box itself) is always of
**temporary** nature and should **only be used thriftily**.:

::

     <pre> #WarningBox
    Warning goes here... 

.. raw:: html

   </pre>

 

.. raw:: html

   </pre>

-

   -   

Use the following markup to give **important information**.

These boxes contain information that **should be kept in mind** since
the described phenomenon is very likely to be encountered by the reader
again and again when working with SeqAn.

In contrast to the CautionBox this box type is of **permanent** nature
and the given information are valid for a long time.

::

     <pre> #ImportantBox
    Important information goes here... 

.. raw:: html

   </pre>

 

.. raw:: html

   </pre>

-

   -   

Use the following markup to give further / **optional information**.
These are information that support the understanding but are too
distinct to be put in a normal paragraph.:

::

     <pre> #InfoBox
    Optional information goes here... 

.. raw:: html

   </pre>

 

.. raw:: html

   </pre>

-

   -   

Use the following markup to format assignments (for further details see
[#assignments]):

::

     <pre> #AssignmentBox
    Assignment goes here... 

.. raw:: html

   </pre>

 

.. raw:: html

   </pre>

-

   -  Use ``seqan:<Category>.<Item Name>`` to create links to the Seqan
      documentation.

| ``Note that this will mereley generate the URLs that ``\ *``dddoc``*\ `` would create but does not perform any checking.``
| ``The most common cases are:``

| ``[seqan:Page.Sequences]``\ `` ::``
| ``  [seqan:Page.Sequences]``
| ``seqan:Class.Finder``\ `` ::``
| ``  seqan:Class.Finder``
| ``seqan:"Concept.Simple Type"``\ `` ::``
| ``  seqan:"Concept.Simple Type"``
| ``seqan:"Spec.Chunk Pool Allocator"``\ `` ::``
| ``  seqan:"Spec.Chunk Pool Allocator"``
| ``[seqan:"Spec.Chunk Pool Allocator" Alternative Title]``\ `` ::``
| ``  [seqan:"Spec.Chunk Pool Allocator" Alternative Title]``

Structure
~~~~~~~~~

Meta Information
^^^^^^^^^^^^^^^^

Place ``[[TOC]]`` directly after the tutorial‘s title.

::

    #FoldOut
    ----
    tutorial_guide_old

Based on the [Tutorial/Template template tutorial] provide information
regarding:

::

    #FoldOut
    ----
    workshop2011: The participants solved the tutorials in their listed order.

| ``learning objective::``
| ``  Describe the learning objective in your own words.``
| ``difficulty::``
| ``  Valid values: Very basic, Basic, Average, Advanced, Very advanced``
| ``duration::``
| ``  In average how much time will a user spend on absolving this tutorial? If you expect more than 90 minutes please split your tutorial up into multiple ones.``
| ``prerequisites::``
| ``  A list of absolved tutorials and other requirements you expect your reader to fulfill.``

Introduction
^^^^^^^^^^^^

In the next paragraph introductory information are given that answer the
following questions:\\\\

::

    #FoldOut
    ----
    Evaluation Workshop Sep/2011: Tutorial did not provide a good overview of SeqAn.

-

   -  What is this tutorial about?
   -  Why are the information important?
   -  What are the communicated information used for?
   -  What can the reader expect to know after having absolved the
      tutorial?

Section
^^^^^^^

Introduction
^^^^^^^^^^^^

In each section's introduction part you answer the following questions:

-

   -  What is this section about?
   -  What are the central concepts in this section?
   -  What is your partial learning objective?

Explanations / Examples
^^^^^^^^^^^^^^^^^^^^^^^

The main part consists of the description of the topic. This is the
space where enough knowledge is transmitted to **enable the reader to
solve all assignments**. Further details are contained in the
[Tutorial/Template tutorial template] and in the didactics section.

::

    #FoldOut
    ----
    Evaluation Workshop Sep/2011: Tasks can be solved with means known from tutorial

Try not to get lost in details. If you have useful but still optional
information to give use a InfoBox.

::

    #FoldOut
    ----
    Evaluation Workshop Sep/2011: Details are boring (meta, mem allocation, basics ...)

    Not all specializations are necessary in the tutorial, too confusing

    Besprechung Manuel, Jochen, Sabrina, Björn: Assignment: Sonderfälle, dürfen - und wenn wichtig - sollten genannt werden. Detailverliebtheit ist hier aber fehl am Platze.

==== Assignments [=#assignments] ====

The assignments‘ purpose in general is to support the reader‘s
understanding of the topic in question. For this each assignment is of a
special type (Review, application and transfer), has an objective, hints
and a link to the complete solution.

::

    #FoldOut
    ----
    workshop2011: Inexperienced participants and beginners could only manage to go through very few tutorials.

Depending on the assignment‘s type the reader is guided through the
assignment solving by providing him with partial solutions.

::

    #FoldOut
    ----
    Evaluation Workshop Sep/2011: Walkthrough tutorials could be a solution (a la Annes aligner ppts)

There must always be an assignments of type Review. Assignments must
always appear in an ascending order concerning their types and no „type
gap“ must occur.

::

    #FoldOut
    ----
    Evaluation Workshop Sep/2011: There should always be level 1 exercises (first one in tutorial is level 4)

    We should address different capabilites (level 1, 2, 3...)? (different opinions);

    Besprechung Manuel, Jochen, Sabrina, Björn, 05.07.2012: Aufgabentypen dürfen nur in geordneter Reihenfolge erscheinen, d.h. keine „Application“ without a preceding „Review“

Thus the only valid orders are:

-

   -  Review
   -  Review, application
   -  Review, application, transfer

The order Review, transfer is invalid since a „type gap“ (application
type missing) occurred.

All assignments must be accompanied by a solution.

::

    #FoldOut
    ----
    User-Feedback PMSB12: participants complained about missing solutions

Further Section
^^^^^^^^^^^^^^^

as many further sections as you like

Didactics
~~~~~~~~~

Type
^^^^

As already mentioned in the assignment structure description each
assignment is of one type.\\\\

::

    #FoldOut
    ----
    Evaluation Workshop Sep/2011: Basics mention advanced concepts (was confusing)

    Not all specializations are necessary in the tutorial, too confusing)

workshop2011: Inexperienced participants and beginners could only manage
to go through very few tutorials. Besprechung Manuel, Jochen, Sabrina,
Björn: Welche Aufgabentypen (3) gibt es?)

.. raw:: html

   </pre>

These levels are: Review:: knowledge fortification (mainly through
repetition, optionally with slight variations) Application:: supervised
problem solving (finely grained step-by-step assignment with at least
one hint and the interim solution per step) Transfer:: knowledge
transfer (problem solving in a related problem domain / class)

Based on the chosen level you should design your assignment.

Duration
^^^^^^^^

The time needed to absolve a tutorial must not exceed 90 minutes. Split
your tutorial up (e.g. Tutorial I, Tutorial II) if you want to provide
more information.\\\\

::

    #FoldOut
    ----
    workshop2011: Inexperienced participants and beginners could only manage to go through very few tutorials.

Language
^^^^^^^^

Make use of a simple language. This is neither about academic decadence
nor about increasing the learning barrier. You are not forced to
over-simplify your subject but still try to use a language that is also
appropriate for those who don‘t fully meet the tutorials prerequisites.

Mental Model
^^^^^^^^^^^^

When your describe and explain your topic give as many examples as
possible. Try to adopt the reader's perspective and imagine - based on
your target group and prerequisites - your reader's mental model. The
mental model can be described as an imagination of the interaction of
central concepts. Try to support the reader in developing a mental model
that fits best to your topic.\\\\

::

    #FoldOut
    ----
    Evaluation Workshop Sep/2011: Basics mention advanced concepts (was confusing)

    Not all specializations are necessary in the tutorial, too confusing)

Integration
~~~~~~~~~~~

-

   -  Add a link to your tutorial to https://trac.seqan.de/wiki/Tutorial
      \\\\

::

    #FoldOut
    ----
    tutorial_guide_old

-

   -  Above you stated the tutorials your tutorial has as prerequisites.
      Add the link in a way that all required tutorials are listed above
      your tutorial.\\\\

::

    #FoldOut
    ----
    workshop2011: The participants solved the tutorials in their listed order.

    Evaluation Workshop Sep/2011: Order of tutorials could be improved (for a beginner metafunctions is not central

.
~

.
~

.
~

Sources
~~~~~~~

Almost everything stated on this page is based on empirically gathered
data. Those sources that are references by ``more`` elements are listed
here.

tutorial\_guide\_old
^^^^^^^^^^^^^^^^^^^^

https://trac.seqan.de/wiki/HowTo/WriteTutorials?version=44

/Users/bkahlert/Dropbox/Freie Universität
Berlin/Promotion/Verbesserung/20120702 TutorialTodo – Seqan
Trac.webarchive)

Consolidated 2012-07-09 ✔

team\_feedback\_workshop11
^^^^^^^^^^^^^^^^^^^^^^^^^^

Team-Feedback „Evaluation Workshop Sep/2011“

https://projects-320336000000011019.wiki.zoho.com/Evaluation-Workshop-Sep-2011.html

Consolidated 2012-07-13 ✔

user\_feedback\_workshop11
^^^^^^^^^^^^^^^^^^^^^^^^^^

User-Feedback, Workshop11

Section „Tutorial Requirements“

https://projects-320336000000011019.wiki.zoho.com/Tutorials.html

/Users/bkahlert/Dropbox/Freie Universität
Berlin/Promotion/Verbesserung/SeqAn-BioStore Requirements.pages
(extracted from /Users/bkahlert/Dropbox/Freie Universität
Berlin/Promotion/Verbesserung/\_Umfrage.numbers)

Consolidated 2012-07-09 ✔

user\_feedback\_pmsb12
^^^^^^^^^^^^^^^^^^^^^^

User-Feedback PMSB12 (extrahiert aus /Users/bkahlert/Dropbox/Freie
Universität Berlin/Promotion/Verbesserung/\_Umfrage.numbers) 

Consolidated 2012-07-17 ✔

user\_feedback\_workshop11
^^^^^^^^^^^^^^^^^^^^^^^^^^

User-Feedback, Workshop11

Section „Tutorial Requirements“

https://projects-320336000000011019.wiki.zoho.com/Tutorials.html

/Users/bkahlert/Dropbox/Freie Universität
Berlin/Promotion/Verbesserung/SeqAn-BioStore Requirements.pages
(extracted from /Users/bkahlert/Dropbox/Freie Universität
Berlin/Promotion/Verbesserung/\_Umfrage.numbers)

Consolidated 2012-07-09 ✔

meeting\_20120705
^^^^^^^^^^^^^^^^^

Meeting Manuel, Jochen, Sabrina, Björn, 05.07.2012

Tutorial Präambel
^^^^^^^^^^^^^^^^^

-

   -  Welche Aufgabentypen (3) gibt es?
   -  Formatierung von Dateinamen, Code, Output

Tutorial
^^^^^^^^

-

   -  Hervorhebung key concepts
   -  Assignment: Sonderfälle, dürfen - und wenn wichtig - sollten
      genannt werden. Detailverliebtheit ist hier aber fehl am Platze.
   -  Aufgabentypen dürfen nur in geordneter Reihenfolge erscheinen,
      d.h. keine „Application“ without a preceding „Review“

Tutorial source
^^^^^^^^^^^^^^^

-

   -  One line per sentence (easier diff traceability)
   -  Easier to see how long a sentence actually is.

Consolidated 2012-07-10 ✔

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
