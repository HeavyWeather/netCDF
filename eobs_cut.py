def eobs_cut(PATH,LATS,LONS):

      """ allows for the subselection of a list of variables for a target region ('LATS','LONS') when given a path ('PATH') to an E-obs input file:
  
            www.ecad.eu/E-OBS/
  
            Specifies output files based on parameter selection:
  
            var+"uk_0.22deg_rot_v7.0.nc"
  
     """
  from nCDF_basics import *
	# First check that the environment we are working in is suitable.
	check_nco_available()
	check_cdo_available()

	varlist=['pp','rr','tx','tn','tg']
	for var in varlist:	
		infile=PATH+var+"_0.22deg_rot_v7.0.nc"
		outfile=var+"uk_0.22deg_rot_v7.0.nc"
		nco_hyperslab_latlon(LONS,LATS,infile,outfile)
