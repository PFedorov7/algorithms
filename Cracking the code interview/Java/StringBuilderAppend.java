package com.example.algorithms;


/* StringBuilder creates a resizable array of all the strings,
    copying them back to a string only when necessary. */
public class StringBuilderAppend {

    public static String joinWords(String[] words){
        StringBuilder sentence = new StringBuilder();
        for (String w: words) {
            sentence.append(w);
        }
        return sentence.toString();
    }
}
