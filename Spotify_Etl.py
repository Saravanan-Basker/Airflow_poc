import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import re
import pandas as pd


def extract_spotify_data():

    sp = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id="a0c2f4fab00d40e190ae0b402591a4e6",
                                                              client_secret="6c0960ba906e4cbfab53fc78596d4ec1"))

    file_path = "/home/saravanab/Desktop/Airflow_env/artists_urls.txt"

    with open(file_path,"r") as file:
        content=file.readlines()
        
        artist_list = []
        for artist_url in content:
          artist_url = artist_url.strip()
          try:
            artist_id = re.search(r'(?<=/artist/)([a-zA-Z0-9]+)',artist_url).group(1)
            artist = sp.artist(artist_id)
            #print(f'yes its working{artist}')
          except AttributeError:
                print(f"Track ID not found in URL: {artist_url}")
          except Exception as e:
                print(f"Error processing URL {artist_url}: {e}")  

          artist_data = {
                    'artist_name':artist['name'],
                    'Uri':artist['uri'],
                    'popularity':artist['popularity'],
                    'followers':artist['followers']['total'],
                    'type':artist['type']
                      }  
          artist_list.append(artist_data)


    df = pd.DataFrame(artist_list)
    df.to_csv("spotify_data.csv")
    


