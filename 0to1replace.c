// This program job is to replace 0 to 1 in any given number,for example if we take 120035, then uotput of this program will be 121135.
#include<stdio.h>
#include<string.h>
#include<math.h>
int main()
{
    int num,b,c,f,g;
    printf("enter the number you want to check");
    scanf("%d", &num);
    f=printf("the number you have entered is:%d\n",num);
    f-=32;
    g=0;
    for(int i=1;i<=f;i++){
        b=num%10;
        g=g+b*pow(10,f-i);
        num=num/10;

    }
    for(int i=1;i<=f;i++){
        if(g%10==0){
            printf("1");
            g=g/10;

        }else{c=g%10;
              printf("%d",c);
              g=g/10;
        }
    }

    return 0;

}


