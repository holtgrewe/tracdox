.. _build-manual:

Build Manual
------------

This manual contains information about building SeqAn applications both integrating SeqAn into your own build system and using the SeqAn build system.

Using the SeqAn Build System
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`build-manual-using-the-seqan-build-system`
  This article describes how to use the SeqAn build system for development and packaging.
  Using the SeqAn build system is the most convenient way of getting started.
  The SeqAn build system is also described in the Getting Started tutorial.

Integration with your own Build System
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`build-manual-integration-with-your-own-build-system`
  This article explains how to build your SeqAn application if you already have your own build system in place.
  Read this if you want to use plain Makefiles or Visual Studio projects.

FindSeqAn CMake Module
~~~~~~~~~~~~~~~~~~~~~~

:ref:`build-manual-using-the-find-seqan-cmake-module`

  If you want to roll your own CMake-based build system then you can use the FindSeqAn module for the easy integration of SeqAn in your project as any other library.

.. toctree::
   :hidden:
   :glob:
   :maxdepth: 2

   BuildManual/*
