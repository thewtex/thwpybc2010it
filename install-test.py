#!/usr/bin/env python

# This scripts tests an installation for all required and optional modules and
# packages for The Hacker Within Python Bootcamp 2010 ( aka thwpybc2010 ).
# http://hackerwithin.org/cgi-bin/hackerwithin.fcgi/wiki/PyBc

# To run it, issue
#   python ./install-test.py

# Matt McCormick <matt@mmmccormick.com>  created 26 November 2009

import sys


if( sys.version_info[0] >= 3 ):
    print 'Error: Python 2.X is suggested for THW Python 2010 Bootcamp. Python 3.X found.'
    sys.exit(1)
print 'Checking Python version...'
if( sys.version_info[0] < 2 or sys.version_info[1] < 5 ):
    print 'Error: Python 2.5 or greater required, Python', sys.version, ' found.'
    sys.exit(1)
print 'Success.\n'



print 'Checking for modules...'
required_deps = [ 
        [ 'IPython', '0.8' ],
        [ 'matplotlib', '0.98' ],
        [ 'numpy', '1.1.0' ],
        [ 'rpy2', '2.0.4' ],
        [ 'scipy', '0.6.0' ],
        ]

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
            print "FAILURE:     Could not import", mod_name
            error.append( mod_name )
            continue

        try:
            mod_version = mod.__version__.split('.')
            requested_mod_version = dep[1].split('.')
            for i in range( len( requested_mod_version ) ):
                if int( mod_version[i] ) < int( requested_mod_version[i] ):
                    raise ImportError
        except ImportError:
            print "FAILURE:     Module", mod_name, "needs version", requested_mod_version, "but version", mod_version, "found"
            error.append( mod_name )
            continue
        except AttributeError:
# no .__version__
            pass

        print "Success: ", mod_name
        success.append( mod_name )

    return ( success, error )


required_success, required_error = test_deps( required_deps )

print "\nChecking for Python IDLE IDE..."
idle_found = False
try:
    import idlelib
    print "IDLE found."
    idle_found = True
except ImportError:
    print "IDLE not found."


indent = '    '
print '\n\nSummary:'

print '\nRequired Dependencies:'
print indent, "Adequate version found:     ", required_success
print indent, "Adequate version not found: ", required_error
if( len( required_error ) > 0 ):
    print '\n', indent, 'Please see one of the instructors to help resolve all errors in \
the required dependencies'

print '\nText Editor:'
if idle_found:
    print indent, "IDLE IDE was found."
else:
    print indent, "IDLE IDE was not found."
print """A programmer's text editor is needed.  If you do not have a preferred editor,
the IDLE Python IDE comes with all python distributions and has a sufficient
text editor.

"""
