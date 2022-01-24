from gtts import gTTS

import env
import html


def makeaudio(limit, _id, language, tld):
    reddit = env.reddit
    submission = reddit.submission(id = _id)
    submission.comments.replace_more(limit = 1)  # itterates the more comments# 1 time
    print(submission.comments)
    f = open("screenshot/comments.html", "w", encoding = 'utf-8')
    f.write(html.hh())
    f.close()
    f = open("screenshot/comments.html", "a", encoding = 'utf-8')
    postauthor = submission.author
    postcontent = submission.selftext
    score = submission.score
    title = submission.title
    print('************************************')
    print(title)
    print('************************************')
    if postcontent == '':
        print('ding ding ding')
        postcontent = title
    else:
        print('dong')
        if len(postcontent) < 2:
            postcontent = title
        print(len(postcontent))
    print('************************************')
    htmltemp = html.header(0, title, postauthor, ' 10h', postcontent, score)
    f.write(htmltemp)
    myobj = gTTS(text = postcontent, lang = language, tld = tld)
    myobj.save("redditpost/" + str(0) + ".mp3")
    for idx, top_level_comment in enumerate(submission.comments):
        print(idx)
        print('---------------------------------------------------------------')
        print(f'Comment Id: {top_level_comment.id}')
        print(f'Comment Content: {top_level_comment.body}')
        print(f'Username: {top_level_comment.author}')
        print(f'Time Created UTC: {top_level_comment.created_utc}')
        print(
            f'Comment Score: {top_level_comment.score}')  # suppose we can break out of this loop when karma drops
        # below a set value??
        print('---------------------------------------------------------------')
        if idx == limit:
            break
        if top_level_comment.stickied is True:  # removes mod and stickied comments
            print('skipped')
            mytext = 'skipped'
            myobj = gTTS(text = mytext, lang = language, tld = tld)
            myobj.save("redditpost/" + str(idx + 1) + ".mp3")
            htmltemp = html.html(idx + 1, 'skipped', ' 10h', 'skipped', '0')
            f.write(htmltemp)
        else:
            mytext = top_level_comment.body
            myobj = gTTS(text = mytext, lang = language, tld = tld)
            myobj.save("redditpost/" + str(idx + 1) + ".mp3")
            htmltemp = html.html(idx + 1, top_level_comment.author, ' 10h', top_level_comment.body,
                                 top_level_comment.score)
            f.write(htmltemp)
    f.write(html.hb())
    f.close()
