%%cu
#include<cuda.h>
#include<stdio.h>
#include<stdlib.h>
__global__ void kernelFunc(int *d_A,int*d_result,int n){
    int blockId=blockIdx.y*gridDim.x+blockIdx.x;
    int threadId=blockId*blockDim.x+threadIdx.x;
    int colstart=blockIdx.x*(n/2);
    int rowstart=blockIdx.y*(n/2);
   printf("colstart for %d is %d to %d\n",blockId,colstart,colstart+(n/2)-1);
    printf("rowstart for %d is %d to %d\n",blockId,rowstart,rowstart+(n/2)-1);
    int sum=0;
    int row1=0,col1=0;
  
    for(int i=rowstart;i<rowstart+(n/2);i++){
      row1++;
        for(int j=colstart;j<colstart+(n/2);j++){
           col1++;
    
            if(row1==col1){
               // printf("i %d j %d",i,j);
            //   printf("row and col %d %d",row1,col1);
                 
                sum+=d_A[i*n+j];

              

            }
           

             
        }
         col1=0;
          
    }
    d_result[blockId]=sum;
    printf("\ndiag sum for %d is %d\n",blockId,sum);
}
int main(){
    int n=6;
    int*h_A;
    h_A=(int*)malloc(n*n*sizeof(int));

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            h_A[i*n+j]=(i*n+j)+1;
        }
    }

    printf(" matrix ele \n");
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            printf("%d     ",h_A[i*n+j]);
        }
        printf("\n");
    }


    int*d_A;
    cudaMalloc((void**)&d_A,n*n*sizeof(int));
    cudaMemcpy(d_A,h_A,n*n*sizeof(int),cudaMemcpyHostToDevice);

    int*result,*d_result;
    result=(int*)malloc(4*sizeof(int));
    cudaMalloc((void**)&d_result,4*sizeof(int));

    dim3 dimGrid(2,2,1);
    dim3 dimBlock(1,1,1);

    kernelFunc<<<dimGrid,dimBlock>>>(d_A,d_result,n);

    cudaMemcpy(result,d_result,4*sizeof(int),cudaMemcpyDeviceToHost);

    for(int i=0;i<n-1;i++){
        printf("%d ",result[i]);
   }
    
   cudaFree(d_result);
   cudaFree(d_A);

}