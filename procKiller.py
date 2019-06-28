import ctypes

k_handle=ctypes.WinDLL("kernel32.dll")
u_handle=ctypes.WinDLL("user32.dll")

PROCESS_ALL_ACCESS= (0x000F0000 | 0x00100000 | 0xFFF)

lpWindowName=ctypes.c_char_p(input("Enter Window Name to kiLL:").encode("utf-8"))

hWnd=u_handle.FindWindowA(None,lpWindowName)

if hWnd==0:
	print("ERROR!! Could not catch handle.Error Code: {}".format(k_handle.GetLastError()))
	exit(1)
else:
	print("Grabbed the Handle.")

lpdwProcessId=ctypes.c_ulong()

response=u_handle.GetWindowThreadProcessId(hWnd,ctypes.byref(lpdwProcessId))

if response==0:
	print("[ERROR] Could Not Get PID from Handle! Error Code: {0}".format(k_handle.GetLastError()))
else:
	print("[INFO] Found PID...")
	

dwDesiredAccess = PROCESS_ALL_ACCESS
bInheritHandle = False
dwProcessId = lpdwProcessId

hProcess = k_handle.OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId)

if hProcess <= 0:
	print("[ERROR] Could Not Grab Privileged Handle! Error Code: {0}".format(k_handle.GetLastError()))
else:
	print("[INFO] Privileged Handle Opened...")
	
uExitCode = 0x1

response = k_handle.TerminateProcess(hProcess, uExitCode)

if response == 0:
	print("[ERROR] Could Not Kill Process! Error Code: {0}".format(k_handle.GetLastError()))
else:
	print("[INFO] Process Killed...")
	


