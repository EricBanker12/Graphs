import os
import random
import sys
import time

sys.path.append(os.path.join(__file__, '../../graph'))

from graph import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            raise Exception("You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            raise Exception("Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        
        # Add users
        for i in range(num_users):
            self.add_user(f'user_{i+1}')

        def all_permutation_selection(): # O(n^2)
            # Create friendships
            # To create N random friendships,
            # you could create a list with all possible friendship combinations,
            # shuffle the list, then grab the first N elements from the list.
            possible_friendships = []
            for user_id in self.users:
                for friend_id in range(user_id + 1, self.last_id + 1):
                    possible_friendships.append((user_id, friend_id))

            random.shuffle(possible_friendships)

            # Create n friendships where n = avg_friendships * num_users // 2
            # avg_friendships = total_friendships / num_users
            # total_friendships = avg_friendships * num_users
            for i in range(num_users * avg_friendships // 2):
                friendship = possible_friendships[i]
                self.add_friendship(friendship[0], friendship[1])

        def random_selection(): # O(n)
            num_friendships = num_users * avg_friendships // 2
            while num_friendships > 0:
                try:
                    a = random.randint(1, num_users)
                    b = random.randint(1, num_users)
                    self.add_friendship(a, b)
                    num_friendships -= 1
                except:
                    continue

        # all_permutation_selection()
        random_selection()


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        
        # bfs all friends
        queue = Queue()
        queue.enqueue((user_id, [user_id]))
        while queue.size():
            user, path = queue.dequeue()
            if not user in visited:
                visited[user] = path
                friends = self.friendships[user]
                for friend in friends:
                    queue.enqueue((friend, [*path, friend]))

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    start = time.perf_counter()
    sg.populate_graph(1000, 5)
    print(f'{time.perf_counter() - start:.2}s')
    # print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    # print(connections)
    print(len(connections), sum([len(connections[key]) for key in connections])//len(connections) )
