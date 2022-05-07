%%cu
#include<stdio.h>
#include<stdlib.h>
__global__ void kernelFunc(int *d_A,int*d_result,int n){
    int blockId=blockIdx.y*gridDim.x+blockIdx.x;
    int threadId=blockId*blockDim.x+threadIdx.x;
    int col=threadId%(n/2);
    int row=threadId/n;
    int sum=0;
    for(int i=0;i<n/2;i++){
        for(int j=0;j<n/2;j++){
            if(row==col){
                sum+=d_A[row*(n/2)+col];
            }
        }
    }
    //d_result[blockIdx]=sum;
    printf("diag sum for %d is %d\n",blockId,sum);
}
int main(){
    int n=4;
    int*h_A;
    h_A=(int*)malloc(n*n*sizeof(int));
    

    //printf("Enter matrix ele \n");
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            //scanf("%d",&h_mat[i][j]);
            h_A[i*n+j]=(i*n+j)+1;
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

    dim3 dimGrid(2,2,1);
    dim3 dimBlock(1,1,1);

    kernelFunc<<<dimGrid,dimBlock>>>(d_A,d_result,n);

    // cudaMemcpy(result,d_result,4*sizeof(int),cudaMemcpyDeviceToHost);

    // for(int i=0;i<4;i++){
    //     printf("%d ",result[i]);
    // }
    
    // cudaFree(d_result);
    // cudaFree(d_A);
}
}