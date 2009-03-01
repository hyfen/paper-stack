import datetime

# seconds | minutes | hours & minutes | days | weeks 
def fminute(seconds):
    #if seconds < 120:
    #    ret = '1 mine'
    #else:
    ret = ''
    if seconds > 59:
        ret = '%d min' % (seconds / 60)
    return ret

def as_time_ago(dtime):
    td = datetime.datetime.utcnow() - dtime
    ret = ''
    hour = 60 * 60
    if not td.days:
        if td.seconds < 60:
            if td.seconds == 1:
                ret = '1s'
            else:
                ret = '%ds' % td.seconds
        elif td.seconds < hour:
            ret = fminute(td.seconds)
        else:
            if td.seconds < hour * 2:
                ret = '1 hr'
            else:
                ret = '%d hrs' % (td.seconds / hour)
                                        # only show min for <= 6 hrs
            if td.seconds % hour != 0 and (td.seconds / hour) < 7:
                ret += ' ' + fminute(td.seconds % hour)
    elif td.days < 7:
        if td.days == 1:
            ret = '1 day'
        else:
            ret = '%d days' % td.days
    else:
        if td.days == 7:
            ret = '1 week'
        else:
            ret = '%d weeks' % (td.days / 7)

    return ret + ' ago'



import cgi
import re

# calling this should not be filtered!
re_string = re.compile(r'(?P<htmlchars>[<&>])|(?P<space>^[ \t]+)|(?P<lineend>\r\n|\r|\n)|(?P<protocal>(^|\s)((http|ftp)://.*?))(\s|$)', re.S|re.M|re.I)
def plaintext2html(text, tabstop=4):
    #text = web.websafe(text) # unnecessary?
    # does this do a good enough job protecting?
    #    i think so but i'm no expert..
    def do_sub(m):
        c = m.groupdict()
        if c['htmlchars']:
            return cgi.escape(c['htmlchars'])
        if c['lineend']:
            return '<br />'
        elif c['space']:
            t = m.group().replace('\t', '&nbsp;'*tabstop)
            t = t.replace(' ', '&nbsp;')
            return t
        elif c['space'] == '\t':
            return ' '*tabstop;
        else:
            url = m.group('protocal')
            if url.startswith(' '):
                prefix = ' '
                url = url[1:]
            else:
                prefix = ''
            last = m.groups()[-1]
            if last in ['\n', '\r', '\r\n']:
                last = '<br>'
            # handle too long urls that firefox 2 won't wrap
            url2 = url
            display_url = ""
            while len(url2) > 78:
                display_url += url2[:78] + " "
                url2 = url2[78:]
            display_url += url2
            return '%s<a href="%s">%s</a>%s' % (prefix, url, display_url, last)
    return re.sub(re_string, do_sub, text)


