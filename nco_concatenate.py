def nco_concatenate(infilestr, outfile ):
    """ infilestr is given as a string of file names to concatenate to a given output ('outfile'), 
    works along the time dimension by default """
    command = "ncrcat --overwrite --history "+\
              infilestr+" "+outfile+""
    process_cmd(command) 
