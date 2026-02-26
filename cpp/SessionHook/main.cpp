//mmoran

//Be able to tarck user LOCK/UNLOCK, windows shutdown?

#include <windows.h>
#include <wtsapi32.h>
#include <iostream>

#pragma comment(lib, "Wtsapi32.lib")



//Window
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam){
	switch (uMsg)
	{
	//Catch lock/unlock
	case WM_WTSSESSION_CHANGE:
		if (wParam == WTS_SESSION_LOCK)
			std::cout << "User Locked Screen!" << std::endl;
		else if (wParam == WTS_SESSION_UNLOCK)
			std::cout << "User Unlocked Screen!" << std::endl;
		break;

	//Catch shutdown or logoff
	case WM_QUERYENDSESSION:
		std::cout << "System is Shutting down or User is logging off." << std::endl;

		return TRUE; //Allow Shutdown


	case WM_ENDSESSION:
		if (wParam)
			std::cout << "Session is ending" << std::endl;
		break;

	}

	//hand off to next window
	return DefWindowProc(hwnd, uMsg, wParam, lParam);
}


int main(int argc, char const *argv[])
{
	HINSTANCE hInstance = GetModuleHandle(NULL);

	WNDCLASS wc = {};
	wc.lpfnWndProc = WindowProc;
	wc.hInstance = hInstance;
	wc.lpszClassName = "HiddenWindowClass";
	RegisterClass(&wc);

	HWND hwnd = CreateWindowEx(0, "HiddenWindowClass", "temp", 0, 0,0,0,0,HWND_MESSAGE,NULL,hInstance, NULL);

	WTSRegisterSessionNotification(hwnd, NOTIFY_FOR_THIS_SESSION);

	

	std::cout << "Monitoring user state ..." << std::endl;

	MSG msg;

	while(GetMessage(&msg, NULL, 0, 0))
	{
		TranslateMessage(&msg);
		DispatchMessage(&msg);

	}
	return 0;
}