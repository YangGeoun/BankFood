import requests
from models import Youtube

def getYoutube():
    url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&key=AIzaSyDhIuh0Zm5__5XL7Mb6MjhNdsLb_EENEOc&q=금융&maxResults=10'
    response = requests.get(url).json()
    for video in response.get('items'):
        video = Youtube()
        video.title = video.get('snippet').get('title')
        video.description = video.get('snippet').get('description')
        video.video_id = video.get('id').get('videoId')
        video.image_url = video.get('snippet').get('thumbnails').get('high').get('url')
        video.save()

getYoutube()