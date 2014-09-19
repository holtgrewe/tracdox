How To: Automate Tests With CTest
---------------------------------

TOC

The dashboard lives at `the SeqAn CDash
site <http://www.seqan.de/cdash/index.php?project=SeqAn>`__.

For Linux and Mac OS X
~~~~~~~~~~~~~~~~~~~~~~

Create ``~/Nightly`` where everything will take place and check out the
trunk:

::

    cd ~
    mkdir Nightly
    cd Nightly
    svn co http://svn.seqan.de/seqan/trunk seqan-trunk

Now, get the build scripts:

::

    cp seqan-trunk/misc/ctest/run_nightly.sh .
    cp seqan-trunk/misc/ctest/Seqan_Nightly.cmake.example Seqan_Nightly.cmake
    cp seqan-trunk/util/cmake/CTestConfig.cmake seqan-trunk/

Adjust the build name and site name in ``Seqan_Nightly.cmake``. Now,
test the setup by running:

::

    chmod u+x run_nightly.sh
    ./run_nightly.sh

Add ``run_nightly.sh`` to your nightly *cron* jobs:

::

    crontab -e

Example crontab file:

::

    #min    hour    mday    month   wday    command
    05      1       *       *       *       sh -l ${HOME}/Nightly/run_nightly.sh > /dev/null

For Windows
~~~~~~~~~~~

Create ``Nightly`` in your home directory where everything will take
place and check out the trunk:

::

    cd /D %HOME%
    mkdir Nightly
    cd Nightly
    svn co http://svn.seqan.de/seqan/trunk seqan-trunk

Now, get the build scripts:

::

    copy seqan-trunk\misc\ctest\run_nightly.sh .
    copy seqan-trunk\misc\ctest\Seqan_Nightly.cmake.example Seqan_Nightly.cmake
    copy seqan-trunk\util\cmake\CTestConfig.cmake seqan-trunk\

Adjust the build name and site name in ``Seqan_Nightly.cmake``. Now,
test the setup by running:

::

    run_nightly.bat

Add ``run_nightly.bat`` to nightly Scheduled Tasks of Windows
(analogously to the `CTest
Tutorial <http://www.vtk.org/Wiki/CMake_Scripting_Of_CTest#On_Windows_.2F_Cygwin_.2F_MinGW>`__):

#.

   #. Open "Scheduled Tasks" from Control Panel.

| ``  2. Select Add Scheduled Task``
| ``  3. Select Next to select command.``
| ``  4. Click Browse... and select ``\ ``run_nightly.bat``\ ``.``
| ``  5. Click Next and select name and repetition date. Repetition date for Nightly dashboards should be Daily.``
| ``  6. Click Next and select time to start the dashboard.``
| ``  7. Click Next and select Open advanced properties... to fine tune the scheduled task.``
| ``  8. Select Next and type password of the user.``
| ``  9. Task is created. The Advanced Properties dialog should open.``
| ``  10. In advanced properties, specify full command name. This is very important that you use double quotes in case you have space in your path.``
| ``  11. Select 'Ok, which will ask for password again.``
| ``  12. The new task should be created.``

Sparse Checkouts
~~~~~~~~~~~~~~~~

This is only necessary/interesting if you are a developer with read
permissions to more than *core*, *extras*, and your own sandbox. You can
checkout only a subset of the directories in the repository using a
Subversion feature called *sparse directories.*

Also consult the `Subversion reference on sparse
checkouts <http://svnbook.red-bean.com/en/1.5/svn.advanced.sparsedirs.html>`__.

::

    #sh
    svn co --depth immediates https://svn.seqan.de/seqan/trunk seqan-trunk-sparse
    cd seqan-trunk-sparse
    svn update --set-depth infinity build core docs extras misc util
    svn update --set-depth files sandbox

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
