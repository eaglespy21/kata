package com.example;

public class BinarySearch {
    public int doBinarySearch(int arr[], int val){
        int low = 0;
        int high = arr.length;
        while (low <= high){
            int mid = (low+high)/2;
            if (arr[mid] > val){
                high = mid - 1;
            }
            else if(arr[mid] < val){
                low = mid + 1;
            }
            else{
                return mid;
            }
        }
        return -1;
    }
}
