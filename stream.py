from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
import json
import datetime


# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key=""
consumer_secret=""

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token=""
access_token_secret=""

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """

    def __init__(self, api=None):
        self.api = api or API()

        #here are the new addtions
        #nothing else has been changed
        self.tweetbuffer = ""
        self.tweetbufferlength = 0



    def on_data(self, data):

        #do not look at retweets
        if 'retweeted_status' in data:
            return True

        #ok so your not a retweet now let us get what we want
        text = json.loads(data)['text']
        time = json.loads(data)['created_at']
        tweet = json.loads(data)['id_str']
        
        #format one tweet and add it to the buffer
        self.tweetbuffer += tweet.encode('utf-8') + "\n"
        self.tweetbuffer += time.encode('utf-8)') + "\n"
        self.tweetbuffer += text.encode('utf-8)') + "\n\n" 

	    #increment tweetbufferlength
        self.tweetbufferlength += 1
	    
	    #if we have 5000 or more tweets in the buffer
        if self.tweetbufferlength >= 500:

	    	print "dumping buffer to file"

	    	#open the file
	    	f = open('060413_1.txt','a+')


	    	#dump the buffer to the file
	    	f.write(self.tweetbuffer)
	    	
	    	#close the file
	    	f.close()

	    	print "dump successful\n"
	    	
	    	#empty the buffer and it's length
	    	self.tweetbuffer = ""
	    	self.tweetbufferlength = 0
            
	    # #print to the screen takes a lot of time it turns out
	    # #this will print the working message one a minute
	    # if datetime.time.second is 1:
        #     	print "working as of "
        #     	print datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
	    # 	print "there are",self.tweetbufferlength,"tweets in the buffer\n"
        #   
        return True


    def on_error(self, status):
        print status
        return True



if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    #then we just make a instance of the new StdStream class
    stream = Stream(auth, l)
    stream.filter(track=['I feel'])
