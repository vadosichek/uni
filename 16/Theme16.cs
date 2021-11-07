using System;

namespace uni_prog {
    public class Theme16 {
        public static void Main() {
            WriteTask(1); Task1(10);
            WriteTask(2); Task2(5,1,2);
            WriteTask(3); Task3(5, 2, 5);
            WriteTask(4); Task4(new int[] { 1, 2, 3, 4, 5 });
            WriteTask(5); Task5(new int[] { 1, 2, 3, 4, 5 });
        }

        private static void Task1(int N) {
            int[] arr = new int[N];
            for(int i = 0, j = 1; i < N; i++, j += 2)
                arr[i] = j;
            WriteArray(arr);
        }

        private static void Task2(int N, int A, int D) {
            int[] arr = new int[N];
            for(int i = 0; i < N; i++)
                arr[i] = A * (int)Math.Pow(D, i);
            WriteArray(arr);
        }

        private static void Task3(int N, int A, int B) {
            int[] arr = new int[N];
            arr[0] = A; arr[1] = B; arr[2] = A + B;
            for(int i = 3; i < N; i++)
                arr[i] = arr[i - 1] * 2;
            WriteArray(arr);
        }

        private static void Task4(int[] A) {
            for(int i=0; i < A.Length; i++) {
                Console.Write("{0} ", A[i]);
                Console.Write("{0} ", A[A.Length - 1 - i]);
            }
            Console.WriteLine();
        }

        private static void Task5(int[] A) {
            for(int i = 1; i < A.Length; i+=2) {
                Console.Write("{0} ", A[i]);
            }
            Console.WriteLine();
            for(int i = 0; i < A.Length; i += 2) {
                Console.Write("{0} ", A[A.Length - 1 - i]);
            }
            Console.WriteLine();
        }

        private static void WriteArray(int[] arr) {
            for(int i = 0; i < arr.Length; i++)
                Console.Write("{0} ", arr[i]);
            Console.WriteLine();
        }

        private static void WriteTask(int N) {
            Console.WriteLine("Task {0}:", N);
        }
    }
}
