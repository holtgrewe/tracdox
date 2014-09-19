Assignment 1
------------

Task
~~~~

Become acquainted with online search algorithms for multiple sequences
and search "Simon, send more money!" simultaneously for "mo", "send",
"more". For every match output the begin and end position in the
haystack and which needle has been found.

Solution
~~~~~~~~

Online search algorithms for multiple sequences expect needles of type
``String<String<...> >``. We choose a seqan:Class.String of
seqan:Shortcut.CharString and append the 3 needles via
seqan:Function.appendValue. Please note that we have to use
seqan:Function.appendValue and not seqan:Function.append as a single
needle is a string and not a string of strings.
.. includefrags:: core/demos/tutorial/find/find_assignment1.cpp
   :fragment: initialization

We use a seqan:Class.Pattern specialized with the seqan:Spec.WuManber
algorithm for the search and initialize it with our needles string. For
every match found by seqan:Function.find we output the begin and end
position and the match region in the haystack as well as the index of
the found needle which is returned by ``position(pattern)``.
.. includefrags:: core/demos/tutorial/find/find_assignment1.cpp
   :fragment: output

Program output:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    [2,4)   0   mo
    [7,11)  1   send
    [12,14) 0   mo
    [12,16) 2   more
    [17,19) 0   mo

.. raw:: html

   </pre>

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
