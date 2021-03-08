from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_api=True, screenshot_each_action=False)
"初始化"
auto_setup(__file__)


"获取设备号"
def appid():
    a = poco.adb_client.get_device_info()
    print(a)
    print('手机链接成功')
    return a['serialno']



if __name__ == "__main__":
    appid()