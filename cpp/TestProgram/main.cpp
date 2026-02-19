//2026-02-18
//Zedex01
//Pulled from win32 api docs

#ifndef UNICODE
#define UNICODE
#endif

#include "resource.h"
#include <windows.h>

//Toolbar
#include <commctrl.h>
#pragma comment(lib, "comctl32/lib")

//status symbols
const char* k = "[+] ";
const char* i = "[*] ";
const char* e = "[-] ";

//Basic Window:
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam);

//Alternative entry point for window:
int WINAPI wWinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, PWSTR pCmdLine, int nCmdShow){

	//Register window class:
	const wchar_t CLASS_NAME[] = L"Sample Window Class";

	WNDCLASS wc = {};

	wc.lpfnWndProc = WindowProc;
	wc.hInstance = hInstance;
	wc.lpszClassName = CLASS_NAME;

	//Setting the icon for the top left
	wc.hIcon = LoadIcon(hInstance, MAKEINTRESOURCE(IDI_ICON1));

	RegisterClass(&wc);

	//Create the window
	HWND hwnd = CreateWindowEx(
		0,						//Optional Windows Styles
		CLASS_NAME,				//Window Class
		L"Test Program",		//Window Text
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


	//Toolbar:
	INITCOMMONCONTROLSEX icex{};
	icex.dwSize = sizeof(icex);
	icex.dwICC = ICC_BAR_CLASSES;
	InitCommonControlsEx(&icex);



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


				//Custom Brush:
				HBRUSH hBrush = CreateSolidBrush(RGB(18,18,18));
				//All painting happens here
				FillRect(hdc, &ps.rcPaint, hBrush);

				//Fill with sys Color:
				//FillRect(hdc, &ps.rcPaint, (HBRUSH) (COLOR_WINDOW+1));

				EndPaint(hwnd, &ps);
			}
			return 0;

		case WM_CREATE:
			{
				//Create Toolbar window
				HWND hToolBar = CreateWindowEx(
					0,
					TOOLBARCLASSNAME,
					NULL,
					WS_CHILD | WS_VISIBLE | TBSTYLE_FLAT | TBSTYLE_TOOLTIPS || CCS_TOP,
					0,0,0,0,
					hwnd,
					NULL,
					GetModuleHandle(NULL),
					NULL);
			}
			return 0;
	}
	return DefWindowProc(hwnd, uMsg, wParam, lParam);
}
