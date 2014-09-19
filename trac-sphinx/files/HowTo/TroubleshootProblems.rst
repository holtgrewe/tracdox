How To: Troubleshooting Problems
--------------------------------

TOC()

This section collects some useful tricks for troubleshooting when
programming with SeqAn.

Compile Time Errors
~~~~~~~~~~~~~~~~~~~

Use Multiple Compilers
^^^^^^^^^^^^^^^^^^^^^^

We recommend to use subdirectories below *build* when running CMake so
you are able to generate Makefiles for different compilers. You can
specify the compiler to use when running CMake with the environment
variable ``CXX``. For example:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    cd build
    mkdir Debug-gcc4.3
    cd Debug-gcc4.3
    CXX=g++-4.3 cmake ../..
    cd ..
    mkdir Debug-clang
    cd Debug-clang
    CXX=clang++ cmake ../..
    cd ..

Problems Before The Build Process Is Initiated
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sometimes it is necessary to regenerate the build files by CMake, e.g.
after installing a new version of python. Since CMake keeps a lot of
information in a cache file it is advisable to also delete this file:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    cd build
    rm CMakeCache.txt
    cmake ..

Use Clang
^^^^^^^^^

The error reporting of llvm/clang is much better than the one of the
GCC. Try installing the Clang++ compiler and see what it has to say
about your programs. Especially, for template-errors, this is very
useful. SeqAn should compile with clang++ versions >= 2.9.

Consider the following program:

::

    #cpp
    #include <seqan/graph_types.h>

    int main(int, char const **)
    {
        using namespace seqan;

        typedef unsigned int TCargo;
        typedef Graph<Directed<TCargo> > TGraph;
        typedef VertexDescriptor<TGraph>::Type TVertexDescriptor;

        TGraph g;

        TVertexDescriptor vertBerlin = addVertex(g);
        TVertexDescriptor vertHamburg = addVertex(g);

        addEdge(g, vertBerlin, vertHamburg, 289);

        return 0;
    }

Can you spot the error? This is what g++ 4.2 has to say about it:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    template_error.cpp: In function ‘int main(int, const char**)’:
    template_error.cpp:16: error: no matching function for call to ‘addEdge(main(int, const char**)::TGraph&, main::TVertexDescriptor&, main::TVertexDescriptor&, int)’

.. raw:: html

   </pre>

