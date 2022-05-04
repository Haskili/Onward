import sys


# Define the function being processed
def testing_function(input_data):
    from time import sleep
    from random import randint
    sleep(randint(1, 3))
    return input_data


# Define the function testing 
# concurrent-based execution
def concurrent_test():

    # Import requirements
    from concurrent.futures import as_completed, ProcessPoolExecutor
    from progress_stdout import stdout_standard

    # Define the input data
    DATA = [task for task in range(0, 10)]

    # Initialize the status bar
    state = stdout_standard(len(DATA))
    state.initialize()

    # Execute tasks
    with ProcessPoolExecutor(max_workers = 4) as executor:
        futures = [
            executor.submit(testing_function, data)
            for data in DATA
        ]

        for future in as_completed(futures):
            future.result()
            state.update()


# Define the function testing
# asyncio-based execution
async def asyncio_test():

        # Import requirements
        from asyncio import as_completed, get_event_loop, wrap_future
        from concurrent.futures import ProcessPoolExecutor
        from progress_stdout import stdout_asyncio

        # Define the input data
        DATA = [task for task in range(0, 10)]

        # Initialize the status bar
        state = stdout_asyncio(len(DATA))
        await state.initialize()

        # Execute tasks
        with ProcessPoolExecutor(max_workers = 4) as executor:
            loop = get_event_loop()

            futures = [
                wrap_future(executor.submit(testing_function, data), loop = loop)
                for data in DATA
            ]

            for future in as_completed(futures):
                result = await future
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