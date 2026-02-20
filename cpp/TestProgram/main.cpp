//2026-02-18
//Zedex01
//Pulled from win32 api docs

#ifndef UNICODE
#define UNICODE
#endif

//Buttons
#define ID_FILE_NEW   1001
#define ID_FILE_OPEN  1002
#define ID_FILE_EXIT  1003



#include "resource.h"
#include <windows.h>

//Toolbar
#include <commctrl.h>
#pragma comment(lib, "comctl32/lib")

//Modern Windows Desktop Manager:
#include <dwmapi.h>
#pragma comment(lib, "dwmapi.lib")


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

	BOOL useDarkBorder = TRUE;
	DwmSetWindowAttribute(hwnd, DWMWA_BORDER_COLOR, &useDarkBorder, sizeof(useDarkBorder));


	//Toolbar:
	//INITCOMMONCONTROLSEX icex{};
	//icex.dwSize = sizeof(icex);
	//icex.dwICC = ICC_BAR_CLASSES;
	//InitCommonControlsEx(&icex);

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

				HMENU hMenuBar = CreateMenu();
				HMENU hFileMenu = CreatePopupMenu();	
				AppendMenu(hFileMenu, MF_STRING, ID_FILE_NEW,  L"&New");
				AppendMenu(hFileMenu, MF_STRING, ID_FILE_OPEN, L"&Open");
				AppendMenu(hFileMenu, MF_SEPARATOR, 0, NULL);
				AppendMenu(hFileMenu, MF_STRING, ID_FILE_EXIT, L"E&xit");	
				AppendMenu(hMenuBar, MF_POPUP, (UINT_PTR)hFileMenu, L"&File");	
				SetMenu(hwnd, hMenuBar);
				//Create Toolbar window
				//HWND hToolBar = CreateWindowEx(
				//	0,
				//	TOOLBARCLASSNAME,
				//	NULL,
				//	WS_CHILD | WS_VISIBLE | TBSTYLE_FLAT | TBSTYLE_TOOLTIPS | CCS_TOP,
				//	0,0,0,0,
				//	hwnd,
				//	NULL,
				//	GetModuleHandle(NULL),
				//	NULL);

				//SendMessage(hToolBar, TB_BUTTONSTRUCTSIZE, (WPARAM)sizeof(TBBUTTON), 0);
//
				//SendMessage(hToolBar, TB_LOADIMAGES, IDB_STD_SMALL_COLOR,(LPARAM)HINST_COMMCTRL);
//
				////Create buttons
				//TBBUTTON tbb[3] = {};
//
				//tbb[0].iBitmap = STD_FILENEW;
				//tbb[0].idCommand = ID_BTN_NEW;
				//tbb[0].fsState = TBSTATE_ENABLED;
				//tbb[0].fsStyle = TBSTYLE_BUTTON;
//
				//tbb[1].iBitmap = STD_FILEOPEN;
				//tbb[1].idCommand = ID_BTN_OPEN;
				//tbb[1].fsState = TBSTATE_ENABLED;
				//tbb[1].fsStyle = TBSTYLE_BUTTON;
//
				//tbb[2].iBitmap = STD_FILESAVE;
				//tbb[2].idCommand = ID_BTN_SAVE;
				//tbb[2].fsState = TBSTATE_ENABLED;
				//tbb[2].fsStyle = TBSTYLE_BUTTON;
//
				////Add them:
				//SendMessage(hToolBar, TB_ADDBUTTONS,(WPARAM)3,(LPARAM)&tbb);
//
				//SendMessage(hToolBar, TB_AUTOSIZE, 0, 0);
//
				//ShowWindow(hToolBar, TRUE);


			}
			break;

			case WM_COMMAND:
			{
			    switch (LOWORD(wParam))
			    {
			    	case ID_FILE_NEW:
			    	    MessageBox(hwnd, L"New clicked", L"Menu", MB_OK);
			    	    break;
	
			    	case ID_FILE_OPEN:
			    	    MessageBox(hwnd, L"Open clicked", L"Menu", MB_OK);
			    	    break;
	
			    	case ID_FILE_EXIT:
			    	    PostQuitMessage(0);
			    	    break;
			    }
			}
			break;



	}
	return DefWindowProc(hwnd, uMsg, wParam, lParam);
}
