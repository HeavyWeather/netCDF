def nco_hyperslab_latlon( str1 , str2 , infile , outfile ):
    """ to hyperslab an E-obs or HadRM3 file ('infile') in longitude and latitude
     str1: 'longitude, xx.xx, xx.xx' 
     str2: 'latitude, xx.xx, xx.xx' 
     to a specified output ('outfile') """
    command = "ncks --overwrite --history"+\
              " --dimension "+str1+\
	      " --dimension "+str2+\
              " --output "+outfile+\
              " "+infile
    process_cmd(command)  
