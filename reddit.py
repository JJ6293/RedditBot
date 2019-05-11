#Created by Justin James
#importing tools 
import praw
import config
import time
import websocket
import os


#logging into reddit api
def bot_login():
	print ("Logging in")
    #assigning reddit config to r
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "killa bot")
	print ("Successfully Logged in")

	return r

def run_bot(r, replies):
    print ("gathering comments")
    #obtaining comments from a specific subreddit for keywords
    for comment in r.subreddit('CoDCompetitive').comments(limit=10):
        #if a user comments the string in the specified subreddit, reply with humorous quote along with a hyperlink to a youtube video IF the comment was not already made by the same user OR the keyword was said by the bot itself (spam prevention)
        if "Killa" in comment.body and comment.id not in replies and comment.author != r.user.me():
            print ("String found " + comment.id)
            comment.reply("Adam Sloss is the reason guacamole is now free at chipotle. He walked in, ordered a burrito, and asked for guac. The lady said \"sir, just so you know, guac is extra.\" Adam took off his hat, scratched his head and said \"what nega? It's literally right next to all the free shit dawg I'm not paying extra\" *dolphin laugh.* From that day, chipotle never charged for guac again. The Supreme Court calls it \"sloss vs guac\" and it will be in history books until the end of time.\n [WOOOOOOOOOOOOOOO](https://www.youtube.com/watch?v=NadRcgS4fQo)")
            print ("Replied to comment to id code:" + comment.id)
            
            #adds comment id to "replies"
            replies.append(comment.id)
            
            #prints comment IDs that have been replied to
            print(replies)
            
            #open text file with comment IDs
            with open("replies.txt", "a") as file:
                file.write(comment.id + "\n")
    
    print ("Sleep")
    #Sleep for 60 seconds
    time.sleep(60)

#retrieves comments saved in text file
def saved_comments():
    
    
    if not os.path.isfile("replies.txt"):
        replies = []
       
    else: 
        with open ("replies.txt", "r") as file:
            replies = file.read()
            replies = replies.split("\n")
            replies = list(filter(None, replies))

    return replies


r = bot_login()
replies = []
replies = saved_comments()
print (replies)

while True:
	run_bot(r, replies)