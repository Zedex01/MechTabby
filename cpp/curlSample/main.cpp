
#include <iostream>
#include <windows.h>

#include <curl/curl.h>

//status symbols
const char* k = "[+] ";
const char* i = "[*] ";
const char* e = "[-] ";


void WriteCallback(void* contents, size_t size, size_t nmemb, void* userp) {
	std::cout << i << "callback fired" << std::endl;
}

int main(int argc, char* argv[]){

	//CURL C
	CURL* curl = curl_easy_init();

	if (curl) {
		std::cout << k << "libcurl linked succesfully!" << std::endl;
		std::cout << curl_version() << std::endl;
		
		CURLcode result;

		//Set the URL
		curl_easy_setopt(curl, CURLOPT_URL, "http://localhost:5000/upload");

		//Set as a POST request:
		curl_easy_setopt(curl, CURLOPT_POST, 1L);

		//Set Callback:
		curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);

		//Set Headers:
		struct curl_slist* headers = nullptr;
		headers = curl_slist_append(headers, "Content-Type: application/json");
		curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);

		//Set Body
		curl_easy_setopt(curl, CURLOPT_POSTFIELDS, "{\"name\": \"Matt\", \"Age\": 24}");

		//make resquest
		result = curl_easy_perform(curl);


		if (result != CURLE_OK) {
			std::cout << e << "Request Failed: " << curl_easy_strerror(result) << std::endl;
		} else {
			std::cout << k << "POST sent succesfully!" << std::endl;

		}

		curl_easy_cleanup(curl);
	}

	return WN_SUCCESS;



}