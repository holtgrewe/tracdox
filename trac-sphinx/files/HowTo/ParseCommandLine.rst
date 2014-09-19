How To: Parsing Command Line Parameters
---------------------------------------

::

    #WarningBox
    '''''DEPRECATED''''': SeqAn has a new module for parsing the command line, arg_parse.

    See [[Tutorial/ParsingCommandLineArguments| the Parsing Command Line Arguments tutorial]].

::

    #FoldOut
    Click ''more...'' to see the old, deprecated documentation.
    ----
    The CommandLineParser should give everyone the possibility to rapidly develop tools with SeqAn without the hassle of always having to write his own parser for the command line arguments. The proposed interface is only a first draft and it definitely needs some refurbishment but it already makes command line parsing much easier. For the way how it is used see the small code example below.

    === Some details ===

    The parser supports two names for the options. One single char name (e.g. <tt>h</tt> for <tt>-h</tt>) and a long name (e.g. <tt>help</tt> for <tt>--help</tt>). Values can be passed by either leaving a space between option and value (e.g. <tt>-i 5</tt>) or an equality sign between the option and the value (e.g. <tt>--int=5</tt>, note that this only works with the long option name).

    Boolean options can also be concatenated in the short form (e.g. <tt>-a -b -c</tt> is the same as <tt>-abc</tt>).

    === TODO and future plans ===

    ''(Please leave a short note here if you have requests, hints or suggestions) ''

    *support multiple option values (currently <tt>-a 5 -a 6</tt> will overwrite the fist value and you will only see the second one)
    *support some more formating options for the help output
    *support options concatenated with their -fVALUE should be the same as -f VALUE
    *store/return error code (invalid argument, invalid option, etc.)
    *support named arguments (e.g. <ARG1> -> <INPUT FILE>)

    === A small example ===

    We first initialize the parser simply by constructing it with the application name as parameter (if it is not passed the parser will try to determine it during parsing). Note that the help option is added by default.

    [[Include(source:trunk/core/demos/howto/cmdparser_example.cpp, fragment=headers)]]

    We then add the different options our program supports by passing seqan:Class.CommandLineOption objects to the seqan:Function.addOption method.
    The seqan:Class.CommandLineOption constructor parameters are:

     shortName ::
       The short option name (e.g. -h for the help option). If your option should not have a short name pass the empty string <tt>""</tt>.
     longName ::
       The long name of the option (e.g. --help for the help option). If your option does not support a long name, pass the empty string <tt>""</tt>.
     argumentsPerOption ::
       For options that take more than 1 argument, this parameter defines the number of arguments per option.
     helpText ::
       A description of the option which is later displayed when the user passes <tt>-h</tt> to your application.
     optionType ::
       The option type. A list of supported option types is shown below.
     defaultValue ::
       The default value of this option.

    '''Supported option types are:'''

    *<tt>OptionType::Double</tt> an option which takes a double as an argument.
    *<tt>OptionType::Int</tt> an option which takes an integer as an argument.
    *<tt>OptionType::String</tt> an option which takes a string/sequence as an argument.
    *<tt>OptionType::Boolean</tt> an option which works only as a boolean switch.
    *<tt>OptionType::Mandatory</tt> an option which has to be set by the user.
    *<tt>OptionType::Hidden</tt> an option which will be excluded from the help message (e.g. if you want options only for debugging).

    [[Include(source:trunk/core/demos/howto/cmdparser_example.cpp, fragment=cmdparser-options)]]

    We can also add some additional text to the help output.

    [[Include(source:trunk/core/demos/howto/cmdparser_example.cpp, fragment=cmdparser-add-lines)]]

    More specific, we can add a title using seqan:Function.addTitleLine and a usage line using seqan:Function.addUsageLine.

    [[Include(source:trunk/core/demos/howto/cmdparser_example.cpp, fragment=cmdparser-header)]]

    And we can tell the parser that we definitely need one (or more) non optional arguments.

    [[Include(source:trunk/core/demos/howto/cmdparser_example.cpp, fragment=cmdparser-arguments)]]

    We then parse the command line using the <tt>parse</tt> method. The parser will return <tt>false</tt> if there are any problems with the user output. It will also print some hints to the passed stream (e.g. <tt>std::cerr</tt>).

    [[Include(source:trunk/core/demos/howto/cmdparser_example.cpp, fragment=cmdparser-parse)]]

    The option values and arguments passed by the user are determined using the seqan:Function.getOptionValueShort and seqan:Function.getOptionValueLong methods depending on whether you specify the short or long option name.

    [[Include(source:trunk/core/demos/howto/cmdparser_example.cpp, fragment=cmdparser-get-values)]]

    Finally, exit the program.

    [[Include(source:trunk/core/demos/howto/cmdparser_example.cpp, fragment=main-end)]]

.. raw:: mediawiki

   {{TracNotice|{{PAGENAME}}}}
