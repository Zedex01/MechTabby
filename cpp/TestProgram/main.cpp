//2026-02-18
//Zedex01
//Pulled from win32 api docs

#include <iostream>
#include <windows.h>

//status symbols
const char* k = "[+] ";
const char* i = "[*] ";
const char* e = "[-] ";

//Basic Window:
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam);

//Alternative entry point for window:
int WINAPI wWinMain(HINSTANCE hInstance, HINSTANCE, hPrevInstance, PWSTR pCmdLine, int nCmdShow){

	//Register window class:
	const wchar_t CLASS_NAME[] = L"Sample Window Class";

	WNDCLASS wc = {};

	wc.lpfnWndProc = WindowProc;
	wc.hInstance = hInstance;
	wc.lpszClassName = CLASS_NAME;

	RegisterClass(&wc);

	//Create the window
	HWND hwnd = CreateWindowEx(
		0,						//Optional Windows Styles
		CLASS_NAME,				//Window Class
		L"Learn to program",	//Window Text
		WS_OVERLAPPEDWINDOW, 	//Window Style
		
		//Size and position:
		CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT,

		NULL,					//Parent Window
		NULL,					//Menu
		hInstance,				//Instance Handle
		NULL);    				//Additioanl App Data

	//If cannot get handle, return 0
	if (hwnd == NULL){
		return 0;
	}

	ShowWindow(hwnd, nCmdShow);

	//Run the message loop
	MSG msg = {};

	while (GetMessage(&msg, NULL, 0, 0) > 0){
		TranslateMessage(&msg);
		DispatchMessage(&msg);
	}

	return 0;
}


//Callback
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam){
	switch(uMsg){
		case WM_DESTROY:
			PostQuitMessage(0);
			return 0;

		case WM_PAINT:
			{
				PAINTSTRUCT ps;
				HDC hdc = BeginPaint(hwnd, &ps);

				//All painting happens here

				FillRect(hdc, &ps.rcPaint, (HBRUSH), (COLOR_WINDOW+1));

				EndPaint(hwnd, &ps);
			}
			return 0;
	}
	return DefWindowProc(hwnd, uMsg, wParam, lParam);
}
