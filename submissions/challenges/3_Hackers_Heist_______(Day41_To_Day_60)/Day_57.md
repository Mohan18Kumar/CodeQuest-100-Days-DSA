## **Day 57: The Traffic Manager – Cumulative Data with Fenwick Tree** 🚦📊

### **📜 Kahani / Story**  
The multiverse’s digital highways are under siege by The Glitch, causing chaotic traffic and data congestion. In response, the Debuggers have deployed a Traffic Management System to monitor the flow of vehicles (or data packets) in real-time.

Echo explains,  
*"Imagine each junction’s vehicle count is recorded in an array. To quickly manage the traffic, we need to update counts and query the total vehicles passing through up to a given junction. This is exactly where a Fenwick Tree (Binary Indexed Tree) comes into play—efficiently handling prefix sum queries and updates. Today, your challenge is to implement this structure."*

Nariyal Bhai adds,  
*"Yeh bilkul waise hai jaise hum real-world traffic sensors se data lete hain and then use efficient algorithms to calculate cumulative traffic. Efficiency se hi traffic control hota hai!"*

Mayur concludes,  
*"Tumhara code hi decide karega ki system kitna responsive hoga. Implement a Fenwick Tree to dynamically update and query traffic data, ensuring that our multiverse roads remain clear and congestion-free."*

Iss tarah, tumhari coding journey DSA ke advanced concepts ko real-world traffic management ke scenarios se connect karti hai.

---

### **🎯 Challenge: Traffic Manager using Fenwick Tree**  
Write a program that:  
1. **Takes an initial array of integers as input**, where each element represents the number of vehicles at a specific junction.  
2. **Builds a Fenwick Tree (Binary Indexed Tree)** to support:  
   - **Update operations:** Adjust the vehicle count at a given junction.  
   - **Prefix sum queries:** Quickly compute the total number of vehicles from the start up to any junction.
3. **Processes a series of queries** where each query is either an update or a prefix sum request, and then **prints the result**.

*Note:*  
- Updates and queries should be handled in O(log n) time using the Fenwick Tree.
- This simulates real-world scenarios where quick data aggregation is essential for effective traffic management.

---

### **🔍 Example Input/Output**

#### **Example 1**  
**Input:**  
```
Initial Traffic Data: 5 3 7 6 2
Number of queries: 3
Query 1: Query prefix sum up to index 3
Query 2: Update index 2 by adding 4 (new value becomes 11)
Query 3: Query prefix sum up to index 3
```  
**Output:**  
```
Prefix sum (index 3) before update: 5 + 3 + 7 + 6 = 21
Prefix sum (index 3) after update: 5 + 3 + 11 + 6 = 25
```

#### **Example 2**  
**Input:**  
```
Initial Traffic Data: 10 20 15 5 30
Number of queries: 2
Query 1: Update index 1 by adding 5 (new value becomes 25)
Query 2: Query prefix sum up to index 4
```  
**Output:**  
```
Prefix sum (index 4): 10 + 25 + 15 + 5 + 30 = 85
```

#### **Example 3**  
**Input:**  
```
Initial Traffic Data: 8 12 10 7 9 11
Number of queries: 2
Query 1: Query prefix sum up to index 2
Query 2: Query prefix sum up to index 5
```  
**Output:**  
```
Prefix sum (index 2): 8 + 12 + 10 = 30
Prefix sum (index 5): 8 + 12 + 10 + 7 + 9 + 11 = 57
```

---

### **💡 Hints**  
- **Fenwick Tree Basics:**  
  - Build an array (tree) that stores cumulative frequencies.  
  - Update the tree by adding the difference to all relevant nodes.
- **Query:**  
  - Use the tree to compute prefix sums in logarithmic time by traversing the tree from the given index down to 0.
- **Real-World Connection:**  
  - This is similar to how real-time systems continuously update and query cumulative traffic or sensor data for dynamic decision-making.

---

### **📝 Tumhara Task**  
- Write your solution in **any programming language** (Python, C++, Java, etc.).  
- Save your file as `day57_traffic_manager.[ext]` (for example, `day57_traffic_manager.py`).

---

### **🌟 Motivational Quote**  
*"Efficiency in data management is the backbone of progress. Let your code be the driving force that clears the path to innovation!"* 🚀

---

Your Traffic Manager challenge combines advanced DSA with a real-world application in traffic data analysis. Tumhara solution will ensure that the multiverse's data streams are efficiently updated and queried, keeping the digital highways smooth and clear.  
Ready for **Day 58**? Let's continue our journey and tackle the next challenge!