Task 2: Allocators
------------------

Task
~~~~

Write a program which compares the runtimes of the seqan:"Spec.Simple
Allocator" and the seqan:"Spec.Multi Pool Allocator" for pool sizes
(10,100,1000) for allocating and deallocating memory.

Solution
~~~~~~~~

We start in this assignment by including the ``basic.h`` SeqAn header
and defining two different allocators, one seqan:"Spec.Multi Pool
Allocator" and one seqan:"Spec.Simple Allocator".
.. includefrags:: core/demos/tutorial/basics/allocator.cpp
   :fragment: definitions

Given these fixed allocators we allocate now various size blocks, namely
of size 10, 100, and 1000. We repeat the allocation a number of times
and then clear the allocated memory. For each of the block sizes we
output the system time needed to allocate and clear the memory.
.. includefrags:: core/demos/tutorial/basics/allocator.cpp
   :fragment: time-measurements

Running this program results in the following output which shows the
advantage of the seqan:"Spec.Multi Pool Allocator":

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
    Knut-Reinert-MacBook-Air reinert ~/seqan/projects/library/demos/tutorial
     darwin10.0 : basics/allocator
    Allocating and clearing 100000 times blocks of size 10 with MultiPool Allocator took 0.00200295
    Allocating and clearing 100000 times blocks of size 10 with Standard Allocator took 0.0451179
    Allocating and clearing 100000 times blocks of size 100 with MultiPool Allocator took 0.0599239
    Allocating and clearing 100000 times blocks of size 100 with Standard Allocator took 0.127033
    Allocating and clearing 100000 times blocks of size 1000 with MultiPool Allocator took 0.368732
    Allocating and clearing 100000 times blocks of size 1000 with Standard Allocator took 0.560434

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
