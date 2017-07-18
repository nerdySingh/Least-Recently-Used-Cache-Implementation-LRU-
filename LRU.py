import csv
l = []
marks = []
cache=[]
copy_cache = ['99', '95', '88', '82', '75', '70', '65', '60', '55', '50', '45', '40', '35', '30', '25', '20', '15', '10', '5', '100', '0']
cache_hit = []
cache_miss =[]
lru_counter = []
flag =[]

def addToCache(mark):
    if len(cache) == 0:
        cache.append(mark)
    if len(cache) >=1:
        search(mark)

def search(mark):
    for i in range(len(cache)):
        if cache[i] != mark:
            break
    cache.append(mark)

def sort(cache):
    for i in range(len(cache)):
        for j in range(len(cache)):
            if int(cache[i]) < int(cache[j]):
                temp = cache[i]
                cache[i] = cache[j]
                cache[j] = temp
    return cache

def searchInCache(copy_cache):
    #implementing binary search
    start = 0
    end = len(cache)-1
    found = False
    while start <= end and not found:
        mid = (start + end) // 2
        if cache[mid] == copy_cache:
            found = True
            cache_hit[mid]+=1
            lru_counter[mid]+=1
        else:
            if copy_cache < cache[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return found

def cacheReplacement(found,j):
    if found == False:
        for i in range(len(lru_counter)):
            if lru_counter[i]==0:
                #replace the item now
                cache[i] = copy_cache[j]
                lru_counter[i] +=1
                cache_miss[i]+=1
                break
            else:
                lru_counter[i]=0
            
    

def printRecord():
    print("Cache\t LRU_Counter\t Cache_Hit\t Cache_Miss\t ")
    for i in range(len(marks)):
        print(cache[i],"\t",lru_counter[i])

def lruImplementation(cache):
    cache = sort(cache)
    for i in range(len(cache)):
        found = searchInCache(copy_cache[i])
        flag.append(found)
        cacheReplacement(found,i)
    printRecord()


with open("lru.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")
    for row in readCSV:
        l.append(row)
for i in range(1,len(l)):
    marks.append(l[i][2])

for i in range(len(marks)):
    addToCache(marks[i])
    cache_hit.append(0)
    cache_miss.append(0)
    lru_counter.append(0)

    
lruImplementation(cache) 
