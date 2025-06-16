## **Day 56: The Signal Range Analyzer – Efficient Data Queries!** 📊🔍

### **📜 Kahani / Story**  
In the central communications hub of the multiverse, engineers constantly monitor streams of signal data to detect any sudden anomalies. Tumhe ab ek challenge diya gaya hai jisme aapko large signal data arrays mein se quickly sum, average, ya other metrics nikalne hain within a given range. 

Echo explains,  
*"Real-world systems require rapid data analysis to ensure seamless operations. Imagine a signal monitoring system where you need to instantly find the total signal strength in a specific time interval. For such cases, advanced DSA techniques like Segment Trees help answer range queries efficiently."*

Nariyal Bhai adds,  
*"Bilkul, yeh segment tree waise hi hai jaise ek high-speed analyzer, jo large datasets ko break karke tumhe required information turant provide karta hai. It’s a perfect mix of theory and real-world application!"*

Mayur concludes,  
*"Tumhara challenge hai to implement a Segment Tree that supports range sum queries on an array of signal strengths. Isse tumhe DSA ka advanced concept bhi aayega, aur real-world data analytics ke liye ek powerful tool bhi."*

Iss tarah, tumhari coding journey DSA ke advanced concepts ko real-world signal processing se jodti hai – ensuring that both theory and practice work hand in hand.

---

### **🎯 Challenge: Range Sum Query using Segment Tree**  
Write a program that:  
1. **Takes an array of integers as input**, representing signal strength values over time.  
2. **Builds a Segment Tree** to efficiently answer range sum queries.  
3. **Processes a number of queries**, where each query specifies a start and end index.  
4. **Prints the sum of elements** in the given range for each query.

*Note:*  
- The Segment Tree should be built to support efficient range sum queries (with O(log n) time per query).  
- This challenge simulates real-world systems where rapid data analytics is required.

---

### **🔍 Example Input/Output**

#### **Example 1**  
**Input:**  
```
Enter signal strengths (space-separated): 3 8 2 6 5 4 7
Enter number of queries: 2
Query 1 - Enter range (start end): 1 3
Query 2 - Enter range (start end): 2 6
```  
**Output:**  
```
Sum for range [1, 3]: 3 + 8 + 2 = 13
Sum for range [2, 6]: 8 + 2 + 6 + 5 + 4 = 25
```

#### **Example 2**  
**Input:**  
```
Enter signal strengths (space-separated): 10 20 30 40 50
Enter number of queries: 1
Query 1 - Enter range (start end): 0 4
```  
**Output:**  
```
Sum for range [0, 4]: 10 + 20 + 30 + 40 + 50 = 150
```

#### **Example 3**  
**Input:**  
```
Enter signal strengths (space-separated): 5 1 3 2 7 6
Enter number of queries: 2
Query 1 - Enter range (start end): 0 2
Query 2 - Enter range (start end): 3 5
```  
**Output:**  
```
Sum for range [0, 2]: 5 + 1 + 3 = 9
Sum for range [3, 5]: 2 + 7 + 6 = 15
```

---

### **💡 Hints**  
- **Building the Segment Tree:**  
  - Recursively build the tree where each node stores the sum of a segment of the array.  
- **Range Query:**  
  - Use the tree to answer each query in O(log n) time by combining the results of overlapping segments.
- **Real-World Connection:**  
  - This method is similar to how high-speed data analyzers in communication systems quickly compute statistics on continuous streams of data.

---

### **📝 Tumhara Task**  
- Write your solution in **any programming language** (Python, C++, Java, etc.).  
- Save your file as `day56_signal_range_analyzer.[ext]` (e.g., `day56_signal_range_analyzer.py`).

---

### **🌟 Motivational Quote**  
*"When data flows rapidly, efficiency is key. Build the tools that let you see the bigger picture, one segment at a time!"* 🚀

---

Your Signal Range Analyzer challenge seamlessly blends advanced DSA techniques with real-world data processing. Tumhara solution will empower rapid analysis of signal strengths, ensuring the multiverse stays in optimal condition.  
Ready for **Day 57**? Let's keep progressing!