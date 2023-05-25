import pandas as pd
import re

def clean_tweets_dataset(filename):
    data = pd.read_csv(filename, encoding='ISO-8859-1')

    clean_tweets = []
    for index, row in data.iterrows():
        tweet = str(row['tweet']).lower()
        clean_tweets.append(' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()))

    cleaned_filename = "cleaned_" + filename
    data['clean_tweet'] = clean_tweets
    data.to_csv(cleaned_filename, index=False)

# Clean the 'tweets.csv' dataset
clean_tweets_dataset('tweets.csv')

# Clean the 'labeled_data1.csv' dataset
clean_tweets_dataset('labeled_data1.csv')
