import pymongo
from pymongo import MongoClient
from training import produceComparator
# import training
import statistics
import ctypes
from tkMessageBox import *

comp = produceComparator()
comparator = comp[len(comp) - 1]
masterprofile = comp[:-1]

def verifyUser():
	try:
		client = MongoClient('localhost', 27017)
		db = client.pressKeyData
		#change database name here
		print "Database name: {0}".format(db)
		collection = db.users
		#change collection name here if required
		print "Collection name: {0}".format(collection)
		userprofile = []
		dic = {}
		keys = list("rana happy")
		# print keys
		for index in list(range(10))[::2]:
			'''check indexing range here'''
			document = collection.find_one({"sourceKey":keys[index],"targetKey":keys[index+1]})
			flightTime = 
			dwellTime = 
			latencyTime = 
			dwellTime /= 1000.0
			latencyTime /= 1000.0
			print latencyTime
			print dwellTime
			dic["dwell"] = dwellTime
			dic["latency"] = latencyTime
			userprofile.append(dic)

		print userprofile
		dissimilarity_list = []
		for dic1,dic2 in zip(userprofile,masterprofile):
			dw = dic1["dwell"]
			la = dic1["latency"]
			md = dic2["dwell"]
			ml = dic2["latency"]
			dist = ((((md - dw)**2) + ((ml - la)**2))**(1/2))
			print dist
			dissimilarity_list.append(dist)
		print dissimilarity_list
		dissimilarity = sum(dissimilarity_list)
		print dissimilarity
		authentication_value = 0 if dissimilarity > comparator else 1
		print authentication_value
		if authentication_value == 1:
			showerror("User Authentication", "Legitimate User")
		elif authentication_value == 0:
			showerror("User Authentication", "Fake User")

	except pymongo.errors.ConnectionFailure, e:
		error_text = "Error: {0}".format(e)
		print(error_text)

verifyUser()