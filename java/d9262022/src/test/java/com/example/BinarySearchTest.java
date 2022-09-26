package com.example;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.Arrays;
import java.util.Random;

import org.junit.jupiter.api.Test;

import com.example.BinarySearch;

public class BinarySearchTest {
    @Test
    public void testDoBinarySearch(){
        BinarySearch bSearch = new BinarySearch();
        int arr[] = new Random().ints(9000, 0, 10000).toArray();
        Arrays.sort(arr);
        for (int num: arr){
            int res = bSearch.doBinarySearch(arr, num);
            assertTrue(res >= 0);
            assertEquals(num, arr[res]);
        }
    }
}
