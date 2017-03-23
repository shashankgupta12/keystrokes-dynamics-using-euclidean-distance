import statistics
from calculatetimings import calculateLatencyTime, calculateInterkeyTime
import json
import matplotlib.pyplot as plt

all_latencyTime = []
all_interkeyTime = []

def produceMasterProfile():
	with open('data.json', 'r') as f:
		data = json.load(f)
	for timings in data:
		lt = calculateLatencyTime(timings['keyPressData'], timings['keyReleaseData'])
		ikt = calculateInterkeyTime(timings['keyPressData'], timings['keyReleaseData'])
		all_latencyTime.append(lt)
		all_interkeyTime.append(ikt)

	master_latencyTime = [statistics.mean(time) for time in zip(*all_latencyTime)]
	master_interkeyTime = [statistics.mean(time) for time in zip(*all_interkeyTime)]
	# print(master_latencyTime)
	# print(master_interkeyTime)
	plt.figure(1)
	plt.plot(master_latencyTime, master_interkeyTime)
	# plt.show()
	return (master_latencyTime, master_interkeyTime)

def calculateTrajectoryDissimilarities():
	dissimilarityValues = []
	master_latencyTime, master_interkeyTime = produceMasterProfile()
	for lt, ikt in zip(all_latencyTime, all_interkeyTime):
		euclideanDistance = [((x1 - x2)**2 + (y1 - y2)**2)**(1/2) for x1, y1, x2, y2 in zip(master_latencyTime, master_interkeyTime, lt, ikt)]
		dissimilarityValues.append(sum(euclideanDistance))
		plt.figure(1)
		plt.plot(lt, ikt)

	plt.savefig("plot.png")
	return dissimilarityValues

def generateComparator():
	dissimilarityValues = calculateTrajectoryDissimilarities()
	# print(dissimilarityValues)
	mean = statistics.mean(dissimilarityValues)
	stdev = statistics.stdev(dissimilarityValues)
	SIGMA = 3.00
	# print(mean, stdev)
	return (mean + (SIGMA * stdev))

# print(generateComparator())
# print(calculateTrajectoryDissimilarities())