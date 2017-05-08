#include <iostream>
#include "nested1/nested3/add.h"

int main() {
	std::cout << "hello world\n";
	std::cout << HELLO  << "\n";

	if (add(3, 4) > 6) {
		std::cout << "you can do math!\n";
	} else {
		std::cout << "you really really can't do math\n";
	}
}
