
import sys
import csv
import re
import numpy

def readValues(reader, columnIndices, regex, regexIndex, arrays, zeros = True):
	temp = [0, 0, 0]
	for row in reader:
		for i in range(len(columnIndices)):
			columnIndex = columnIndices[i]
			array = arrays[i]
			try:
				element = row[columnIndex]
				m = re.match(regex, element)
				num_matches = int(m.group(regexIndex))
				if zeros:
					array.append(num_matches)
				else:
					if num_matches != 0:
						array.append(num_matches)
					else:
						temp[i] = temp[i] + 1
			except Exception, e:
				continue
	print temp
	return arrays


def main(zeros):
	android_vs_chrome = []
	android_vs_chrome_mobile = []
	chrome_vs_chrome_mobile = []
	for i in range(1, len(sys.argv)):
		dir = sys.argv[i]
		path = dir + '/imageComparison.csv'
		#print path
		csvfile = open(dir + '/imageComparison.csv', 'rU')
		reader = csv.reader(csvfile)
		readValues(reader, [10, 11, 12], r"(\d+)( total matches)?", 1, [android_vs_chrome, android_vs_chrome_mobile, chrome_vs_chrome_mobile], zeros)
	print "android_vs_chrome length " + str(len(android_vs_chrome))
	print "android_vs_chrome_mobile length " + str(len(android_vs_chrome_mobile))
	print "chrome_vs_chrome_mobile length " + str(len(chrome_vs_chrome_mobile))
	print "------------------Android VS. Chrome----------------------"
	print "Mean: " + str(numpy.mean(android_vs_chrome))
	print "Median: " + str(numpy.median(android_vs_chrome))
	print "Variance: " + str(numpy.var(android_vs_chrome))
	print "Standard Deviation: " + str(numpy.std(android_vs_chrome))
	print "\n"
	print "------------------Android VS. Chrome Mobile----------------------"
	print "Mean: " + str(numpy.mean(android_vs_chrome_mobile))
	print "Median: " + str(numpy.median(android_vs_chrome_mobile))
	print "Variance: " + str(numpy.var(android_vs_chrome_mobile))
	print "Standard Deviation: " + str(numpy.std(android_vs_chrome_mobile))
	print "\n"
	print "------------------Chrome VS. Chrome Mobile----------------------"
	print "Mean: " + str(numpy.mean(chrome_vs_chrome_mobile))
	print "Median: " + str(numpy.median(chrome_vs_chrome_mobile))
	print "Variance: " + str(numpy.var(chrome_vs_chrome_mobile))
	print "Standard Deviation: " + str(numpy.std(chrome_vs_chrome_mobile))

print "Count 0's"
main(True)
print "\n"
print "Don't Count 0's"
main(False)