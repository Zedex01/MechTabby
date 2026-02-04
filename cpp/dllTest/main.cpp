//Dll Dynamic load at runtime

#include <windows.h>
#include <iostream>

//Create a new datatype 
typedef void (*SayHelloFunc)();

int main() {

	// === Load the dll ===
	HMODULE hDll = LoadLibraryA("myLibrary.dll");

	// === Check dll exists ===
	if (!hDll) {
		std::cerr << "Dll failed to load!" << std::endl;
		return 1;
	}


	//Get Function from dll

	//Create new var of custom datatype, grab function from dll
	SayHelloFunc say_hello = (SayHelloFunc)GetProcAddress(hDll, "say_hello");

	//check it was got:
	if (!say_hello) {
		std::cerr << "say_hello not found!" << std::endl;
		return 1;
	}

	//Call Function:
	say_hello();

	//unload dll:
	FreeLibrary(hDll);
	return 0;

}