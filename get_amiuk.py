def get_amiuk(indx):

	"""grabs all Agrometeorological Index (AMI) data for a single index ('indx'), and emplaces
	it into asingle python array. Horribly overspecified otherwise, might need config file or 
	some way of determining input dimensions."""
	
	from netCDF4 import Dataset
	import numpy as np
	import pylab
	runpath='/exports/work/geos_cxc/users/ahardin4/output/amibatch/'
	obspath='/exports/work/geos_cxc/users/ahardin4/Data/ami/'
	runs=['afgcx','afixa','afixc','afixh','afixi','afixj','afixk','afixl','afixm','afixo','afixq']
	amiuk=np.zeros((len(runs)+1,149,46,36)) #149,40,34
	obs=['e-obs']
	
	#indx='phs_count_plus'
	for run in range(0,len(runs)):
		path=runpath+runs[run]+'/ami.wide.'+runs[run]+'a.pe.1950.2098.nc'
		idata = Dataset(path, 'r', format='NETCDF3_CLASSIC')
		index=idata.variables[indx]
		print index.shape
		temp=index[:,0,:,:] #temp=index[:,0,:,:]
		amiuk[run,:,:,:]=temp
		
	#indx='phs_count'
	odata = Dataset(obspath+'ami.wide.e-obs.22degrot.v7.1950.2010.nc','r',format='NETCDF3_CLASSIC')
	index2=odata.variables[indx]
	temp2=index2[:,0,:,:] #index[0:61,0,:,:]
	#comment out last two lines and swap this for only modelled indices
	#will need some measurement of length in indexing alldat to ensure first period
	print temp2.shape
	for i in range(0,39): #0:39
		j=39-i
		amiuk[11,0:61,i,0:34]=temp2[0:61,j,0:34] #0:34
	datlats=idata.variables['lat']
	datlons=idata.variables['lon']
	return (amiuk,datlats,datlons)
