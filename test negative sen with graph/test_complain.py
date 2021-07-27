# import SentimentIntensityAnalyzer class 
# from vaderSentiment.vaderSentiment module. 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
import csv

# function to print sentiments 
# of the sentence. 
print("\n1st statement :")
comp_id = input("enter the complain id\n") 
sentence = input("enter the complain\n") 
	# Create a SentimentIntensityAnalyzer object. 
sid_obj = SentimentIntensityAnalyzer() 

	# polarity_scores method of SentimentIntensityAnalyzer 
	# oject gives a sentiment dictionary. 
	# which contains pos, neg, neu, and compound scores. 
sentiment_dict = sid_obj.polarity_scores(sentence) 
	
print("Overall sentiment dictionary is : ", sentiment_dict) 
print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative") 
print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral") 
print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive") 

print("Sentence Overall Rated As", end = " ") 

	# decide sentiment as positive, negative and neutral 
if sentiment_dict['compound'] >= 0.05 : 
	print("Positive",sentiment_dict['compound']) 

elif sentiment_dict['compound'] <= - 0.05 : 
	print("Negative",sentiment_dict['compound']) 

else : 
	print("Neutral",sentiment_dict['compound'])
	
with open('names.csv', 'a') as csvfile:
        fieldnames = ['complain_id', 'complain']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #writer.writeheader()
        writer.writerow({'complain_id': comp_id, 'complain': sentiment_dict['compound']})
