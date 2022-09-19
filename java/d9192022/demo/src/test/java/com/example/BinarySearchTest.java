package com.example;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.Arrays;
import java.util.Random;

import org.junit.jupiter.api.Test;

public class BinarySearchTest {
    @Test
    public void testBinarySearch(){
        BinarySearch bSearch = new BinarySearch();
        int [] arr = {1,2,3,4,5};
        int val = 5;
        int res = bSearch.doSearch(arr, val);
        assertTrue(res >= 0);
        assertEquals(val, arr[res]);
    }

    @Test
    public void testBinarySearchRandom(){
        int [] arr = new Random().ints(10, 0, 100).toArray();
        Arrays.sort(arr);
        BinarySearch bSearch = new BinarySearch();
        for (int i=0; i <arr.length; i++){
            int val = arr[i];
            int res = bSearch.doSearch(arr, val);
            assertTrue(res >= 0);
            assertEquals(val, arr[res]);
        }
    }
}
