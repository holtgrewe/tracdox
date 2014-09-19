How To: Submit Patches
----------------------

TOC

Also see: wiki:HowTo/WriteTickets

Patches are the easiest way to get bugs fixed and features added to
SeqAn. You can submit patches by creating a new ticket and attaching a
patch file.

Creating A Patch With Subversion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Patches should be written against the trunk version. First, check out
SeqAn if you are not working with the trunk version and update SeqAn if
you are already working at the SVN trunk:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    $ svn co http://svn.seqan.de/seqan/trunk seqan-trunk
    $ cd seqan-trunk

.. raw:: html

   </pre>

OR

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    $ cd seqan-trunk
    $ svn update

.. raw:: html

   </pre>

Now, we update the file *random.h* and add a new file in the module
*random*:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    $ cd core/include/seqan
    $ vi random.h
    ... some changes ...
    $ vi random/MYFILE

.. raw:: html

   </pre>

We have to register the file with the local Subversion repository:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    $ svn add random/MYFILE

.. raw:: html

   </pre>

Now, we can create a patch file:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    $ svn diff > my_patch.diff
    $ cat my_patch_diff
    Index: random/MYFILE
    ===================================================================
    --- random/MYFILE   (revision 0)
    +++ random/MYFILE   (revision 0)
    @@ -0,0 +1 @@
    +This is an example file.
    Index: random.h
    ===================================================================
    --- random.h    (revision 7851)
    +++ random.h    (working copy)
    @@ -18,6 +18,8 @@
       Author: Manuel Holtgrewe &lt;manuel.holtgrewe@fu-berlin.de&gt;
      ============================================================================
       Umbrella header for the random module.
    +
    +  This is a new comment that should go into the patch.
      ==========================================================================*/

     #ifndef SEQAN_RANDOM_H_

.. raw:: html

   </pre>

Then, go to [/seqan/newticket New Ticket] in the Trac system, create a
ticket and attach the patch file.

Properties Of A Good Patch
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Describe what the patch does.
-  If the patch fixes a bug then give a short example of the problem.
-  Please include a test that highlights the bug, i.e. it does not
   compile or fail without the patch to SeqAn but the patch fixes this
   issue.
-  Indicate what configuration is required for the bug to appear, i.e.
   the operating system, compiler and, trunk revision.

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
