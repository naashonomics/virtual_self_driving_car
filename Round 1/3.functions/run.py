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

def Move50StepsForward():
    Move10StepsForward()
    Move10StepsForward()
    Move10StepsForward()
    Move10StepsForward()
    Move10StepsForward()


Move50StepsForward()
Move50StepsForward()
Move50StepsForward()
Move50StepsForward()

#######################
## End Learning Here
#######################