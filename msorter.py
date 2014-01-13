"""
Sort your music.  Call this in a directory with your music to get it sorted.
"""

import os
import eyed3
import pdb

artists = {}
for dirname, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        song_full_path = os.path.join(dirname, filename)
        try:
            af = eyed3.load(song_full_path)
            artists[str(af.tag.artist).title()] = \
                {'title': str(af.tag.title).title(), \
                'track_num': str(af.tag.track_num[0]).rjust(2, '0'), \
                'filepath': song_full_path}
            # This ^ does not work, need a data structure containing albums

        except AttributeError:
            print('Got attribute error')
            pass


pdb.set_trace()
