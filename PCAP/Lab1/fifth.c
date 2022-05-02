#include "mpi.h"
#include<stdio.h>
int reverse(int x){
	int rev=0;
	while(x!=0){
		int rd=x%10;
		rev=rev*10+rd;
		x=x/10;
	} 
	return rev;
}


int main(int argc, char* argv[]){

int arr[9] = {51,12,13,14,15,16,17,54,34};
	int rank;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	printf("\nRank = %d\n",rank);
	int rev=reverse(arr[rank]);
	printf("original=%d , rev=%d\n",arr[rank],rev);
	MPI_Finalize();
	return 0;
}