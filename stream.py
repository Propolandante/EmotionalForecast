from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="3CILoRRD7cW9zynmS5hQ"
consumer_secret="tvuFMAw5YcEsggk6xeSNGAI3qey8YYh8q01B28uupA"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="17454258-4YPtYrWSSvaHcxGn8o4c3Pq6rhdNSxH8LYIlFfq90"
access_token_secret="y2XvTslVxYNqqQaB5RUOurBO9Pw7dJd5w7rQk5s"

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['I feel'])
