from pandas import DataFrame

class Params:
	"""
	Parameters class.

	This file centralizes anything that can be 
	parametrized in the code.
	"""

	raw_data = '../data/raw/'
	external_data = '../data/external/'
	processed_data = '../data/processed/'
	intermediate_data = '../data/intermediate/'

	log_name = '../log/dump.log'

	# if this is set to True, then all the nodes will be automatically 
	# considered not up-to-date and will be rerun.
	rerun = True 

	## Database connection params
	user = 'postgres'
	password = 'xxx'
	host = 'localhost'
	database = 'xxx'