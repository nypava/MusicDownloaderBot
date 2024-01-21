from youtubesearchpython import VideosSearch, Video

class Youtube:
    def __init__(self, text):
       self.video = VideosSearch(text + " Music", limit = 10)

    def image(self):
        video_id = self.video.result()['result'][0]["id"]
        return f"https://img.youtube.com/vi/{video_id}/0.jpg"

    def videos(self):
        videos = []

        for video in self.video.result()['result']:
            videos.append([video["id"], video["title"], video["duration"]])

        return videos

def nameFinder(id):
    video = Video.getInfo(id)
    return video["title"]
