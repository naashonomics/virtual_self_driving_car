print("hello world!")
from browser import document, window, alert
env = window.env

######################
# Start Learning Here
######################
def Move10StepsForward():
    env.step(0)
    env.step(0)
    env.step(0)
    env.step(0)
    env.step(0)
    env.step(0)
    env.step(0)
    env.step(0)
    env.step(0)
    env.step(0)

def Move50StepsForware():
    Move10StepsForward()
    Move10StepsForward()
    Move10StepsForward()
    Move10StepsForward()
    Move10StepsForward()

Move50StepsForware()

# Move10StepsForward()
# Move10StepsForward()
# Move10StepsForward()
# Move10StepsForward()
# Move10StepsForward()
# Move10StepsForward()
# Move10StepsForward()
# Move10StepsForward()
# Move10StepsForward()
# Move10StepsForward()

#######################
## End Learning Here
#######################