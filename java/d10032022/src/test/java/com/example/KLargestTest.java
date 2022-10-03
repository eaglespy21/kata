package com.example;

import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.Arrays;
import java.util.Collections;
import java.util.Random;

import org.junit.jupiter.api.Test;

public class KLargestTest {
    @Test
    public void testDoKLargest(){
        KLargest kLargest = new KLargest();
        int[] _arr = new Random().ints(100, 0, 100).toArray();
        Integer[] arr = Arrays.stream(_arr).boxed().toArray(Integer[]:: new);
        int k = 5;
        Integer[] res = kLargest.doKLargest(arr, k);
        Arrays.sort(arr, Collections.reverseOrder());
        for (int i=0;i<k; i++){
            assertTrue(Arrays.asList(res).contains(arr[i]));
        }
    }
}
