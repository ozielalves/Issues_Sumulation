from contextlib import redirect_stdout
import re

reUrls = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
reUser = r'@\w+'
fake_newers = []

with open("tweets.in", encoding="utf-8") as f:
    tweets = [line.strip() for line in f.readlines()]
    rtts = [ i for i in tweets if i[:4] == 'RT @' ]
    for i in rtts:
        Url = re.findall(reUrls, i)
        if Url:
            User = re.findall(reUser, i)
            fake_newers.append([User[0], Url[0]])    
    
with open("tweets.out", "w", encoding="utf-8") as f:
    with redirect_stdout(f):
            for i in sorted(fake_newers):
                print('\t'.join(i))