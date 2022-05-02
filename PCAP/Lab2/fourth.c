#include<mpi.h>
#include<stdio.h>
#include<stdlib.h>
#define MCW MPI_COMM_WORLD
int main(int argc,char*argv[]){
	int rank,size,num;
	MPI_Comm_rank(MCW,&rank);
	MPI_Comm_size(MCW,&size);
	MPI_Status status;
	if(rank==0){
		printF("Enter a number:\n");
		scanf("%d",&num);
		printf("In process %d\n",rank);
		printf("sent %d",num);
		MPI_Send(&num,1,MPI_INT,rank+1,0,MCW);
		MPI_Recv(&num,1,MPI_INT,size-1,0,MCW);
		printf("In process %d\n",rank);
		printf("Received %d\n\n",num);
	}
	else{
		MPI_Recv(&num,1,MPI_INT,rank-1,0,MCW,&status);
		printf("In process %d\n",rank);
		printf("Received %d\n",num);
		num++;
		printf("Sent %d\n\n",num);
		MPI_Send(&num,1,MPI_INT,(rank+1)%size,0,MCW);
	}
	MPI_Finalize();
}