import csv
import os
import re

import spotipy  # library for interacting with spotify api
from spotipy.oauth2 import SpotifyClientCredentials  # handles oath sign in with spotify api credentials
import requests  # make http requests
from bs4 import BeautifulSoup  # read page content from when opening genius urls
import nltk  # nlp library
from nltk.sentiment.vader import SentimentIntensityAnalyzer  # module for sentiment analysis
from nltk.corpus import stopwords  # used to remove common words like 'the, at, and' from lyrics

nltk.download('vader_lexicon')
nltk.download('stopwords')


# search for a song on genius with song title and artist name, returns url to lyrics page for the song
def get_genius_url(title, artist):
    genius = 'https://api.genius.com/search'
    data = {'q': title + ' ' + artist}
    headers = {'Authorization': 'Bearer ' + 'O-txEXzcRqwinpQX3P5AMzLRka8sq1HwBfZFBlSGCdaDZa14P4uXyeSKbgTCvARM'}
    response = requests.get(genius, data=data, headers=headers)
    song_url = ''
    for hit in response.json()['response']['hits']:
        if artist == hit['result']['primary_artist']['name']:
            # print(title + '|' + artist)
            song_url = hit['result']['url']
            break
    return song_url


# parse lyrics page for lyrics, returns lyrics
def get_genius_lyrics_from_url(genius_url):
    lyrics = requests.get(genius_url)
    html = BeautifulSoup(lyrics.text, 'html.parser')
    genius_lyrics = html.find('div', class_='lyrics').get_text()
    return genius_lyrics


# cleans up song lyrics, removing empty lines, section headings, and any data that is not lyrical content
def lyrical_analysis(song_lyrics):
    lines = re.split(r'\n', song_lyrics)
    filtered = ""
    for line in lines:
        line = re.sub(r'[\(\[].*?[\)\]]|\n|\u2005|\u205f', '', line)
        filtered += line + '\n'
    cleaned_lyrics = os.linesep.join([line for line in filtered.splitlines() if line])
    sia = SentimentIntensityAnalyzer()

    # object to return with sentiment data
    senti_data = {}

    # count for lines that are mostly positive, mostly negative, or mostly neutral
    positive = 0
    negative = 0
    neutral = 0

    # iterate line by line through lyrics, read line scores, judge positivity and update the respective count
    for line in cleaned_lyrics.split('\n'):
        line_sentiment = sia.polarity_scores(line)
        score = line_sentiment['compound']
        if score >= 0.5:
            positive += 1
        elif score < -0.1:
            negative += 1
        else:
            neutral += 1

    # small calculations to populate senti_data
    total = positive + neutral + negative
    senti_data['num_positive'] = positive
    senti_data['num_negative'] = negative
    senti_data['num_neutral'] = neutral
    senti_data['positivity'] = positive / total
    senti_data['negativity'] = negative / total
    senti_data['neutrality'] = neutral / total
    return senti_data


# count the number of unique words from tokanized array
def count_unique_words(array_of_words):
    unique_words = []
    for word in array_of_words:
        if word not in unique_words:
            unique_words.append(word)
    return len(unique_words)


# remove common stopwords from lyrics, tokenize lyrics
def remove_stopwords(song_lyrics):
    lines = re.split(r'\n', song_lyrics)
    filtered = ""
    for line in lines:
        line = re.sub(r'[\(\[].*?[\)\]]|\n|\u2005|\u205f', ' ', line)
        filtered += line + 'n'
    lyrics_words = re.split(r',| |_|-|!', filtered)
    stops = stopwords.words('english')
    removed_stopwords = [word for word in lyrics_words if word not in stops and word != '']
    return removed_stopwords


def get_track_data(offset):
    count = offset
    # Dictionary to assign track IDs to the track names, for easy lookup
    tracks = {}

    # get top 50 songs in 2020
    track_results = sp.search(q='year:2016', type='track', limit=50, offset=offset)

    # populate tracks dictionary with track ids as keys, track names as values
    for i, t in enumerate(track_results['tracks']['items']):
        tracks[t['id']] = [t['name'], t['artists'][0]['name']]

    # get audio data for each track in tracks
    audio_data = sp.audio_features(tracks.keys())

    # get lyrical data from for each song
    for record in audio_data:
        try:
            print(str(count) + '/1998 songs looked up')
            print(tracks[record['id']][0] + " | " + tracks[record['id']][1])

            # store song name and artist name in audio_data
            record['name'] = tracks[record['id']][0]
            record['artist'] = tracks[record['id']][1]

            # fetch url to lyrics page for song
            url = get_genius_url(record['name'], record['artist'])

            # if url exists, perform lyrical analyses. add lyrical information to the audio data already contained in audio_data
            if url != '':
                lyrics = get_genius_lyrics_from_url(url)
                sentiment_data = lyrical_analysis(lyrics)
                record['num_positive'] = sentiment_data['num_positive']
                record['num_negative'] = sentiment_data['num_negative']
                record['num_neutral'] = sentiment_data['num_neutral']
                record['positivity'] = sentiment_data['positivity']
                record['negativity'] = sentiment_data['negativity']
                record['neutrality'] = sentiment_data['neutrality']
                lyrics = remove_stopwords(lyrics)
                record['word_count'] = len(lyrics)
                record['unique_word_count'] = count_unique_words(lyrics)
            else:
                record['word_count'] = 0
            count += 1
        except Exception as e:
            print(record)
    # return array of song data of songs that were successfully analyzed
    return [track for track in audio_data if (hasattr(track, 'word_count') and track['word_count'] != 0)]


# API Tokens
clientID = '688f828e787d49768560dc3b01ad1527'
clientSecret = '1c92d4cff46546558e68bacdcb17a029'

credentialsManager = SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret)
sp = spotipy.Spotify(client_credentials_manager=credentialsManager)

data_to_save = []

for num in range(0, 1998, 50):
    for track_data in get_track_data(num):
        data_to_save.append(track_data)
fields = data_to_save[0].keys()
with open('./data/tracks2016.csv', 'w') as data_file:
    writer = csv.DictWriter(data_file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data_to_save)

print(data_to_save)
print('Length of data_to_save: ' + str(len(data_to_save)))
