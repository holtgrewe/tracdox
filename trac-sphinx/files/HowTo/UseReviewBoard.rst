How To: Use Review Board
------------------------

TOC()

For SeqAn, we use `Code
Review <http://en.wikipedia.org/wiki/Code_review>`__ as a means to
ensure code quality. For this, we use [www.reviewboard.or Review Board]
(RB) 1.5. The RB instance lives at https://reviewboard.seqan.de, the
full `user manual can be found
here <http://www.reviewboard.org/docs/manual/1.6/users/>`__.

First, go to https://reviewboard.seqan.de and create a new account
through the "Create one now" link. As the user name, pick the same name
as your SVN login (if this is your ZEDAT login, please use this). Do not
pick a valuable password, e.g. generate one `using this
tool <http://www.gaijin.at/olspwgen.php>`__.

Aims for Code Reviews in SeqAn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our aim for code review is not to find bugs in codes.

Rather, the aim is to

-  make sure that the code is **consistent** with the SeqAn coding style
   guide and the general code "look and feel" of SeqAn, and
-  have a **second pair of eyes** examine your code to spot weak points
   (e.g. to find code that could be simplified).

Code review is mandatory for code to go into core.

Within core, all commits should be reviewed, with the exception of very
small fixes.

Code Review Best Practices
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Break down your changes into small pieces if necessary, this makes
   them easier to review.

Review Workflow
~~~~~~~~~~~~~~~

The review workflow has two roles: **Author** and **Reviewer** of the
code.

#. The author

-

   -  creates some changes in his local checkout,
   -  computes a diff using ``svn diff > patch.diff``, and
   -  creates a new review request.

``2. The reviewer``

-

   -  opens the review request,
   -  examines the changes,
   -  adds comments, and
   -  optionally marks it as good enough to commit *"Ship it!"*.

| ``3. If the code was marked as ``\ *``"Ship``
``it!"``*\ ``, the author can now commit his changes.``
| ``4. If the code needs some more changes, the author``

-

   -  updates the code,
   -  creates a new patch with ``svn diff > patch.diff``, and
   -  updates the review request with his patch.

``5. The reviewer then starts at point 2 again.``

Since the code is reviewed before it is committed, this review workflow
is called **pre-commit review**.

Furthermore workflow above does not require any tools besides the
Subversion client and is thus proposed to be the standard way to
creating reviews.

Creating Review Requests
~~~~~~~~~~~~~~~~~~~~~~~~

This section contains a small example on how to create a code review. In
this example, Alice is the code author and Bob is the reviewer. (It was
performed with revision 10850).

Alice wants to make the ``_intPow()`` function (which computes *a to the
power of b* for integers efficiently) public and document it.

Creating The Patch
^^^^^^^^^^^^^^^^^^

First, she looks for all occurences of ``_intPow()`` and then edits the
files.

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    $ cd path/to/seqan/checkout
    $ ack _intPow core include
    core/tests/index/test_qgram_index.h
    142:    int pos_size = intPow((unsigned)ValueSize<Dna>::VALUE, weight(shape));
    170:    int pos_size = intPow((unsigned)ValueSize<Dna>::VALUE, weight(shape));
    224:    int pos_size = intPow((unsigned)ValueSize<Dna>::VALUE, q);

    core/tests/basic/test_basic_math.h
    [...]
      vi core/tests/index/test_qgram_index.h core/tests/basic/test_basic_math.h [...]

.. raw:: html

   </pre>