And this is what Clang++ 2.9 says about it (the actual output is
coloured with better readability). Do you spot the error now? The
solution is below the output.

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    sandbox/mysandbox/demos/template_error.cpp:16:5: error: no matching function for call to 'addEdge'
        addEdge(g, vertBerlin, vertHamburg, 289);
        ^<s>~</s>~
    In file included from sandbox/mysandbox/demos/template_error.cpp:1:
    In file included from core/include/seqan/graph_types.h:58:
    core/include/seqan/graph_types/graph_impl_directed.h:572:1: note: candidate function template not viable: requires 3 arguments, but 4 were
          provided
    addEdge(Graph&lt;Directed&lt;TCargo, TSpec> >& g,
    ^
    core/include/seqan/graph_types/graph_impl_directed.h:600:1: note: candidate template ignored: deduced conflicting types for parameter
          'TCargo' ('unsigned int' vs. 'int')
    addEdge(Graph&lt;Directed&lt;TCargo, TSpec> >& g,
    ^
    In file included from sandbox/mysandbox/demos/template_error.cpp:1:
    In file included from core/include/seqan/graph_types.h:59:
    core/include/seqan/graph_types/graph_impl_undirected.h:402:1: note: candidate function template not viable: requires 3 arguments, but 4
          were provided
    addEdge(Graph&lt;Undirected&lt;TCargo, TSpec> >& g,
    ^
    core/include/seqan/graph_types/graph_impl_undirected.h:438:1: note: candidate template ignored: failed template argument deduction
    addEdge(Graph&lt;Undirected&lt;TCargo, TSpec> >& g,
    ^
    In file included from sandbox/mysandbox/demos/template_error.cpp:1:
    In file included from core/include/seqan/graph_types.h:60:
    core/include/seqan/graph_types/graph_impl_automaton.h:407:1: note: candidate template ignored: failed template argument deduction
    addEdge(Graph&lt;Automaton&lt;TAlphabet, TCargo, TSpec> >& g,
    ^
    core/include/seqan/graph_types/graph_impl_automaton.h:428:1: note: candidate function template not viable: requires 5 arguments, but 4 were
          provided
    addEdge(Graph&lt;Automaton&lt;TAlphabet, TCargo, TSpec> >& g,
    ^
    In file included from sandbox/mysandbox/demos/template_error.cpp:1:
    In file included from core/include/seqan/graph_types.h:61:
    core/include/seqan/graph_types/graph_impl_wordgraph.h:110:1: note: candidate template ignored: failed template argument deduction
    addEdge(Graph&lt;Automaton&lt;TAlphabet, String&lt;TAlphabet>, WordGraph&lt;TSpec> > >& g,
    ^
    core/include/seqan/graph_types/graph_impl_wordgraph.h:137:1: note: candidate template ignored: failed template argument deduction
    addEdge(Graph&lt;Automaton&lt;TAlphabet, String&lt;TAlphabet>, WordGraph&lt;TSpec> > >& g,
    ^
    core/include/seqan/graph_types/graph_impl_wordgraph.h:150:1: note: candidate function template not viable: requires 5 arguments, but 4 were
          provided
    addEdge(Graph&lt;Automaton&lt;TAlphabet, String&lt;TAlphabet>, WordGraph&lt;TSpec> > >& /*g*/,
    ^
    In file included from sandbox/mysandbox/demos/template_error.cpp:1:
    In file included from core/include/seqan/graph_types.h:62:
    core/include/seqan/graph_types/graph_impl_tree.h:468:1: note: candidate function template not viable: requires 3 arguments, but 4 were
          provided
    addEdge(Graph&lt;Tree&lt;TCargo, TSpec> >& g,
    ^
    core/include/seqan/graph_types/graph_impl_tree.h:496:1: note: candidate template ignored: failed template argument deduction
    addEdge(Graph&lt;Tree&lt;TCargo, TSpec> >& g,
    ^
    In file included from sandbox/mysandbox/demos/template_error.cpp:1:
    In file included from core/include/seqan/graph_types.h:64:
    core/include/seqan/graph_types/graph_impl_hmm.h:406:1: note: candidate function template not viable: requires 3 arguments, but 4 were
          provided
    addEdge(Graph&lt;Hmm&lt;TAlphabet, TCargo, TSpec> >& g,
    ^
    core/include/seqan/graph_types/graph_impl_hmm.h:418:1: note: candidate template ignored: failed template argument deduction
    addEdge(Graph&lt;Hmm&lt;TAlphabet, TCargo, TSpec> >& g,
    ^
    1 error generated.

.. raw:: html

   </pre>

While the output is overly verbose, get the important clue that the
error is caused when deducing the type for the ``addEdge()`` function
template. The function itself exists, but none of the candidates has the
correct types. The problem is that we specify the cargo type as
``unsigned int`` in the definition of the graph but in the program, we
try to use ``int`` as the cargo. Corrected, we have to use an
``unsigned int`` literal ``289u`` instead of ``289`` in line 16:

::

    #cpp
        addEdge(g, vertBerlin, vertHamburg, 289u);

Run Time Errors
~~~~~~~~~~~~~~~

This section lists some useful tools for troubleshooting run time
errors.

Valgrind
^^^^^^^^

| ``Type ::``
| `` Memory checker and debugger.``
| ``Homepage ::``
| `` ``\ ```http://valgrind.org/`` <http://valgrind.org/>`__
| ``Operating Systems ::``
| `` Linux, Mac Os X (trunk version for recent Os X versions)``
| ``Costs ::``
| `` Free, GPL``

Valgrind is one of the most useful tools for debugging memory access
problems.

Libmemusage
^^^^^^^^^^^

| ``Type ::``
| `` Memory Usage Reporting``
| ``Homepage ::``
| `` ``\ ```http://www.faqs.org/docs/linux_scratch/appendixa/glibc.html`` <http://www.faqs.org/docs/linux_scratch/appendixa/glibc.html>`__
| ``Operating Systems ::``
| `` Linux (GNU libc required)``
| ``Costs ::``
| `` Free, GPL``

Automatically installed on all major Linux systems, libmemusage allows
to see information on memory allocation, e.g. the maximum amount of
allocated memory over the program's running time. It does so at a quite
low overhead.

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    $ LD_PRELOAD=libmemusage.so g++ --version
    g++ (Debian 4.4.5-8) 4.4.5
    Copyright (C) 2010 Free Software Foundation, Inc.
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.


    Memory usage summary: heap total: 22837, heap peak: 21038, stack peak: 5312
             total calls   total memory   failed calls
     malloc|         86          18909              0
    realloc|          4           3920              0  (nomove:1, dec:0, free:0)
     calloc|          1              8              0
       free|         46           1852
    Histogram for block sizes:
        0-15             24  26% ==================================================
       16-31              3   3% ======
       32-47             16  17% =================================
       48-63             19  20% =======================================
       64-79              4   4% ========
       80-95              3   3% ======
       96-111             3   3% ======
      112-127             3   3% ======
      160-175             2   2% ====
      176-191             1   1% ==
      192-207             1   1% ==
      208-223             1   1% ==
      272-287             1   1% ==
      432-447             1   1% ==
      560-575             1   1% ==
      768-783             1   1% ==
      944-959             1   1% ==
     1024-1039            1   1% ==
     1600-1615            1   1% ==
     2048-2063            1   1% ==
     4064-4079            3   3% ======

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
