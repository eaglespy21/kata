package d9142022night;

class BinarySearch{
    public int do_search(int[] arr, int key){
        int low = 0;
        int high = arr.length;
        while (low <= high){
            int mid = (low + high) / 2;
            if (arr[mid] > key){
                high = mid - 1;
            }
            else if(arr[mid] < key){
                low = mid + 1;
            }
            else{
                return mid;
            }
        }
        return -1;
    }
}

