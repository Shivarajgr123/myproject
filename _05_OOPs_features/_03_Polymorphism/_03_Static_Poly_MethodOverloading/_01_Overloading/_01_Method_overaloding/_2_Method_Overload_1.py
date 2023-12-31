class FeedbackForm:

    def __init__(self):
        pass

    def feedback(self, rating=10, comments=None):   # method overloading (function overloading)
        print("Feedback is :", rating, ", ", comments)

# Method overloading
feed = FeedbackForm()

feed.feedback()   # Default args
feed.feedback(4)  # Default args
feed.feedback(9, 'Good')  # Positional args
feed.feedback(comments='Very Bad')  # keyword args

'''
In java/.net
def feedback(self):
    pass

def feedback(self, rating):
    pass
    
def feedback(self, rating, comments):
    pass

def feedback(self,comments):
    pass
    
feedback(10)
'''

#Function overloading
def sum(a=10, b=20, c=30):
    print("Sum is ", a+b+c)

# Overloading - Depends on how many arguments we are passing
sum()
sum(15)
sum(15, 25)
sum(15, 25, 35)
sum(b=200, a=100)
sum(b=200, c=300)
sum(a=100, c=300)
sum(b=200, a=100, c=300)



def sum(x, y):
    print("AdditionL :", x+y)

sum(10,20)

def sum(x,y,z):
    print("AdditionL :", x + y + z)

sum(10,20,30)
sum(10,20)
