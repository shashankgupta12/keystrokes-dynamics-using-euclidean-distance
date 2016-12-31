import pymongo
from pymongo import MongoClient
import statistics
# import matplotlib.pyplot as plt

def produceComparator():
	try:
		client = MongoClient('localhost', 27017)
		db = client.pressKeyData
		print "Database name: {0}".format(db)
		collection = db.users
		print "Collection name: {0}".format(collection)
		masterprofile = []
		userprofile= []
		keys = list("rana happy")
		print keys
		for index in list(range(10))[::2]:
			'''check indexing range here'''
			print keys[index]
			print keys[index+1]
			documents = collection.find({"sourceKey":keys[index],"targetKey":keys[index+1]})
			# mongoDB returns an iterable
			# print len(list(documents))
			flightTime = []
			dwellTime = []
			latencyTime = []
			dic1 = {}
			dic2 = {}
			for document in documents:
				flightTime.append(document["calculations"]["flightTime"])
				dwellTime.append(document["calculations"]["dwellTime"])
				latencyTime.append(document["calculations"]["latencyTime"])
			print flightTime
			print dwellTime
			print latencyTime
			for index,item in enumerate(dwellTime):
					dwellTime[index] = item/1000.0
			for index,item in enumerate(latencyTime):
					latencyTime[index] = item/1000.0
			print dwellTime
			print latencyTime
			dic1["dwell"] = statistics.mean(dwellTime)
			dic1["latency"] = statistics.mean(latencyTime)
			masterprofile.append(dic1)
			# dic2["keyCombination"] = "{0}{1}".format(keys[index],keys[index+1])
			dic2["dwell"] = dwellTime
			dic2["latency"] = latencyTime
			userprofile.append(dic2)

		dissimilarity = []
		major_dwell = []
		major_latency = []
		for dic in masterprofile:
			major_dwell.append(dic["dwell"])
			major_latency.append(dic["latency"])
		# plt.figure(1)
		# plt.plot(major_dwell,major_latency)
		print masterprofile
		print userprofile
		# for i in range(len(userprofile[0]["dwell"])):
		for i in range(9):
			'''check what range to take here'''
			#the above loop keeps in mind that there is only one richa 
			#type word typed in the training data as in there is only one
			#word where 'i' follows 'r', 'c' follows 'i', and so on 
			user_dwell = []
			user_latency = []
			for index in list(range(5)):
				'''check what range to take here'''
				dissimilarity_list = []	
				masterDwell = masterprofile[index]["dwell"]
				# print masterDwell
				masterLatency = masterprofile[index]["latency"]
				# print masterLatency
				md = masterDwell
				ml = masterLatency
				# print md
				# print ml
				dw = userprofile[index]["dwell"][i]
				la = userprofile[index]["latency"][i]
				# print dw
				# print la
				user_dwell.append(dw)
				user_latency.append(la)
				# a = numpy.array(md,ml)
				# b = numpy.array(dw,la)
				dist = ((((md - dw)**2) + ((ml - la)**2))**(1/2))
				# dist = numpy.linalg.norm(a - b)
				print dist
				dissimilarity_list.append(dist)
			dissimilarity.append(sum(dissimilarity_list))
			print dissimilarity
		# 	plt.figure(1)
		# 	plt.plot(user_dwell,user_latency)
		
		# plt.show()	
		stdev_dissimilarity = statistics.stdev(dissimilarity)
		mean_dissimilarity = statistics.mean(dissimilarity)
		SIGMA = 3.00
		comparator = mean_dissimilarity + (SIGMA * stdev_dissimilarity)
		print(comparator)
		masterprofile.append(comparator)
		return masterprofile

	except pymongo.errors.ConnectionFailure, e:
		error_text = "Error: {0}".format(e)
		print(error_text)

print produceComparator()