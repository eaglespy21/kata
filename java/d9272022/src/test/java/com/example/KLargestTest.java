package com.example;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.Arrays;
import java.util.Collections;
import java.util.Random;

import org.junit.jupiter.api.Test;

import com.example.KLargest;

public class KLargestTest {
    @Test
    public void testDoKLargest(){
        KLargest kLargest = new KLargest();
        int[] arr = new Random().ints(9000, 0, 10000).toArray();
        Integer[] arr1 = Arrays.stream(arr).boxed().toArray(Integer[]::new);
        // Need to understand this syntax
        int k = 5;
        Integer[] res = kLargest.doKLargest(arr1, k);
        Arrays.sort(arr1, Collections.reverseOrder());
        for (Integer num: res){
            assertTrue(Arrays.asList(arr1).subList(0, k).contains(num));
        }
    }
}
