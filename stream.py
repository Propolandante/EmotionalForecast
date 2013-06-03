from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
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
    def on_data(self, data):

        if 'retweeted_status' in data:
            return True

        
        

        f = open('060213_2.txt','a+')
        
        text = json.loads(data)['text']
        time = json.loads(data)['created_at']
        tweet = json.loads(data)['id_str']
        
        f.write(tweet.encode('utf-8') + "\n")
        f.write(time.encode('utf-8)') + "\n")
        f.write(text.encode('utf-8)') + "\n")
        
        f.write("\n")
        
        f.close()
        print "working as of "
        print datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
        return True


    def on_error(self, status):
        print status
        return True

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['I feel'])
