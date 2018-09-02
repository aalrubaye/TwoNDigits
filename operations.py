__author__ = 'Abdul Rubaye'
from random import randint
import datetime
import xlwt


def random(n):
    start_range = 10**(n-1)
    end_range = (10**n)-1
    return randint(start_range, end_range)


def run_arithmetic_operations(pid, n_digits):

    # Prepares the excel sheet to write the results into
    results = xlwt.Workbook(encoding="utf-8")
    sheet1 = results.add_sheet(str(n_digits) + "_digits_Sheet")

    # Finding the remainder of dividing the PID # by 4
    # The remainder will be used later to specify the operation type
    remainder = pid % 4 # 24 bytes

    # Running the operation 1000 times as it is asked in the assignment
    for i in range (0, 1000):
        # Finding the two random numbers of the length "n_digits"
        operand_1 = random(n_digits)
        operand_2 = random(n_digits)

        # Gets the time of starting the operation
        start_time = datetime.datetime.now()

        # Based on the remainder, we select the appropriate operator
        if remainder == 0:
            result = operand_2 + operand_1 # 2 bytes for results
        elif remainder == 1:
            result = operand_2 - operand_1
        elif remainder == 2:
            result = operand_2 * operand_1
        else:
            result = operand_2 / operand_1

        # Finds the elapsed time
        elapsed_time = datetime.datetime.now() - start_time

        # Writes the results to an excel sheet to plot the result afterwards
        sheet1.write(i,0, elapsed_time.microseconds)

    # save into xls file
    results.save("div_Results_of_"+str(n_digits)+".xls")


# The main function
if __name__ == "__main__":
    # PID, you need to change the number to a PID number
    pid = 0000000  # the number is replaced with 00000... for privacy reasons

    # input size, number of digits
    n = 4  # can be changed to any other sizes

    # calling the function
    run_arithmetic_operations(pid, n)
