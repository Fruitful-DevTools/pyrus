import time

def backoff(func, max_retries=5, delay=1, backoff=2):
    
    """
    Executes a function with exponential backoff and retry if an exception occurs.

    Args:
        func (callable): The function to execute.
        max_retries (int): The maximum number of retries.
        delay (float): The initial delay in seconds between retries.
        backoff (float): The backoff factor applied to the delay after each retry.

    Returns:
        The result of the function if it is successful, otherwise raises the last caught exception.
    """

    # Initialise attempts counter
    attempts = 0

    # While the attempts is lessthan/equal to maximum number of defined tries
    while attempts <= max_retries:

        # attempt to return the functions value
        try:
            return func()

        # if there is an exception
        except Exception as e:

            # and the number of attempts is the same as the max number of tries
            if attempts == max_retries:

                # raise an exception
                raise e

            # otherwise, add one to the attempts counter
            # square the delay time
            else:
                attempts += 1
                time.sleep(delay)
                delay *= backoff
