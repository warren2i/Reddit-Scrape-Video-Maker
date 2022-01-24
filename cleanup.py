import os
def clean():
    image_folder = 'redditpost'
    audio_folder = 'redditpost'
    video_folder = 'finished'

    image_files = [os.path.join(image_folder, img)
                   for img in os.listdir(image_folder)
                   if img.endswith(".png")
                   ]
    audio_files = [os.path.join(audio_folder, mp3)
                   for mp3 in os.listdir(audio_folder)
                   if mp3.endswith(".mp3")
                   ]
    video_files = [os.path.join(video_folder, mp4)
                   for mp4 in os.listdir(video_folder)
                   if mp4.endswith(".mp4")
                   ]
    for image in enumerate(image_files):
        os.remove(image[1])
    for mp3 in enumerate(audio_files):
        os.remove(mp3[1])
    for mp4 in enumerate(video_files):
        print(mp4)
        os.remove(mp4[1])
    os.remove('screenshot/comments.html')
    os.remove('screenshot/screenshot.png')

    print(image_files)
    print(audio_files)