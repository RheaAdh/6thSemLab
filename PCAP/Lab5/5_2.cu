#include <cuda.h>
#include <stdlib.h>
#include <stdio.h>
__global__ void selSortKernel(float *unsortedArr, float *sortedArr, int n)
{
    int idx = threadIdx.x + blockIdx.x * blockDim.x;
    float key = unsortedArr[idx];
    int pos = 0;
    for (int i = 0; i < n; i++)
    {
        if (unsortedArr[i] < key || (unsortedArr[i] == key && i < idx))
        {
            pos++;
        }
    }
    sortedArr[pos] = key;
}
void selSort(float *unsortedArr, float *sortedArr, int n)
{
    int size = n * sizeof(float);
    float *d_unsortedArr;
    float *d_sortedArr;
    cudaMalloc((void **)&d_unsortedArr, size);
    cudaMalloc((void **)&d_sortedArr, size);
    cudaMemcpy(d_unsortedArr, unsortedArr, size,
               cudaMemcpyHostToDevice);
    selSortKernel<<<1, n>>>(d_unsortedArr, d_sortedArr, n);
    cudaMemcpy(sortedArr, d_sortedArr, size, cudaMemcpyDeviceToHost);
    cudaFree(d_unsortedArr);
    cudaFree(d_sortedArr);
}
int main()
{
    float *h_unsortedArr, *h_sortedArr;
    int n = 5;
    int size = n * sizeof(float);
    h_unsortedArr = (float *)malloc(size);
    h_sortedArr = (float *)malloc(size);
    for (int i = 0; i < 5; i++)
    {
        h_unsortedArr[i] = rand() % 50;
    }
    selSort(h_unsortedArr, h_sortedArr, n);
    printf("unsortedArr: ");
    for (int i = 0; i < n; i++)
    {
        printf("%f, ", h_unsortedArr[i]);
    }
    printf("\n\n");
    printf("sortedArr: ");
    for (int i = 0; i < n; i++)
    {
        printf("%f, ", h_sortedArr[i]);
    }
    printf("\n");
    return 0;
}