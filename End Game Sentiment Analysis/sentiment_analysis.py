import tweeter_api as tw
import csv
from textblob import TextBlob as tb

tw.check("Working")
store={}
def call_params():
	api=tw.get_api()
	print("1")
	return api

def get_tweets(api):
	tweets=api.search("EndGame")
	return tweets
	
def find_sentiment(api,tweets):
	with open('sentiments.csv', 'w') as csvfile:
		filewriter = csv.writer(csvfile, delimiter=',',quotechar='|')
		for tweet in tweets:
			analysis = tb(tweet.text)
			store["text"]=str(analysis)
			#print(store)
			print(analysis)
			if analysis.sentiment.polarity >=0 :
				tweetSentiments=True
				store["result"]="Positive"
				print("+ve")
			if analysis.sentiment.polarity<0:
				tweetSentiments=False
				store["result"]="negative"
				print("-ve")
			else :
				print("something went wrong!")
			filewriter.writerow([store['text'].encode("utf-8"),store['result'].encode("utf-8")])

def main():
	api=call_params()
	tweets = get_tweets(api)
	#for tweet in tweets:
	#	print(tweet.text)
	find_sentiment(api,tweets)

if __name__ =='__main__':
	main()
