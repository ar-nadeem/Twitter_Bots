
import tweepy, time, sys, codecs, smtplib

print("C O D E By ReVoLuTioN")
print("\n")
time.sleep(2)

print("Logging in .... \n")
#######################################################################################################################################
CONSUMER_KEY = keys['c_k']
CONSUMER_SECRET = keys['c_s']
ACCESS_TOKEN = keys['a_t']
ACCESS_TOKEN_SECRET = keys['a_s']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
#######################################################################################################################################
print("Logged IN \n")
