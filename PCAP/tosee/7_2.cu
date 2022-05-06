//2. Write a program in CUDA to perform parallel Sparse Matrix - Vector Multiplication using compressed sparse row (CSR) storage format. Represent the input sparse matrix in CSR format in the host code.


#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include<stdio.h>

__global__ void SpMV_CSR(int num_rows, int *data, int *col_index, int *row_ptr, int *x, int *y){
    
    int row = blockIdx.x * blockDim.x + threadIdx.x;

    if(row < num_rows){
        int dot = 0;
        int row_start = row_ptr[row];
        int row_end = row_ptr[row+1];
        for(int elem = row_start; elem < row_end; elem++){
            dot+= data[elem] * x[col_index[elem]];
        }
        y[row]+=dot;
    }
}

int main(){

    int i,j,n,d=0,k=0,r=1,num_row;

    printf("Enter size of nxn matrix: ");

    scanf("%d",&n);

    int arr[n][n];

    printf("Enter nxn sparse matrix:\n");

    for(i = 0; i<n; ++i){
        for(j = 0; j<n; ++j){
            scanf("%d",&arr[i][j]);
            if(arr[i][j]!=0){
                ++d;
            }
        }
    }

    num_row = n;

    int data[d],col_index[d],row_ptr[num_row+1];

    row_ptr[0] = 0;

    for(i = 0; i<n; ++i){
        for(j = 0; j<n; ++j){
            if(arr[i][j]!=0){
                data[k] = arr[i][j];
                col_index[k] = j;
                ++k;
            }
        }
        row_ptr[r++] = k;
    }
    row_ptr[r] = k;

    printf("Enter values of x array: ");

    int x[num_row];

    for(i = 0; i<num_row; ++i){
        scanf("%d",&x[i]);
    }

    int y[num_row];

    printf("Enter values of y array: ");

    for(i = 0; i<num_row; ++i){
        scanf("%d",&y[i]);
    }
    int *d_data,*d_col_index,*d_row_ptr,*d_x,*d_y;

    cudaMalloc((void**)&d_data,d*sizeof(int));
    cudaMalloc((void**)&d_col_index,d*sizeof(int));
    cudaMalloc((void**)&d_row_ptr,r*sizeof(int));
    cudaMalloc((void**)&d_x,num_row*sizeof(int));
    cudaMalloc((void**)&d_y,num_row*sizeof(int));

    cudaMemcpy(d_data,data,d*sizeof(int),cudaMemcpyHostToDevice);
    cudaMemcpy(d_col_index,col_index,d*sizeof(int),cudaMemcpyHostToDevice);
    cudaMemcpy(d_row_ptr,row_ptr,r*sizeof(int),cudaMemcpyHostToDevice);
    cudaMemcpy(d_x,x,num_row*sizeof(int),cudaMemcpyHostToDevice);
    cudaMemcpy(d_y,y,num_row*sizeof(int),cudaMemcpyHostToDevice);

    SpMV_CSR<<<1,num_row>>>(num_row,d_data,d_col_index,d_row_ptr,d_x,d_y);

    cudaMemcpy(y,d_y,num_row*sizeof(int),cudaMemcpyDeviceToHost);

    printf("\nThe value after matrix mult: ");

    for(i = 0; i<num_row; ++i){
        printf(" %d",y[i]);
    }
    
    printf("\n");

    cudaFree(d_data);
    cudaFree(d_col_index);
    cudaFree(d_row_ptr);
    cudaFree(d_x);
    cudaFree(d_y);

    return 0;



}