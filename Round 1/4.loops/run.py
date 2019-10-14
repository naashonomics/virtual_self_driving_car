from browser import document, window, alert
window.indexedDB.deleteDatabase('brython_stdlib')
print("hello world!")
env = window.env

######################
# Start Learning Here
######################

def Move100StepsForward():
    numberOfTimes = range(100)
    for everySingleNumberInTheRange in numberOfTimes:
        print(everySingleNumberInTheRange)
        env.step(0)

Move100StepsForward()


#######################
# End Learning Here
#######################
