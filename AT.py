import tweepy, time, sys, codecs, smtplib, random
from keys import keys
print("C O D E By ReVoLuTioN")
print("\n")
time.sleep(2)

print("Logging in .... \n")
#######################################################################################################################################
CONSUMER_KEY = ('*')
CONSUMER_SECRET = '*'
ACCESS_KEY = '*-*'
ACCESS_SECRET = '*'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
#######################################################################################################################################
print("Logged IN \n")
nouns = ("CUTIE puppy", "Fast car", "Cute rabbit", "that girl", "this monkey", " .")
verbs = ("runs", "hits", "jumps", "drives", "barfs","Stares","Kills me","Laughs","Chats", "Follows me", "Loves me", ". ")
adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.", "Happly.", "Lovingly.", "Carefully.",". ")
adj = ("adorable", "clueless", "dirty", "odd", "stupid", "LMAO ", "LOL ", "SMH "," ")

num1 = random.randrange(0,5)
num2= random.randrange(0,11)
num3= random.randrange(0,8)
num4= random.randrange(0,8)
tweet= nouns[num1] + ' ' + verbs[num2] + ' ' + adv[num3] + ' ' + adj[num4]
print(tweet)
api.update_status(tweet)
time.sleep(600)
