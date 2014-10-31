def check_cdo_available():
    """ simple command for cdo checking, with error reporting specific to the Eddie supercomputing cluster """
    import os,subprocess,sys
    try:
        subprocess.Popen(["cdo","-V"],stderr=subprocess.STDOUT,stdout=subprocess.PIPE).returncode
    except:
        print "ERROR: CDO could not be found."
        print "   This program cannot run without access to cdo."
        print "   See the wiki for information on how to add that module on"
        print "   Eddie but in short you can use: "
        print "                             module load geos/sciio-utils/1 "
        print "   Exiting."
        import sys
        sys.exit(1)
