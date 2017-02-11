##########################################################################################################################################################
#
#       File Name     :        grammar_check_bot.py
#       Description   :        Replies with grammar advice when a reddit user uses "could/would/should have" wrong.
#       Author        :        Aniruth Oblah
#
##########################################################################################################################################################

import praw
import config

reddit = praw.Reddit(user_agent=config.my_user_agent,
                     client_id=config.my_client_id,
                     client_secret=config.my_client_secret,
                     username=config.my_username,
                     password=config.my_password)


couldawouldashoulda = ['could of ', 'should of ', 'would of ']

reply_template = "It's not 'could of/would of/should of'. It's 'could have/should have/would have' (or could've, should've, or would've ). If you have received this reply mistakenly, please let me know. I'm working on making the world a better place by fixing one grammatical mistake at a time."




subreddit = reddit.subreddit('grammar_check_bot')
for submission in subreddit.hot(limit=10):
        #print(submission.title + submission.id)
        post = reddit.submission(id = submission.id)
        all_comments = post.comments.list()
        for comment in all_comments:
                print(comment.body)
                if any(trigger in comment.body for trigger in couldawouldashoulda):
                        #comment.reply(reply_template)
                        print(reply_template)                                 
