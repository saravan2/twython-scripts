import sys
import traceback
from twython import Twython, TwythonError
import twiden

def usage():
    print("twsefvfr.py \"search\"")


def main():
    try:
        if len(sys.argv) < 2:
            print("** Abort : Attempt again with message as second parameter **")
            usage()
            sys.exit(-1)
        twitter = Twython(twiden.twitter_app_key, twiden.twitter_app_secret, twiden.twitter_oauth_token, twiden.twitter_oauth_token_secret)
        search_results = twitter.search(q = sys.argv[1], count = 50)
        settings = twitter.get_account_settings()
        self = twitter.show_user(screen_name = settings['screen_name']) 
        for tweet in search_results["statuses"]:
            tw_user_id = tweet['user']['id']
            tw_id = tweet['id']
            # We don't want to retweet our tweets
            if tw_user_id != self['id']:
                # Quick hack to prevent re re tweet
                # Better way to do is filter results from your timeline tweets 
                #if tweet['retweet_count'] == 0:
                    #twitter.retweet(id = tw_id)
                    #twitter.create_favorite(id = tw_id)
                    #twitter.create_friendship(user_id = tw_user_id)
    except TwythonError as te:
        print(te)
    except SystemExit as se:
        sys.exit(se)
    except:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

if __name__ == "__main__":
    main() 
