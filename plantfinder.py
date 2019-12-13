import praw
import sys
import os

def login(cfg):
    """
    Returns reddit object for logging in.

    Param:
    Path to reddit.cfg file with client id,
                                 client secret, 
                                 user agent, 
                                 username, 
                                 password
    """
    with open('{}reddit.cfg'.format(cfg)) as config:
        x = config.read().splitlines()

    client_id = x[0]
    client_secret = x[1]
    user_agent = x[2]
    username = x[3]
    password = x[4]

    reddit = praw.Reddit(client_id=client_id,
                        client_secret=client_secret,
                        user_agent=user_agent,
                        username=username,
                        password=password,
                        )
    return reddit

cfgpath = 'C:/Users/Frankie/OneDrive/Programming/'

reddit = login(cfgpath)
# ======================================= VARIABLES ======================================= #
subreddits = ['bonsai', 'indoorgarden', 'houseplants', 'succulents', 'plants',]
plant = input("Enter the plant to search for: ")
time = input("Enter the timeframe ('hour', 'day', 'week', 'month', 'year', 'all'): ")
limit = int(input("Enter the number of posts to check (limit 1000): "))
# ========================================================================================= #


style = '<link rel="stylesheet" type="text/css" href="../fonts.css">\n<link href="https://fonts.googleapis.com/css?family=Roboto+Condensed&display=swap" rel="stylesheet">'



savefile = "data/{}_{}.html".format(plant, time)

if os.path.exists(savefile):
    os.remove(savefile)

with open(savefile, 'a', encoding='utf-8') as output:
    print(f'{style}', file=output)

for sub in subreddits:

    subreddit = reddit.subreddit(sub)
    print("\nSearching r/{} for {}".format(subreddit, plant))
    for x, submission in enumerate(subreddit.top(time_filter=time, limit=limit)):
        
        with open(savefile, 'a', encoding='utf-8') as output:
            if plant in submission.title.lower():
                print("Adding submission {} of {}...".format(x, limit))
                print(f'<h1 id="kappa">{submission.title}</h1><br><a href="https://old.reddit.com{submission.permalink}"><img src="{submission.url}"onerror=this.src="https://static.umotive.com/img/product_image_thumbnail_placeholder.png" class="center"></a><br><h2 id="kappa2">u/{submission.author}<br>r/{sub}<br>Score: {submission.score}', file=output)

input("\nDone!\nPress enter to exit.")