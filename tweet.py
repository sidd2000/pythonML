#!/usr/bin/python3

import tweepy


# consumer keys and access tokens, used for OAuth
consumer_key = '02rSqnC65ivFJqRCB2G69ktwh'
consumer_secret = 'p1No1NFSDmN2zxovEr9wyxLuCWWkn2EKvGQMJ4nKWheEw5noKO'
access_token = '889506304225665024-jgmCLgzDB42gO90OfsQ5eqiUPZP1JPm'
access_token_secret = 'q8wJpvCc2M3SvowHTMtDrKXHJx7zjDrfX7cBLxrYypdpp'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# creation of the actual interface, using authentication
api = tweepy.API(auth)
#api.update_status('Test')


#!!!Get information about yourself!!!

user = api.me()

print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.friends_count))


#!!!Get information about any user!!!

user = api.get_user("@mparmar1997")

print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.friends_count))


#!!!Search tweet!!!

tweet=input("Enter whatever you wanna search here:  ")
search = tweepy.Cursor(api.search, q=tweet, lang="ne").items(30000)

#!!!Printing tweets!!!

for item in search:
    print (item)
    
