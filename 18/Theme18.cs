using System;

namespace uni_prog {
    public class Theme18 {
        public static void Main() {
            int[] A = new int[] { 1, 2, 3, 4, 5 };
            int[] B = new int[] { 5, 4, 10, 2, 1 };
            int[] C = new int[] { 9, 2, 3, 4, 5, 6, 7, 8, 10, 11 };
            WriteTask(1); Task1(A, B);
            WriteTask(2); Task2(B);
            WriteTask(3); Task3(A);
            WriteTask(4); Task4(A);
            WriteTask(5); Task5(C);
        }

        private static void Task1(int[] A, int[] B) {
            int t;
            for(int i = 0; i < A.Length; i++) {
                t = A[i]; A[i] = B[i]; B[i] = t;
            }
            WriteArray(A);
            WriteArray(B);
        }

        private static void Task2(int[] A) {
            double[] B = new double[A.Length];
            int s = 0;
            for(int i = 0; i < A.Length; i++) {
                s += A[i];
                B[i] = s / (double)(i + 1);
            }
            WriteArray(B);
        }

        private static void Task3(int[] A) {
            int d = 0;
            for(int i = A.Length - 1; i >= 0; i--)
                if(A[i] % 2 != 0) {
                    d = A[i];
                    break;
                }
            for(int i =0; i<A.Length; i++)
                A[i] += d;
            WriteArray(A);
        }

        private static void Task4(int[] A) {
            int mx = 0, mn = 0;
            for(int i=1; i<A.Length; i++) {
                if(A[i] > A[mx]) mx = i;
                if(A[i] < A[mn]) mn = i;
            }
            for(int i = Math.Min(mx, mn)+1; i < Math.Max(mx, mn); i++)
                A[i] = 0;
            WriteArray(A);
        }

        private static void Task5(int[] A) {
            for(int i=1; i<A.Length-1; i++) {
                if(A[i] <= A[0] && A[i + 1] >= A[0]) {
                    int t = A[0];
                    for(int j = 0; j < i; j++)
                        A[j] = A[j + 1];
                    A[i] = t;
                    WriteArray(A);
                    return;
                }
            }
        }

        private static void WriteArray(int[] arr) {
            for(int i = 0; i < arr.Length; i++)
                Console.Write("{0} ", arr[i]);
            Console.WriteLine();
        }
        private static void WriteArray(double[] arr) {
            for(int i = 0; i < arr.Length; i++)
                Console.Write("{0} ", arr[i]);
            Console.WriteLine();
        }

        private static void WriteTask(int N) {
            Console.WriteLine("Task {0}:", N);
        }
    }
}
