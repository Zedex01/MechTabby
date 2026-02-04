#include <iostream>
#include <windows.h>
#include <string>

int main() {
    // Path to the DLL to inject
    const char* dllPath = "C:\\path\\to\\myinject.dll";
    // Name of the process to inject into
    const char* targetProcess = "notepad.exe"; 

    // 1. Get the process ID (PID) of the target process
    // (Simplification: Assumes notepad is running. A real injector would enumerate processes)
    HWND hwnd = FindWindowA(NULL, "Untitled - Notepad");
    DWORD procID;
    GetWindowThreadProcessId(hwnd, &procID);

    // 2. Open the Target Process
    HANDLE hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, procID);
    if (hProcess == NULL) {
        std::cout << "Failed to open process" << std::endl;
        return 1;
    }

    // 3. Allocate memory in the target process for the DLL path
    LPVOID pDllPath = VirtualAllocEx(hProcess, NULL, strlen(dllPath) + 1, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);

    // 4. Write the DLL path to the allocated memory
    WriteProcessMemory(hProcess, pDllPath, (LPVOID)dllPath, strlen(dllPath) + 1, NULL);

    // 5. Get the address of LoadLibraryA from Kernel32.dll
    LPVOID pLoadLibrary = (LPVOID)GetProcAddress(GetModuleHandleA("kernel32.dll"), "LoadLibraryA");

    // 6. Create a remote thread that calls LoadLibraryA with the path to the DLL
    HANDLE hThread = CreateRemoteThread(hProcess, NULL, 0, (LPTHREAD_START_ROUTINE)pLoadLibrary, pDllPath, 0, NULL);

    if (hThread) {
        std::cout << "Successfully injected!" << std::endl;
        CloseHandle(hThread);
    }

    CloseHandle(hProcess);
    return 0;
}