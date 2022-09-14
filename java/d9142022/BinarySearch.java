package d9142022;

public class BinarySearch {
    public int doSearch(int []arr, int key){
        int left = 0;
        int right = arr.length;
        while (left < right){
            int mid = (left + right) / 2;
            if (arr[mid] > key){
                right = mid - 1;
            }
            else if(arr[mid] < key){
                left = mid + 1;
            }
            else{
                return mid;
            }
        }
        return -1;
    }
}
