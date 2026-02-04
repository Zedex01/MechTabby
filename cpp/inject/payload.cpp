//Env: Windows 11 Enterprise
//  10.0.26100 Build 26100

#include <windows.h>


//Entry point for the DLL:
BOOL WINAPI DllMain(
    HINSTANCE hinstDLL, //Handler to dll module
    DWORD fdwReason, //Reason for calling Function
    LPVOID lpvReserved ) //Reserved
{
    switch (fdwReason) {

    //Runs on process attach
    case DLL_PROCESS_ATTACH:

        //Create Meassgebox pop_up
        MessageBox(NULL, "YOU HAVE BEEN INJECTED!", "Inject Payload", MB_ICONQUESTION | MB_OK);
        
        break;
    }

    return 0;
}