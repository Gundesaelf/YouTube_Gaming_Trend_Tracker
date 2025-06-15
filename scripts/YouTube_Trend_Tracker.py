import requests
import sqlite3
from datetime import datetime

API_KEY = 'your_api_key_here'
base_url = "https://www.googleapis.com/youtube/v3/videos"
params = {
    "part": "snippet,statistics",
    "chart": "mostPopular",
    "videoCategoryId": "20",
    "regionCode": "US",
    "maxResults": 50,
    "key": API_KEY
}
db = sqlite3.connect(r"C:\Databases\ytTrends.db")
curs = db.cursor()

curs.executescript("""
CREATE TABLE IF NOT EXISTS trending_videos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    video_id TEXT,
    title TEXT,
    channel TEXT,
    views INTEGER,
    date_published DATE,
    video_url TEXT
)
""")

def fetch_videos(url, params):
    videos = []
    while len(videos) < 200:
        response = requests.get(url, params=params)
        data = response.json()
        
        videos.extend(data["items"])
        
        if "nextPageToken" in data:
            params["pageToken"] = data["nextPageToken"]
        else:
            break

    return videos[:200]

videos = fetch_videos(base_url, params)

for video in videos:
    video_id = video["id"]
    title = video["snippet"]["title"]
    channel = video["snippet"]["channelTitle"]
    
    views = int(video.get('statistics', {}).get('viewCount', 0))
    
    date_published = datetime.strptime(video["snippet"]["publishedAt"], "%Y-%m-%dT%H:%M:%SZ").strftime("%d%b%Y")
    video_url = f"https://www.youtube.com/watch?v={video_id}"

    curs.execute("""
        INSERT OR REPLACE INTO trending_videos (video_id, title, channel, views, date_published, video_url) 
        VALUES (?, ?, ?, ?, ?, ?);
    """, (video_id, title, channel, views, date_published, video_url))

db.commit()
curs.close()
db.close()

print('\n\nDatabase updated\n\n')
