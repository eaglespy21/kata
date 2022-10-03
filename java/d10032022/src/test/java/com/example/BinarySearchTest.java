package com.example;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.Arrays;
import java.util.Random;

import org.junit.jupiter.api.Test;

public class BinarySearchTest {
    @Test
    public void testDoBinarySearch(){
        BinarySearch binarySearch = new BinarySearch();
        int arr[] = new Random().ints(100, 0, 100).toArray();
        Arrays.sort(arr);
        for (int val: arr){
            // Got an index out of bounds error when -1 was returned which is new
            int res = binarySearch.doBinarySearch(arr, val);
            assertEquals(val, arr[res]);
        }
    }
}
