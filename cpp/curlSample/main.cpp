
#include <iostream>
#include <windows.h>

#include <curlpp/cURLpp.hpp>     // Core curlpp initialization / cleanup
#include <curlpp/Options.hpp>     // For setting options like URL, POST data, headers
#include <curlpp/Easy.hpp>        // Optional, Easy request interface (often included via CURLpp.hpp)

//Examples can be found here: https://github.com/jpbarrette/curlpp/tree/master/examples
//using namespace curlpp::options;


int main(int argc, char* argv[]){

	std::cout << "Hello, World!" << std::endl;

	//const char* url[] = "http://localhost:5000/upload"

	//char data[] = "{\"name\" : \"Matt\", \"Age\": 24}"

	//create the request object:
	curlpp::Easy request;

	//Set url:
	//request.setOpt<curlpp::options::Url>("http://localhost:5000/upload");

	//perform the request:
	//request.perform();

}