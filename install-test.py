#!/usr/bin/env python

# This scripts tests an installation for all required and optional modules and
# packages for The Hacker Within Python Bootcamp 2010 ( aka thwpybc2010 ).
# http://hackerwithin.org/cgi-bin/hackerwithin.fcgi/wiki/PyBc

# To run it, issue
#   python ./install-test.py

# Matt McCormick <matt@mmmccormick.com>  created 26 November 2009

required_deps = [ ['IPython', '0.9' ],
        [ 'numpy', '1.2' ],
        [ 'matplotlib', '0.98' ],
        [ 'basemap', '0.98' ] ]

optional_deps = [ ['enthought.mayavi'] ]

def test_deps( deps ):
    """Test whether the given dependencies can be imported.

    deps:
        A nested list where each item contains a dependency.  Each dependency
        contains a list of the package/module name followed by a string giving the
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
            print "Error: Could not import", mod_name
            error.append( mod_name )
            continue

        try:
            mod_version = mod.__version__.split('.')
            requested_mod_version = dep[1].split('.')
            for i in range( len( requested_mod_version ) ):
                if int( mod_version[i] ) < int( requested_mod_version[i] ):
                    raise ImportError
        except ImportError:
            print "Error: Module", mod_name, "needs version",
            requested_mod_version, "but version", mod_version, "found"
            error.append( mod_name )
            continue
        except AttributeError:
# no .__version__
            pass

        print "Success: ", mod_name
        success.append( mod_name )

    return ( success, error )


print 'Testing installation for THW Python Bootcamp dependencies...'

required_success, required_error = test_deps( required_deps )

optional_success, optional_error = test_deps( optional_deps )

indent = '    '
print '\n\nSummary:'

print '\nRequired Dependencies:'
print indent, "Successful:", required_success
print indent, "Errors:", required_error
if( len( required_error ) > 0 ):
    print '\n', indent, 'Please see one of the instructors to help resolve all errors in \
the required dependencies'

print '\nOptional Dependencies:'
print indent, "Successful:", optional_success
print indent, "Errors:", optional_error
