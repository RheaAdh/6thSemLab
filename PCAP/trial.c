#include "mpi.h"
#include<stdio.h>
#include<stdlib.h>

int main(int argc, char * argv[]){
    int rank,size,i,N;
    MPI_Init(&argc,&argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    MPI_Comm_size(MPI_COMM_WORLD,&size);
    MPI_Status status;
    int arr[size],num,arr2[size];

    if(rank == 0){
        printf("Enter %d numbers: ",size);
        N = size;
        for(i = 0; i<N; ++i){
            scanf("%d",&arr[i]);
        }
    }

    MPI_Scatter(arr,1,MPI_INT,&num,1,MPI_INT,0,MPI_COMM_WORLD);
    
    num = rand();
    printf("Num at process %d = %d\n",rank,num);
    if(rank != 0){
        MPI_Send(&num,1,MPI_INT,0,1,MPI_COMM_WORLD);
    }
    else{
        arr2[0] = num;
        for(i = 1; i<N; ++i){
            MPI_Recv(&arr2[i],1,MPI_INT,i,1,MPI_COMM_WORLD,&status);
        }
        printf("The new array is - \n");
        for(i = 0; i<N; ++i){
            num = arr[i]+arr2[i];
            printf("%d ",num);
        }
        printf("\n");
    }
    MPI_Finalize();
    return 0;
}
