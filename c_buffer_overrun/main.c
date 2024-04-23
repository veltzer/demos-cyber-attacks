#include <stdio.h>
#include <string.h>

void greet(char *name) {
	char password[20]="very_secret";
	char buffer[20]; // Fixed-size buffer
	strcpy(buffer, name); // Potentially overflows buffer if name is too long
	printf("Hello, %s!\n", buffer);
	printf("password is %s!\n", password);
	printf("buffer is %p\n", buffer);
	printf("password is %p\n", password);
}

void rstrip(char* str) {
	// Get the length of the string (excluding newline)
	int bytes_read = strlen(str);
	// Check if newline exists (fgets might not read the entire buffer)
	if (bytes_read > 0 && str[bytes_read - 1] == '\n') {
		// Replace newline with null terminator
		str[bytes_read - 1] = '\0';
	}
}


int main() {
	printf("Try putting a long name...\n");
	char name[100]; // User input buffer (no size check)
	printf("Enter your name: ");
	fgets(name, sizeof(name), stdin); // Can read entire line, potentially exceeding buffer size
	rstrip(name);
	greet(name);
	return 0;
}

