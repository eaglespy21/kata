package com.example;

import java.util.Arrays;
import java.util.PriorityQueue;

public class KLargest {
    public Integer[] doKLargest(Integer[] arr, int k){
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>(Arrays.asList(arr).subList(0, k));
        for (int i=k; i< arr.length; i++){
            if (arr[i] > pq.peek()){
                pq.poll();
                pq.add(arr[i]);
            }
        }
        return pq.toArray(new Integer[0]);  // Need to understand what this syntax means
    }
}
