package com.example;

import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.Arrays;
import java.util.Collections;
import java.util.Random;
import java.util.stream.Stream;

import org.junit.jupiter.api.Test;

public class KLargestTest {
    KLargest kLargest = new KLargest();
    @Test
    public void testDoKLargest(){
        int arr[] = new Random().ints(100, 0, 100).toArray();
        // Here we are converting a stream to an array so we need a generator that allocates the
        // new array
        Integer arr1[] = Arrays.stream(arr).boxed().toArray(Integer[]:: new);
        int k = 5;
        Integer[] res = kLargest.doKLargest(arr1, k);
        Arrays.sort(arr1, Collections.reverseOrder());
        for (int i=0;i<k;i++){
            System.out.println(arr1[i] + " " + res[i]);
            assertTrue(Arrays.asList(res).contains(arr1[i]));
        }
    }
}
