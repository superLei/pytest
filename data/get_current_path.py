import os

def get_cur_path():
    import os
    return os.path.dirname(__file__)
def get_cur_path1():
    import os
    return os.path.abspath(os.curdir)

def get_cur_path2():
    import sys
    return sys.argv[0]

if __name__ == '__main__':
    print "dayede"
    print get_cur_path()
    print get_cur_path1()
    print get_cur_path2()
    print "dayede"