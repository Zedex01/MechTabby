//Note: Keep track of binareis x64/x86, you need to match the other

#include <windows.h>
#include <iostream>

//status symbols
const char* k = "[+] ";
const char* i = "[*] ";
const char* e = "[-] ";

//Every process has an id: PID
DWORD PID = NULL;
HANDLE hProcess, hThread = NULL;

//cpp style
int main(int argc, char* argv[]){
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

	//Fun Fact: pids can only have a value that is a multiple of 4.

	//Check for missing access:
	if (hProcess == NULL) {
		std::cout << e << "Could not get a handle to the process " << PID << " " << GetLastError() << std::endl;
		return 1;
	}

	std::cout << k << "Got Process handle: " << hProcess << std::endl;

	//Alocate bytes into memory:



	return 0;
}