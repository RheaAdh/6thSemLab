#include "mpi.h"
#include<stdio.h>
int main(int argc, char *argv[]){
	int rank, size, x;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	MPI_Status status;
	if(rank == 0){
		printf("In master process(Rank 0) , Enter a number: ");
		scanf("%d",&x);
		for(int i=1; i<5; i++){
			MPI_Send(&x,1,MPI_INT,i,1,MPI_COMM_WORLD);
			fprintf(stdout, "Master process sends %d to process %d\n", x,i);
		}
	}
	else{
		MPI_Recv(&x,1,MPI_INT,0,1,MPI_COMM_WORLD,&status);
		fprintf(stdout,"Number received %d in process %d\n",x,rank);
		fflush(stdout);
	}
	MPI_Finalize();
	return 0;
}