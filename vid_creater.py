import moviepy.video.io.ImageSequenceClip
from moviepy.editor import *
from mutagen.mp3 import MP3


def makevideo(name):
    image_folder = 'redditpost'
    audio_folder = 'redditpost'
    durations = []
    image_files = [os.path.join(image_folder, img)
                   for img in os.listdir(image_folder)
                   if img.endswith(".png")
                   ]
    audio_files = [os.path.join(audio_folder, mp3)
                   for mp3 in os.listdir(audio_folder)
                   if mp3.endswith(".mp3")
                   ]
    audios = []

    for mp3 in os.listdir(audio_folder):
        if mp3.endswith(".mp3"):
            # print(mp3)
            audio = MP3("redditpost/" + mp3)
            print(f"{audio.info.length},")
            durations.append(audio.info.length)

    for audio in audio_files:
        audios.append(AudioFileClip(audio))

    clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, durations = durations)
    new_audioclip = concatenate_audioclips(audios)
    clip.audio = new_audioclip
    clip.write_videofile(name + '.mp4', fps = 30, codec = 'libx264', bitrate = '1200000')
