#!/home/ec2-user/anaconda3/bin/python3
import sys
import traceback
import time
from twython import Twython, TwythonError
import twiden

def usage():
    print("twdelq.py \"search\" <optional count>")
    print("Advanced search queries eg : from:<screen name> AND +filter:retweets")

def main():
    try:

        notDeleted = 0
        _count = -1

        # Command line processing
        if len(sys.argv) < 2:
            print("** Abort : Attempt again with query as second parameter and optional count**")
            usage()
            sys.exit(-1)
        if len(sys.argv) >= 3:
            _count = int(sys.argv[2])
            if _count <= 0:
                usage()
                sys.exit(-1)
        if len(sys.argv) >= 4:
            print("Ignoring unwanted arguments")

        twitter = Twython(twiden.twitter_app_key, twiden.twitter_app_secret, twiden.twitter_oauth_token, twiden.twitter_oauth_token_secret)

        while True:
            qCount = 50 if (_count > 0 and _count > 50) else _count
            search_results = twitter.search(q = sys.argv[1], count = qCount)
            if (len(search_results["statuses"]) == 0):
                print("**Running search query now produced 0 tweets to delete **\n")
                break
            for tweet in search_results["statuses"]:
                tw_user_id = tweet['user']['id']
                tw_id = tweet['id']
                tw_user_mentions = tweet['entities']['user_mentions']
                print("Attempting to delete : {}".format(tweet['text']))
                try:
                    twitter.destroy_status(id = tw_id)
                except TwythonError as tei:
                    print("User id : {}\nTweet id : {}\nTweet : {}\nUser Mentions : {}\n**could not be deleted**\n".fortmat(tw_user_id, tw_id, tweet['text'], tw_user_mentions)) 
                    print(tei)
                    notDeleted += 1
                    pass

            time.sleep(60)

            if (_count < 0):
                continue

            _count = _count - qCount
            if (_count <= 0):
                break

        #End of while

        if notDeleted:
            print("** {} tweets could not be deleted **".fortmat(notDeleted))                  
    except TwythonError as te:
        print(te)
    except SystemExit as se:
        sys.exit(se)
    except:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

if __name__ == "__main__":
    main() 
