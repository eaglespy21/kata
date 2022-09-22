package com.example;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.Arrays;
import java.util.Random;

import org.junit.jupiter.api.Test;

public class BinarySearchTest {

    private final BinarySearch bSearch = new BinarySearch();

    @Test
    public void doBinarySearchTest(){
        int arr[] = new Random().ints(9000, 0, 10000).toArray();
        Arrays.sort(arr);
        for (int i=0; i<arr.length; i++){  // Is there a for each loop in Java?
            int val = arr[i];
            int res = bSearch.doBinarySearch(arr, val);
            assertTrue(res >= 0);
            assertEquals(val, arr[res]);
        }
    }
}
