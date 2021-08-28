import os
from plexapi.server import PlexServer

# $env:PLEX_URL = 'http://192.168.1.200:32400'
# $env:PLEX_TOKEN = 'PbvKmsmCPYKUdUsd56GX'
# dir env:

PLEX_URL = os.environ['PLEX_URL']
PLEX_TOKEN = os.environ['PLEX_TOKEN']
plex = PlexServer(PLEX_URL, PLEX_TOKEN)

def main() :

    print ("Hello World!")
    print(PLEX_URL)
    print(PLEX_TOKEN)

    connected = plex.clients()
    session = plex.sessions()

    nowPlaying = [x.title for x in session]
    currentlyConnected = [x.title for x in connected]

    print(f"Currently Connected {currentlyConnected}")
    print(f"Now playing {nowPlaying}")

main()