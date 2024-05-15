from Google import Create_Service
import random

CLIENT_SECRET_FILE  =  'secret.json'
API_NAME  =  'youtube'
API_VERSION  =  'v3'
SCOPES  = ['https://www.googleapis.com/auth/youtube']

playlist_id ="PL1n0B6z4e_E5apcm1SQxlNqLEez2IxnJI"

youtube =  Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

response = youtube.playlistItems().list(
    part='contentDetails',
    playlistId=playlist_id,
    maxResults=50
).execute()

playlistItems = response['items']
nextPageToken = response.get('nextPageToken')

while nextPageToken:
    response = youtube.playlistItems().list(
        part='contentDetails',
        playlistId=playlist_id,
        maxResults=50,
        pageToken=nextPageToken
    ).execute()

    playlistItems.extend(response['items'])
    nextPageToken = response.get('nextPageToken')

for item in playlistItems:
    print('Deleting {0}'.format(item['id']))
    youtube.playlistItems().delete(id=item['id']).execute()

print('Deletion complete')

with open('videos1.txt') as ff:
        f = list(ff)        
        random.shuffle(f)
        for line in f:
            print("line: " + line.strip())
            request = youtube.playlistItems().insert(
                part="snippet",
                body={
                "snippet": {
                    "playlistId": playlist_id,
                    "position": 0,
                    "resourceId": {
                    "kind": "youtube#video",
                    "videoId": line.strip()
                    }
                }
                }
            )
            try:
                response = request.execute()
                print(response)
            except:
                print("An error occured")

"""

def main():

    
            
if __name__ == "__main__":
    main()

    """