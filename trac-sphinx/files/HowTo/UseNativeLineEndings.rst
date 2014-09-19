How To: Use Native Line Endings
-------------------------------

In order to minimize conflicts, we have assigned the Subversion property
*svn:eol-style* to all text files in the SeqAn repository. If you are a
SeqAn developer, you should set this property for all new text files
(including source files).

Subversion can do this automatically for you. Add the contents of the
file [source:trunk/misc/svn-eol-style.txt misc/svn-eol-style.txt] to
your Subversion configuration file. Usually, these files are located in
*~/.subversion/config* or *C:\\Documents and
Settings\\{username}\\Application Data\\Subversion\\config*.

More information can be found in the `Chapter "Advanced Topics" in the
Subversion Manual <http://svnbook.red-bean.com/en/1.1/ch07s02.html>`__.

Copy And Paste Me
~~~~~~~~~~~~~~~~~

For your copy-and-paste convenience, you can also find this file's
contents below.

Include(source:/trunk/misc/svn-eol-style.txt)

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
