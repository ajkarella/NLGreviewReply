import pandas as pd
import bs4 as bs
import urllib.request
import pickle
from threading import Thread

def replyExtractor(busID):
    source = urllib.request.urlopen('https://www.yelp.com/biz/' + busID).read()
    soup = bs.BeautifulSoup(source, 'html')
    comments = soup.find_all("div", class_="review__373c0__13kpL border-color--default__373c0__2oFDT")

    repliedReviews = []
    for i in comments:
        blocks = i.find_all("div",
                            class_="block-quote__373c0__1C5O7 padding-l3__373c0__1scQ0 border-color--default__373c0__2oFDT")
        for i2 in blocks:
            if i2.text[0:26] == "Business owner information":
                repliedReviews.append((i.text, i2.text))
    return repliedReviews

with open("businessIDs.txt", "rb") as fp:
    c = pickle.load(fp)

businessWithReplies = []
def threadedWork(start,finish):
    j = 0
    for i in c[start:finish]:
        try:
            print(str(j) + "/" + str(len(c[start:finish])))
            info = replyExtractor(i)
            businessWithReplies.append(info)
            j = j + 1
        except:
            print("ConnectionResetError: whoopsie")

# this was making too many visits to the site at once
#for i in range(19):
#    Thread(target=threadedWork, args=(i*10000,(i*10000)+10000)).start()

threadedWork(3100,5100)


with open("comments.txt", "wb") as fp:   #Pickling
    pickle.dump(businessWithReplies, fp)