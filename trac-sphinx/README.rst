SeqAn Sphinx Documentation
==========================

Setup
-----

Get SeqAn

  # git clone git@github.com:seqan/seqan.git seqan-git
  # cd seqan-git
  # git checkout develop

Build dox documentation (we use the generated search index to check dox links).

  # cd dox ; ./dox_only.sh; cd ..
  # cd ..

Get tracdox

  # git clone git@github.com:holtgrewe/tracdox.git tracdox

(Install virtualenv package, this allows easy, local python installs)

Setup virtualenv

  # cd tracdox
  # virtualenv virtualenv
  # . virtualenv/bin/activate
  # pip install sphinx sphinx_rtd_theme sphinxcontrib-bibtex

Install seqansphinx package (in virtualenv because of `. virtualenv/bin/activate`.

  # pushd seqansphinx
  # python setup.py install
  # popd

Add link to seqan-git for includes

  # pushd trac-sphinx
  # ln -s $(pwd)/../../seqan-git seqan

Build documentation

  # make html
  # google-chrome build/html/index.html

Adding Tutorials
----------------

1. *move* over from files/ to source/directory, this gives a good overview of what is done
2. Include file in in `.. toctree::` in Tutorial.rst
3. Look into Tutorial.rst for link to this tutorial (:ref:`tutorial-link-name`)
4. Add link target at top of new file.
5. Call "make html" to update the Sphinx output and see what is broken ;)

Image files etc. can easiest be downloaded from Trac.

Article Formatting
------------------

Each article should start as follows:

::
    .. sidebar:: ToC

       .. contents::


    .. _link-name:

The ``link-name`` should contain the "path" to the document, e.g. the document
in ``Tutorial/Sequences`` has the link target ``tutorial-sequences`.

Format assignments as follows.

Assignment 1
^^^^^^^^^^^^

.. container:: assignment

   Type
     Review

   Objective
     In the following assignment, you will write a small function that builds the reverse complement of a given string.
     Copy the code below and add the following functionalities:

     #. Use the ``resize`` function to ``resize`` the ``revComplGenome`` variable.
     #. Using the ``getRevCompl`` function, get the reverse complement for every nucleotide ``genome`` and store it in reverse order ``revComplGenome``.
     #. Print out the original genome and the reverse complement.

     .. code-block:: cpp

        #include <seqan/sequence.h>
        #include <seqan/basic.h>
        #include <iostream>
        #include <seqan/file.h>
        #include <seqan/modifier.h>

        using namespace seqan;

        Dna getRevCompl(Dna const & nucleotide)
        {
            if (nucleotide == (Dna)'A')
                return (Dna)'T';
            if (nucleotide == (Dna)'T')
                return (Dna)'A';
            if (nucleotide == (Dna)'C')
                return (Dna)'G';
            return (Dna)'C';
        }

        int main()
        {
            DnaString genome = "TATATACGCGCGAGTCGT";
            DnaString revComplGenome;

            // Your code snippet

            // And to check if your output is correct,
            // use the given SeqAn function reverseComplement(),
            // which modifies the sequence in-place
            reverseComplement(genome);
            std::cout << genome << std::endl;
            return 0;
        }

   Hints
     Remember that the last element in ``genome`` is stored at position ``length(genome) - 1``.

   Solution
     Click *more...* to see the solution.

     .. container:: foldable

        .. code-block:: cpp

           #include <seqan/sequence.h>
           #include <seqan/basic.h>
           #include <iostream>
           #include <seqan/file.h>
           #include <seqan/modifier.h>

           using namespace seqan;

           Dna getRevCompl(Dna const & nucleotide)
           {
               if (nucleotide == (Dna)'A')
                   return (Dna)'T';
               if (nucleotide == (Dna)'T')
                   return (Dna)'A';
               if (nucleotide == (Dna)'C')
                   return (Dna)'G';
               return (Dna)'C';
           }

           int main()
           {
               DnaString genome = "TATATACGCGCGAGTCGT";
               DnaString revComplGenome;
               resize(revComplGenome, length(genome));

               for (unsigned i = 0; i < length(genome); ++i)
               {
                   revComplGenome[length(genome) - 1 - i] = getRevCompl(genome[i]);
               }

               std::cout << genome << std::endl;
               std::cout << revComplGenome << std::endl;
               reverseComplement(genome);
               std::cout << genome << std::endl;
               return 0;
           }
