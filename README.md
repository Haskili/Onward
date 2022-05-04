# Onward
Python progress-bar designed to be easily re-implemented in whatever ("normal"/`concurrent`/`asyncio`/etc.) application it's needed in. All that's required of the developer is to re-implement this in their own project is to derive their own class from the base class in `progess.py` (based on the libraries being used), and then update the `refresh(...)` member function as needed to pipe output to whatever source is desired. 

An example is shown in the `progress_stdout.py` file, where the standard output is used as the chosen output device for the progress bar, with both `concurrent` and `asyncio` examples provided. To verify, please use the provided file `run_tests.py` with the argument(s) `-c` and `-a` for testing methods using the `concurrent` and `asyncio` libraries respectively.