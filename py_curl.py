"""py_curl.py: Script to implement a  curl command """

__author__      = "Fida Mohammad Thoker"
__copyright__   = "EIS"
import requests
import json
import sys

def py_curl(url,json_data):
	''' 
	function: Sends a get request to server 
	Arguments: url : url of the webservice
	           payload: query data to be sent with the get request
	Returns:  server response 
	'''
	data = {'data': json.dumps(json_data)}
	#send get request with payload data to the server
	try:
		r = requests.get(url, params=data)
	except Exception,e:
	# exception handling
    		print "Error in get request: %s"%e
    		sys.exit(1)
	# check the status code of server response
  	if r.status_code != 200:
	# error handling
    		print "HTTP ERROR code=: %s"%r.status_code
    		sys.exit(1)
  	else:
		# get the data recieved from server
    		ret_data = r.content
    		return ret_data

# get the payload data and server url from commandline 
if len(sys.argv)==1:
	# error handling
	print "Incorrect Program usage"
	print "Run the program using following format"
	print '''python get.py '{"query": "SELECT ?v4 WHERE { ?v4 ?v2 ?v6 ; ?v7 ?v3 . } ", "slots": [{"p": "is", "s": "v7", "o": "<http://lodqa.org/vocabulary/sort_of>"}, {"p": "is", "s": "v3", "o": "rdf:Class"}, {"p": "verbalization", "s": "v3", "o": "rivers"},{"p": "is", "s": "v2", "o": "rdf:Property"}, {"p": "verbalization", "s": "v2", "o": "flow"},{"p": "is", "s": "v6", "o": "rdf:Resource|rdfs:Literal"}, {"p": "verbalization", "s": "v6", "o": "Seoul"}], "score": "1.0", "question": "Which rivers flow through Seoul"}' http://121.254.173.77:2357/agdistis/run '''
	sys.exit(1)

else:
	payload = sys.argv[1]
	#load the payload into a json object
	json_object = json.loads(payload)
	# get url from commandline argument
	url = sys.argv[2]

ret_val = py_curl(url,json_object)
# print the response of server
print ret_val
