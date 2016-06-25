# _*_ coding:utf-8 _*_
#Twitter Re-Tweeter Bot
import tweepy, time, sys, codecs, smtplib
# argfile = str(sys.argv[1])
###############################################################
fromaddr = 'arnad33m@gmail.com'
toaddrs  = 'xspidera777@gmail.com'
username = 'arnad33m@gmail.com'
password = '1234Qwerasdfzxc'
server = smtplib.SMTP('smtp.gmail.com:587')
msg = "\r\n".join([
		   "From: arnad33m@gmail.com",
		   "To: xspidera777@gmail.com",
		   "Subject: TwitterBOT ",
		   "",
		   "The Script has Started YAY"
		   ])
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
##############################################################
count=0
print("\n")
print("C O D E By ReVoLuTioN")
print("\n")
time.sleep(2)
from random import randint
import random
spam=int(input("Input the number of the variable spam (250 if you dont know) : \n"))

print("Logging in .... \n")
#######################################################################################################################################
CONSUMER_KEY = 'yModro0JDLIi4ovEuqA5XPdGd'
CONSUMER_SECRET = 'tF7CxFoUjkvVSlfSyGAvjtdyiYxAlr9hJqynaE5QKWYySOFbrO'
ACCESS_KEY = '745986163417165824-YcQ19Dt8wp9uRLnfyl6i1JQZ2wz90Ay'
ACCESS_SECRET = 'PYU6ObO5Y3m0zy2EzHvkX1mLs5AwK5aPPTUHq95KgjNQ5'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
#######################################################################################################################################
print("Logged IN \n")
print("Looking for Tweets to RT and FOLLOW \n ")
print("==========================================\n")
print ("===================LETS WIN SOME STUFF======================\n")
print("==========================================\n")
for tweet in tweepy.Cursor(api.search,
						   q="RT and follow",
						   rpp=100,
						   result_type="recent",
						   include_entities=True,
						   lang="en").items():
	 count=count+1
	 if (count > spam):
		 print("Waiting for LIMIT time to go away (Half hour)")
		 msg = "\r\n".join([
		   "From: arnad33m@gmail.com",
		   "To: xspidera777@gmail.com",
		   "Subject: TwitterBOT ",
		   "",
		   "Current Tweets",count,"And still Going on, NOW WAITING FOR HALF AN HOUR"
		   ])
		 server.ehlo()
		 server.starttls()
		 server.sendmail(fromaddr, toaddrs, msg)
		 server.quit()
		 time.sleep(1800)
		 spam=spam+300
	 print (tweet.text.encode('cp850', errors='replace'))
	 try:
		 api.retweet(tweet.id)
	 except:
		 print("+++++++++++++++ALREADY RETWEETED or limit reached+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		 count=count-1
		 pass
	 str(tweet.text)
	 try:
		 a1=tweet.text.index("@")
	 except:
		 print("++++++++++++++++CANT FIND THE AUTHOR OF TWEET++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		 pass
	 try:
		  user=tweet.text[a1:]
		  a2=user.index(" ")
		  user=user[:a2]
	 except:
		  print("+++++++++++++++AUTHOR WANTS YOU TO FOLLOW SOMEONE ELSE OR HIS NAME IS HIIDEN+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		  pass
	 try:
		 a3=user.index(":")
		 user=user[:a3]
	 except:
		 print("+++++++++++++++AUTHOR WANTS YOU TO FOLLOW SOMEONE ELSE OR HIS NAME IS HIIDEN+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		 pass
	 print(user.encode('cp850', errors='replace'))
	 try:
		 api.create_friendship(user)
	 except:
		 print("+++++++++++++++CANT FOLLOW USER HAS BANNED YOU FROM FOLLWING HIM OR YOU ALREADY FOLLOWS HIM+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		 pass
	 print("DONE RT AND FOLLOW TWEET NO",count)
