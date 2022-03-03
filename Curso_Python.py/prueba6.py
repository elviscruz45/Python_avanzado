'''def print_args(farg, *args):
   print("formal arg: %s" % farg)
   for arg in args:
       print("another positional arg: %s" % arg)
       
       
       
print_args(1, "two", 3)

'''






def example(a, **kw):
    print (kw)


example(3, c=4) # => {'b': 3, 'c': 4}