# coding=utf8
# (@(\w+))
# http://twitter.com/$2
# take gropu 2
# parser url and opase name
# (#(\w+))
# (https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*))
import re
import random
import requests



def down_img(link, carp):
    regex = r"([\w-]+\.(?:jpg|jpeg|svg|png|gif|webp|webp))"
    m = re.search(regex, link)
    name = ""
    if m:
        name = m.group(1)
    else:
        name = str(random.getrandbits(32))
    h = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Mobile Safari/537.36"}
    data = requests.get(link, headers=h)
    with open("{}/{}".format(carp, name), "wb") as f:
        f.write(data.content)
        data.close()

def rrss(test_str):
    regex = r"(@(\w+))"
    subst = "<a rel='nofolow norefer' href=\"https://twitter.com/\\2\" target=\"_blank\">\\1</a>"
    result = re.sub(regex, subst, test_str, 0, re.IGNORECASE | re.UNICODE)
    if result:
        test_str = result
    regex = r"(#(\w+))"
    subst = "<a href=\"https://twitter.com/hashtag/\\2\" target=\"_blank\">\\1</a>"
    result = re.sub(regex, subst, test_str, 0, re.IGNORECASE | re.UNICODE)
    if result:
        test_str = result
    regex = r"[^\'\"](https?:\/\/((www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6})\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*))"
    subst = " <a href=\"\\1\" target=\"_blank\" rel='nofollow norefer'>\\2</a>"
    result = re.sub(regex, subst, test_str, 0, re.IGNORECASE | re.UNICODE)
    if result:
        test_str = result
    return test_str
    # Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.