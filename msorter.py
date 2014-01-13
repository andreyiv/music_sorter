"""
Sort your music.  Call this in a directory with your music to get it sorted.
"""

import os
import eyed3

albums = {}
for dirname, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        song_full_name = os.path.join(dirname, filename)
        try:
            af = eyed3.load(song_full_name)
            albums[str(af.tag.album).title()] = song_full_name
