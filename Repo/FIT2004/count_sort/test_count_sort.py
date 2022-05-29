import unittest
import timeit
from count_start_stable import sort_counting_stable


class TestCountingSort(unittest.TestCase):

    def test_counting_sort(self):
        # Input lists
        short_array = [6,3,1,7,2,8,1,7]
        long_array = [79, 98, 10, 16, 84, 75, 18, 77, 88, 83, 21, 49, 15, 53, 100, 39, 5, 72, 68, 11]

        # Expected outputs
        expected_short = [1, 1, 2, 3, 6, 7, 7, 8]
        expected_long = [5, 10, 11, 15, 16, 18, 21, 39, 49, 53, 68, 72, 75, 77, 79, 83, 84, 88, 98, 100]

        # Short array unit test
        starttime = timeit.default_timer()          # Record start time of counting sort
        result = sort_counting_stable(short_array)  # Store output of counting sort into result
        endtime = timeit.default_timer()            # Record end time of counting sort
        self.assertEqual(result, expected_short, 'Short array result is not sorted or is incorrect') # Check if output matches expected output
        total_time_s = endtime - starttime # Calculate total time taken to sort short array
        print('Result (short array): ' + str(result) + '\n' + 'Time : ' + str(total_time_s) + '\n')

        # Long array unit test
        starttime = timeit.default_timer()          # Record start time of counting sort
        result = sort_counting_stable(long_array)   # Store output of counting sort into result
        endtime = timeit.default_timer()            # Record end time of counting sort
        self.assertEqual(result, expected_long, 'Long array result is not sorted or is incorrect') # Check if output matches expected output
        total_time_l = endtime - starttime # Calculate total time taken to sort short array
        print('Result (long array): ' + str(result) + '\n' + 'Time : ' + str(total_time_l) + '\n')

        print(total_time_l - total_time_s)

