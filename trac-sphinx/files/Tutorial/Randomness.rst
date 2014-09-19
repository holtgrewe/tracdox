Randomness
----------

TOC

| ``Learning Objective ::``
| `` In this tutorial, you will get a short walk-through of SeqAn's module ``\ ``random``\ ``.``
| `` The module contains code for generating random numbers in various distributions.``
| ``Difficulty ::``
| `` Basic``
| ``Duration ::``
| `` 10 min``
| ``Prerequisites ::``
| `` Tutorial Basics,``
| `` Tutorial Sequences``

This tutorial explains how to use the module ``random``. ``random``
primarily provides the two classes :dox:`Rng` (**R**\ andom
**N**\ umber **G**\ enerator) and :dox:`Pdf` (**P**\ robability
**D**\ ensity **F**\ unctions).

::

    #comment
    At the moment, SeqAn provides the <tt>Mersenne Twister</tt> pseudorandom number generator.
    You have to specialize :dox:`Rng` as :dox:`MersenneTwisterRng Mersenne Twister Rng` to access this random generator. The class :dox:`Pdf` is used to set probability distribution functions. These functions are available through a specialization of :dox:`Pdf`. There are three different probability distribution functions available: :dox:`LogNormalPdf Log-NormalPdf`, :dox:`NormalPdf Normal Pdf` and :dox:`UniformPdf Uniform Pdf`.

Random Number Generation
~~~~~~~~~~~~~~~~~~~~~~~~

Instances of the class :dox:`Rng` are responsible for random number
generation. Currently, SeqAn provides only one specialization, the
:dox:`MersenneTwisterRng`. This class is used for
generating random 32-bit numbers. These 32-bit numbers are then used by
the :dox:`Pdf` specializations to generate random numbers in certain
distributions as explained further below.

The full example can be found in the file
[source:trunk/core/demos/tutorial/random/random\_examples.cpp
random\_examples.cpp].

First, we include the header ``<seqan/random.h>`` to get access to the
module's functionality.

.. includefrags:: core/demos/tutorial/random/random_examples.cpp
   :fragment: header

During the initialization of the :dox:`Rng` object you have to pass a
seed used as a start point for the randomization. Finally, function
:dox:`Rng#pickRandomNumber pickRandomNumber` picks a random number from a
:dox:`Rng`.

.. includefrags:: core/demos/tutorial/random/random_examples.cpp
   :fragment: random-number-generation-raw

The output of this fragment is:

::

    #ShellBox
    pickRandomNumber(rng) == 1608637542

:dox:`MersenneTwisterRng Mersenne Twister Rng` generates 32-bit
``unsigned`` numbers. However, you should not rely on any specific type
and use :dox:`Value` metafunction instead.

.. includefrags:: core/demos/tutorial/random/random_examples.cpp
   :fragment: random-number-generation-metafunction-value

If you prefer a special distribution of the randomly generated numbers
you can use the above mentioned specializations of :dox:`Pdf`. SeqAn
currently provides normal, log-normal and uniform probability density
functions. Note, for uniform distributions the range of values is given
as a closed interval, i.e. the last value is enclosed in the range.

.. includefrags:: core/demos/tutorial/random/random_examples.cpp
   :fragment: random-number-generation-pdf

The output of this fragment is:

::

    #ShellBox
    pickRandomNumber(rng, uniformDouble) == 0.950714
    pickRandomNumber(rng, uniformInt) == 27
    pickRandomNumber(rng, normal) == 0.419823

Also note that you can initialize the :dox:`LogNormalPdf Log-Normal Pdf`
either with mean and standard deviation of the log-normal distribution
or the underlying normal distribution. By default, you initialize it
with the mean and standard deviation (mu and sigma) of the underlying
normal distribution. Use the tags [dox:LognormalConstruction#MuSigma
MuSigma] and :dox:`LognormalConstruction#MeanStdDev MeanStdDev` in the
constructor to select a mode.

.. includefrags:: core/demos/tutorial/random/random_examples.cpp
   :fragment: random-number-generation-log-normal

The output of this fragment is:

::

    #ShellBox
    pickRandomNumber(rng, logNormal) == 1.22431
    pickRandomNumber(rng, logNormal2) == 2.78004
    pickRandomNumber(rng, logNormal3) == 0.00155248

Shuffling
~~~~~~~~~

The function :dox:`shuffle` allows to shuffle a container, given
a random number generator:

.. includefrags:: core/demos/tutorial/random/random_examples.cpp
   :fragment: shuffling

The output of this fragment is:

::

    #ShellBox
    shuffle("Hello World!") == oreWlloHld

Submit a comment
~~~~~~~~~~~~~~~~

If you found a mistake, or have suggestions about an improvement of this
page press:
[/newticket?component=Documentation&description=Tutorial+Enhancement+for+page+http://trac.seqan.de/wiki/Tutorial/Randomness&type=enhancement
submit your comment].

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
