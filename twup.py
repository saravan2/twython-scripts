#!/home/ec2-user/anaconda3/bin/python3
import sys
import traceback
from twython import Twython, TwythonError
import twiden

def usage():
    print("twup.py \"<status>\"")


def main():
    try:
        if len(sys.argv) < 2:
            print("** Abort : Attempt again with message as second parameter **")
            usage()
            sys.exit(-1)
        if len(sys.argv[1]) > 140:
            print("** Abort : Attempt again with message less than 140 characters **")
            usage()
            sys.exit(-1)
        twitter = Twython(twiden.twitter_app_key, twiden.twitter_app_secret, twiden.twitter_oauth_token, twiden.twitter_oauth_token_secret)
        twitter.update_status(status = sys.argv[1])
    except TwythonError as te:
        print(te)
    except SystemExit as se:
        sys.exit(se)
    except:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

if __name__ == "__main__":
    main() 
