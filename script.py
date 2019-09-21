import random

#amount of random posts to fetch
post_limit = 10

#replace this with your script client id, secret etc.
#visit the praw docs for more information
reddit = praw.Reddit(client_id='YOUR_CLIENT_SCRIPT_ID', client_secret="YOUR_CLIENT_SCRIPT_SECRET", password='YOUR_REDDIT_USERNAME', user_agent='your random user agent', username='YOUR_REDDIT_PASSWORD')

#add more subreddits if you want to
subreddit_list = ["somebodycodethis", "ProgrammingPrompts"]

#get x new posts from a random subreddit
posts = reddit.subreddit(random.choice(subreddit_list)).new(limit=post_limit)

#trash method for chosing a random post
random_post_number = random.randint(0,post_limit)

for i , post in enumerate(posts):
    if i==random_post_number:
        print("successfully picked a random coding project from reddit...")
       
        #save the data to our output file, idea.txt
        output_file = open("idea.txt","w")
        output_file.write("idea name: " + post.title + "\n")
        output_file.write("amount of comments: " + str(post.num_comments)+ "\n")
        output_file.write("post score: " + str(post.score)+ "\n")
        output_file.write("post text: " + post.selftext)
        output_file.close()
        print("successfully wrote data to file 'idea.txt'.")
