# accessign gloa vaiable inside function using global function.
# Global Keywird: Examples.

a = 16
def f1():
    a = 565
    print("value of a inside f1",a)
    print("globals a is",[globals()]['a'])

f1()
print("value of a outside f1",a)


#adding more complex examples:

count = 0

def f2():
    global count
    count += 1
    print("value of count inside f2", count)

f2()
print("value of count outside f2", count)
f2()
print("value of count outside f2", count)
