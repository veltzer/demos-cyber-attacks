#include <stdio.h>
#include <string.h>


int main() {
	printf("Try putting a long name...\n");
	char name[20]; // User input buffer (no size check)
	// cppcheck-suppress constVariable ; the demo shows this being overwritten by the overflow
	char password[20]="very_secret";
	printf("password before is [%s]\n", password);
	printf("Enter your name: ");
	// cppcheck-suppress bufferAccessOutOfBounds ; the overrun past name[20] into password is the whole point of this demo
	fgets(name, 40, stdin);
	printf("password after is [%s]\n", password);
	return 0;
}

