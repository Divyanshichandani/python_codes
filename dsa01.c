/*/waf which prints below pattern.call the methos from main().
pattern - print your sap id in combination of * as for sapid in combination of * as for sap id 50001272.
o/p:
5
*0
**0
***0
****1
*****2
******7
*******2/*/

#include<stdio.h>
void pattern();
int main() {
printf("The Pattern is:\n");
pattern();
}

void pattern()
{
    int rows =7 , SAP[8] = {5,0,0,0,1,2,7,2};
    printf("5\n");
    // for printing rows
    for (int i = 0,x = 1; i < rows; i++) {
    // for printing star
        for (int j = 0; j <= i; j++) {
            printf("*\t");
        }
        printf("%d",SAP[x]);
        x++;
        printf("\n");
    }
}