import pprint
from browser import document, window, alert, aio

print("hello world!")
env = window.env


async def PrintNiceMessage(message):
    await window.swal(message, "", "success")

######################
# Start Learning Here
######################


async def MoveManyStepsForwardSlowly(numberOfSteps):
        stepSize = 20 # Changed for this version        
        stepChunks, leftover = divmod(numberOfSteps, stepSize)

        for everySingleNumberInTheRange in range(stepChunks):
                await aio.sleep(0.1) # Changed for this version
                MoveManyStepsForward(stepSize)

        MoveManyStepsForward(leftover)


def MoveManyStepsForward(numberOfSteps):
    for everySingleNumberInTheRange in range(numberOfSteps):
        env.step(0)


async def TurnLeftSlowly():
        env.step(1)
        await aio.sleep(0.5)
        env.step(1)
        await aio.sleep(0.5)


async def MoveForwardAsLongAsRoadIsClear():
        roadIsClear = True
        while roadIsClear == True:
                await MoveManyStepsForwardSlowly(50)
                lidarState = env.getState().lidar
                lidarState.reverse()
                carFrontLidarLine = lidarState[2]
                lineSum = carFrontLidarLine[0]+carFrontLidarLine[1]+carFrontLidarLine[2]+carFrontLidarLine[3]+carFrontLidarLine[4]
                if lineSum == 0:
                        roadIsClear = False

async def main():
        totalNumberOfStepsCounter = 0        
        stepIncrementSize = 50
        MovingAndTurningIsPossible = True
        while MovingAndTurningIsPossible == True:
                await MoveForwardAsLongAsRoadIsClear()
                await TurnLeftSlowly()
                lidarState = env.getState().lidar
                lidarState.reverse()
                middleLine = [lidarState[0][2], lidarState[1][2], lidarState[2][2], lidarState[3][2], lidarState[4][2]]
                middleLineSum = sum(middleLine)
                if middleLineSum == 0:
                        MovingAndTurningIsPossible = False
        
        

aio.run(main())


#######################
# End Learning Here
#######################
