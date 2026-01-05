import allure

@allure.feature("Hello World Feature")
@allure.story("Hello World Story")
@allure.severity(allure.severity_level.BLOCKER)  
@allure.title("Hello World Test Case")
def test_hello_world():
    """First test case that prints Hello World"""
    with allure.step("Asserting True is True"):
        assert True
    with allure.step("Printing Hello World message"):
        message = "Hello World from pytest!"
        print(message)
        allure.attach(message, name="Message", attachment_type=allure.attachment_type.TEXT)


@allure.feature("Basic Tests Feature")
@allure.story("Math Operations Story")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Simple Math Test Case")
def test_simple_math():
    """Simple math test"""
    with allure.step("Calculating 2 + 2"):
        result = 2 + 2
    with allure.step("Asserting the result is 4"):
        assert result == 4
        print(f"2 + 2 = {result}")
        allure.attach(f"2 + 2 = {result}", name="Calculation Result", attachment_type=allure.attachment_type.TEXT)
        

@allure.feature("Basic Tests Feature")
@allure.story("String Operations Story")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("String Operations Test Case")
def test_string_operations():
    """Simple string operations test"""
    with allure.step("Creating a string"):
        text = "Hello"
    with allure.step("Asserting the string is 'Hello' and its length is 5"):
        assert text == "Hello"
        assert len(text) == 5
        print(f"Text is: {text}, length: {len(text)}")
        allure.attach(f"Text: {text}, Length: {len(text)}", name="String Info", attachment_type=allure.attachment_type.TEXT)


@allure.feature("Failure Tests Feature")
@allure.story("Intentional Failure Story")     
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Intentional Failure Test Case")            
def test_intentional_fail():
    """Failing test"""
    with allure.step("Asserting 2 + 2 equals 5 to demonstrate failure"):
        assert 2 + 2 == 5 
        print("This test is designed to fail.")
        allure.attach("This test is designed to fail.", name="Failure Info", attachment_type=allure.attachment_type.TEXT)