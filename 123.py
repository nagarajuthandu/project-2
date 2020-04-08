def test(x,y,*args):
        print(args)
        print(x,y)
	x=0
        for val in args:
            x=x+val
        return x
