#include<cuda.h>
#include<stdio.h>
#include<stdlib.h>
__global__ void kernelFunc(int *d_A,int*d_result,int n){
    //one thread in the block calculates diagnol sum
    int idx=2*blockIdx.y+blockIdx.x;
    int row=blockIdx.y;
    int col=blockIdx.x;
    int sum=0;
  
    for(int i=0;i<n/4;i++){
        for(int j=0;j<n/4;j++){
            if(row==col){
                sum+=d_A[i*n+j];
            }
        }
    }
    d_result[idx]=sum;
    
}
int main(){
    int h_mat[100][100];
    int n;
    printf("Enter N of matrix N*N\n");
    scanf("%d",&n);
    
    int*h_A;
    h_A=(int*)malloc(n*n*sizeof(int));

    printf("Enter matrix ele \n");
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            scanf("%d",&h_mat[i][j]);
            h_A[i*n+j]=h_mat[i][j];
        }
    }
    printf(" matrix ele \n");
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            printf("%d",h_A[i*n+j]);
        }
        printf("\n");
    }
    int*d_A;
    cudaMalloc((void**)&d_A,n*n*sizeof(int));
    cudaMemcpy(d_A,h_A,n*n*sizeof(int),cudaMemcpyHostToDevice);

    int*result,*d_result;
    result=(int*)malloc(4*sizeof(int));
    cudaMalloc((void**)&d_result,4*sizeof(int));

    cudaMemcpy(d_result,result,4*sizeof(int),cudaMemcpyHostToDevice);

    dim3 dimGrid(n/2,n/2,1);
    dim3 dimBlock(1,1,1);

    kernelFunc<<<dimGrid,dimBlock>>>(d_A,d_result,n);

    cudaMemcpy(result,d_result,4*sizeof(int),cudaMemcpyDeviceToHost);

    for(int i=0;i<4;i++){
        printf("%d ",result[i]);
    }
    
    cudaFree(d_result);
    cudaFree(d_A);
}
