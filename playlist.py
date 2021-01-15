from dotenv import load_dotenv, find_dotenv
import os
import requests
import json

load_dotenv()
token = os.getenv('TOKEN')
user_id = '12170530026'

endpoint_url = "https://api.spotify.com/v1/recommendations?"

# OUR FILTERS
limit=10
market="US"
seed_genres="indie"
target_danceability=0.9

query = f'{endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres}&target_danceability={target_danceability}'

response =requests.get(query, 
               headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {token}"})

json_response = response.json()
print(json_response)
uris = []

for i in json_response['tracks']:
            uris.append(i)
            print(f"\"{i['name']}\" by {i['artists'][0]['name']}")

def create_playlist(name):


    endpoint_url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    request_body = json.dumps({
            "name": name,
            "description": "My first programmatic playlist, yooo!",
            "public": True # let's keep it between us - for now
            })
    response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                            "Authorization":f"Bearer {token}"})
    
    print(response.json()['id'])

    return response.status_code


def get_playlist_id(playlist_name):

    endpoint_url =  f"https://api.spotify.com/v1/users/{user_id}/playlists"

    response = requests.get( url = endpoint_url, headers={"Content-Type":"application/json", 
                                                        "Authorization":f"Bearer {token}"})

    data = []

    json_response = response.json()

    for i in json_response['items']:
        data.append( (i['name'], i['id']) )
    
    data = dict(data)

    pl_id  = data[playlist_name]

    return pl_id

def fill_playlist(tracks, playlist_id):

    endpoint_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

    request_body = json.dumps({
            "uris" : tracks
            })

    response = requests.post(url = endpoint_url, data = request_body, 
                            headers={"Content-Type":"application/json", 
                                    "Authorization":f"Bearer {token}"})

    return response.status_code

pl_name = 'alarm_playlist'

#create_playlist(pl_name)
pl_id = get_playlist_id(pl_name)
print(pl_id)
print(fill_playlist(uris, pl_id))