"""
Sort your music.  Call this in a directory with your music to get it sorted.
"""

import os
import sys
import eyed3
import tree

import pdb

music_collection = tree.Link('collection', 'my collection')
songs = []

path = sys.argv[1] if len(sys.argv) > 1 else '.'
for dirname, dirnames, filenames in os.walk(path):
    for filename in filenames:
        song_full_path = os.path.join(dirname, filename)
        try:
            af = eyed3.load(song_full_path)
            songs.append({'title': str(af.tag.title).title(),
                'album': str(af.tag.album).title(),
                'artist': str(af.tag.artist).title(),
                'track_num': af.tag.track_num,
                'full_path': str(song_full_path)})

        except AttributeError:
            #print('Got attribute error for song: ' + str(song_full_path))
            pass


print('Sorting songs into albums')
albums = {}
# Sort songs into albums
for song in songs:
    try:
        albums[song['album']]['songs'].append(song)
    except KeyError:
        albums[song['album']] = {'songs': [song], 'artists': []}

# Get artists for albums
for album in albums:
    artists = {}
    for song in albums[album]['songs']:
        artists[song['artist']] = 0
    albums[album]['artists'] = artists.keys()

for album in albums:
    if len(albums[album]['artists']) > 1:
        print 'Album: ' + str(album) + ', has more than 1 artist, artists: ', str(albums[album]['artists'])

