//Simple dll function made by chatGPT
//Building dlls:
//g++ -shared -o MyLibrary.dll MyLibrary.cpp -Wl,--out-implib,libMyLibrary.a
//-shared makes it build as dll

//-Wl,--out-implib,libMyLibrary.a creates an import library (optional if you want to link at compile time, not runtime).


//can either load dlls at compile OR at runtime

#include <windows.h> //windows api

//__declspec(dllexport) makes the function callable outside of the dll
//extern "C" prevents naming issues, makes it easily callable from main.
#define EXPORT extern "C" __declspec(dllexport)

// A simple function to export
EXPORT void say_hello() {
    MessageBoxA(NULL, "Hello from DLL!", "DLL Message", MB_OK);
}

/*
// Optional: DLL entry point
BOOL APIENTRY DllMain(HMODULE hModule,
                      DWORD  ul_reason_for_call,
                      LPVOID lpReserved) {
    return TRUE;
}*/