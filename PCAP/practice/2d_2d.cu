#include<cuda.h>
#include <stdlib.h>
#include <stdio.h>
__global__ void matrixMul(float *d_A, float *d_B, float *d_C,int ha,int wb,int wa)
{
 int row=blockIdx.y*blockDim.y+threadIdx.y;
 int col=blockIdx.x*blockDim.x+threadIdx.x;
  if(row<ha && col<wb){
      int sum=0;
      for(int k=0;k<wa;k++){
          if(row==0&&col==0){
              printf("%d x %d \n",row*wa+k,k*wb+col);
          }
          sum+=d_A[row*wa+k]*d_B[k*wb+col];
      }
      d_C[row*wb+col]=sum;
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

    float matA[100][100],matB[100][100];
    
    
     printf("enter a:\n");
        for(int i = 0; i < ha; ++i)
    {
       for(int j = 0; j < wa ; ++j) 
       {
          scanf("%f",&matA[i][j]);
          h_A[i*wa+j]=matA[i][j];
       }
    }
    printf("enter b:\n");
        for(int i = 0; i < hb; ++i)
    {
       for(int j = 0; j < wb ; ++j) 
       {
          scanf("%f",&matB[i][j]);
          h_B[i*wb+j]=matB[i][j];
       }
    }
printf(" a:\n");
    for (int i = 0; i < ha; i++)
    {
        for (int j = 0; j < wa; j++)
        {
            printf("%f ", h_A[i*wa+j]);
        }
        printf("\n");
    }
    printf("b:\n");
    for (int i = 0; i < hb; i++)
    {
        for (int j = 0; j < wb; j++)
        {
            printf("%f ", h_B[i*wb+j]);
        }
        printf("\n");
    }


    float *d_A, *d_B, *d_C;

    cudaMalloc((void **)&d_A, sizea);
    cudaMalloc((void **)&d_B, sizeb);
    cudaMalloc((void **)&d_C, sizec);

    cudaMemcpy(d_A, h_A, sizea, cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, h_B, sizeb, cudaMemcpyHostToDevice);
   // dim3 dimBlock(ceil(wb/2.0),ceil(ha/2.0), 1);
   // dim3 dimGrid(2,2,1);
   dim3 dimBlock(ceil(wb/2.0),ceil(ha/3.0), 1);
    dim3 dimGrid(2,3,1);
    matrixMul<<<dimGrid, dimBlock>>>(d_A, d_B, d_C,ha,wb,wa);

    cudaMemcpy(h_C, d_C, sizec, cudaMemcpyDeviceToHost);

    printf("\n\n");
    for (int i = 0; i < ha; i++)
    {
        for (int j = 0; j < wb; j++)
        {
            printf("%f ", h_C[i * wb + j]);
        }
        printf("\n");
    }
    printf("\n\n");
    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);
}