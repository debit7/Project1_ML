import Hits 
import matplotlib.pyplot as plt
with open("project1-hits.txt") as f:
    array = f.read().splitlines()
    
    f.close()
dicts = {}
hits=[]
hour=[]
for items in array:
    hours=items.split(',')[0]
    views=items.split(',')[1]
    if views!="nan":
        hour.append(hours)
        hits.append(views)
        # dicts[hours] = int(views)
    
        # dicts[hours] = 0




plt.scatter(hour, hits)
plt.show()