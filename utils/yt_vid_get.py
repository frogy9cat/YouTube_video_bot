from youtube_search import YoutubeSearch
# from pytube import YouTube

def video_from_yt(text):

    results = YoutubeSearch(text, max_results=30).to_dict()
    videos = []
    
    for result in results:
            
        data = {}    
        
        title = result.get('title')
        data['title']=title

        image = str(result.get('thumbnails')[0])
        image = image.split(".jpg")[0]+".jpg"
        data['image'] = image

        vid_url = result.get('url_suffix')
        data['url'] = "https://www.youtube.com"+vid_url

        channel = result.get('channel')
        data['channel'] = channel

        views = result.get('views')
        data['views'] = views

        videos.append(data)

    
    return videos


url = "https://www.youtube.com/watch?v=UXAe_OzLNXg"




# def ddl(url):
    
#     yt = YouTube(url)
#     # stream = yt.streams.get_highest_resolution()
#     # stream.download()
    

#     # yt = YouTube(url)
#     # vid = yt.streams.get_highest_resolution()

#     # yt.streams = yt.streams.filter(progressive=True,file_extension='mp4', res='720p')
#     # yt.streams.first().download()

# print(ddl(url))

