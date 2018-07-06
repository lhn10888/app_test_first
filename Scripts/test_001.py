import allure,pytest
class Test:
    @allure.step(title="第一个测试")
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test01(self):
        allure.attach("描述","这是第一个描述")
        assert  1
    @allure.step(title="第二个测试")
    def test02(self):
        allure.attach("描述","这是第二个描述")
        assert  0