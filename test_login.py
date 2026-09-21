import allure
@allure.feature("login")
@allure.story("login")
@allure.title("login")
@allure.description("login")
@allure.severity(allure.severity_level.NORMAL)
def test_login():
    with allure.step("open login page"):
        print("login page opened")
    with allure.step("enter username"):
        print("enter username")
    with allure.step("enter password"):
        print("enter password")
    with allure.step("click login button"):
        print("click login button")
    assert True