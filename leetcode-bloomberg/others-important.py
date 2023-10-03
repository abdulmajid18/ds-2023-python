"""

Given the time operation hours of different banks, you have to test whether a transaction is valid or not. For a transaction to be valid it has to fall between the operating hours of the bank.

Input example - operation hours of different banks

04:20 - 12:30
19:00 - 21:45
14:00 - 17:30
12:30 - 14:00

Test - 11:00 - 17:30
Output - true



"""



def is_valid_transaction(operation_hours, transaction_time):
    # Convert time strings to minutes since midnight
    def time_to_minutes(time_str):
        hours, minutes = map(int, time_str.split(':'))
        return hours * 60 + minutes

    transaction_start = time_to_minutes(transaction_time[0])
    transaction_end = time_to_minutes(transaction_time[1])

    for hours in operation_hours:
        start_time = time_to_minutes(hours[0])
        end_time = time_to_minutes(hours[1])

        if start_time <= transaction_start <= end_time and start_time <= transaction_end <= end_time:
            return True

    return False

# Example usage:
operation_hours = [["04:20", "12:30"], ["19:00", "21:45"], ["14:00", "17:30"], ["12:30", "14:00"]]
transaction_time = ["11:00", "17:30"]
result = is_valid_transaction(operation_hours, transaction_time)
print(result)  # Output: True
