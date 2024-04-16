from API_keys import soundcloud_private_key, soundcloud_public_key, spotify_private_key, spotify_public_key

import spotipy as sp
from spotipy.oauth2 import SpotifyClientCredentials

# Set up your Spotify API credentials
client_id = 'your_client_id'
client_secret = 'your_client_secret'

# Create a Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Define your test function
def test_spotipy():
    # Your test code goes here
    # For example, you can search for a track
    results = sp.search(q='track:Believer artist:Imagine Dragons', type='track')
    track = results['tracks']['items'][0]
    print(f"Track: {track['name']}, Artist: {track['artists'][0]['name']}")

# Run the test function
test_spotipy()