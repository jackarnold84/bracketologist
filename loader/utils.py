import re


def clean_text(text, allowed='\s!@#$&()\\-`.+,/\"'):
    rgx = '[^a-zA-Z0-9%s]' % allowed
    return re.sub(rgx, '', text)
