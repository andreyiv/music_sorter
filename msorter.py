"""
Sort your music.  Call this in a directory with your music to get it sorted.
"""

import os
import sys
import io
import eyed3
import json
import time
import logging


# create logger
logger = logging.getLogger('log')
logger.propagate = False # Stops the logging from being picked up by eyed3
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.FileHandler('log.log')
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

logger.info('Started sorting music.')
songs = []

path = sys.argv[1] if len(sys.argv) > 1 else '.'
for dirname, dirnames, filenames in os.walk(path):
    for filename in filenames:
        song_full_path = os.path.join(dirname, filename)
        logger.debug('Current file: ' + song_full_path + '\n')
        try:
            af = eyed3.load(song_full_path)
            songs.append({u'title': unicode(af.tag.title).title(),
                u'album': unicode(af.tag.album).title(),
                u'artist': unicode(af.tag.artist).title(),
                u'track_num': af.tag.track_num,
                u'full_path': song_full_path})

        except AttributeError:
            logger.info('Could not read ID3 data from file: ' +
                song_full_path)
            pass


# Sort songs into albums
albums = {}
for song in songs:
    try:
        albums[song['album']]['songs'].append(song)
    except KeyError:
        albums[song['album']] = {u'songs': [song], u'artists': []}

# Get artists for albums
for album in albums:
    artists = {}
    for song in albums[album]['songs']:
        artists[song['artist']] = 0
    albums[album]['artists'] = artists.keys()

# Request the user to select an artist when an album has more than one artist
for album in albums:
    if len(albums[album]['artists']) > 1:
        print('Album: ' + unicode(album) + ', has more than 1 artist, artists: ')
        count = 0
        for artist in albums[album]['artists']:
            count += 1
            print(unicode(count) + '. ' + artist)
        artist_index = raw_input('Please enter the number corresponding to the main artist: ')
        print('Artist chosen: ' + unicode(albums[album]['artists'][int(artist_index) - 1]))
        albums[album]['artists'] = [albums[album]['artists'][int(artist_index) - 1]]

# Reorganize albums:songs into artists:albums:songs
artists = {}
for album in albums:
    try:
        artists[albums[album]['artists'][0]].append({album: albums[album]})
    except KeyError:
        artists[albums[album]['artists'][0]] = [{album: albums[album]}]

fp = io.open('albums_db.txt', 'wb')
temp = json.dumps(albums, indent=4)
fp.write(temp)
fp.close()

fp = io.open('artists_db.txt', 'wb')
fp.write(json.dumps(artists, indent=4, encoding="utf-8"))
fp.close()
