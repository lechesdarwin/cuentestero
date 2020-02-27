# coding=utf8
# (@(\w+))
# http://twitter.com/$2
# take gropu 2
# parser url and opase name
# (#(\w+))
# (https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*))

# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"(@(\w+))"

test_str = "hola mi name is @klasdha perknwefk @asndasjk #jkas #klhas kjewqioejhqwiod http://asd.com asdklhqwkl en http://ww.com dwqdhqw @dwde"

subst = "<a href=\"https://twitter.com/\\2\" target=\"_blank\">\\1</a>"
# You can manually specify the number of replacements by changing the 4th argument
result = re.sub(regex, subst, test_str, 0, re.IGNORECASE,re.UNICODE)

if result:
    print (result)

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.

regex = r"(#(\w+))"

test_str = "hola mi name is <a href=\"https://twitter.com/klasdha\" target=\"_blank\">@klasdha</a> perknwefk <a href=\"https://twitter.com/asndasjk\" target=\"_blank\">@asndasjk</a> #jkas #klhas kjewqioejhqwiod http://asd.com asdklhqwkl en http://ww.com dwqdhqw <a href=\"https://twitter.com/dwde\" target=\"_blank\">@dwde</a>"

subst = "<a href=\"https://twitter.com/hashtag/\\2\" target=\"_blank\">\\1</a>"

# You can manually specify the number of replacements by changing the 4th argument
result = re.sub(regex, subst, test_str, 0, re.IGNORECASE|re.UNICODE)

if result:
    print (result)

# the above tag defines encoding for this document and is for Python 2.x compatibility
regex = r"[^\'\"](https?:\/\/((www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6})\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*))"

test_str = "hola mi name is <a href=\"https://twitter.com/klasdha\" target=\"_blank\">@klasdha</a> perknwefk <a href=\"https://twitter.com/asndasjk\" target=\"_blank\">@asndasjk</a> <a href=\"https://twitter.com/hashtag/jkas\" target=\"_blank\">#jkas</a> <a href=\"https://twitter.com/hashtag/klhas\" target=\"_blank\">#klhas</a> kjewqioejhqwiod http://asd.com/kjdka?asa=asdj asdklhqwkl en http://ww.com dwqdhqw <a href=\"https://twitter.com/dwde\" target=\"_blank\">@dwde</a>"

subst = "<a href=\"\\1\" target=\"_blank\">\\2</a>"

# You can manually specify the number of replacements by changing the 4th argument
result = re.sub(regex, subst, test_str, 0, re.IGNORECASE|re.UNICODE)

if result:
    print (result)

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
