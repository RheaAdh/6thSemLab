#include "mpi.h"
#include<stdio.h>
int main(int argc, char *argv[]){
	int rank, size;
	int x[100];
	int buf[100];
	int MAX_SIZE=100;
	int n;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	MPI_Status status;
	if(rank == 0){
		printf("In master process(Rank 0) , Enter a number: ");
		for(int i=0; i<6; i++)
			scanf("%d",&x[i]);
		MPI_Buffer_attach(buf,MAX_SIZE);
		for(int i=1; i<6; i++){
			MPI_Bsend(&x[i],1,MPI_INT,i,1,MPI_COMM_WORLD);
			fprintf(stdout, "Master process sent %d to process %d\n", x[i],i);
		}
		MPI_Buffer_detach(buf,&MAX_SIZE);
	}
	else if(rank%2 == 0){
		MPI_Recv(&n,1,MPI_INT,0,1,MPI_COMM_WORLD,&status);
		fprintf(stdout,"Received %d in process %d and the square = %d\n",n,rank,n*n);
		fflush(stdout);
	}
	else{
		MPI_Recv(&n,1,MPI_INT,0,1,MPI_COMM_WORLD,&status);
		fprintf(stdout,"Received %d in process %d and the cube = %d\n",n,rank,n*n*n);
		fflush(stdout);
	}
	MPI_Finalize();
	return 0;
}