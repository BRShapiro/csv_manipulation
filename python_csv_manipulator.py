import csv

from collections import Counter


def bestDirectors(TR, TC): #returns most frequent key pairings
    
    directors = []
    
    shared_items = set(TR.keys()) & set(TC.keys()) #finds matching keys from dicts
    
    for line in TR.keys():
        for line2 in shared_items:
            if(line == line2):
                directors.append(castDict.get(line))  
    
    allDirectors = [''.join(x) for x in directors] #converts a list of lists to a list of strings
    
    counter = Counter(allDirectors) #analyzes the list data
    top_five = counter.most_common(5)
    
    print(top_five)
    

def bestActors(TR,FC):
    
    shared_items = set(TR.keys()) & set(FC.keys()) #finds matching keys from dicts

    #print(shared_items)
    actors = []
    
    for line in TR.keys():
        for line2 in shared_items:
            if(line == line2):
                actors.append(FC.get(line))  
            
            
    flattenList = [i for sublist in actors for i in sublist] #parses list
    
    counter = Counter(flattenList) #analyzes the list data
    top_five = counter.most_common(5)
    
    print(top_five)

def topPaidActors(TG,FC):

    shared_items = set(TG.keys()) & set(FC.keys()) #finds matching keys from dicts

    #print(shared_items)
    actors = []
    paid = []
    temp = []
    
    
    for line in TG.keys():
        for line2 in shared_items:
            if(line == line2):
                paid.append(TG.get(line))
                actors.append(FC.get(line)) 
    
    totalPay = [float(''.join(x)) for x in paid]
    
    for line in totalPay:
        split = []
        split.append(16*line/31) 
        split.append(8*line/31)
        split.append(4*line/31)
        split.append(2*line/31)
        split.append(line/31)
        temp.append(split)
        
    actors = [i for sublist in actors for i in sublist] #parses list
    temp = [i for sublist in temp for i in sublist] #parses list
    
    
    actorpay = dict(zip(actors,temp))
    
    sum((Counter(d) for d in actorpay), Counter())
    total = Counter(actorpay)
    top_five = total.most_common(5)
    print(top_five)
        
        
#MAIN FUNCTION
       
    #rank, title, year, IMBd rating
csv_file = open('imdb-top-rated.csv','r')
csv_TR_read = csv.DictReader(csv_file)

    #rank, title, year, USA Box Office
csv_file = open('imdb-top-grossing.csv','r', encoding="utf8")
csv_TG_read = csv.reader(csv_file)
    
    #title, year, director, actor 1, 2, 3, 4, 5
csv_file = open('imdb-top-casts.csv','r', encoding="utf8") 
csv_TC_read = csv.reader(csv_file)

csv_file = open('imdb-top-casts.csv','r', encoding="utf8") 
csv_TC = csv.reader(csv_file)


castDict = {}
topDict = {}
grossDict = {}
fullCast = {}
actor = {}
director = {}
newDict = {}


for i, x in enumerate(csv_TR_read):
    topDict[(x['Title'], x['Year'])] = [x['IMDb Rating']]
    
for i, x in enumerate(csv_TG_read):
    grossDict[(x[1], x[2])] = [x[3]]

for i, x in enumerate(csv_TC_read):
    castDict[(x[0], x[1])] = [x[2]]
    
for i, x in enumerate(csv_TC):
    fullCast[(x[0], x[1])] = [x[3],x[4],x[5],x[6],x[7]]
    
    
    #function calls
    
print("Top 5 Directors with Best Ratings:")
bestDirectors(topDict, castDict)
print("\nTop 5 Directors Frequently Charting the USA Box Office:")
bestDirectors(topDict, grossDict)
print("\nTop 5 Actors in Top Rated Movies:")
bestActors(topDict, fullCast)
print("\nTop 5 Highest Paid Actors:")
topPaidActors(grossDict, fullCast) 
