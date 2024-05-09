#include <stdio.h>
#include <string.h>


int main() {
	printf("Try putting a long name...\n");
	char name[20]; // User input buffer (no size check)
	char password[20]="very_secret";
	printf("password before is [%s]\n", password);
	printf("Enter your name: ");
	fgets(name, 40, stdin);
	printf("password after is [%s]\n", password);
	return 0;
}

