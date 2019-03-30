Quiz 2

Hilmi Raditya Prakoso - 5116100164
Falah Ath Thariq Razzaq - 5116100151
Rahmad Yanuar - 5116100159


Description

There is few shortest path algorithm, one of them is Djikstra Path Algorithm.  Djikstra’s algorithm is very similar to Prim’s Algorithm for minimum spanning tree. Like Prim’s MST, we generate a shortest path tree with given source as root. We maintain two sets, one set contains vertices included in shortest path tree, other set includes vertices not yet included in shortest path tree. At every step of the algorithm, we find a vertex which is in the other set (set of not yet included) and has a minimum distance from the source.

Below are the step of Djistra Algorithm

1.  Create a set sptSet (shortest path tree set) that keeps track of vertices included in shortest path tree, i.e., whose minimum distance from source is calculated and finalized. Initially, this set is empty.
2. Assign a distance value to all vertices in the input graph. Initialize all distance values as INFINITE. Assign distance value as 0 for the source vertex so that it is picked first.
