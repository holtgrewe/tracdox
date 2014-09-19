We want to have a generic version, similar to the function
``ExchangeFirstValues`` on the previous page. Hence we could define the
function as follows:
.. includefrags:: core/demos/tutorial/basics/swap.cpp
   :fragment: swap-declaration
The function is now quite generic allowing any container of type ``T``.
In addition we specify two positions that should be swapped (as integers
which is not really generic, but it suffices for the demo) an the length
of the swapped region. Now we can define a helper variable ``help``,
which can be of type ``T``.
.. includefrags:: core/demos/tutorial/basics/swap.cpp
   :fragment: swap-metafunction
and do the swapping
.. includefrags:: core/demos/tutorial/basics/swap.cpp
   :fragment: swap-work
Thats it. We can now test our generic swap function using for example a
``String`` of characters or a ``String`` of integers.
.. includefrags:: core/demos/tutorial/basics/swap.cpp
   :fragment: swap-apply

The whole program taken together looks as follows:
.. includefrags:: core/demos/tutorial/basics/swap.cpp
   :fragment: swap-headers
.. includefrags:: core/demos/tutorial/basics/swap.cpp
   :fragment: swap-declaration
.. includefrags:: core/demos/tutorial/basics/swap.cpp
   :fragment: swap-metafunction
.. includefrags:: core/demos/tutorial/basics/swap.cpp
   :fragment: swap-work
.. includefrags:: core/demos/tutorial/basics/swap.cpp
   :fragment: swap-main
.. includefrags:: core/demos/tutorial/basics/swap.cpp
   :fragment: swap-apply

The output of the program is:

::

    #html
    <pre class="wiki" style="background-color:black;color:lightgray">
     darwin10.0 : ./demos/tutorial_swap
    ATTAAATT
    133111311333

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
