import tweepy as tp

api_key="0Kslf1Qb4Odkk3UHZNbMy5Z25"
api_sec_key="5mlrqrFjPlDfcKPDNiVtTKngtlhLdvjNyRI2PV5MgQa3xKXloK"
access_token="1124541858049183744-d74TmNeUK88G0Wdto15lksavByQqjN"
access_token_secret="8svGoMsHZzkjtH1f6ORrDF6hK823xiCI3XzTZRe2EAKmA"



def get_api():
	auth= tp.OAuthHandler(api_key,api_sec_key)
	auth.set_access_token(access_token,access_token_secret)
	return tp.API(auth)

def testing():
	get_api().update_status(status="Testing phase 2")

def check(s):
	print(s)