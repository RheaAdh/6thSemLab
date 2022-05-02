#include "mpi.h"
#include<stdio.h>
int checkprime(int n){
	if(n==0||n==1)return 0;
	for(int i=2;i*i<=n;i++){
		if(n%i==0){
			return 0;
		}
	}
	return 1;
}

int arr[9] = {51,12,13,14,15,16,17,54,34};

int main(int argc, char* argv[]){
	int rank;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	if(rank<50){
		if(checkprime(rank)){
			printf("%d ,",rank);
		}
	}
	else{
		if(checkprime(rank)){
			printf("%d ,",rank);
		}
	}
	MPI_Finalize();
	return 0;
}