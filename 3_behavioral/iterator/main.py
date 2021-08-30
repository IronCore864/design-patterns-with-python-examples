from __future__ import annotations
from abc import ABC, abstractmethod
from collections.abc import Iterable, Iterator
from typing import Any, List


class SocialNetwork(ABC):
    @abstractmethod
    def create_friends_iterator(self, facebook, profile_id):
        pass

    @abstractmethod
    def create_coworkers_iterator(self, facebook, profile_id):
        pass


class Facebook(SocialNetwork):
    def create_friends_iterator(self, profile_id):
        return FacebookIterator(self, profile_id, "friends")

    def create_coworkers_iterator(self, profile_id):
        return FacebookIterator(self, profile_id, "coworkers")

    def social_graph_request(self, profile_id, type):
        # mock
        if type == 'friends':
            return [
                Profile("FriendA", "a@gmail.com"),
                Profile("FriendB", "b@gmail.com"),
                Profile("FriendC", "c@gmail.com"),
                Profile("FriendD", "d@gmail.com")
            ]
        return [
            Profile("Coworker1", "1@gmail.com"),
            Profile("Coworker2", "2@gmail.com"),
            Profile("Coworker3", "3@gmail.com"),
            Profile("Coworker4", "4@gmail.com")
        ]


class Profile():
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_email(self):
        return self.email


class ProfileIterator(ABC):
    @abstractmethod
    def get_next(self):
        pass

    @abstractmethod
    def has_more(self):
        pass


class FacebookIterator(ProfileIterator):
    def __init__(self, facebook, profile_id, type):
        self.facebook = facebook
        self.profile_id = profile_id
        self.type = type
        self.current_position = 0
        self.cache = None

    def __lazy_init(self):
        if not self.cache:
            self.cache = self.facebook.social_graph_request(
                self.profile_id,
                self.type
            )

    def get_next(self):
        res = self.cache[self.current_position]
        if self.has_more():
            self.current_position += 1
        return res

    def has_more(self):
        self.__lazy_init()
        return self.current_position < len(self.cache)


class SocialSpammer:
    def send(self, iterator: ProfileIterator, message: str):
        while iterator.has_more():
            profile = iterator.get_next()
            print(f'{message} sent to {profile.get_email()}')


def client_code():
    network = Facebook()
    spammer = SocialSpammer()

    iterator = network.create_friends_iterator('fake_profile_id')
    spammer.send(iterator, "Very important message")

    iterator = network.create_coworkers_iterator('fake_profile_id')
    spammer.send(iterator, "Very important message")


if __name__ == "__main__":
    client_code()
