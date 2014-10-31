def hadRM3_cut(startyr,nyrs,PATH,RUN,VAR,LATS,LONS):
  """ allows for the subselection of a given variable ('VAR') for given years ('startyr', 'nyrs'), 
  and a target region ('LATS','LONS') when given a path ('PATH') to a hadRM3 input file:
  
  badc.nerc.ac.uk/data/hadrm3-ppe-uk/
  
  Specifies output files based on parameter selection:
  
   "+RUN+"a.pe"+decades[decade]+years[(startyr+year)%10]+".nc"
  
  """
  
  
	import calendar, string
	from netCDF4 import Dataset
  	from nCDF_basics import *

	decades=string.ascii_letters
	years=string.digits
	months = []
	for i in range(1,13):
	     	months.append((calendar.month_abbr[i]))

	check_nco_available()
	check_cdo_available()
	yearlist=[]
	for year in range (0,nyrs):
		decade=(((startyr+year)%1900)-((startyr+year)%1900)%10)/10
		monthlist = []
		monthlist2 = []
		for i in range(0,12):
			month=i
			infile=PATH+RUN+"/ape/"+RUN+"a.pe"+decades[decade]+years[(startyr+year)%10]+string.lower(months[month])+".nc"
			nco_extract(VAR, infile, "mtemp"+months[month]+".nc")
			nco_hyperslab_latlon(LONS,LATS,"mtemp"+months[month]+".nc","mtemp2"+months[month]+".nc")
			monthlist.append(("mtemp"+months[month]+".nc"))
			monthlist2.append(("mtemp2"+months[month]+".nc"))
		nco_concatenate_time(" ".join(monthlist2), RUN+"a.pe"+decades[decade]+years[(startyr+year)%10]+".nc")
		yearlist.append((RUN+"a.pe"+decades[decade]+years[(startyr+year)%10]+".nc"))
		command="rm "+" ".join(monthlist2)+" "+" ".join(monthlist)
		process_cmd(command) 
		print "Annual file complete: "+RUN+"a.pe"+decades[decade]+years[(startyr+year)%10]+".nc"
	nco_concatenate_time(" ".join(yearlist), RUN+"a.pe."+str(startyr)+"."+str(startyr+nyrs-1)+".nc")
	command="rm "+" ".join(yearlist)+" "
	process_cmd(command) 
	
