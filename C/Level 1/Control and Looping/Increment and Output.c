#include <stdio.h>
int main() 
{
  int n, i;
  scanf("%d", &n);
  for(i=1; i<n; ++i){
    printf("%d ", i);
  }
  for(i=i; i!=0; --i){
    if(i==1){
      printf("%d", i);
    }
    else{
      printf("%d ", i);
    }
  }
	return 0;
}