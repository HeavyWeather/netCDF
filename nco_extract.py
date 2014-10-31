def nco_extract( var , infile , outfile ):
    """ extracts a given variable from one netCDF file ('infile') to another ('outfile')
    'var' is the name of the variable desired, as shown by ncdump -h """
    command = "ncks --overwrite --history"+\
              " --variable "+var+\
              " --output "+outfile+\
              " "+infile
    process_cmd(command)
