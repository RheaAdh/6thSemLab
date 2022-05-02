//1.Perform tiled 1D convolution using shared memory. Find and display the time taken by the kernel. 

//1D conv using tiled
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include<stdio.h>

#define TILE_SIZE 4
#define MAX_MASK_WIDTH 5
__constant__ int M[MAX_MASK_WIDTH];

__global__ void convolution_1D_basic_kernel(int *N, int *P, int Mask_Width, int Width){
    
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    __shared__ int N_ds[TILE_SIZE + MAX_MASK_WIDTH -1];
    
    int n = Mask_Width/2;

    int halo_index_left = (blockIdx.x-1)*blockDim.x + threadIdx.x;
    if(threadIdx.x >= blockDim.x - n){
        N_ds[threadIdx.x - (blockDim.x - n)] = (halo_index_left < 0)? 0:N[halo_index_left];
    }

    N_ds[n+threadIdx.x] = N[blockIdx.x * blockDim.x + threadIdx.x];

    int halo_index_right = (blockIdx.x + 1)*blockDim.x + threadIdx.x;
    if(threadIdx.x < n){
        N_ds[n + blockDim.x + threadIdx.x] = (halo_index_right >= Width)? 0: N[halo_index_right];
    }

    __syncthreads();

    int Pvalue = 0;
    for(int j = 0; j<Mask_Width; ++j){
        Pvalue += N_ds[threadIdx.x + j] * M[j];
    }
    P[i] = Pvalue;
}

int main(void)
{
    int i,mw,w;
    printf("enter 1d array size: ");
    scanf("%d",&w);
    printf("mask array size: ");
    scanf("%d",&mw);

    int n[w],m[mw],ans[w];
    int *d_n,*d_m,*d_ans;
    int size = w*sizeof(int);
    int maskSize = mw*sizeof(int);
    float elapsedTime; 
    cudaEvent_t start, stop; 

    cudaEventCreate(&start); 
    cudaEventCreate(&stop); 

    cudaMalloc((void**)&d_n,size);
    cudaMalloc((void**)&d_m,maskSize);
    cudaMalloc((void**)&d_ans,size);

    printf("enter elements of 1D array: ");
    for(i=0;i<w;i++)
        scanf("%d",&n[i]);
    printf("enter elements of mask array: ");
    for(i=0;i<mw;i++)
        scanf("%d",&m[i]);

    cudaMemcpy(d_n,n,size,cudaMemcpyHostToDevice);
    cudaMemcpy(d_m,m,maskSize,cudaMemcpyHostToDevice);

    cudaMemcpyToSymbol(M,m,maskSize);

    cudaEventRecord(start, 0); 
    convolution_1D_basic_kernel<<<ceil(w/TILE_SIZE),TILE_SIZE>>>(d_n,d_ans,mw,w);
    cudaEventRecord(stop, 0); 
    cudaEventSynchronize(stop); 
    cudaEventElapsedTime(&elapsedTime, start, stop);
    cudaMemcpy(ans,d_ans,size,cudaMemcpyDeviceToHost);
    
    printf("\nWith tiled shared mem:\n");
    for(i=0;i<w;i++)
        printf("%d\t",ans[i]);
    printf("\nTime Taken=%f\n",elapsedTime);
    printf("\n");
    return 0;
}