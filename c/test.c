#include <stdio.h>


void generate_text(char* buffer)
{
	for (int i = 0; i<9; i++)
	{
		sprintf(buffer, "%d", i);
		buffer++;
	}
}

int main(void)
{
	char buffer[30];
	generate_text(buffer);
	
	printf("This is some test file\n");
	printf("Here is numbers :) { %s }\n", buffer);

	return 0;
}
