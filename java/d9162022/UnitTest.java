package d9162022;

import java.util.Random;

public class UnitTest {
    public void unitTest(){
        BinarySearch bobj = new BinarySearch();
        int arr[] = {1,2,3,4,5};
        int val = 5;
        int res = bobj.do_search(arr, val, true);
        if (res == -1){  // In java, like in python arr[-1] points to the last element
            System.out.println("Val " + val + " not found");
            System.out.println("Failure");
        }
        else{
            assert val == arr[res];
            System.out.println("Success");
        }

    }
    public void unitTestAdv(){
        BinarySearch bobj = new BinarySearch();
        int [] arr = new Random().ints(1000, 0, 10000).toArray();
        for (int i = 0; i < arr.length; i++){
            int val = arr[i];
            int res = bobj.do_search(arr, val, false);
            if (res == -1){
                System.out.println("Val" + val + " not found");
                System.out.println("Failure");
                return;
            }
            else{
                assert val == arr[res];
            }
        }
        System.out.println("Success");
    }
}
