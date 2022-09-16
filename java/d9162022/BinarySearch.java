package d9162022;

import java.util.Arrays;

public class BinarySearch {
    public int do_search(int []arr, int val, Boolean isSorted){
        if (!isSorted){
            Arrays.sort(arr);
        }
        int low = 0;
        int high = arr.length;
        while (low <= high){
            int mid = (low + high) / 2;
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
