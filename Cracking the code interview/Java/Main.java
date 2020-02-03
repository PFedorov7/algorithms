package com.example.algorithms;

import static com.example.algorithms.ArrayListMerge.merge;
import static com.example.algorithms.StringBuilderAppend.joinWords;


public class Main {
    public static void main(String[] args) {

        String[] words = {"asd", "asd", "asd"};
        String[] more = {"qwe", "qwe", "qwe"};

        System.out.println(merge(words, more));
        System.out.println(joinWords(words));


    }
}
