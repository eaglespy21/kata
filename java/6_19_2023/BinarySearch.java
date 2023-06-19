import java.util.Random;
import java.util.Arrays;

class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        UnitTest ut = new UnitTest();
        ut.unitTest();
    }
}

class UnitTest 
{
    public void unitTest()
    {
        int arr[] = new Random().ints(10, 0, 1000).toArray();
        Arrays.sort(arr);
        for(int i=0;i<arr.length;i++)
        {
            System.out.print(arr[i] + " ");
        }
        BinarySearch bs = new BinarySearch();
        for (int i=0; i<arr.length; i++)
        {
            int foundI = bs.search(arr, arr[i], true);
            if (foundI == i)
            {
                //System.out.println("Found it!");
            }
            else
            {
                // If the array contains duplicates only the first key will be found 
                System.out.println("Didn't find it!");
                System.out.println(foundI + " " + i);
            }
                
        }
    }
}

class BinarySearch
{
    public int search(int[] arr, int key, boolean isSorted)
    {
        if (!isSorted)
            Arrays.sort(arr);
        int low = 0;
        int high = arr.length;
        while (low <= high)
        {
            int mid = (low + high) / 2;
            if (arr[mid] == key)
                return mid;
            else if(arr[mid] < key)
                low = mid + 1;
            else if(arr[mid] > key)
                high = mid - 1;
            else
                System.out.println("Not possible");
        }
        return -1; 
    }
}
