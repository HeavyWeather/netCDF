def check_nco_available():
    import subprocess,sys
    try:
        subprocess.Popen(['ncap','--version'],stderr=subprocess.STDOUT,stdout=subprocess.PIPE).returncode
    except:
        print "ERROR: NCO could not be found."
        print "   This program cannot run without access to the NCO toolbox"
        print "   See the wiki for information on how to add that module on"
        print "   Eddie but in short you can use: "
        print "                             module load geos/sciio-utils/1 "
        print "   Exiting."
        import sys
        sys.exit(1)
