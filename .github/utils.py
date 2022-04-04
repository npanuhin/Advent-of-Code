import os


def mkpath(*paths):
    return os.path.normpath(os.path.join(*map(str, paths)))


def clamp(x, bottom, top):
    return bottom if x < bottom else top if x > top else x


def md_link(text, link):
    return "[{}]({})".format(text, link)
