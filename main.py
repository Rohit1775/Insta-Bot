# first install insta loader (copy paste the below line in your cmd)
# pip intsall instaloader

import instaloader

insta = instaloader.Instaloader()

acc = 'mahi7781'

insta.download_profile(acc, profile_pic_only=False)
