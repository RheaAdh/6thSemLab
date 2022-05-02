#include "mpi.h"
#include<stdio.h>
#include<string.h>

void tgl(char s[100]){
	for(int i=0; i<strlen(s);i++)  {
        if(s[i]>=65 && s[i]<=90)
        	s[i]+=32;
        else if(s[i]>=97 && s[i]<=122)
        	s[i]-=32;
 	}
}

int main(int argc, char *argv[]){
	int rank, size;
	char word[100];
	int MAX_SIZE = 100;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	MPI_Status status;
	if(rank == 0){
		printf("Enter the word: ");
		scanf("%s",word);
		MPI_Ssend(word,MAX_SIZE,MPI_CHAR,1,1,MPI_COMM_WORLD);
		fprintf(stdout, "Word : \"%s\" sent from process 0\n", word);
		MPI_Recv(word,MAX_SIZE,MPI_CHAR,1,1,MPI_COMM_WORLD,&status);
		fprintf(stdout,"Word : \"%s\"received from process 1\n",word);
		fflush(stdout);
	}
	else{
		MPI_Recv(word,MAX_SIZE,MPI_CHAR,0,1,MPI_COMM_WORLD,&status);
		fprintf(stdout,"Word: \"%s\"received in process 1\n",word);
		tgl(word);
		printf("Toggled string: \"%s\", being sent to process 0.\n",word);
		MPI_Ssend(word,MAX_SIZE,MPI_CHAR,0,1,MPI_COMM_WORLD);
		fflush(stdout);
	}
	MPI_Finalize();
	return 0;
}