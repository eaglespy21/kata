package com.example;

import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.Arrays;
import java.util.Collections;
import java.util.Random;

import org.junit.jupiter.api.Test;

public class KLargestTest {
    @Test
    public void testDoKLargest(){
        KLargest kLargest = new KLargest();
        int arr[] = new Random().ints(100, 0, 100).toArray();
        Integer arr1[] = Arrays.stream(arr).boxed().toArray(Integer[]::new);
        int k = 5;
        Integer res[] = kLargest.doKLargest(arr1, k);
        assertNotNull(res);
        Arrays.sort(arr1, Collections.reverseOrder());
        Integer expected[] = Arrays.copyOfRange(arr1, 0, k);
        for (int i=0; i<k; i++){
            System.out.println(res[i]);
            assertTrue(Arrays.asList(expected).contains(res[i]));
        }
    }
}
