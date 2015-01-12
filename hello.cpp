
#include <iostream>
#include <stdio.h>
using namespace std;

int main(int argc, char *argv[])
{	
	cout <<"This is a Hello Interpreter" <<endl;
	if (argc != 2)
	{
		cout <<"Usage: hello filename" <<endl;
		return 0;
	}
	cout <<"Interpreter start:" <<endl;
	cout <<"argv[0]: " <<argv[0] <<";    argv[1]: " <<argv[1] <<endl;

	if (0 != access(argv[1], R_OK))
	{
		cout <<"file " <<argv[1] <<"not exist" <<endl;
		return 0;
	}

	FILE *fp = fopen(argv[1], "r");
	if (fp == NULL)
	{
		cout <<"open file failed" <<endl;
		return 0;
	}
	char buf[512];
	while(fgets(buf, sizeof(buf), fp) != NULL)
	{
		if (buf[0] == '#')
			cout <<"This line is a comment: ";
		cout <<buf;
	}

	cout <<"Interpreter end" <<endl <<endl;
	return 0;
}