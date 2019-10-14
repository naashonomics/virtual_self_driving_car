
print("hello world!")
from browser import document, window, alert, aio
env = window.env

for initialMove in range(5):
    env.step(0)

async def sleep():
    await aio.sleep(0.2)

def isRoadAheadAvailable():
        lidarState = env.getState().lidar
        lidarState.reverse()
        carFrontLidarLine = lidarState[2]  # Radar line rigth in front of us
        if (carFrontLidarLine == [0,0,0,0,0]): # We're about to hit something!
            return False
        else: # Road is clear!
            return True

######################
# Start Learning Here
######################

def MoveManyStepsForward(numberOfSteps):
    for everySingleNumberInTheRange in range(numberOfSteps):
        env.step(0)

async def main():
    numberOfSteps = 0
    while (isRoadAheadAvailable() == True):
        MoveManyStepsForward(10)
        numberOfSteps += 10
        await sleep()
        
    if (numberOfSteps > 700):
        print("Fill some gas!")
    else:
        print("You have enough gas")
  ### Ending the program
#######################
## End Learning Here
#######################
aio.run(main())








                
            