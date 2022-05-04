from numpy import linspace, average
from time import perf_counter, strftime, gmtime


class progress():
    def __init__(self, iterations, length = 25, marker = '█'):
        self.iterations = iterations
        self.length = length
        self.marker = marker

        self.iteration = 0
        self.checkpoints = linspace(1, iterations, length, dtype = int)
        self.timing = {
            "initialization": None,
            "step": None,
            "all": []
        }


    def initialize(self):
        """
        Initialize the progression information and call the class-specific
        version of 'self.refresh()' to refresh the status message

        Arguments:
                self (progress): The class object operated on

        Returns:
                None

        Raises:
                None
        """

        # Update the iteration amount
        self.iteration = 0

        # Update the timing information
        now = perf_counter()
        self.timing["step"] = now
        self.timing["initialization"] = now

        # Call the class-specific method for refreshing
        # the UI of the progress information
        self.refresh(
            progression = ''.join([' ' for index in range(self.length)]), 
            completion = 0.0, 
            estimation = 0,
            elapsed = 0
        )


    def update(self, amount = 1):
        """
        Update the iteration information and call the class-specific
        version of 'self.refresh()' to refresh the status message

        Arguments:
                self (progress): The class object operated on
                amount (integer): The amount of iterations since last update

        Returns:
                None

        Raises:
                None
        """

        # Update the iteration amount
        self.iteration += amount

        # Update the timing information
        now = perf_counter()
        step = now - self.timing["step"]
        self.timing["all"].append(step)

        # Generate the formatted string from the time elapsed
        elapsed = now - self.timing["initialization"]
        elapsed = f"{strftime('%M:%S', gmtime(int(elapsed)))}"

        # Calculate the estimated time remaining in seconds
        # and generate a corrosponding formatted string
        estimation = ((self.iterations - self.iteration) 
                            * average(self.timing["all"]))

        estimation = f"{strftime('%M:%S', gmtime(int(estimation)))}"

        # Calculate the percentage complete
        completion = (self.iteration/self.iterations) * 100.0

        # Generate the UI bar to be filled for each
        # index of 'self.checkpoints' that's exceeded
        # by the current value of 'self.iterations'
        progression = ''.join([
            ' ' if (self.iteration < self.checkpoints[index])
            else  self.marker 
            for index in range(self.length)
        ])

        # Call the class-specific method for refreshing
        # the UI of the progress information
        self.refresh(progression, completion, estimation, elapsed)

        # Update the timing delta for step times
        self.timing["step"] = now


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
        pass


class progress_asyncio(progress):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    async def initialize(self):
        """
        Initialize the progression information and call the class-specific
        version of 'self.refresh()' to refresh the status message

        Arguments:
                self (progress): The class object operated on

        Returns:
                None

        Raises:
                None
        """

        # Update the iteration amount
        self.iteration = 0

        # Update the timing information
        now = perf_counter()
        self.timing["step"] = now
        self.timing["initialization"] = now

        # Call the class-specific method for refreshing
        # the UI of the progress information
        await self.refresh(
            progression = ''.join([' ' for index in range(self.length)]), 
            completion = 0.0, 
            estimation = 0,
            elapsed = 0
        )


    async def update(self, amount = 1):
        """
        Update the iteration information and call the class-specific
        version of 'self.refresh()' to refresh the status message

        Arguments:
                self (progress): The class object operated on
                amount (integer): The amount of iterations since last update

        Returns:
                None

        Raises:
                None
        """

        # Update the iteration amount
        self.iteration += amount

        # Update the timing information
        now = perf_counter()
        step = now - self.timing["step"]
        self.timing["all"].append(step)

        # Generate the formatted string from the time elapsed
        elapsed = now - self.timing["initialization"]
        elapsed = f"{strftime('%M:%S', gmtime(int(elapsed)))}"

        # Calculate the estimated time remaining in seconds
        # and generate a corrosponding formatted string
        estimation = ((self.iterations - self.iteration) 
                            * average(self.timing["all"]))

        estimation = f"{strftime('%M:%S', gmtime(int(estimation)))}"

        # Calculate the percentage complete
        completion = (self.iteration/self.iterations) * 100.0

        # Generate the UI bar to be filled for each
        # index of 'self.checkpoints' that's exceeded
        # by the current value of 'self.iterations'
        progression = ''.join([
            ' ' if (self.iteration < self.checkpoints[index])
            else  self.marker 
            for index in range(self.length)
        ])

        # Call the class-specific method for refreshing
        # the UI of the progress information
        await self.refresh(progression, completion, estimation, elapsed)

        # Update the timing delta for step times
        self.timing["step"] = now


    async def refresh(self, progression, completion, estimation, elapsed):
        pass


class progress_stdout(progress):
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
        print(f"\t{completion:5.1f}% |{progression}| {ratio} {timing}", end = '\r')

        # Check for end of iterations, which requires a flush
        if self.iteration == self.iterations:
            print('')


class progress_stdout_asyncio(progress_asyncio):
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
        print(f"\t{completion:5.1f}% |{progression}| {ratio} {timing}", end = '\r')

        # Check for end of iterations, which requires a flush
        if self.iteration == self.iterations:
            print('')