#include "mpi.h"
#include<stdio.h>

int main(int argc, char* argv[]){
	int rank;
	int x = 5, y = 9;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	if(rank == 0){
		printf("ADD (Rank = %d) :\n %d + %d = %d\n",rank,x,y,x+y);
	}
	else if(rank == 1){
		printf("SUB (Rank = %d) :\n%d - %d = %d\n",rank,x,y,x-y);
	}
	else if(rank == 2){
		printf("MUL(Rank = %d) :\n%d * %d = %d\n",rank,x,y,x*y);
	}
	else if(rank == 3){
		printf("DIV(Rank = %d) :\n%d / %d = %d\n",rank,x,y,x/y);
	}
	else
		printf("Invalid process\n");

	MPI_Finalize();
	return 0;
}