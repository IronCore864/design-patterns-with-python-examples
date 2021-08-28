from __future__ import annotations
from abc import ABC, abstractmethod


class AudioPlayer:
    def __init__(self):
        self.state = ReadyState(self)
        self.playing = False
        self.songs = ["Song A", "Song B", "Song C", "Song D"]
        self.current_song = 0

    def change_state(self, state: State):
        self.state = state

    def click_lock(self):
        self.state.click_lock()

    def click_play(self):
        self.state.click_play()

    def click_next(self):
        self.state.click_next()

    def click_previous(self):
        self.state.click_previous()

    def start_playback(self):
        self.playing = True
        print(f'Start playing song {self.songs[self.current_song]}.')

    def stop_playback(self):
        self.playing = False
        print('Stop playing.')

    def next_song(self):
        self.current_song += 1
        self.current_song %= len(self.songs)
        print(f'Start playing song {self.songs[self.current_song]}.')

    def previous_song(self):
        self.current_song -= 1
        if self.current_song < 0:
            self.current_song + len(self.songs)
        print(f'Start playing song {self.songs[self.current_song]}.')


class State(ABC):
    def __init__(self, player):
        self.player = player

    @abstractmethod
    def click_lock():
        pass

    @abstractmethod
    def click_play():
        pass

    @abstractmethod
    def click_next():
        pass

    @abstractmethod
    def click_previous():
        pass


class LockedState(State):
    def click_lock(self):
        if self.player.playing:
            self.player.change_state(PlayingState(self.player))
        else:
            self.player.change_state(ReadyState(self.player))

    def click_play(self):
        # Locked, so do nothing.
        pass

    def click_next(self):
        # Locked, so do nothing.
        pass

    def click_previous(self):
        # Locked, so do nothing.
        pass


class ReadyState(State):
    def click_lock(self):
        self.player.change_state(LockedState(self.player))

    def click_play(self):
        self.player.start_playback()
        self.player.change_state(PlayingState(self.player))

    def click_next(self):
        self.player.next_song()

    def click_previous(self):
        self.player.previous_song()


class PlayingState(State):
    def click_lock(self):
        self.player.change_state(LockedState(self.player))

    def click_play(self):
        self.player.stop_playback()
        self.player.change_state(ReadyState(self.player))

    def click_next(self):
        self.player.next_song()

    def click_previous(self):
        self.player.previous_song()


if __name__ == "__main__":
    winamp = AudioPlayer()
    print('Start, click play:')
    winamp.click_play()
    print('Click next:')
    winamp.click_next()
    print('Click next:')
    winamp.click_next()
    print('Click previous:')
    winamp.click_previous()
    print('Click play (already playing, should stop):')
    winamp.click_play()
    print('Click lock')
    winamp.click_lock()
    print('Click play (locked, should do nothing)')
    winamp.click_play()
    print('Click lock (already locked, will unlock')
    winamp.click_lock()
    print('Click play (just unlocked, will continue playing)')
    winamp.click_play()
