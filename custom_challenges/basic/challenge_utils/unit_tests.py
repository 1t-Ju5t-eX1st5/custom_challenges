import datetime

class UnitTest():
    """
    Mimics the unit test library used by Codewars

    Functions:
    assert_equals: runs a given function, then checks if the result obtains is the same as the expected result or not, as well as the runtime (in milliseconds)
    calculate_runtime: calculates the runtime for a given function
    """
    def __init__(self, challenge_id: str):
        self.challenge_id = challenge_id or ""
    
    def assert_equals(self, code_to_test, expected_result) -> str:
        """
        Checks if the result of a function is the same as the expected result, and returns the runtime (in millseconds)

        Arguments:
        code_to_test (func): The function that is being tested, code must have at least 1 "return" function to return the result from the code
        expected_result (Any): The expected result from the code

        Returns:
        res (str): Returns 1 of 3 possible results
            - Exception/error has occured: "Returned error x"
            - Test failed, no errors: "Expected (result x), got (result y) instead with runtime of x ms"
            - Test passed: "Test passed with runtime of x ms
        
            
        Credits to Codewars for giving me this idea btw :)
        """
        test_res = ""
        try:
            start_time = datetime.datetime.now()
            test_res = code_to_test()
        except Exception as e:
            return f"Returned error {e}"
        else:
            end_time = datetime.datetime.now()
            delta = end_time - start_time
            if test_res == expected_result:
                return f"Test passed with runtime of {delta.total_seconds() * 1000} ms"
            else:
                return f"Expected \'{expected_result}\', got \'{test_res}\' instead with runtime of {delta.total_seconds() * 1000} ms"
    
    def calculate_runtime(self, code_to_test) -> str:
        """
        Calculates the total runtime for a given function

        Arguments:
        code_to_test (func): The function that is being tested, code must have at least 1 "return" function to return the result from the code

        Returns:
        res (str): Returns 1 of 2 possible results
            - Exception/error has occured: "Returned error x"
            - Test passed: "Code executed successfully with runtime of x ms
        """
        try:
            start_time = datetime.datetime.now()
            code_to_test()
        except Exception as e:
            return f"Returned error {e}"
        else:
            end_time = datetime.datetime.now()
            delta = end_time - start_time
            return f"Code executed successfully with runtime of {delta.total_seconds() * 1000} ms"
        
    def describe(self, description: str):
        # Errr....
        print(description)