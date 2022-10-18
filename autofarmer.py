
from time import sleep
import win32gui, win32ui, win32con, win32api

def main():
    window_name = "Nova Ragnaro"
    hwnd = win32gui.FindWindow(None, window_name)
    hwnd = get_inner_windows(hwnd)['Nova Ragnarok']
    win = win32ui.CreateWindowFromHandle(hwnd)

    command_list(hwnd)


def list_window_names():
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(hex(hwnd), '"' + win32gui.GetWindowText(hwnd) + '"')
    win32gui.EnumWindows(winEnumHandler, None)


def get_inner_windows(whndl):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            hwnds[win32gui.GetClassName(hwnd)] = hwnd
        return True
    hwnds = {}
    win32gui.EnumChildWindows(whndl, callback, hwnds)
    return hwnds

def full_buff(hwnd):
    # press C
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x43, 0)
    sleep(0.01)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x43, 0)
    sleep(0.2)

    # press V
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x56, 0)
    sleep(0.01)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x56, 0)
    sleep(0.2)

    # press B
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x42, 0)
    sleep(0.01)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x42, 0)
    sleep(0.2)

    # press N
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x4E, 0)
    sleep(0.01)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x4E, 0)
    sleep(0.2)

    # press M
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x4D, 0)
    sleep(0.01)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x4D, 0)
    sleep(0.2)

    # press ,
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0xBC, 0)
    sleep(0.01)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0xBC, 0)
    sleep(0.2)

def fast_buff(hwnd):
    # press C
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x43, 0)
    sleep(0.01)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x43, 0)
    sleep(0.2)

    # press V
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x56, 0)
    sleep(0.01)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x56, 0)
    sleep(0.2)

    # press B
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x42, 0)
    sleep(0.01)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x42, 0)
    sleep(0.2)


def attack(hwnd):
    # press M
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x5A, 0)
    sleep(0.01)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x5A, 0)
    sleep(2)

    # press M
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x5A, 0)
    sleep(0.01)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x5A, 0)
    sleep(1)

    # press ,
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x58, 0)
    sleep(0.01)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x58, 0)
    sleep(1)

def command_list(hwnd):
    full_buff(hwnd)
    attack(hwnd)
    attack(hwnd)
    attack(hwnd)
    attack(hwnd)
    attack(hwnd)
    attack(hwnd)
    attack(hwnd)
    attack(hwnd)
    attack(hwnd)
    attack(hwnd)
    fast_buff(hwnd)
    attack(hwnd)
    attack(hwnd)
    attack(hwnd)
    attack(hwnd)
    attack(hwnd)
    attack(hwnd)
    attack(hwnd)
    attack(hwnd)
    attack(hwnd)
    attack(hwnd)

while True:
    main()