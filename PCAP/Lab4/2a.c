#include<stdio.h>
#include "mpi.h"
#include<stdlib.h>

void ErrorHadler(int error_code){
	char error_string[1000];
	int length_of_error_string,error_class;

	MPI_Error_class(error_code,&error_class);
	MPI_Error_string(error_code,error_string,&length_of_error_string);

	fprintf(stderr,"%d %s \n",error_class,error_string);

}


int main(int argc, char *argv[]){

	int i,rank,size,factsum,fact = 1,error_code;
	float area;

	MPI_Init(&argc,&argv);
	MPI_Errhandler_set(MPI_COMM_WORLD,MPI_ERRORS_RETURN);
	
	error_code = MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	if(error_code != MPI_SUCCESS)
		ErrorHadler(error_code);

	error_code = MPI_Comm_size(MPI_COMM_WORLD,&size);
	if(error_code != MPI_SUCCESS)
		ErrorHadler(error_code);

	float currSum = 0;
	float breadth = (float)(1/(size * 5000.0));
	float height;
	//Assume each process computes 100 rectangles
	float startVal = (float)((rank * 1.0)/size);
	float endVal = (float)((rank + 1.0)/size);

	for(float i = startVal; i < endVal; i = i + breadth){
		height = (float)(4.0/(1 + i * i));
		currSum = currSum + breadth * height;
	}

	printf("Breadth = %f, Current sum in process %d = %f\n",breadth,rank,currSum);

	error_code = MPI_Reduce(&currSum,&area,1,MPI_FLOAT,MPI_SUM,0,MPI_COMM_WORLD);
	if(error_code != MPI_SUCCESS)
		ErrorHadler(error_code);
	
	if(rank == 0)
		printf("Value of pi = %f\n",area);


	MPI_Finalize();
	exit(0);

}