#include <iostream>
#include "../nested2/nested3/add.h"
#include "../nested2/subtract.h"

int main() {
	std::cout << "hello world\n";
	std::cout << HELLO  << "\n";

	if (add(3, 4) > 6) {
		std::cout << "you can do math!\n";
	} else {
		std::cout << "you really really can't do math\n";
	}
}