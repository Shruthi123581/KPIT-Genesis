
def do_twice(f,v):
    f(v)
    f(v)

def print_spam(s):
    print(s)
    print(s)

def print_twice(bruce):
    print(bruce)
    print(bruce)

do_twice(print_spam,'shruthi')
do_twice(print_twice,'spam')


def do_four(f,v):
    do_twice(f,v)
    do_twice(f,v)


do_four(print_spam,"shruthi")



