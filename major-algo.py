import pymongo
import statistics
import numpy

def databaseConnect():
	try:
		conn = pymongo.MongoClient()
		db = conn["database_name"]
		for collection in db.collection_names():
			if collection == "system.indexes":
				continue
			else:
				masterprofile = []
				userprofile= []
				keys = list(collection)
				for index in range(len(keys) - 1):
					documents = collection.find({"sourceKey":keys[index],"targetKey":keys[index+1]})
					flightTime = []
					dwellTime = []
					latencyTime = []
					dic1 = {}
					dic2 = {}
					for document in documents:
						flightTime.append(docuument["calculations"]["fightTime"])
						dwellTime.append(docuument["calculations"]["dwellTime"])
						latencyTime.append(docuument["calculations"]["latencyTime"])
						for index,item in enumerate(dwellTime):
							dwellTime[index] = item/1000
						for index,item in enumerate(latencyTime):
							latencyTime[index] = item/1000
					dic1["dwell"] = statistics.mean(dwellTime)
					dic1["latency"] = statistics.mean(latencyTime)
					masterprofile.append(dic1)
					dic2["keyCombination"] = "{0}{1}".format(keys[index],keys[index+1])
					dic2["dwell"] = dwellTime
					dic2["latency"] = latencyTime
					userprofile.append(dic2)

				for index in range(len(keys) - 1):
					dissmilarity_list = []	
					masterDwell = masterprofile[index]["dwell"]
					masterLatency = masterprofile[index]["latency"]
					a = numpy.array(masterDwell,masterLatency)
					for i in range(len(userprofile[index]["dwell"])):
						dw = userprofile[index]["dwell"][i]
						la = userprofile[index]["latency"][i]
						b = numpy.array(dw,la)
						dist = numpy.linalg.norm(a - b)
						dissmilarity_list.append(dist)
					sum(dissmilarity_list)



					documents = collection.find({"sourceKey":keys[index],"targetKey":keys[index+1]})
					dissmilarity_list = []
					for docuument in documents:
						# key = "{0}{1}".format(keys[index],keys[index+1])

					dissmilarity = sum(dissmilarity_list)



	


	except pymongo.errors.ConnectionFailure, e:
		error_text = "Error: {0}".format(e)
		print(error_text)






for json_file_name in open("filelist.txt"):
	with open(json_file_name) as json_data:
		data = json.load(data_file)
		# append data to each of the list above for 20 users




import json
from pprint import pprint
# import statistics

with open('data.json') as data_file:    
    data = json.load(data_file)

# pprint(data)

print(data)

# for time in data:
# 	key_hold_time.append(time/1000)

# for time in data:
# 	interkey_time.append(time/1000)

# statistics.stdev()
# statistics.mean()
# let selected features be X and Y