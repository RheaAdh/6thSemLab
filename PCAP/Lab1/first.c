#include "mpi.h"
#include<stdio.h>
#include<math.h>

int main(int argc, char* argv[]){
	int rank;
	int x = 2;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	int p = pow(x,rank);
	printf("rank: %d\n x: %d\n pow(%d,%d): %d\n",rank,x,x,rank,p);
	printf("----\n");
	MPI_Finalize();
	return 0;
}