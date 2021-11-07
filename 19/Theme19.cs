using System;
using System.Collections.Generic;
using System.Linq;

namespace uni_prog {
    public class Theme19 {
        public static void Main() {
            int[] A = new int[] { 1, 1, 1, 4, 4, 5 };
            int[] B = new int[] { 1, 1, 2, 4, 4, 5, 5, 5, 5 };
            int[] C = new int[] { -1, 1, 2, 3, 4, -5, 1, 2, 3, -2 };
            WriteTask(1); Task1(A);
            WriteTask(2); Task2(B);
            WriteTask(3); Task3(A);
            WriteTask(4); Task4(C);
            WriteTask(5); Task5(C);
        }

        private static void Task1(int[] A) {
            List<int> a = new List<int>(A);
            for(int i = 0; i < a.Count-1;) {
                if(a[i] == a[i + 1]) a.Remove(a[i + 1]);
                else i++;
            }
            WriteList(a);
        }

        private static void Task2(int[] A) {
            List<int> a = new List<int>(A);
            foreach(int i in A) {
                if(A.Count(x => x == i) == 2)
                    a.RemoveAll(x => x == i);
            }
            WriteList(a);
        }

        private static void Task3(int[] A) {
            List<int> a = new List<int>(A);
            int mni = a.IndexOf(a.Min());
            int mxi = a.IndexOf(a.Max()) + 1;

            if(mni <= 0) a.Insert(0, 0);
            else a.Insert(mni, 0);
            a.Insert(mxi + 1, 0);
            WriteList(a);
        }

        private static void Task4(int[] A) {
            List<int> a = new List<int>(A);
            for(int i = 0; i < a.Count; i++) {
                if(a[i] < 0) {
                    a.Insert(i + 1, 0);
                    i++;
                }
            }
            WriteList(a);
        }

        private static void Task5(int[] A) {
            List<int> a = new List<int>(A);
            for(int i = 0; i < a.Count; i++) {
                if(a[i] > 0) {
                    a.Insert(i, 0);
                    i++;
                }
            }
            WriteList(a);
        }

        private static void WriteList(List<int> lst) {
            for(int i = 0; i < lst.Count; i++)
                Console.Write("{0} ", lst[i]);
            Console.WriteLine();
        }

        private static void WriteTask(int N) {
            Console.WriteLine("Task {0}:", N);
        }
    }
}
