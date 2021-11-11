def func1(normal,*args,**kwargs):
    print("This is a Normal Argument\n")
    print(normal,"\n")
    print("This is a *args Argument\n")
    for item in args:
        print(item,"\n")
    print("This is a **kwargs Argument\n")
    print(kw)
har=["Harry","Rohan","Hammad","Skillf","The Programmer"]
normal="I Am A Normal Argument"
kw={"Rohan":"Monitor","Harry":"Fittness Trainer"}
func1(normal,*har,**kw)

