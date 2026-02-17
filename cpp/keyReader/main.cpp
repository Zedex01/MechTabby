//2026-02-09
//Zedex01

#include <iostream>
#include <fstream>
#include <windows.h>
#include <commdlg.h>

#include <filesystem>
namespace fs = std::filesystem;

#include "dep/json.hpp"
using json = nlohmann::ordered_json;


//status symbols
const char* k = "[+] ";
const char* i = "[*] ";
const char* e = "[-] ";

fs::path pOut;
fs::path pIn;

std::string sOutputFileName = "fileout";

//Set time seperator (ms)
const int timeout = 5000;

//Useage:
//	a.exe <input file> [-o <output file>](optional)

fs::path getSelfPath(){
	//get root dir:
	char szBuffer[MAX_PATH];

	//Get the location of self:
	GetModuleFileNameA(
		NULL, //The proc handle you want to get the path to. when null, returns path of self 
		szBuffer, //A pointer to a buffer that receives the fully qualified path of the module.
		MAX_PATH); //The max size of the path

	//Create a path object
	std::filesystem::path pSelf = szBuffer;

	return pSelf;
}

// ==== Main ====
int main (int argc, char* argv[]){
	
	//Catch improper arg use
	if (argc < 2 || argc == 3 || argc > 4){
		std::cout << e << "Improper use of arguments." << std::endl;
		return 1;
	}

	//Set Input path:
	pIn = (getSelfPath()).parent_path() / std::string(argv[1]);

	//Check input path exists
	if (!fs::exists(pIn)){
		std::cout << e << "Input file not found: " << pIn << std::endl;
		return 1;
	}
	std::cout << k << "Input file found: " << pIn.filename() << std::endl;

	//Create a default outputfile
	if (argc == 2) {
		//set output path:
		pOut = (getSelfPath()).parent_path() / sOutputFileName;
	}

	//Use custom output file
	else if (argc == 4) {
		//Check for proper arg useage
		if (std::string(argv[2]) != "-o"){
			std::cout << "e" << "Improper argument" << std::endl;
			return 1;
		}

		//set output path:
		pOut = (getSelfPath()).parent_path() / std::string(argv[3]);
	}

	//Get data 
	json rawData;

	//Set Output Stream
	std::ofstream out(pOut);

	//Set Input Stream
	std::ifstream in(pIn);

	//Read in data from input:
	in >> rawData;

	std::cout << "Version: " << rawData["version"] << std::endl;

	std::string sBuffer;
	int last_time = -1;
	int this_time = -1;

	//itter through all events:
	for (const json& event : rawData["events"]){
		//Print info from that event:
		sBuffer = event["k"];
		this_time = event["t"];

		if (last_time != -1){
			if ((this_time - last_time) >= timeout){
				//std::cout << "\n=========================" << std::endl;
				out << "\n=========================" << std::endl;
			}
		}

		//sBuffer.erase(std::remove(sBuffer.begin(), sBuffer.end(), '"'), sBuffer.end());
		last_time = this_time;

		//std::cout << sBuffer;
		out << sBuffer;

	}

}

