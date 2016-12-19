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
					# dic2["keyCombination"] = "{0}{1}".format(keys[index],keys[index+1])
					dic2["dwell"] = dwellTime
					dic2["latency"] = latencyTime
					userprofile.append(dic2)

				dissimilarity = []
				for i in range(len(userprofile[index]["dwell"])):
					#the above loop keeps in mind that there is only one richa 
					#type word typed in the training data as in there is only one
					#word where 'i' follows 'r', 'c' follows 'i', and so on 
					for index in range(len(keys) - 1):
						dissimilarity_list = []	
						masterDwell = masterprofile[index]["dwell"]
						masterLatency = masterprofile[index]["latency"]
						a = numpy.array(masterDwell,masterLatency)
						dw = userprofile[index]["dwell"][i]
						la = userprofile[index]["latency"][i]
						b = numpy.array(dw,la)
						dist = numpy.linalg.norm(a - b)
						dissimilarity_list.append(dist)
					dissimilarity.append(sum(dissimilarity_list))

				stdev_dissimilarity = statistics.stdev()
				mean_dissimilarity = statistics.mean()
				SIGMA = 3.00
				comparator = mean_dissimilarity + (SIGMA * stdev_dissimilarity)

	except pymongo.errors.ConnectionFailure, e:
		error_text = "Error: {0}".format(e)
		print(error_text)