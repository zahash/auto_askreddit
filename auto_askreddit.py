import praw
import requests
import os
import argparse

# give it whatever name you like
user_agent = "My askreddit bot"

# https://www.youtube.com/watch?v=wAN8b38U_8c
# watch the above video to know how to get client_id and client_secret
client_id = "xxxxx"
client_secret = "xxxxx"

# your reddit username and password
username = "xxxxx"
password = "xxxxx"


reddit = praw.Reddit(
    user_agent=user_agent,
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
)

reddit.validate_on_submit = True

if __name__ == "__main__":
    os.environ["NO_PROXY"] = "127.0.0.1"
    
    ap = argparse.ArgumentParser(allow_abbrev=False)
    ap.add_argument("-n", "--nsamples", default=1, type=int, help="number of titles to generate")
    ap.add_argument("-t", "--temperature", default=0.9, type=float, help="How creative must the titles be? (values between 0 and 1)")
    ap.add_argument("-b", "--batch_size", default=1, type=int, help="How many titles to generate in one iteration? (more batch size is faster but requires more ram)")
    
    args = ap.parse_args()
        

    PARAMS = {"nsamples": args.nsamples, "temperature": args.temperature, "batch_size": args.batch_size}

    print("Getting titles ...")
    response = requests.get(url="http://127.0.0.1:5000/generate", params=PARAMS)
    titles = response.json().get("titles")

    for title in titles:
        print("\n", title)
        if input("post this title (y/n): ").lower() == "y":
            print("posting ...")
            reddit.subreddit("askreddit").submit(title, selftext="")
            
