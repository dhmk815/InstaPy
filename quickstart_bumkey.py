""" Quickstart script for InstaPy usage """

# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace


# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

# get an InstaPy session!

#session = InstaPy(username="lexus8545", password="yl921227@")
session = InstaPy(username="daebeom.j", password="baboisdaebeom")
session.set_comments(comments=['Nice photo!', 'Great!', 'Gorgeous!', 'Love it!'])
session.set_do_comment(enabled=True, percentage=100)


#session.set_do_follow(enabled=True, percentage=100)
# geckodriver_path="/Users/bumkeyman/dev/insta-auto-liker/geckodriver")

with smart_run(session):
    # general settings
    #session.set_dont_include(["friend1", "friend2", "friend3"])

    # activity
    #session.like_by_tags(["제주신라호텔"], amount=5)
    # location of The Shilla Jeju
    #session.like_by_locations(["38005310"], amount=10)
    # # location of 네스트호텔
    # session.like_by_locations(["404210993"], amount=100)

    # activity: like_by_users w/ taggedImages
    # session.like_by_users(["forloveandlemons"], amount=10, user_tagged=True)

    # activity: 
    

