#include <cuda.h>
#include <stdlib.h>
#include <stdio.h>
#define MAX_WIDTH 7
#define MAX_MASK_WIDTH 5
__constant__ int M[MAX_MASK_WIDTH];
__global__ void kernel_1d_conv_const_mem(int *N, int *P, int mask_width, int width)
{
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    int Pvalue = 0;
    int N_start_point = i - (mask_width / 2);
    for (int j = 0; j < mask_width; j++)
    {
        if (N_start_point + j >= 0 && N_start_point + j < width)
        {
            Pvalue += N[N_start_point + j] * M[j];
        }
    }
    P[i] = Pvalue;
}
__global__ void kernel_1d_conv_shared_mem(int *N, int *P, int mask_width, int width)
{
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    extern __shared__ int N_shared[];
    // copy to shared memory
    N_shared[i] = N[i];
    __syncthreads();
    int Pvalue = 0;
    int N_start_point = i - (mask_width / 2);
    for (int j = 0; j < mask_width; j++)
    {
        if (N_start_point + j >= 0 && N_start_point + j < width)
        {
            Pvalue += N_shared[N_start_point + j] * M[j];
        }
    }
    P[i] = Pvalue;
}
int main()
{
    cudaEvent_t start, stop;
    cudaEventCreate(&start);
    cudaEventCreate(&stop);
    int width = MAX_WIDTH;
    int mask_width = MAX_MASK_WIDTH;
    int *h_N = (int *)calloc(width, sizeof(int));
    int *h_P = (int *)calloc(width, sizeof(int));
    int *h_M = (int *)calloc(mask_width, sizeof(int));
    for (int i = 0; i < width; i++)
    {
        h_N[i] = i + 1;
    }
    h_M[0] = 7;
    h_M[1] = 5;
    h_M[2] = 9;
    h_M[3] = 8;
    h_M[4] = 6;
    int *d_N;
    int *d_P;
    int size = width * sizeof(int);
    cudaMalloc((void **)&d_N, size);
    cudaMalloc((void **)&d_P, size);
    cudaMemcpy(d_N, h_N, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_P, h_P, size, cudaMemcpyHostToDevice);
    cudaMemcpyToSymbol(M, h_M, mask_width * sizeof(int));
    cudaEventRecord(start);
    kernel_1d_conv_const_mem<<<1, MAX_WIDTH>>>(d_N, d_P, mask_width, width);
    cudaEventRecord(stop);
    cudaMemcpy(h_P, d_P, size, cudaMemcpyDeviceToHost);
    cudaEventSynchronize(stop);
    float milliseconds = 0;
    cudaEventElapsedTime(&milliseconds, start, stop);
    printf("P: ");
    for (int i = 0; i < width; i++)
    {
        printf("%d, ", h_P[i]);
    }
    printf("\n");
    printf("Time to taken for 1D convolution kernel with constant memory for M is %f ms\n",
           milliseconds);
    printf("= = = = = = = = = = \n");
    /* == Shared Memory == */
    h_P = (int *)calloc(width, sizeof(int));
    cudaMemcpy(d_P, h_P, size, cudaMemcpyHostToDevice);
    cudaEventRecord(start);
    kernel_1d_conv_shared_mem<<<1, MAX_WIDTH, MAX_WIDTH>>>(d_N, d_P,
                                                           mask_width, width);
    cudaEventRecord(stop);
    cudaMemcpy(h_P, d_P, size, cudaMemcpyDeviceToHost);
    cudaEventSynchronize(stop);
    milliseconds = 0;
    cudaEventElapsedTime(&milliseconds, start, stop);
    printf("P: ");
    for (int i = 0; i < width; i++)
    {
        printf("%d, ", h_P[i]);
    }
    printf("\n");
    printf("Time to taken for 1D convolution kernel with shared memory is %f ms\n",
           milliseconds);
}
