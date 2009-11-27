#!/usr/bin/env python

# This scripts tests an installation for all required and optional modules and
# packages for The Hacker Within Python Bootcamp 2010 ( aka thwpybc2010 ).
# http://hackerwithin.org/cgi-bin/hackerwithin.fcgi/wiki/PyBc

# To run it, issue
#   python ./install-test.py

# Matt McCormick <matt@mmmccormick.com>  created 26 November 2009

required_deps = [ ['IPython', [0, 9] ],
        [ 'numpy', [1, 2] ],
        [ 'matplotlib', [0, 98] ],
        [ 'basemap', [0, 98] ] ]

#optional_deps = [ ['basemap'

def test_deps( deps ):
    """Test whether the given dependencies can be imported.

    deps:
        A nested list where each item contains a dependency.  Each dependency
        contains a list of the package/module name followed by a list giving the
        minimum required version.

    returns:
        A tuple where the first entry is a list of the successfully found
        modules and the second entry is a list of modules  where an error was
        found.
        """

    success = []
    error = []
    for dep in deps:
        mod_name = dep[0]

        try:
            mod = __import__( mod_name )
        except ImportError:
            print "Could not import ", mod_name
            error.append( mod_name )
            continue

        try:
            mod_version = mod.__version__.split('.')
            for i in range( len( dep[1] ) ):
                if int( mod_version[i] ) < dep[1][i]:
                    raise ImportError
        except ImportError:
            print "Module ", mod_name, " has too low of a version."
            error.append( mod_name )
            continue

        success.append( mod_name )

    return ( success, error )


success, error = test_deps( required_deps )

