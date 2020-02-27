(@(\w+))
http://twitter.com/$2
take gropu 2
parser url and opase name
(#(\w+))
(https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*))

import re

regex = r"(@(\w+))"
test_str = "hola mi name is @klasdha perknwefk @asndasjk #jkas #klhas kjewqioejhqwiod http://asd.com asdklhqwkl en http://ww.com dwqdhqw @dwde"
subst = "<a href=\"https://www.twitter/\\2 target=\"_blank\">\\1</a>"
i = re.match(regex,test_str)
# You can manually specify the number of replacements by changing the 4th argument
result = re.sub(regex, subst, test_str, 0)
if result:
    print

regex = r"(https?:\/\/(www\.)?([-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6})\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*))"

test_str = ("hola mi name is <a href=\"https://www.twitter/klasdha target=\"_blank\">@klasdha</a> perknwefk <a href=\"https://www.twitter/asndasjk target=\"_blank\">@asndasjk</a> #jkas #klhas kjewqioejhqwiod http://asd.com/sasa asdklhqwkl en http://ww.com dwqdhqw <a href=\"https://www.twitter/dwde target=\"_blank\">@dwde</a>\n"
	"http://ww.com asdas http://ww.com \n")

subst = "<a href=\"\\1\" target=\"_blank\">\\3</a>"

# You can manually specify the number of replacements by changing the 4th argument
result = re.sub(regex, subst, test_str, 0)

if result:
    print (result)

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.