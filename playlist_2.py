from dotenv import load_dotenv, find_dotenv
import os
import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import argparse
import logging

load_dotenv()

class radio_playlist:

    def __init__(self, pl_name):
        self.pl_name = pl_name
        scope = "playlist-modify-public"
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
        self.user_id = self.sp.me()['id']

    def create_playlist(self):

        try:
            self.get_pl_id()
        except:
            self.sp.user_playlist_create(self.user_id, name = self.pl_name)

    def generate_tracks(self):

        tracks = self.sp.recommendations(seed_genres=['deep-house', 'detroit-techno'], limit=7) 
        uris= []

        for i in tracks['tracks']:
            uris.append(i['id'])

        return uris

    def get_pl_id(self):
        playlists = self.sp.user_playlists(self.user_id)
        data = []

        for i in playlists['items']:
            data.append( (i['name'], i['id']) )
        
        data = dict(data)
        pl_id  = data[self.pl_name]

        return pl_id

    def fill_playlist(self):
        self.sp.playlist_add_items(self.get_pl_id(), self.generate_tracks() )

    def clear_playlist(self):
        remove = []
        tracks = self.sp.playlist_tracks(self.get_pl_id())

        for i in tracks['items']:
            remove.append(i['track']['id'])

        self.sp.playlist_remove_all_occurrences_of_items(self.get_pl_id(), remove)


if __name__ == '__main__':
    
    c = radio_playlist('Anthony_alarm')
    c.create_playlist()
    c.clear_playlist()
    c.fill_playlist()