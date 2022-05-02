#include <cuda.h>
#include <stdio.h>
#include <stdlib.h>
__global__ void matAddKernel_1a(float *a, float *b, float *c, int n)
{
    int ridA = threadIdx.x;
    int i;
    for (i = 0; i < n; i++)
    {
        c[ridA * n + i] = a[ridA * n + i] + b[ridA * n + i];
    }
}
__global__ void matAddKernel_1b(float *a, float *b, float *c, int m)
{
    int col = threadIdx.x;
    int n = blockDim.x;
    int i;
    for (i = 0; i < m; i++)
    {
        c[i * n + col] = a[i * n + col] + b[i * n + col];
    }
}
__global__ void matAddKernel_1c(float *a, float *b, float *c)
{
    int row = threadIdx.x;
    int col = threadIdx.y;
    int n = blockDim.y;
    c[row * n + col] = a[row * n + col] + b[row * n + col];
}
void matAdd(float *a, float *b, float *c, int m, int n)
{
    int size = m * n * sizeof(float);
    float *d_A;
    float *d_B;
    float *d_C;
    cudaMalloc((void **)&d_A, size);
    cudaMalloc((void **)&d_B, size);
    cudaMalloc((void **)&d_C, size);
    cudaMemcpy(d_A, a, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, b, size, cudaMemcpyHostToDevice);
    int i, j;
    printf("A:\n");

    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            printf("%f ", *(a + i * n + j));
        }
        printf("\n");
    }

    printf("B:\n");

    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            printf("%f ", *(b + i * n + j));
        }
        printf("\n");
    }

    printf("\n");
    matAddKernel_1a<<<1, m>>>(d_A, d_B, d_C, n);
    cudaMemcpy(c, d_C, size, cudaMemcpyDeviceToHost);
    printf("A+B(From the first Kernel):\n");

    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            printf("%f ", *(c + i * n + j));
        }
        printf("\n");
    }

    printf("\n");
    matAddKernel_1b<<<1, n>>>(d_A, d_B, d_C, m);
    cudaMemcpy(c, d_C, size, cudaMemcpyDeviceToHost);

    printf("A+B(From the second Kernel):\n");
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            printf("%f ", *(c + i * n + j));
        }
        printf("\n");
    }

    printf("\n");
    matAddKernel_1c<<<(1, 1), (m, n)>>>(d_A, d_B, d_C);
    cudaMemcpy(c, d_C, size, cudaMemcpyDeviceToHost);

    printf("A+B(From the third Kernel):\n");
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            printf("%f ", *(c + i * n + j));
        }
        printf("\n");
    }

    printf("\n");
    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);
}
int main()
{
    float *a, *b, *c;
    int n = 3, m = 5;
    int size = m * n * sizeof(float);
    a = (float *)malloc(size);
    b = (float *)malloc(size);
    c = (float *)malloc(size);
    int i, j, k = 5;
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            *(a + i * n + j) = float(k);
            *(b + i * n + j) = float(k + 2);
            k += 1;
        }
    }
    matAdd(a, b, c, m, n);
}