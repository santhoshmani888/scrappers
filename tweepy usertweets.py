
# coding: utf-8

# In[59]:

import csv
import tweepy
from textblob import TextBlob
import datetime


# In[64]:

consumer_key = ""
consumer_secret = ""
access_token = ""
access_secret = ""


# In[65]:


auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api=tweepy.API(auth)


# In[66]:

csvFile=open('tweets.csv','a')


# In[67]:

csvWriter = csv.writer(csvFile)

# Add headers to our CSV file
headers = ['Date', 'Tweet', 'User', 'Link']

csvWriter.writerow(headers)

for tweet in tweepy.Cursor(api.search, 
                    q='@realDonaldTrump', 
                    show_user = True,
                    since= datetime.datetime.now().date(), 
                    include_entities=True).items():
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'), tweet.user.screen_name, "https://twitter.com/" + str(tweet.user.screen_name) + "/status/" + str(tweet.id)])
csvFile.close()


# In[ ]:




# In[ ]:




# In[ ]:



