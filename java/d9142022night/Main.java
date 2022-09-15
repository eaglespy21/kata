package d9142022night;

import java.util.Arrays;
import java.util.Random;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) {
        // int [] arr = {1,2,3,4,5};
        // int [] arr = new Random().ints(5, 0, 100).toArray();
        int[] arr = IntStream.generate(() -> new Random().nextInt(1000)).limit(10).toArray();
        Random rd = new Random();
        // int[] arr = new int[5];
        // for (int i =0; i < arr.length; i++){
        //     // arr[i] = rd.nextInt(100);
        //     System.out.println(arr[i]);
        // }
        Arrays.sort(arr);
        BinarySearch bsobj = new BinarySearch();
        int key = rd.nextInt(arr.length);
        int res = bsobj.do_search(arr, arr[key]);
        // TODO: Change name of key, its overloaded
        if (key == res){
            System.out.println("Test passed " + key);
        }
        else{
            System.out.println("Test failed " + key + " " + res);
        }
        System.out.println(res);
    }
}
