#include "mpi.h"
#include<stdio.h>

int main(int argc, char* argv[]){
	int rank;
	char str[5] = "HeLLO";
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	printf("Rank = %d\n",rank);
	printf("Original string is %s\n",str);
	if(str[rank]>=65 && str[rank]<=90)
        str[rank]+=32;
    else if(str[rank]>=97 && str[rank]<=122)
        str[rank]-=32;
	printf("Modified string is %s\n",str);
	MPI_Finalize();
	return 0;
}