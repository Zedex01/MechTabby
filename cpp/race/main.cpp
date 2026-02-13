#include <windows.h>
#include <iostream>
#include <vector>
#include <thread>
#include <random>

//global 

//LPCSTR is a Long pointer to a const str / char[]
//these work by providing a pointer to the first char of the char[]
// systems automatically find the string by reading from start till the null terminator
//L"" just means this is a wide string literal
const wchar_t* info = L"Hello, World!";
const wchar_t* caption = L"Notice";

HHOOK gHook;


int randRange(int min, int max) {
	static std::mt19937 rng(std::random_device{}());
	std::uniform_int_distribution<int> dist(min,max);

	return dist(rng);
}


//Callback function to move the location of the current popup:
LRESULT CALLBACK CBTProc(int nCode, WPARAM wParam, LPARAM lParam){
	
	//HCBT_ACTIVATE [5] indicates that a window is about to be opened
	if (nCode == HCBT_ACTIVATE){
		//A window is about to be opened!

		//Get the handle to the window about to be opened
		HWND hwnd = (HWND)wParam;

		//get screen size:
		int screenW = GetSystemMetrics(SM_CXSCREEN);
		int screenH = GetSystemMetrics(SM_CYSCREEN);

		//aprox message box size:
		int boxW = 300;
		int boxH = 160;

		int x = randRange(0, screenW-boxW);
		int y = randRange(0, screenH-boxH);

		//set the window position of the new window:
		SetWindowPos(hwnd, nullptr, x, y, 0, 0, SWP_NOSIZE | SWP_NOZORDER | SWP_NOACTIVATE);

		//remove hook after moving window:
		UnhookWindowsHookEx(gHook);

	}


	//Hand hook down the chain
	return CallNextHookEx(gHook, nCode, wParam, lParam);
}


void OpenPopup(){
	//Set hook on thread
	gHook = SetWindowsHookEx(WH_CBT, CBTProc, nullptr, GetCurrentThreadId());

	//create popup
	MessageBoxW(NULL, L"OMG YOUR COMPUTER HAS A VIRUS!!!!", L"RACE!", MB_OK | MB_ICONERROR | MB_TOPMOST);
}

// ===== MAIN =====
int main (int argc, char* argv[]) {

	//threading:
	//run a thread with:
		//std::thread t(some_function);
	//this starts a thread running some_function
	//calling :
		// t.join()
	//makes main wait until the thread finishes

	//alternativly, lambdas can be used for threads:
	//std::thread t([]() {
	//	std::cout << "This is lamda in a thread" << std::endl;
	//});

	//You can have threads work independantly outside of main by using:
	//t.detach()
	//**WARNING: detached threads MUST NOT access memory outside of scope.


	//Create a vector to contain the threads:
	std::vector<std::thread> threads;

	auto start = std::chrono::high_resolution_clock::now();

	//Open i amount of popups!
	for (int i = 0; i < 250; i++){
		//create lambda threads and add them		
		threads.emplace_back(OpenPopup);
		std::cout << "Popup: " << i << std::endl;

		Sleep(130);
	}

	//Now wait for all threads to finish:
	for (auto& t : threads) {
		t.join();
	}

	auto end = std::chrono::high_resolution_clock::now();

	auto elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);

	std::cout << "DONE!, your time: " << elapsed.count() << std::endl;

	return EXIT_SUCCESS;
}