#!/home/ec2-user/anaconda3/bin/python3
import sys
import traceback
import time
from twython import Twython, TwythonError
import twiden

def usage():
    print("Proper usage : \ntwdelall.py")

def main():
    try:

        notDeleted = 0

        # Command line processing
        if len(sys.argv) > 1:
            usage()
            printf("Ignoring unwanted arguments")

        twitter = Twython(twiden.twitter_app_key, twiden.twitter_app_secret, twiden.twitter_oauth_token, twiden.twitter_oauth_token_secret)

        while True:

            timeline = twitter.get_user_timeline(count = 50)

            if (len(timeline) == 0):
                print("** No tweets left to delete **")
                break

            for tweet in timeline:
                print(tweet)
                break
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
