import tweepy, time, sys, codecs, smtplib, random, serial
print("")
count=0+0+0+0+0+0+0+0+0
spam=250
######################################################################################################################################
fromaddr = 'arnad33m@gmail.com'
toaddrs	 = 'xspidera777@gmail.com'
username = 'arnad33m@gmail.com'
password = '*******'
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
print("Done Emailing")
#######################################################################################################################################
CONSUMER_KEY = ('yModro0JDLIi4ovEuqA5XPdGd')
CONSUMER_SECRET = 'tF7CxFoUjkvVSlfSyGAvjtdyiYxAlr9hJqynaE5QKWYySOFbrO'
ACCESS_KEY = '745986163417165824-YcQ19Dt8wp9uRLnfyl6i1JQZ2wz90Ay'
ACCESS_SECRET = 'PYU6ObO5Y3m0zy2EzHvkX1mLs5AwK5aPPTUHq95KgjNQ5'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
nouns = ("CUTIE puppy", "Fast car", "Cute rabbits", "that girl", "this monkey", " .")
verbs = ("runs", "hits", "jumps", "drives", "barfs","Stares","Kills me","Laughs","Chats", "Follows me", "Loves me", ". ")
adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.", "Happly.", "Lovingly.", "Carefully.",". ")
adj = ("adorable", "clueless", "dirty", "odd", "stupid", "LMAO ", "LOL ", "SMH "," ")
#######################################################################################################################################
ser = serial.Serial('COM3',9600)
time.sleep(.50)
ser.write(str.encode("/////////////////"))
time.sleep(0.50)
do=ser.readline()
print(do)
do=do.decode("utf-8")
print(do)
do=do[:2]
ser.write(str.encode('\r'))


do=ser.readline()
print(do)
do=((ser.readline()).decode("utf-8"))[:2]
while 1:
	if (do=="S1"):
			#ser.write(str.encode("Script 1 Started"))
			print("Script 1")
			do=((ser.readline()).decode("utf-8"))[:2]
			num1 = random.randrange(0,5)
			num2= random.randrange(0,11)
			num3= random.randrange(0,8)
			num4= random.randrange(0,8)
			ser.write(str.encode('\r'))
			tweet= nouns[num1] + ' ' + verbs[num2] + ' ' + adv[num3] + ' ' + adj[num4]
			api.update_status(tweet)
			tweet=tweet[:16]+"\n"+tweet[16:]
			line=str.encode(tweet)
			time.sleep(0.200)
			time.sleep(0.5)
			ser.write(line)

	elif (do=="S2"):
			print("Script 2")
			do=((ser.readline()).decode("utf-8"))[:2]
			if (do=="S0"):
				do="S2"
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
				 if(do=="S0"):
					 do="S2"
				 do=ser.readline()
				 do=do.decode("utf-8")
				 #do=do[:2]
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
				 if (len(tweet.text)>16):

					 tweet.text=tweet.text[:16]+"\n"+tweet[16:]
				 if (len(user)>16):
					 user=user[:16]+"\n"+user[16:]
				 ser.write(str.encode('\r'))
				 ser.write(user)
				 time.sleep(700)
				 ser.write(str.encode('\r'))
				 ser.write(tweet)
				 time.sleep(700)
	else:
				 #try:
				 do=((ser.readline()).decode("utf-8"))[:2]
				 print(do)
				 #except:
				 print("NO SCRIPT")
