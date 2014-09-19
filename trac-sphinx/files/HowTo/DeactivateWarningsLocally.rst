How To: Deactivate Warnings Locally
-----------------------------------

TOC

Compiler warnings often help to find bugs in your code and are useful.
However, sometimes you cannot fix the code that causes the warnings, for
example in:

-  Windows system headers
-  external libraries such as Boost
-  STL headers.

FIX Warnings In Your Own Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In your own code, you should fix warnings.

The following piece of code results in some common warnings.

::

    #cpp
    #include <cassert>
    #include <iostream>

    int main(int argc, char **argv) {
        int result = 0;

        int end = 10;
        for (unsigned i = 5; i < end; ++i) {
            assert(i - 6 >= 0);
        }

        return 0;
    }

Compiling the code gives warnings about:

-  unused variables and parameters,
-  comparison of signed and unsigned expressions and
-  comparisons that always yield true.

::

    $ g++ -W -Wall -pedantic WarningsDemo.cpp
    WarningsDemo.cpp: In function ‘int main(int, char**)’:
    WarningsDemo.cpp:8: warning: comparison between signed and unsigned integer expressions
    WarningsDemo.cpp:9: warning: comparison of unsigned expression >= 0 is always true
    WarningsDemo.cpp:5: warning: unused variable ‘result’
    WarningsDemo.cpp: At global scope:
    WarningsDemo.cpp:4: warning: unused parameter ‘argc’
    WarningsDemo.cpp:4: warning: unused parameter ‘argv’

You can fix the code as follows:

-  Either use variables, remove their declarations or get rid of the
   warning by casting them to void.
-  Make one of the compared values signed or unsigned by using the right
   type or the postfix "u" for unsigned literals.

``  For example, ``\ ``5u``\ `` is an ``\ ``unsigned int``\ `` of value 5 while ``\ ``5``\ `` is an ``\ ``int``\ ``.``

-  Either use parameters, remove their names from the function or cast
   them to void.

::

    #cpp
    #include <cassert>
    #include <iostream>

    int main(int, char **) {
        int result = 0;
        (void)result;  // Get rid of unused variable warning for now.

        for (unsigned i = 5; i < 10u; ++i) {
            int x = i;
            assert(x - 5 >= 0);
        }

        return 0;
    }

Suppressing Warnings In GCC
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sadly, there is no way to deactivate warnings locally with GCC. You can
only deactivate warnings for a whole file using the `system headers
pragma <http://gcc.gnu.org/onlinedocs/gcc-3.2.2/cpp/System-Headers.html#System%20Headers>`__.
However, this is not viable if you do not want to edit the offending
header yourself.

Suppressing Warnings in MSVC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In Visual Studio, you can suppress warnings using ``#pragma warning`` as
`discussed
here <http://stackoverflow.com/questions/1723572/what-is-the-best-solution-for-suppressing-warning-from-a-ms-include-c4201-in-mms>`__.

An example:

::

    #cpp
    #ifdef PLATFORM_WINDOWS_VS
    // Disable warning C4522 locally (multiple assignment operators).
    #pragma warning( disable: 4522 )
    #endif  // PLATFORM_WINDOWS_VS

    // Warning C4522 is disabled here.

    #ifdef PLATFORM_WINDOWS_VS
    // Enable warning C4522 again (multiple assignment operators).
    #pragma warning( default: 4522 )
    #endif  // PLATFORM_WINDOWS_VS

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
