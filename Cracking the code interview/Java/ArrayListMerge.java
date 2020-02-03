package com.example.algorithms;

import java.util.ArrayList;

/* array-like data structure that offers dynamic resizing */
public class ArrayListMerge {
    public static ArrayList<String> merge(String[] words, String[] more) {
        ArrayList<String> sentence = new ArrayList<String>();
        for (String w : words) sentence.add(w);
        for (String w : more) sentence.add(w);
        return sentence;
    }
}
