## **Day 58: The Circuit Optimizer – Power Grid Reconnection** ⚡🌐

### **📜 Kahani / Story**  
The Glitch has struck again, causing chaos in the multiverse’s power grid. Critical power lines have been severed, leaving cities in darkness. In the central control hub, engineers are working tirelessly to restore connectivity with minimal cost and maximum efficiency.

Echo explains,  
*"Imagine a vast network of power stations and substations. Due to the disruption, we need to reconnect them with the least amount of wiring to restore full functionality. This is where the Minimum Spanning Tree (MST) comes into play. Tumhara challenge hai MST implement karna – using either Kruskal’s or Prim’s algorithm – to rebuild the power grid efficiently."*

Nariyal Bhai adds,  
*"Yeh bilkul waise hi hai jaise circuits ko design karte waqt hum cost-effective paths choose karte hain. Tumhara code ensure karega ki har station sahi tarah se connected ho without wasting resources."*

Mayur concludes,  
*"This is a true test of both your DSA skills and practical engineering intuition. Find the MST to restore the power grid, and let your code be the spark that lights up the multiverse once again!"*

Iss tarah, tumhari coding journey ab real-world power distribution challenges se directly link ho gayi hai, jahan advanced DSA techniques ensure karte hain efficient connectivity.

---

### **🎯 Challenge: Minimum Spanning Tree (MST) for Power Grid Reconnection**  
Write a program that:  
1. **Takes as input a weighted undirected graph**, where nodes represent power stations and edges represent the cost of connecting them.  
2. **Finds the Minimum Spanning Tree (MST)** using Kruskal’s or Prim’s algorithm.  
3. **Prints the edges included in the MST and the total cost** to reconnect the power grid.

*Note:*  
- Assume the graph is connected.
- If using Kruskal’s algorithm, implement union-find (disjoint set) data structure for cycle detection.

---

### **🔍 Example Input/Output**

#### **Example 1**  
**Input:**  
```
Number of nodes: 4
Edges (format: u v weight):
1 2 3
1 3 1
2 3 7
2 4 5
3 4 2
```  
**Output:**  
```
MST Edges:
1 - 3 (Weight: 1)
3 - 4 (Weight: 2)
1 - 2 (Weight: 3)
Total Cost: 6
```

#### **Example 2**  
**Input:**  
```
Number of nodes: 5
Edges:
1 2 2
1 3 3
2 3 1
2 4 4
3 5 6
4 5 5
```  
**Output:**  
```
MST Edges:
2 - 3 (Weight: 1)
1 - 2 (Weight: 2)
1 - 3 (Weight: 3) or 2 - 4 (Weight: 4) [depending on algorithm implementation]
3 - 5 (Weight: 6)
Total Cost: (Calculated cost based on selected edges)
```
*(Note: The MST edges may vary if there are multiple valid MSTs, but the total cost should be minimum.)*

#### **Example 3**  
**Input:**  
```
Number of nodes: 3
Edges:
1 2 10
2 3 15
1 3 5
```  
**Output:**  
```
MST Edges:
1 - 3 (Weight: 5)
1 - 2 (Weight: 10)
Total Cost: 15
```

---

### **💡 Hints**  
- **For Kruskal’s Algorithm:**  
  - Sort all edges by weight.  
  - Use a disjoint set (union-find) to check for cycles while adding the smallest edge.
- **For Prim’s Algorithm:**  
  - Start from an arbitrary node and add the smallest edge connecting the MST to a new node.
- **Real-World Connection:**  
  - This problem mirrors the design of efficient power distribution networks in real-world engineering, where cost minimization is key.

---

### **📝 Tumhara Task**  
- Write your solution in **any programming language** (Python, C++, Java, etc.).  
- Save your file as `day58_circuit_optimizer.[ext]` (for example, `day58_circuit_optimizer.py`).

---

### **🌟 Motivational Quote**  
*"Let your code be the spark that reconnects the world. Efficient design is the cornerstone of progress – build it with passion and precision!"* 🚀

---

Your Circuit Optimizer challenge combines advanced DSA concepts with real-world power grid reconnection problems. Tumhara solution will be the blueprint for restoring light to a darkened multiverse.  
Ready for **Day 59**? Let's continue our journey into the realm of efficient systems!