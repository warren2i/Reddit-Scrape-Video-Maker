import re
import make_audio_for_each_comment
import find_and_save_each_comment_as_screenshot
import vid_creater
import env

#***variables***#
subreddit = "Showerthoughts" # subreddit to scrape
nothreads = 25 # how many threads to scrape?
nocomments = 5 # how many comments to scrape?



reddit = env.reddit


def make(thread_id,commentlimit):
        submission = reddit.submission(id=thread_id)
        postcontent = (submission.selftext)
        score = (submission.score)
        title = (submission.title)
        if postcontent == "":
                postcontent = title
        regex = '''[^a-zA-Z0-9/ \+(\-){1,}]{1,}'''
        title = re.sub(regex, '', title)
        title = re.sub('[,/]', ' ', title) ## removed redundant escape chat /,
        make_audio_for_each_comment.makeaudio(commentlimit,thread_id,'en', 'ie')
        find_and_save_each_comment_as_screenshot.screenshotcomments(commentlimit)
        vid_creater.makevideo('finished/'+title[:99])
        f = open('finished/'+title[:99]+".txt", "w")
        f.write(postcontent)
        f.close()
#cleanup.clean()

subreddit = reddit.subreddit(subreddit)
for submission in subreddit.top(limit=nothreads):
        print(submission)
        make(submission.id, nocomments)
