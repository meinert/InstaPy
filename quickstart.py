from instapy import InstaPy

session = InstaPy(username='ppoulsen2018', password='pdSA1209')

session.login()

session.like_by_tags(['løb'], amount=10, media='Photo')

session.end()