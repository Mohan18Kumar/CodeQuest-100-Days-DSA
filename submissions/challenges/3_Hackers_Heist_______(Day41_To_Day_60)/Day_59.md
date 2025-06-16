## **Day 59: The Network Overload – Maximum Flow Challenge** 🚦🔄

### **📜 Kahani / Story**  
The multiverse’s communication network is under siege! The Glitch has overloaded critical channels, causing severe congestion in the data pathways. In the central control center, engineers must ensure that the maximum possible data flows from the source to the destination to maintain system integrity.  

Echo explains,  
*"Imagine a network of pipelines where each pipe has a certain capacity. To ensure the system works smoothly, we need to calculate the maximum flow from the source to the sink. Tumhara challenge hai to implement a maximum flow algorithm – a key concept in DSA and real-world network optimization."*  

Nariyal Bhai adds,  
*"Yeh bilkul waise hai jaise power grids or communication systems mein, jahan hum ensure karte hain ki sabse zyada throughput achieve ho. Tumhara code is the tool that will help us determine the maximum data that can pass through our overloaded network."*  

Mayur concludes,  
*"Let your algorithm be the solution that unclogs the network, ensuring every bit of data finds its way through. This is a true test of your DSA prowess and real-world problem-solving skills!"*

Iss tarah, tumhari coding journey DSA ke advanced concepts ko real-world network optimization se seamlessly connect karti hai.

---

### **🎯 Challenge: Maximum Flow Problem**  
Write a program that:  
1. **Takes a directed graph as input**, representing the network.  
   - Each edge has a capacity (the maximum data it can carry).  
2. **Calculates the maximum flow** from a specified source node to a sink node using an algorithm such as the Ford-Fulkerson method or Edmonds-Karp algorithm.  
3. **Prints the maximum flow value** (i.e., the maximum total data that can be transmitted from the source to the sink).

*Note:*  
- Assume the graph is connected and capacities are positive integers.

---

### **🔍 Example Input/Output**

#### **Example 1**  
**Input:**  
```
Number of nodes: 4
Edges (u v capacity):
1 2 100
1 3 100
2 3 1
2 4 100
3 4 100
Source: 1
Sink: 4
```  
**Output:**  
```
Maximum Flow: 200
```  
*(Explanation: The optimal flow is 100 via path 1-2-4 and 100 via path 1-3-4.)*

#### **Example 2**  
**Input:**  
```
Number of nodes: 6
Edges:
1 2 16
1 3 13
2 3 10
2 4 12
3 2 4
3 5 14
4 3 9
4 6 20
5 4 7
5 6 4
Source: 1
Sink: 6
```  
**Output:**  
```
Maximum Flow: 23
```

#### **Example 3**  
**Input:**  
```
Number of nodes: 3
Edges:
1 2 5
2 3 3
Source: 1
Sink: 3
```  
**Output:**  
```
Maximum Flow: 3
```

---

### **💡 Hints**  
- **Graph Representation:**  
  - Use an adjacency list or matrix to represent the graph along with capacities.  
- **Algorithm:**  
  - For Ford-Fulkerson, use DFS to find augmenting paths and update residual capacities.  
  - Edmonds-Karp, a variant using BFS, ensures better performance in worst-case scenarios.
- **Real-World Connection:**  
  - This problem simulates the optimization of data throughput in overloaded networks—a critical concept in both computer networks and ECE.

---

### **📝 Tumhara Task**  
- Write your solution in **any programming language** (Python, C++, Java, etc.).  
- Save your file as `day59_network_overload.[ext]` (for example, `day59_network_overload.py`).

---

### **🌟 Motivational Quote**  
*"In a world full of congestion, your algorithm can pave the way for clear communication. Unleash your potential and let every node connect seamlessly!"* 🚀

---

Your maximum flow challenge is a perfect fusion of advanced DSA and real-world network optimization. Tumhara code will determine the maximum data that can traverse the network, ensuring the multiverse’s systems remain robust and efficient.  
Ready for **Day 60**? Let's keep the momentum going!