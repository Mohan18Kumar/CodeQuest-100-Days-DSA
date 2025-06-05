## **Day 46: The Signal Router – Find the Shortest Path** 📡🛣️

### **📜 Kahani / Story**  
Tum ab ek high-tech network control center mein ho, jahan data packets ko efficient routes choose karne padte hain to avoid delays and congestion.  
  
Echo explains,  
*"Jab data packets ek network se guzar rahe hote hain, toh har router ko shortest and fastest path choose karna padta hai. Is challenge mein, tumhe ek network graph diya jayega, jisme har edge ka weight signal delay ya cost ko represent karta hai. Tumhara kaam hai, Dijkstra's algorithm ka use karke, starting node se destination tak ka shortest path find karna – just like real-world routing protocols in communication systems."*

Nariyal Bhai adds,  
*"Yeh bilkul waise hi hai jaise hum circuits mein optimal path choose karte hain, taaki signal loss na ho. Tumhara code hi decide karega ki kaunsa path sabse efficient hai."*

Mayur, with his usual dramatic flair, chimes in,  
*"Socho, yeh challenge tumhari network design skills ko test karta hai. Agar tumhara routing sahi hua, toh data packets bina kisi delay ke apni destination tak pahunch jayenge. Ab, let’s optimize the network like true engineers!"*

Iss tarah, tumhari coding journey directly link hoti hai real-world ECE networking concepts se, jahan routing protocols ensure karte hain ke har packet safe aur timely destination tak pohonche.

---

### **🎯 Challenge: Shortest Path Finder (Dijkstra's Algorithm)**  
Write a program that:  
1. **Represents a network graph** using an adjacency list or matrix, where nodes represent routers and edges represent the cost (delay) between them.  
2. **Takes a starting node and a destination node as input.**  
3. **Finds the shortest path from the starting node to the destination node** using Dijkstra's algorithm.  
4. **Prints the shortest path and its total cost.**

*Note:*  
- You may assume that the graph is connected and all edge weights are positive.  
- The input format for the graph can be pre-defined or taken as input based on your implementation.

---

### **🔍 Example Input/Output**

#### **Example 1**  
**Input:**  
```
Graph (as an adjacency list):
A: {B: 4, C: 2}
B: {A: 4, C: 1, D: 5}
C: {A: 2, B: 1, D: 8, E: 10}
D: {B: 5, C: 8, E: 2, Z: 6}
E: {C: 10, D: 2, Z: 3}
Z: {D: 6, E: 3}
Starting Node: A
Destination Node: Z
```  
**Output:**  
```
Shortest Path: A -> C -> B -> D -> E -> Z
Total Cost: 12
```

#### **Example 2**  
**Input:**  
```
Graph:
1: {2: 7, 3: 9, 6: 14}
2: {1: 7, 3: 10, 4: 15}
3: {1: 9, 2: 10, 4: 11, 6: 2}
4: {2: 15, 3: 11, 5: 6}
5: {4: 6, 6: 9}
6: {1: 14, 3: 2, 5: 9}
Starting Node: 1
Destination Node: 5
```  
**Output:**  
```
Shortest Path: 1 -> 3 -> 6 -> 5
Total Cost: 20
```

---

### **💡 Hints**  
- **Graph Representation:**  
  - Use a dictionary (or array) to represent the graph and store edge weights.  
- **Dijkstra's Algorithm:**  
  - Initialize distances to all nodes as infinity except for the starting node (set to 0).  
  - Use a priority queue (min-heap) to extract the node with the smallest distance.  
  - Update distances for adjacent nodes if a shorter path is found.  
- **Path Reconstruction:**  
  - Keep track of predecessors for each node to reconstruct the shortest path after the algorithm finishes.

---

### **📝 Tumhara Task**  
- Write your solution in **any programming language** (Python, C++, Java, etc.).  
- Save your file as `day46_signal_router.[ext]` (e.g., `day46_signal_router.py`).

---

### **🌟 Motivational Quote**  
*"In a complex network, finding the shortest path is not just about speed – it's about precision and strategy. Let your code be the router that guides every packet safely home!"* 🚀

---

Your signal router challenge integrates real-world networking and ECE concepts with advanced coding techniques. Tumhara solution will emulate how modern routers find optimal paths in digital communication systems.  
Ready for **Day 47** as we delve deeper into the multiverse? Let's keep moving forward!