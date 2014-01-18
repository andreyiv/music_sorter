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
            print('Got attribute error for song: ' + str(song_full_path))
            pass


albums = {}
for song in songs:
    try:
        albums[song['album']].append(song)
    except KeyError:
        print('No album')
        albums[song['album']] = [song]

for album in albums:
    print(str(album) + ':')
    for song in albums[album]:
        print('    ' + str(song['artist']))