Then, she creates a `patch
file <http://en.wikipedia.org/wiki/Patch_(Unix)>`__] using ``svn diff``.

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    $ svn diff > int_pow.diff
    $ head int_pow.diff
    Index: core/tests/basic/test_basic_math.h
    ===================================================================
    --- core/tests/basic/test_basic_math.h  (revision 10850)
    +++ core/tests/basic/test_basic_math.h  (working copy)
    @@ -43,10 +43,10 @@
     {
         using namespace seqan;

    -    SEQAN_ASSERT_EQ(_intPow(1, 2), 1);
    -    SEQAN_ASSERT_EQ(_intPow(2, 0), 1);

.. raw:: html

   </pre>

Next, Alice rebuilds all apps, demos and tests and checks that
everything still works as expected.

Creating The Review Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Alice now navigates to https://reviewboard.seqan.de, logs in and clicks
"New Review Request".

`Image(new\_review\_request.png,
width=600px) <Image(new_review_request.png, width=600px)>`__

Alice checked out the URL https://svn.seqan.de/seqan/trunk and created
the diff from the checkout root. Thus, the base directory is ``/trunk``.
She enters this base directory and then uploads the patch. Then, she
clicks "Create Review Request".

`Image(create\_review\_request.png,
width=600px) <Image(create_review_request.png, width=600px)>`__

She is now presented with the view of here *review draft* which is not
publically viewable yet. She fills in the "Summary", "Description",
"Testing Done" and "Reviewers/People" fields. She can edit the fields by
clicking on the little pen symbols right of the labels.

`Image(fill\_out\_properties.png,
width=600px) <Image(fill_out_properties.png, width=600px)>`__

Finally, she clicks "Publish", and then navigates to "My Dashboard".

`Image(publish\_request.png,
width=600px) <Image(publish_request.png, width=600px)>`__

There, she can now see the review request she just submitted in the
"Outgoing Reviews" category.

`Image(outgoing\_reviews.png,
width=600px) <Image(outgoing_reviews.png, width=600px)>`__

Reviewing Code
~~~~~~~~~~~~~~

Now, Bob gets an email that there is a code review request for him. He
logs into https://reviewboard.seqan.de/dashboard/ and finds a new review
request on his dashboard. He clicks on the entry and gets to the review
page.

`Image(select\_request.png,
width=600px) <Image(select_request.png, width=600px)>`__

Here, he can read the summary, description etc. He then clicks on "View
Diff" to see the actual changes from this patch. (Bob can download
Alice's diff using the "Download Diff" in the link bar next to the "View
Diff Link".)

`Image(view\_diff.png,
width=600px) <Image(view_diff.png, width=600px)>`__

Two things appear below the summary/description/... fields: (1) An
overview of all changed files and below this (2) a list of changes.
There are many things that Bob can do here, `full
documentation <http://www.reviewboard.org/docs/manual/dev/users/reviews/reviewing-diffs/>`__
is available from the Review Board project.

`Image(diff\_view.png,
width=600px) <Image(diff_view.png, width=600px)>`__

Bob now goes to the first change using the **j** key, he can navigate to
the next/previous change using **j/k**. He reviews all changes and the
changes look generally good. He adds a remark on the documentation of
``intPow()``, however: The function's documentation should contain a
warning on overflow errors and such. He does so by clicking (1) on the
line he wants to add the comment at (line 63).

`Image(adding\_comment.png,
width=600px) <Image(adding_comment.png, width=600px)>`__

After clicking (2) "Save" (or pressing Ctrl+Enter) the comment is
attached to this line. All comments and changes are automatically stored
on the server. After saving the comment, a small "1" in a rounded
rectangle on the left side indicates the number of comments on this line
so far (3).

Now, a green bar reading "You have a pending review" appears at the top
of the screen. When he clicks "Publish", his comments will be made
public and Alice can now react on the comments. Bob is taken back to the
overview screen.

`Image(review.png, width=600px) <Image(review.png, width=600px)>`__

There, he can now also create a global comment using the "Review" link.

`Image(ship\_it.png, width=600px) <Image(ship_it.png, width=600px)>`__

On the Review screen, Bob tells Alice to make the one additional
comment. Afterwards, she can just commit her changes without further
review.

Using the *post-review* Tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The RBTools package contains the *post-commit* util to programatically
create reviews from the command line. It requires the installation of
Python and the RB Tools package.

Linux RBTool Setup
^^^^^^^^^^^^^^^^^^

Most Linux distributions have a version of the *RB Tools* package in
their repository. However, it is better to install it locally using
virtualenv since this gives you a more recent version.

First, install virtualenv through your package manager, e.g. on
Debian/Ubuntu:

::

    sudo apt-get install python-virtualenv

Then, install it using virtualenv. The following assumes that
``${HOME}/local/virtualenv`` is empty.

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    $ virtualenv ${HOME}/local/virtualenv
    $ ${HOME}/local/virtualenv/bin/easy_install RBTools

.. raw:: html

   </pre>

Now, you have to add ``${HOME}/local/virtualenv/bin`` to your ``PATH``
environment variable.

Next, [#Creatinga.reviewboardrcFile Create a .reviewboardrc file.]

Mac Os X RBTool Setup
^^^^^^^^^^^^^^^^^^^^^

The RBTools package is in MacPorts. However, the following approach
gives you a more recent version and is recommended.

First, install virtualenv (if it is not installed already) and then use
virtualenv:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    $ virtualenv ${HOME}/local/virtualenv
    $ ${HOME}/local/virtualenv/bin/easy_install RBTools

.. raw:: html

   </pre>

Finally, add ``${HOME}/local/virtualenv/bin`` to your ``PATH``
environment variable.

Next, [#Creatinga.reviewboardrcFile Create a .reviewboardrc file.]

Creating a .reviewboardrc File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Copy the following into a file called ``.reviewboardrc`` inside your SVN
checkout of SeqAn, e.g. ``${HOME}/Development/seqan-trunk``.

::

    REPOSITORY = 'https://svn.seqan.de/seqan'
    REVIEWBOARD_URL = 'https://reviewboard.seqan.de'

Creating Review Requests Using post-review
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For creating a review of **existing commits**, you can use the
``--revision-range`` option to the ``post-review`` command. For example,
to create a review of commit number 10827, you have to use the revision
range ``10826:10827``.

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    $ post-review --revision-range 10826:10827

.. raw:: html

   </pre>

Optionally, use the ``--summary`` and ``--description`` options (or the
``--description-file``) options to give the summary and description of
the review on the command line.

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    $ post-review --revision-range 10826:10827 --summary "This is my review summary." --description "This patch does this and that."

.. raw:: html

   </pre>

If you do not give these options then you have to go to the patch on the
RB site and fill these in. You can either use the URL printed by the
``post-review`` command or navigate there from your Dashboard through
the *Outgoing Reviews* category.

To create a review of the **changes in the current working copy**, you
simply call ``post-review`` with the path to the files to review, just
as if you would use the ``svn diff`` command. For example, the following
would create a review with all changes inside ``core/include/basic``.

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    $ post-review core/include/basic

.. raw:: html

   </pre>

More post-review Options
^^^^^^^^^^^^^^^^^^^^^^^^

The following is the output of ``post-review -h``. More help and
explanation is available `in the post-review
documentation <http://www.reviewboard.org/docs/manual/1.6/users/tools/post-review/#post-review>`__.

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    $ post-review -h
    Usage: post-review [-pond] [-r review_id] [changenum]

    Options:
      --version             show program's version number and exit
      -h, --help            show this help message and exit
      -p, --publish         publish the review request immediately after
                            submitting
      -r ID, --review-request-id=ID
                            existing review request ID to update
      -o, --open            open a web browser to the review request page
      -n, --output-diff     outputs a diff to the console and exits. Does not post
      --server=SERVER       specify a different Review Board server to use
      --diff-only           uploads a new diff, but does not update info from
                            changelist
      --target-groups=TARGET_GROUPS
                            names of the groups who will perform the review
      --target-people=TARGET_PEOPLE
                            names of the people who will perform the review
      --summary=SUMMARY     summary of the review
      --description=DESCRIPTION
                            description of the review
      --description-file=DESCRIPTION_FILE
                            text file containing a description of the review
      --guess-summary       guess summary from the latest commit (git/hgsubversion
                            only)
      --guess-description   guess description based on commits on this branch
                            (git/hgsubversion only)
      --testing-done=TESTING_DONE
                            details of testing done
      --testing-done-file=TESTING_FILE
                            text file containing details of testing done
      --branch=BRANCH       affected branch
      --bugs-closed=BUGS_CLOSED
                            list of bugs closed
      --revision-range=REVISION_RANGE
                            generate the diff for review based on given revision
                            range
      --label=LABEL         label (ClearCase Only)
      --submit-as=USERNAME  user name to be recorded as the author of the review
                            request, instead of the logged in user
      --username=USERNAME   user name to be supplied to the reviewboard server
      --password=PASSWORD   password to be supplied to the reviewboard server
      --change-only         updates info from changelist, but does not upload a
                            new diff (only available if your repository supports
                            changesets)
      --parent=PARENT_BRANCH
                            the parent branch this diff should be against (only
                            available if your repository supports parent diffs)
      --tracking-branch=TRACKING
                            Tracking branch from which your branch is derived (git
                            only, defaults to origin/master)
      --p4-client=P4_CLIENT
                            the Perforce client name that the review is in
      --p4-port=P4_PORT     the Perforce servers IP address that the review is on
      --repository-url=REPOSITORY_URL
                            the url for a repository for creating a diff outside
                            of a working copy (currently only supported by
                            Subversion). Requires either --revision-rangeor
                            --diff-filename options
      -d, --debug           display debug output
      --diff-filename=DIFF_FILENAME
                            upload an existing diff file, instead of generating a
                            new diff

.. raw:: html

   </pre>

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
