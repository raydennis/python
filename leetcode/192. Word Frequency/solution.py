from operator import itemgetter

with open('words.txt', 'r') as myfile:
    data=myfile.read().replace('\n', ' ')
    dataList = data.split()
    dataSetCount = [[x,dataList.count(x)] for x in set(dataList)]
    dataListCount = list(dataSetCount)
    sortedList = sorted(dataListCount, key=lambda x: int(x[1]), reverse=True)

print(sortedList)

