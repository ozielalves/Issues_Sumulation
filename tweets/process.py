from contextlib import redirect_stdout
import re

match = re.compile(r'RT (@[A-Za-z0-9_]*).*(https:\/\/[t|.A-Za-z0-9/]+)')
fake_newers = []

with open("tweets.in", encoding="utf-8") as f:
    tweets = [line.strip() for line in f.readlines()]
    for i in tweets:
        matches = re.findall(match, i)
        if matches:
            fake_newers.append([matches[0][0], matches[0][1]])
    
    with open("tweets.out", "w", encoding="utf-8") as f:
        with redirect_stdout(f):
            for i in sorted(fake_newers):
                print('\t'.join(i))  