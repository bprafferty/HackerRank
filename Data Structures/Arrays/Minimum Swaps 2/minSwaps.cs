using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

class Solution {

    // Complete the minimumSwaps function below.
    static int minimumSwaps(int[] arr) {
        int counter = 0;
        int[] ph = new int[arr.Length];

        for (int i = 0; i < arr.Length; i++) {
            int val = arr[i] - 1;
            ph[val] = i;
        }

        for (int i = 0; i < arr.Length; i++) {
            if (arr[i] != i+1) {
                int l = ph[i];
                int temp = arr[i];
                arr[i] = i+1;
                arr[l] = temp;
                ph[i] = i;
                int val = arr[l] - 1;
                ph[val] = l;
                counter += 1;
            }
            
        }

        return counter;

    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int n = Convert.ToInt32(Console.ReadLine());

        int[] arr = Array.ConvertAll(Console.ReadLine().Split(' '), arrTemp => Convert.ToInt32(arrTemp))
        ;
        int res = minimumSwaps(arr);

        textWriter.WriteLine(res);

        textWriter.Flush();
        textWriter.Close();
    }
}
