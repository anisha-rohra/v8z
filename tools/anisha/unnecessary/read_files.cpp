#include <iostream>
#include <fstream>
#include <string>

int main(int argc, char** argv) {

	if (argc < 2) {
		std::cout << "need a file\n";
		return 1;
	}

	std::ifstream myfile;
	std::string line;
	myfile.open(argv[1]);
	if (myfile.is_open()) {
		int count = 10;
		while (count != 0) {
			count = count - 1;
			getline(myfile, line);
			std::cout << line << "\n";
		}
		myfile.close();
		return 0;
	}

	else {
		std::cout << "file could not be opened\n";
	}

}