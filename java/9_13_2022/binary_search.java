public class Example{
    public int binary_search(int arr[], int key) {
        int low = 0;
        int high = arr.length;
        while (low < high)
        {
            int mid = (low + high)/2;
            if (arr[mid] < key) {
                low = mid + 1;
            }
            else if (arr[mid] > key){
                high = mid - 1;
            }
            else{
                return mid;
            }
        }
        return -1;
    }
    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5};
        Example obj = new Example();
        System.out.println(obj.binary_search(arr, 5));
    }
}

//TODO: How to run this program with one of the classes not havin a main function?
//TODO: Fix vscode extension issues

