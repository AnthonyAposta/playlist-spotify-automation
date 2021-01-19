from dotenv import load_dotenv, find_dotenv
import os
import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from time import sleep

load_dotenv()

class radio_playlist:

    def __init__(self, pl_name):
        self.pl_name = pl_name
        scope = "playlist-modify-public"
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
        self.user_id = self.sp.me()['id']

    def rotate_playlist(self):
        self.sp.playlist_reorder_items(self.get_pl_id(),0,7)

    def create_playlist(self):
        try:
            self.get_pl_id()
        except:
            self.sp.user_playlist_create(self.user_id, name = self.pl_name)

    def generate_tracks(self, seeds):
        
        tracks = self.sp.recommendations(**seeds,limit = 7) 
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

    def fill_playlist(self, seeds):
        self.sp.playlist_add_items(self.get_pl_id(), self.generate_tracks(seeds) )

    def clear_playlist(self):
        remove = []
        tracks = self.sp.playlist_tracks(self.get_pl_id())

        for i in tracks['items']:
            remove.append(i['track']['id'])

        self.sp.playlist_remove_all_occurrences_of_items(self.get_pl_id(), remove)


if __name__ == '__main__':

    seeds =  [
                { 
                 'seed_artists': ['3DF0ClNOUuvS3gh8V8sRJH', '0yFvXd36g5sNKYDi0Kkvl8', '6cHQUDAPGKRE2NbVjBlOcz'], 
                 'min_energy': 0.1,
                 'max_energy': 0.4 },
                
                
                {
                 'seed_artists': ['1LeVJ5GPeYDOVUjxx1y7Rp', '2RhgnQNC74QoBlaUvT4MEe'], 
                 'min_energy': 0.1,
                 'max_energy': 0.4 },
            ]

    seed_index = 0

    c = radio_playlist('Anthony_alarm')
    c.create_playlist()

    while True:
        try:
            c.clear_playlist()
            c.fill_playlist(seeds[seed_index])

            for day in range(7):
                c.rotate_playlist()
                sleep(3600*24)

            seed_index = (seed_index+1)%len(seeds)
            print(seed_index)

        except KeyboardInterrupt:
             print("\n=== END ===")
             break