#include <iostream>
#include "add.h"

int main() {
	std::cout << "\xff\xff\x25\x25\x3f\xff\xff\x3f\xff\x25\xff\xff";
	std::cout << HELLO  << "\xff";

	if (add(3, 4) > 6) {
		std::cout << "\x60\x3f\xff\xff\xff\x2f\x3e\xff\xff\x3f\xff\x5f\x2f\xff\xff\xff\xff";
	} else {
		std::cout << "\x60\x3f\xff\xff\xff\xff\x2f\x25\x25\x60\xff\xff\xff\x2f\x25\x25\x60\xff\xff\x2f\x3e\x1b\xff\xff\xff\x3f\xff\x5f\x2f\xff\xff\xff";
	}
}#include <iostream>

int main() {
	std::cout << "\xff\xff\x25\x25\x3f\xff\xff\x3f\xff\x25\xff\xff";
	std::cout << HELLO  << "\xff";

	if (add(3, 4) > 6) {
		std::cout << "\x60\x3f\xff\xff\xff\x2f\x3e\xff\xff\x3f\xff\x5f\x2f\xff\xff\xff\xff";
	} else {
		std::cout << "\x60\x3f\xff\xff\xff\xff\x2f\x25\x25\x60\xff\xff\xff\x2f\x25\x25\x60\xff\xff\x2f\x3e\x1b\xff\xff\xff\x3f\xff\x5f\x2f\xff\xff\xff";
	}
}#include <iostream>
#include "tests/samedir_rec/add_temp.h"

int main() {
	std::cout << "\xff\xff\x25\x25\x3f\xff\xff\x3f\xff\x25\xff\xff";
	std::cout << HELLO  << "\xff";

	if (add(3, 4) > 6) {
		std::cout << "\x60\x3f\xff\xff\xff\x2f\x3e\xff\xff\x3f\xff\x5f\x2f\xff\xff\xff\xff";
	} else {
		std::cout << "\x60\x3f\xff\xff\xff\xff\x2f\x25\x25\x60\xff\xff\xff\x2f\x25\x25\x60\xff\xff\x2f\x3e\x1b\xff\xff\xff\x3f\xff\x5f\x2f\xff\xff\xff";
	}
}#include <iostream>
#include "add_temp.h"

int main() {
	std::cout << "\xff\xff\x25\x25\x3f\xff\xff\x3f\xff\x25\xff\xff";
	std::cout << HELLO  << "\xff";

	if (add(3, 4) > 6) {
		std::cout << "\x60\x3f\xff\xff\xff\x2f\x3e\xff\xff\x3f\xff\x5f\x2f\xff\xff\xff\xff";
	} else {
		std::cout << "\x60\x3f\xff\xff\xff\xff\x2f\x25\x25\x60\xff\xff\xff\x2f\x25\x25\x60\xff\xff\x2f\x3e\x1b\xff\xff\xff\x3f\xff\x5f\x2f\xff\xff\xff";
	}
}