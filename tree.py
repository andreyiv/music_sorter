"""
Module containing Classes making up a tree.
"""

class Node:
    """
    Class to represent a Node in the tree, in this instance a song.
    """
    title = ''
    track_num = 0
    album = ''
    artists = []
    location = ''
    parent = None

    def __init__(self, title, track_num, album, artists, location, parent = None):
        """
        Contructor taking all members as parameters.
        """
        self.title = title
        self.track_num = track_num
        self.album = album
        self.artists = artists
        self.location = location
        self.parent = parent

    def __repr__(self):
        string_representation = '<Node instance containing: ' + \
            'Title = ' + str(self.title) + ', ' + \
            'Track Number = ' + str(self.track_num) + ', ' + \
            'Album = ' + str(self.album) + ', ' + \
            'Artists = ' + str(self.artists) + ', ' + \
            'Location on disk = ' + str(self.location) + '>'
        return string_representation

    def set_parent(self, parent):
        """
        Assigns the parent member.
        """

        self.parent = parent


class Link:
    """
    Class to represent a Link in the tree, basically not an end node.
    """
    type_of_link = '' # Meant to be Collection, Artist, or Album
    name = ''
    children = []
    parent = None

    def __init__(self, type_of_link, name, children = [], parent = None):
        """
        Constructor taking all members as parameters.
        """

        self.type_of_link = type_of_link
        self.name = name
        self.children = children
        self.parent = parent

    def __repr__(self):
        string_representation = '<Link instance of: ' + \
            'Type of link = ' + str(self.type_of_link) + ', '\
            'Name = ' + str(self.name) + ', '\
            'Children = ' + str(self.children) + ', '\
            'Parent = ' + str(self.parent) + '>'
        return string_representation

    def add_child(self, child):
        """
        Adds a child to list of children.
        """

        child.parent = self
        self.children.append(child)

    def set_parent(self, parent):
        """
        Assigns the parent member.
        """

        self.parent = parent

def test_tree():
    """
    Tests the methods in the class above.
    """

    # Test importing
    import tree

    # Make a few nodes
    n1 = tree.Node('t1', 1, 'al1', ['ar1'], '/home/1')
    n2 = tree.Node('t2', 2, 'al2', ['ar2'], '/home/2')
    n3 = tree.Node('t3', 3, 'al3', ['ar3'], '/home/3')

    # Make a few links
    l1 = tree.Link('collection', 'my_c')
    l1_1 = tree.Link('artist', 'ar')
    l1_1_1 = tree.Link('album', 'al')

    # Associate links with nodes
    print('Prior to node association')
    print(l1_1_1)
    print(l1_1)
    print(l1)
    l1_1_1.add_child(n1)
    l1_1_1.add_child(n2)
    l1_1_1.add_child(n3)

    # Associate links with links
    print('Prior to link association')
    print(l1_1_1)
    print(l1_1)
    print(l1)
    l1_1.add_child(l1_1_1)
    print('After first link association')
    print(l1_1_1)
    print(l1_1)
    print(l1)
    l1.add_child(l1_1)
    print('After last link association')
    print(l1_1_1)
    print(l1_1)
    print(l1)
