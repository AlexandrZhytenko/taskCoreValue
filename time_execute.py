from timeit import default_timer

def time_execute(function):
    start_time = default_timer()
    function
    end_time = default_timer()
    time_taken = end_time - start_time
    return time_taken