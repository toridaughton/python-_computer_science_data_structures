from queue import Queue

class Node():
    """Node in a graph representing a person."""

    def __init__(self, name, adjacent=None):
        """Create a person node with friends adjacent"""

        if adjacent is None:
            adjacent = set()

        assert isinstance(adjacent, set), \
            "adjacent must be a set!"

        self.name = name
        self.adjacent = adjacent

    def __repr__(self):
        """Debugging-friendly representation"""

        return f"<Node: {self.name}>"


class FriendGraph():
    """Graph holding people and their friendships."""

    def __init__(self):
        """Create an empty graph"""

        self.nodes = set()

    def __repr__(self):
        return f"<FriendGraph: { {n.name for n in self.nodes} }>"

    def add_person(self, person):
        """Add a person to our graph"""

        self.nodes.add(person)

    def set_friends(self, person1, person2):
        """Set two people as friends"""

        person1.adjacent.add(person2)
        person2.adjacent.add(person1)

    def add_people(self, people_list):
        """Add a list of people to our graph"""

        for person in people_list:
            self.add_person(person)

    def are_connected(self, person1, person2):
        """Are two people connected? Breadth-first search."""

        possible_nodes = Queue(list(self.nodes))
        seen = set()
        possible_nodes.enqueue(person1)
        seen.add(person1)

        while not possible_nodes.is_empty():
            person = possible_nodes.dequeue()
            print("checking", person)
            if person is person2:
                return True
            else:
                for friend in person.adjacent - seen:
                    possible_nodes.enqueue(friend)
                    seen.add(friend)
                    print("added to queue:", friend)
        return False

    def print_friends(self):
        for friend in self.nodes:
            print(friend.name)


def make_simple_friendship(friends, friend1, friend2, friend3):
    friends.set_friends(friend1, friend2)
    friends.set_friends(friend2, friend3)
    friends.set_friends(friend1, friend3)





# Add sample friends
sora = Node("Sora")
riku = Node("Riku")
kairi = Node("Kairi")
roxas = Node("Roxas")
diz = Node("Diz")
namine = Node("Namine")
donald = Node("Donald")
goofy = Node("Goofy")
mickey = Node("King Mickey")

friends = FriendGraph()
friends.add_people([sora,riku,kairi,roxas,diz,namine,donald,goofy,mickey])

make_simple_friendship(friends,sora,riku,kairi)

print(friends.are_connected(sora, kairi))
print(friends.are_connected(riku, kairi))
print(friends.are_connected())


# friends.set_friends(sora, riku)
# friends.set_friends(sora, kairi)
# friends.set_friends(kairi, riku)
# friends.set_friends(sora, roxas)
# friends.set_friends(donald, goofy)
# friends.set_friends(mickey, goofy)
# friends.set_friends(mickey, riku)
# friends.set_friends(roxas, namine)
# friends.set_friends(kairi, namine)