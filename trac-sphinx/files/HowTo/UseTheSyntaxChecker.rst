How To: Use The Syntax Checker
------------------------------

TOC()

The current trunk version of SeqAn contains a syntax checker that is
based on the Python bindings to
`libclang <http://www.google.de/search?q=libclang>`__. This library
exposes the AST of clang to Python which then allows us to implement
style checks from Python programs. The resulting program is located in
*util/bin/pyclangcheck.py*.

Synopsis
~~~~~~~~

You call the program with

-  one or more source files with compilation units (.cpp files) to
   check,
-  one or more directories to use as include directories (similar to the
   directories you would give to a compiler), and
-  an arbitrary number of directories to exclude (useful for external
   code).

Then, the program will parse all compilation units and the files in the
include directories. It will look for violations of rules (currently
mainly naming rules). Finally, it will report the locations of
violations.

::

    ./util/bin/pyclangcheck.py -h
    Usage: pyclangcheck.py [options] file.cpp

    Options:
      -h, --help            show this help message and exit
      -s SOURCE_FILES, --source-file=SOURCE_FILES
                            Specify source (.cpp) files.
      -S SOURCE_FILE_FILES, --source-file-file=SOURCE_FILE_FILES
                            File with path to source files.
      -i INCLUDE_DIRS, --include-dir=INCLUDE_DIRS
                            Specify include directories
      -e EXCLUDE_DIRS, --exclude-dir=EXCLUDE_DIRS
                            Violations in these directories are not shown.
      -q, --quiet           Fewer message.
      -v, --verbose         More messages.
      --ignore-nolint       Ignore // nolint statements.

Suppression of Rule Violations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can suppress violations by adding ``// nolint`` as a line suffix.
This is useful if you write adaptions for STL code that requires
*lower\_case\_naming*.

::

    #cpp
    // ...
    namespace std
    {
        template<typename TContainer, typename TSpec>
        struct iterator_traits<seqan::Iter<TContainer, TSpec> > // nolint
        {
            typedef ::seqan::Iter<TContainer, TSpec> TIter; // nolint

            typedef random_access_iterator_tag iterator_category; // nolint
            typedef typename ::seqan::Value<TIter>::Type value_type; // nolint
            typedef typename ::seqan::Difference<TIter>::Type difference_type; // nolint
            typedef typename ::seqan::Value<TIter>::Type * pointer; // nolint
            typedef typename ::seqan::Reference<TIter>::Type reference; // nolint
        };
    }
    // ...

False Positives and False Negatives
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In case of false positives and false negatives, please create a new
ticket.

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
