How To: Fix Whitespace Automatically
------------------------------------

This page describes how to use `Universal Indent
GUI <http://universalindent.sourceforge.net/>`__ and
`Uncrustify <http://uncrustify.sourceforge.net/>`__ to automatically fix
whitespace such that code resembles the `C++ Style
Guide <StyleGuide/Cpp>`__ more closely.

-  Uncrustify is a command line program that is given a style definition
   and a source file and reformats the source file according to the
   configuration.
-  Universal Indent GUI is a graphical front-end to Uncrustify with life
   preview that allows to manipulate the configuration and immediately
   see the results.

::

    #WarningBox
    At the moment, our ''uncrustify.cfg'' is still work in progress.
    Always check the result before applying the changes to the original file.

Installing Universal Indent GUI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This one is pretty easy. On Ubuntu and other Linux systems, you can use
the package management system to install the GUI and the reformatting
programs. The `Universal Indent GUI download
page <http://sourceforge.net/projects/universalindent/files/uigui/>`__
has binaries for Mac Os X and Windows.

Preview with Universal Indent GUI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When started, the program will present you with a window like the
following.

`Image(uig-1.png, 400px) <Image(uig-1.png, 400px)>`__

First, we set the indenter to Uncrustify.

`Image(uig-2.png, 400px) <Image(uig-2.png, 400px)>`__

Then, we load SeqAn's *uncrustify.cfg* which is located in
*${CHECKOUT}/misc*. We can do so by selecting "Indenter" -> "Load
Indenter Config File" in the program menu.

`Image(uig-3.png, 400px) <Image(uig-3.png, 400px)>`__

Then, we load a file from the SeqAn repository, for example
*core/apps/sak/sak.cpp*.

`Image(uig-4.png, 400px) <Image(uig-4.png, 400px)>`__

Now, we can toy around with the reformatter by checking "Live Indent
Preview".

`Image(uig-5.png, 400px) <Image(uig-5.png, 400px)>`__

The settings on the left panel allow us to tweak the style to our
liking. Any changes can be stored by selecting "Indenter" -> "Load
Indenter Config File" in the program menu. The source can also be
stored, using "File" -> "Save Source File" and "File" -> "Save Source
File As...".

Using The Command Line
~~~~~~~~~~~~~~~~~~~~~~

Uncrustify can also be used via the command line. This is best done
after a rough visual verification that the uncrustify.cfg yields works
for your sources using the Universal Indenter UI.

Work on single file:

::

    $ uncrustify -c ${CHECKOUT}/misc/uncrustify.cfg --replace -f path/to/file.cpp

Batch work:

::

    $ find path/to -name '*.cpp' > list.txt
    $ uncrustify -c ${CHECKOUT}/misc/uncrustify.cfg --replace -F list.txt

Automatically fix whitespaces in Xcode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Uncrustify can also be used directly from Xcode. With Xcode 4 Apple
introduced so called "Behaviors" that can be executed using for instance
keyboard shortcuts. To use uncrustify you can add a new behavior in the
Xcode Preferences (tab Behaviors) and select "*Run*\ ". Here you add the
attached ruby script.

`Image(Xcode - Behavior.png,
400px) <Image(Xcode - Behavior.png, 400px)>`__

**Note:** The script does **not** uncrustify the currently opened source
file but all source files that were changed in your current svn
checkout. Xcode does not provide the information which source file is
currently opened.

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
