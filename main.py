import time
from constants import PART_TWO, PART_ONE
from day_runner import run


#######################################################################################################################
# Main function
#######################################################################################################################
def __main__():
    day = 8
    ##################
    print("------------------------------------------------------------------")
    print("Running Part 1 [TEST]")
    run(day, PART_ONE, True)
    print("------------------------------------------------------------------")
    print("Running Part 1")
    run(day, PART_ONE)

    print("------------------------------------------------------------------")
    print("Running Part 2 [TEST]")
    run(day, PART_TWO, True)
    print("------------------------------------------------------------------")
    print("Running Part 2")
    run(day, PART_TWO)
    ##################
    pass


#######################################################################################################################
# Process
#######################################################################################################################
if __name__ == "__main__":
    # Start time of the program
    start = time.time()

    # Main functionality
    __main__()

    # End time of the program
    end = time.time()
    # Running time of the program
    print("Program ran for: ", end - start, "seconds.")
