#include <cuda.h>
#include <stdlib.h>
#include <stdio.h>

__global__ void vec1a(int *A, int *B, int *C)
{
    int idx = threadIdx.x + blockIdx.x * blockDim.x;
    C[idx] = A[idx] + B[idx];
}
__global__ void vec1b(int *A, int *B, int *C)
{
    int idx = threadIdx.x + blockIdx.x * blockDim.x;
    C[idx] = A[idx] + B[idx];
}
__global__ void vec1c(int *A, int *B, int *C,
                      int n)
{
    int idx = threadIdx.x + blockIdx.x * blockDim.x;
    if (idx < n)
    {
        C[idx] = A[idx] + B[idx];
    }
}
void vecAdd(int *A, int *B, int *C, int n)
{
    int size = n * sizeof(float);
    int *d_A;
    int *d_B;
    int *d_C;
    cudaMalloc((void **)&d_A, size);
    cudaMalloc((void **)&d_B, size);
    cudaMalloc((void **)&d_C, size);
    cudaMemcpy(d_A, A, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, B, size, cudaMemcpyHostToDevice);
    printf("A: ");
    for (int i = 0; i < n; i++)
    {
        printf("%f, ", A[i]);
    }
    printf("\n");
    printf("B: ");
    for (int i = 0; i < n; i++)
    {
        printf("%f, ", B[i]);
    }
    printf("\n\n");
    vec1a<<<n, 1>>>(d_A, d_B, d_C);
    cudaMemcpy(C, d_C, size, cudaMemcpyDeviceToHost);
    printf("A+B (from 1a kernel): ");
    for (int i = 0; i < n; i++)
    {
        printf("%f, ", C[i]);
    }
    printf("\n");
    vec1b<<<1, n>>>(d_A, d_B, d_C);
    cudaMemcpy(C, d_C, size, cudaMemcpyDeviceToHost);
    printf("A+B (from 1b kernel): ");
    for (int i = 0; i < n; i++)
    {
        printf("%f, ", C[i]);
    }
    printf("\n");
    vec1c<<<ceil(n / 256.0), 256>>>(d_A, d_B,
                                    d_C, n);
    cudaMemcpy(C, d_C, size, cudaMemcpyDeviceToHost);
    printf("A+B (from 1c kernel): ");
    for (int i = 0; i < n; i++)
    {
        printf("%f, ", C[i]);
    }
    printf("\n");
    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);
}
int main()
{
    int *h_A, *h_B, *h_C;
    int n = 5;
    int size = n * sizeof(float);
    h_A = (int *)malloc(size);
    h_B = (int *)malloc(size);
    h_C = (int *)malloc(size);
    for (int i = 0; i < n; i++)
    {
        h_A[i] = (i + 1) * 10;
        h_B[i] = i + 1;
    }
    vecAdd(h_A, h_B, h_C, n);
    return 0;
}