#include <stdio.h>
#include <stdlib.h>
int main()
{
    FILE *fp;
    char flag[1035];
    fp = popen("/usr/bin/curl -s http://genflag/flag", "r");
    if (fp == NULL)
    {
        printf("Error found. Please contact administrator.");
        exit(1);
    }
    while (fgets(flag, sizeof(flag), fp) != NULL)
    {
        printf("%s", flag);
    }
    pclose(fp);
    return 0;
}