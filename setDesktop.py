"""
Version: 0.1
Author: lvtoo
e-mail: o@oouul.com
Date: 2019/6/15

"""
import win32api, win32con, win32gui
import time
from random import randint
import os
from PIL import Image


def change_desktop(pic):
    # reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    # a = win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
    # 设置桌面填充模式 0拉伸 1平铺
    # b = win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    # win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, pic, win32con.SPIF_SENDWININICHANGE)
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, pic, win32con.SPIF_SENDCHANGE)
    # a = win32api.MessageBox(0, "测试成功", "提示：", win32con.MB_YESNO + win32con.MB_ICONQUESTION)


def main():
    while True:
        dir_paths = os.listdir('M:/img/sexy/')
        length = len(dir_paths)
        # pic = 'M:\img\sexy\性感吊带美女诱人居家写真图片（10-14）.jpg'
        while True:
            pic = 'M:\\img\\sexy\\' + dir_paths[randint(0, length - 1)]
            img = Image.open(pic)
            if img.size[1] == 1600 and img.size[0] == 900 or img.size[1] == 1920 and img.size[0] == 1080:
                break

        change_desktop(pic)

        time.sleep(7)


if __name__ == '__main__':
    main()
