print("hello world!")
from browser import document, window, alert, aio
window.indexedDB.deleteDatabase('brython_stdlib')
env = window.env

async def sleep():
	await aio.sleep(1)

######################
# Start Learning Here
######################

def MoveStepsForward(ourChoiceOfANumber):
    numberOfTimes = range(ourChoiceOfANumber)
    for everySingleNumberInTheRange in numberOfTimes:
        print(everySingleNumberInTheRange)
        env.step(0)

async def main():
	MoveStepsForward(50)
	await sleep()
	MoveStepsForward(100)
	await sleep()
	MoveStepsForward(20)

#######################
## End Learning Here
#######################

aio.run(main())