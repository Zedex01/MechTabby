//Matthew Moran
//2026-02-05
//
//fs / filesystem example


#include <filesystem>

#include <windows.h>
#include <iostream>

//Status
const char* k = "[+] ";
const char* i = "[*] ";
const char* e = "[-] ";

//To shorten what you need to write
namespace fs = std::filesystem;

// Main
int main(int argc, char* argv[]){
	std::cout << i << "Welcome!" << std::endl;

	//get root dir:
	char szBuffer[MAX_PATH];

	//Get the location of self:
	GetModuleFileNameA(
		NULL, //The proc handle you want to get the path to. when null, returns path of self 
		szBuffer, //A pointer to a buffer that receives the fully qualified path of the module.
		MAX_PATH); //The max size of the path

	//Create a path object
	std::filesystem::path pPath = szBuffer;
	std::cout << i << "Path: " << pPath << std::endl; 

	//get root dir
	std::filesystem::path pRoot = pPath.parent_path();
	std::cout << i << "Root: " << pRoot << std::endl; 

	//Relative Path
	std::filesystem::path pReadMe = pRoot / "README.md";

	//Path Verififcation
	if (std::filesystem::exists(pReadMe) == false) {
		std::cout << e << pReadMe.filename() << " Cannot be found" << GetLastError() << std::endl;	
	}

	std::cout << k << pReadMe.filename() << " found!" << std::endl;

}

