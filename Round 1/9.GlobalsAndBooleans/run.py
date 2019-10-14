from browser import document, window, alert, aio
print("hello world!")
env = window.env
env.step(0)

async def sleep():
    await aio.sleep(0.2)


def isRoadAheadAvailable():
    lidarState = env.getState().lidar
    lidarState.reverse()
    carFrontLidarLine = lidarState[2]  # Radar line rigth in front of us
    if (carFrontLidarLine == [0, 0, 0, 0, 0]):  # We're about to hit something!
        return False
    else:  # Road is clear!
        return True

async def Turn(direction):
    if (direction == 'RIGHT'):
        env.step(-1)
    elif (direction == 'LEFT'):
        env.step(1)
    await sleep()

fullTankConstant = 1450 # A full tank of gas is 900 steps
######################
# Start Learning Here
######################

carGasTank = fullTankConstant

def MoveManyStepsForward(numberOfSteps):
    for everySingleNumberInTheRange in range(numberOfSteps):
        env.step(0)

async def moveForwardUntilNoMoreRoad():
    global carGasTank

    while (carGasTank > 0 and isRoadAheadAvailable() == True):
        MoveManyStepsForward(30)
        await sleep()
        carGasTank -= 30
    

async def moveForwardAndTurn():
    await moveForwardUntilNoMoreRoad()
    await Turn('LEFT')



async def main():
    global carGasTank
    while(carGasTank > 0):
        await moveForwardAndTurn()
         
    
    print("Program End")

aio.run(main())


#######################
# End Learning Here
#######################
