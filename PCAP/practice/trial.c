%%cu
#include <stdlib.h>
#include <stdio.h>
_global_ void matrixMul(float *d_A, float *d_B, float *d_C, int wa, int wb)
{
    int row = threadIdx.x;
    int n = blockDim.y;
    for (int i = 0; i < wb; i++)
    {
        // float k=0;
        for (int j = 0; j < wa; j++)
        {
            printf("row=%d j=%d j=%d i=%d\n", row, j, j, i);
            //printf("%d X %d\n",row*wa+j,j*wb+i);
            //  k+=d_A[row*wa+j]*d_B[j*wb+i];
        }
        //d_C[row*wb+i]=k;
    }
}
int main()
{
    float *h_A, *h_B, *h_C;
    int ha, hb, wa, wb;
    ha = 3;
    wa = 4;
    hb = 4;
    wb = 5;
    int sizea = ha * wa * sizeof(float);
    int sizeb = hb * wb * sizeof(float);
    int sizec = ha * wb * sizeof(float);

    h_A = (float *)malloc(sizea);
    h_B = (float *)malloc(sizeb);
    h_C = (float *)malloc(sizec);

    for (int i = 0; i < ha; i++)
    {
        for (int j = 0; j < wa; j++)
        {
            h_A[i * wa + j] = i * 1.0 * wa + j;
        }
    }
    for (int i = 0; i < hb; i++)
    {
        for (int j = 0; j < wb; j++)
        {
            h_B[i * wb + j] = i * 1.0 * wb + j;
        }
    }
    // for (int i = 0; i < ha; i++)
    // {
    //     for (int j = 0; j < wa; j++)
    //     {
    //         printf("%f ", h_A[i * wa + j]);
    //     }
    //     printf("\n");
    // }
    // printf("\n\n");
    // for (int i = 0; i < hb; i++)
    // {
    //     for (int j = 0; j < wb; j++)
    //     {
    //         printf("%f ", h_B[i * wb + j]);
    //     }
    //     printf("\n");
    // }
    float *d_A, *d_B, *d_C;

    cudaMalloc((void **)&d_A, sizea);
    cudaMalloc((void **)&d_B, sizeb);
    cudaMalloc((void **)&d_C, sizec);

    cudaMemcpy(d_A, h_A, sizea, cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, h_B, sizeb, cudaMemcpyHostToDevice);
    dim3 dimBlock(1, 1, 1);
    dim3 dimGrid(1, 1, 1);
    dimBlock.x = ha;
    dimBlock.y = 1;
    dimBlock.z = 1;
    matrixMul<<<dimGrid, dimBlock>>>(d_A, d_B, d_C, wa, wb);

    cudaMemcpy(h_C, d_C, sizec, cudaMemcpyDeviceToHost);

    printf("\n\n");
    // for (int i = 0; i < ha; i++)
    // {
    //     for (int j = 0; j < wb; j++)
    //     {
    //         printf("%f ", h_C[i * wb + j]);
    //     }
    //     printf("\n");
    // }
    //printf("\n\n");
    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);
}