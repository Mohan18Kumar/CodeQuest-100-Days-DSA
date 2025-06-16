## **Day 54: The Data Packet Reassembler – Merge Overlapping Intervals** 📦🔗

### **📜 Kahani / Story**  
The Glitch has fragmented the data packets, scattering pieces of information across the multiverse's network. Now, our system has captured multiple time intervals representing these packets. However, some intervals overlap due to network congestion and retransmissions.

Echo explains,  
*"Imagine each interval as a time slot during which a packet is active. To rebuild the complete message, you must merge overlapping intervals—just like reassembling fragmented data in real-world systems. This is a common task in network data processing and scheduling."*

Nariyal Bhai adds,  
*"Yeh bilkul waise hai jaise tum log apne daily schedules ko merge karte ho jab timings clash ho jati hain. Tumhara kaam hai in intervals ko merge karke ek clear, continuous timeline banana!"*

Mayur concludes,  
*"This challenge not only reinforces key DSA concepts like sorting and merging but also mirrors real-world packet reassembly in network communications. Tumhara solution ek seamless data stream create karega, jisse multiverse ka message dobara poora ho jayega."*

Iss tarah, tumhari coding journey DSA techniques ko real-world data handling se connect karti hai, ensuring that fragmented packets are seamlessly reassembled.

---

### **🎯 Challenge: Merge Overlapping Intervals**  
Write a program that:  
1. **Takes a list of intervals as input**, where each interval represents a data packet's active time (start and end times).  
2. **Merges all overlapping intervals** to form a set of non-overlapping intervals that cover all the data.
3. **Prints the merged intervals** in ascending order.

*Note:*  
- An interval is represented as `[start, end]`.  
- Two intervals `[a, b]` and `[c, d]` overlap if `a ≤ d` and `c ≤ b`.

---

### **🔍 Example Input/Output**

#### **Example 1**  
**Input:**  
```
Enter intervals (format: start-end, space-separated): 1-3 2-6 8-10 15-18
```  
**Output:**  
```
Merged Intervals: [1, 6] [8, 10] [15, 18]
```  
*(Explanation: Intervals 1-3 and 2-6 merge into 1-6.)*

#### **Example 2**  
**Input:**  
```
Enter intervals (format: start-end, space-separated): 1-4 4-5
```  
**Output:**  
```
Merged Intervals: [1, 5]
```  
*(Explanation: Intervals 1-4 and 4-5 merge into 1-5.)*

#### **Example 3**  
**Input:**  
```
Enter intervals (format: start-end, space-separated): 5-7 1-3 2-4
```  
**Output:**  
```
Merged Intervals: [1, 4] [5, 7]
```  
*(Explanation: After sorting, intervals 1-3 and 2-4 merge into 1-4; 5-7 remains separate.)*

---

### **💡 Hints**  
- **Sorting:**  
  - First, sort the intervals based on the start times.
- **Merging:**  
  - Iterate through the sorted intervals and merge two intervals if the current interval's start is less than or equal to the previous interval's end.
- **Real-World Connection:**  
  - This process is similar to how network systems reassemble fragmented data packets into a continuous stream for further processing.

---

### **📝 Tumhara Task**  
- Write your solution in **any programming language** (Python, C++, Java, etc.).  
- Save your file as `day54_data_packet_reassembler.[ext]` (e.g., `day54_data_packet_reassembler.py`).

---

### **🌟 Motivational Quote**  
*"Fragmented data, like scattered clues, forms a complete picture when merged with precision. Let your code be the bridge that unites every piece into harmony!"* 🚀

---

Your data packet reassembler challenge connects core DSA concepts with real-world network data processing. Tumhara solution will reassemble fragmented intervals into a seamless timeline, ensuring the multiverse's message is restored.  
Ready for **Day 55**? Let's move forward on this journey!