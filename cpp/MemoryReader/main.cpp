
#include <windows.h>
#include <iostream>
#include <vector>
#include <fstream>


/*
OpenProcess()
VirtualQueryEx()
ReadProcessMemory()
*/

int main(int argc, char* argv[]){

	DWORD pid;

	std::cout << "Hello, World!" << std::endl;
	std::cout << "Enter PID: ";
	std::cin >> pid;

	HANDLE hProcess = OpenProcess(
		PROCESS_QUERY_INFORMATION | PROCESS_VM_READ,
		FALSE,
		pid
	);


	if (!hProcess) {
		std::cout << "Failed to open process" << std::endl;
		return 1;
	}


	/*
	*/
	MEMORY_BASIC_INFORMATION mbi;
	uintptr_t address = 0;

	//Loop through memory:
	while (VirtualQueryEx(hProcess, (LPCVOID)address, &mbi, sizeof(mbi))) {
		//only commited memory:
		if (mbi.State == MEM_COMMIT) {

			//Skip no-access and gaurd pages
			if (!(mbi.Protect & PAGE_NOACCESS) && !(mbi.Protect & PAGE_GUARD)) {
				std::vector<char> buffer(mbi.RegionSize);
				SIZE_T bytesRead;

				if (ReadProcessMemory(
					hProcess, 
					mbi.BaseAddress,
					buffer.data(), 
					mbi.RegionSize, 
					&bytesRead)){

					std::cout
						<< "Requested: " << mbi.RegionSize
						<< "\n| Read: " << bytesRead
						<< "\n| Content: " << std::endl;


					for (size_t i = 0; i < bytesRead; i++) {
						printf("%02X ", (unsigned char)buffer[i]);

						if ((i + 1) % 16 == 0)
							printf("\n");
					}

				}

				//Read THis
			}
		}

		//update address to next region
		address += mbi.RegionSize;
	}
	return 0;
}