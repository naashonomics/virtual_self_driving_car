def MoveManyStepsForward(numberOfSteps):
    for everySingleNumberInTheRange in range(numberOfSteps):
        env.step(0)

async def main():
        MoveManyStepsForward(50)
        await sleep()
        MoveManyStepsForward(150)