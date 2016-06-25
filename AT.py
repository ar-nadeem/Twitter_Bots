
import tweepy, time, sys, codecs, smtplib

print("C O D E By ReVoLuTioN")
print("\n")
time.sleep(2)

print("Logging in .... \n")
#######################################################################################################################################
CONSUMER_KEY = keys['CONSUMER_KEY']
CONSUMER_SECRET = keys['CONSUMER_SECRET']
ACCESS_TOKEN = keys['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = keys['ACCESS_TOKEN_SECRET']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
#######################################################################################################################################
print("Logged IN \n")
