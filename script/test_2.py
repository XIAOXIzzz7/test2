from airtest.core.api import *

from Airtest.test_1 import appid
import random




"引入设备号"
serialno = appid()


"链接设备"
auto_setup(__file__, devices=['Android://127.0.0.1:5037/{serial}'.format(serial=serialno)])

"关闭应用"
stop_app("com.road7.phoenix")
"启动应用"
start_app("com.road7.phoenix")
sleep(15)

"初始化poco"
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

def plot_1():
    """新手引导1"""

    touch(Template(r"photo/tpl1614249615214.png", record_pos=(0.188, 0.161), resolution=(2280, 1080)), duration=0.5, times=2)

    sleep(3)
    poco("btn_close").click()

    poco(texture="icon_user").click()

    touch(Template(r"photo/tpl1614238713913.png", record_pos=(-0.075, 0.028), resolution=(2280, 1080)))
    touch(Template(r"photo/tpl1614564709607.png", record_pos=(-0.211, -0.081), resolution=(2280, 1080)))

    id = random.sample('123213ssd2dasd1ad313adad213', 5)
    '将id改为str格式'
    id = ''.join(id)
    text(f"{id}")
    sleep(0.5)
    touch(Template(r"photo/tpl1614305522592.png", record_pos=(-0.231, -0.025), resolution=(2280, 1080)))

    pwd = random.sample('12675hgreta3213daddadaa13213', 5)
    pwd = ''.join(pwd)
    text(f"{pwd}")
    sleep(0.5)
    touch(Template(r"photo/tpl1614238812357.png", record_pos=(-0.03, 0.043), resolution=(2280, 1080)))
    age = random.sample('189879d32adad131dada3213', 5)
    age = ''.join(age)
    text(f"{age}")
    sleep(0.5)
    touch(Template(r"photo/tpl1614241892043.png", record_pos=(0.192, 0.106), resolution=(2280, 1080)))
    sleep(2)
    touch(Template(r"photo/tpl1614242108276.png", record_pos=(0.188, 0.162), resolution=(2280, 1080)))
    sleep(2)
    poco("Txt_CurrServer").click()
    poco("Content").child("ServerItemModel(Clone)")[0].child("Txt_Name").click()
    poco(text='开始游戏').click()
    touch(Template(r"photo/tpl1614306103574.png", record_pos=(0.191, 0.161), resolution=(2280, 1080)), duration=0.5, times=3)
    poco('Placeholder').click()
    for i in range(8):
        keyevent("67")
    user_name = random.sample('zxcvbnmlkjhgfdswwertuiop123412474', 8)
    user_name = ''.join(user_name)
    text(f"{user_name}")
    poco(text='开始游戏').click()
    poco("Txt_CurrServer").click()

    sleep(8)
    touch(Template(r"photo/tpl1614305854630.png", record_pos=(0.186, 0.16), resolution=(2280, 1080)), duration=0.5, times=5)

    poco(text="呀，真是熟悉的开场啊。").wait_for_appearance()
    poco("img_exit").click()
    # 序章战斗
    poco(text="等等，阿银，是不是不太对劲？这是什么？怎么一上来就是战斗？").wait_for_appearance()
    poco('btn_pass').click()
    poco('img_cost').click()
    poco('scr_card').child('BasicListAdapterItem2(Clone)').offspring('outline_qualitybg').swipe([0.008, -0.3454])
    poco(texture="bg_guideinfo").wait_for_appearance()

    poco('scr_card').child('BasicListAdapterItem2(Clone)').offspring('outline_qualitybg').swipe([-0.0322, -0.184])
    poco('StarNode3').wait_for_appearance()
    poco('StarNode3').click()

plot_1()
