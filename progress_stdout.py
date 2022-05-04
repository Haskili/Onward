from progress import progress_standard, progress_asyncio


class stdout_standard(progress_standard):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def refresh(self, progression, completion, estimation, elapsed):
        """
        Refresh the status message with the attributes given

        Arguments:
                self (progress): The class object operated on
                progression (integer): Progression bar string
                completion (float): Percent completed iterations
                estimation (string): Estimated time remaining in seconds
                elapsed (string): Time elapsed since start initialization

        Returns:
                None

        Raises:
                None
        """

        # Generate the formatted strings for the task completion and
        # the (Elapsed/Estimated) timing events
        ratio = f"({self.iteration:03d}/{self.iterations:03d})"
        timing = f"[{elapsed}, {estimation}]"

        # Write out the updated status information
        print(f"\r\t{completion:5.1f}% |{progression}| {ratio} {timing}", end = '')

        # Check for end of iterations, which requires a flush
        if self.iteration == self.iterations:
            print('')


class stdout_asyncio(progress_asyncio):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    async def refresh(self, progression, completion, estimation, elapsed):
        """
        Refresh the status message with the attributes given

        Arguments:
                self (progress): The class object operated on
                progression (integer): Progression bar string
                completion (float): Percent completed iterations
                estimation (string): Estimated time remaining in seconds
                elapsed (string): Time elapsed since start initialization

        Returns:
                None

        Raises:
                None
        """

        # Generate the formatted strings for the task completion and
        # the (Elapsed/Estimated) timing events
        ratio = f"({self.iteration:03d}/{self.iterations:03d})"
        timing = f"[{elapsed}, {estimation}]"

        # Write out the updated status information
        print(f"\r\t[25m{completion:5.1f}% |{progression}| {ratio} {timing}", end = '')

        # Check for end of iterations, which requires a flush
        if self.iteration == self.iterations:
            print('')