import tweetsold as to
import json

consumer_key = 'COETny0iHmAF2myVrHaszW9f6'
consumer_secret = 'PCj3wkUNUXgd5bkBEuPKjYwCjHkQASWzZZCnrIHIs4Vbg6zlkz'
access_token = '3063028566-B8MWMQt0X2SsBeI0yauXQJXlGJylqYIddXO928x'
access_secret = 'cAkr6oy6PUQyObH9jP5ax2jtPAIwEsOHHqMJA6rtdxKaB'


client = to.authentication(consumer_key, consumer_secret, access_token, access_secret)

tweets = to.get_tweets(client, ["ruby", "javascript"], "2017-12-03")

with open("test.json","w") as file:
    json.dump(tweets, file)










	
