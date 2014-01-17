"""
Module containing Classes making up a tree.
"""

class Node:
    """
    Class to represent a Node in the tree, in this instance a song.
    """

    def __init__(self, name, track_num,
                 album, location, artists = None,
                 parent = None):
        """
        Contructor taking all members as parameters.
        """
        self.name = name
        self.track_num = track_num
        self.album = album
        self.location = location
        self.parent = parent
        if artists == None:
            self.artists = []
        else:
            self.artists = artists

    def __repr__(self):
        string_representation = '<Node instance containing: ' + \
            'Name = ' + str(self.name) + ', ' + \
            'Track Number = ' + str(self.track_num) + ', ' + \
            'Album = ' + str(self.album) + ', ' + \
            'Location on disk = ' + str(self.location) + ', ' \
            'Artists = ' + str(self.artists) + '>'
        return string_representation

    def set_parent(self, parent):
        """
        Assigns the parent member.
        """

        self.parent = parent


class Link:
    """
    Class to represent a Link in the tree,
    basically not an end node.
    """

    def __init__(self, type_of_link, name,
                 children = None, parent = None):
        """
        Constructor taking all members as parameters.
        """

        self.type_of_link = type_of_link # Meant to be Collection, Artist, or Album
        self.name = name
        self.parent = parent
        if children == None:
            self.children = []
        else:
            self.children = children

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

        for instance in self.children:
            if instance.name == child.name:
                return False

        child.parent = self
        self.children.append(child)
        return True

    def set_parent(self, parent):
        """
        Assigns the parent member.
        """

        self.parent = parent
        return True

def test_tree():
    """
    Tests the methods in the class above.
    """

    # Test importing
    import tree

    # Make a few nodes
    name = 't1'
    track_num = 1
    album = 'al1'
    location = '/home/1'
    artists = ['ar1']
    n1 = tree.Node(name, track_num, album, location, artists)
    assert n1.name == name
    assert n1.track_num == track_num
    assert n1.album == album
    assert n1.location == location
    assert n1.artists == artists

    name = 't2'
    track_num = 2
    album = 'al2'
    location = '/home/2'
    artists = ['ar2']
    n2 = tree.Node(name, track_num, album, location, artists)
    assert n2.name == name
    assert n2.track_num == track_num
    assert n2.album == album
    assert n2.location == location
    assert n2.artists == artists

    name = 't3'
    track_num = 3
    album = 'al3'
    location = '/home/3'
    artists = ['ar3']
    n3 = tree.Node(name, track_num, album, location, artists)
    assert n3.name == name
    assert n3.track_num == track_num
    assert n3.album == album
    assert n3.location == location
    assert n3.artists == artists

    # Make a few links
    type_of_link = 'collection'
    name = 'my_c'
    l1 = tree.Link(type_of_link, name)
    assert l1.type_of_link == type_of_link
    assert l1.name == name

    type_of_link = 'artist'
    name = 'ar'
    l1_1 = tree.Link(type_of_link, name)
    assert l1_1.type_of_link == type_of_link
    assert l1_1.name == name

    type_of_link = 'album'
    name = 'al'
    l1_1_1 = tree.Link(type_of_link, name)
    assert l1_1_1.type_of_link == type_of_link
    assert l1_1_1.name == name

    # Associate links with nodes
    l1_1_1.add_child(n1)
    assert len(l1_1_1.children) == 1
    assert l1_1_1.children[0] == n1
    l1_1_1.add_child(n2)
    assert len(l1_1_1.children) == 2
    assert l1_1_1.children[0] == n1
    assert l1_1_1.children[1] == n2
    l1_1_1.add_child(n3)
    assert len(l1_1_1.children) == 3
    assert l1_1_1.children[0] == n1
    assert l1_1_1.children[1] == n2
    assert l1_1_1.children[2] == n3

    # Associate links with links
    l1_1.add_child(l1_1_1)
    assert len(l1_1.children) == 1
    assert l1_1.children[0] == l1_1_1
    l1.add_child(l1_1)
    assert len(l1.children) == 1
    assert l1.children[0] == l1_1
