import sys


# Define the concurrent testing functions
def concurrent_function(input_data):
    from time import sleep
    from random import randint
    sleep(randint(1, 3))


def concurrent_test():

    # Import requirements
    from concurrent.futures import as_completed, ProcessPoolExecutor
    from progress import progress_stdout

    # Define the input data
    DATA = [task for task in range(0, 10)]

    # Initialize the status bar
    state = progress_stdout(len(DATA))
    state.initialize()

    # Execute tasks
    with ProcessPoolExecutor(max_workers = 4) as executor:
        futures = [
            executor.submit(concurrent_function, data)
            for data in DATA
        ]

        for future in as_completed(futures):
            future.result()
            state.update()


# Define the asyncio testing functions
async def asyncio_function(input_data):
    from asyncio import sleep
    from random import randint
    await sleep(randint(1, 3))


async def asyncio_test():

        # Import requirements
        from asyncio import as_completed
        from progress import progress_stdout_asyncio

        # Define the input data
        DATA = [task for task in range(0, 10)]

        # Define the tasks
        tasks = [asyncio_function(data) for data in DATA]

        # Start a progress bar for the values
        # across each collection process
        state = progress_stdout_asyncio(len(tasks))
        await state.initialize()

        # Launch each task and retrieve the results
        for task in as_completed(tasks):
            result = await task
            await state.update()


# Run the program driver
if __name__ == "__main__":

    # Run the test(s) as required
    if "-c" in sys.argv:
        concurrent_test()

    if "-a" in sys.argv:
        import asyncio
        asyncio.run(asyncio_test())

    if "-c" not in sys.argv and "-a" not in sys.argv:
        print("Please specify test type with '-c' and/or '-a'")