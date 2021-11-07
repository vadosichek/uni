using System;
namespace uni_prog {
    public class Theme17 {
        public static void Main() {
            int[] A = new int[] { 1, 2, 3, 4, 5 };
            WriteTask(1); Task1(A, 1, 4);
            WriteTask(2); Task2(A);
            WriteTask(3); Task3(A);
            WriteTask(4); Task4(A);
            WriteTask(5); Task5(A);
        }

        private static void Task1(int[] A, int K, int L) {
            double s = 0;
            for(int i = K; i <= L; i++)
                s += A[i];
            s /= (L - K) + 1;
            Console.WriteLine(s);
        }

        private static void Task2(int[] A) {
            int d = A[1] - A[0];
            for(int i=2; i<A.Length; i++)
                if(A[i] - A[i-1] != d) {
                    Console.WriteLine(0);
                    return;
                }
            Console.WriteLine(d);
        }

        private static void Task3(int[] A) {
            int m = 0;
            for(int i = m+2; i < A.Length; i += 2)
                if(A[i] < A[m]) m = i;
            Console.WriteLine(A[m]);
        }

        private static void Task4(int[] A) {
            int lm = -1;
            for(int i = 1; i < A.Length - 1; i++)
                if(A[i] > A[i - 1] && A[i] > A[i + 1])
                    lm = i;
            Console.WriteLine(lm);
        }

        private static void Task5(int[] A) {
            for(int i = 0; i < A.Length; i++)
                for(int j = i + 1; j < A.Length; j++)
                    if(A[i] == A[j]) {
                        Console.WriteLine("{0} {1}", i, j);
                        return;
                    }
        }

        private static void WriteTask(int N) {
            Console.WriteLine("Task {0}:", N);
        }
    }
}
