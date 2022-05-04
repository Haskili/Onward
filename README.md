<h1 align="center">Onward</h1> 
  <p align="center">
    An adaptive Python progress-bar
    <br/><br/>
    [<a href="https://docs.python.org/3/library/concurrency.html">Concurrent Documentation</a>]
    [<a href="https://docs.python.org/3/library/asyncio.html">AsynchIO Documentation</a>]
    [<a href="https://github.com/Haskili/Onward/issues">Issues</a>]
  </p>
</p>
<br></br>

## Overview

Onward is an adaptive Python progress-bar designed to be easily re-implemented in whatever ("normal"/`concurrent`/`asyncio`/etc.) application it's needed in. All that's required of the developer is to re-implement this in their own project is to derive their own class from the base class in `progess.py` (based on the libraries being used), and then update the `refresh(...)` member function as needed to pipe output to whatever source is desired. 

<br>
<p align="center"><img src = "https://i.imgur.com/ELo4Jf0.gif" alt ="" width="90%"></p>
<br>

Shown above is an example in the `progress_stdout.py` file, where the standard output is used as the chosen output device for the progress bar, with both `concurrent` and `asyncio` examples provided. To verify, please use the provided file `run_tests.py` with the argument(s) `-c` and `-a` for testing methods using the `concurrent` and `asyncio` libraries respectively.
<br></br>

## Requirements

<img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLgwjF2JFQ-jvZn53x4bIhemYv7dLQKROIVg&usqp=CAU" alt ="" width="20%" height="20%">
The only external dependency is NumPy, which is utilized in multiple parts of `progress.py`, making it a hard requirement for the code.