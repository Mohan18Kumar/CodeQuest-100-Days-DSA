## **Day 51: The Priority Scheduler – Urgent Alerts First!** ⏱️🔔

### **📜 Kahani / Story**  
In the multiverse control center, systems are monitored 24/7 to detect any critical faults or emergencies. Recently, The Glitch has been sending mixed signals – some are minor alerts, while others are critical warnings that need immediate attention.  
   
Echo explains,  
*"Jab multiple alerts ek saath aate hain, toh humein unmein se sabse important alerts pehle process karna hota hai. Is challenge mein tumhe ek priority scheduler implement karna hai, using a data structure like a priority queue. Yeh DSA concept real-world systems mein bhi use hota hai to ensure urgent alerts are addressed first."*  

Nariyal Bhai adds,  
*"Bilkul waise hi jaise tum log real-world mein critical components ko prioritize karte ho, tumhara code alerts ko unki urgency ke hisaab se sort karega. Yeh simple yet powerful technique hai for efficient system monitoring."*  

Mayur, with his calm yet inspiring tone, chimes in,  
*"Focus on using a priority queue – a heap-based structure that ensures the highest priority (or lowest numerical value) alert is processed first. This is a key concept in both DSA and real-world scheduling systems!"*

Iss tarah, tumhari coding journey merge hoti hai real-world monitoring and DSA concepts se, jahan tum priority queues ka use karke critical alerts ko efficiently process karte ho.

---

### **🎯 Challenge: Priority Scheduler for Alerts**  
Write a program that:  
1. **Takes a list of alerts as input.**  
   - Each alert consists of a description (string) and a priority value (integer), where a lower integer indicates a higher priority.
2. **Uses a priority queue (min-heap)** to process alerts based on their urgency.  
3. **Prints the alerts in the order they should be processed** (from highest to lowest priority).

*Note:*  
- If multiple alerts have the same priority, process them in the order they appear.
- You can use built-in data structures/libraries for the priority queue (e.g., `heapq` in Python, `PriorityQueue` in Java, or `std::priority_queue` in C++ with appropriate comparison).

---

### **🔍 Example Input/Output**

#### **Example 1**  
**Input:**  
```
Alert List:
1. "Low battery warning" with priority 3
2. "Overheating detected" with priority 1
3. "Network latency high" with priority 2
```  
**Output:**  
```
Processing Alerts:
1. Overheating detected (Priority: 1)
2. Network latency high (Priority: 2)
3. Low battery warning (Priority: 3)
```

#### **Example 2**  
**Input:**  
```
Alert List:
1. "Sensor malfunction" with priority 2
2. "Routine maintenance reminder" with priority 5
3. "Critical system failure" with priority 1
4. "Software update available" with priority 4
```  
**Output:**  
```
Processing Alerts:
1. Critical system failure (Priority: 1)
2. Sensor malfunction (Priority: 2)
3. Software update available (Priority: 4)
4. Routine maintenance reminder (Priority: 5)
```

#### **Example 3**  
**Input:**  
```
Alert List:
1. "Door open alert" with priority 3
2. "Fire alarm triggered" with priority 1
3. "Temperature sensor reading high" with priority 2
```  
**Output:**  
```
Processing Alerts:
1. Fire alarm triggered (Priority: 1)
2. Temperature sensor reading high (Priority: 2)
3. Door open alert (Priority: 3)
```

---

### **💡 Hints**  
- **Priority Queue Usage:**  
  - In Python, import the `heapq` module and push tuples of the form `(priority, alert_description)` onto the heap.
- **Input Parsing:**  
  - Represent each alert as a tuple or object containing its description and priority.
- **Real-World Connection:**  
  - This mirrors how real-world systems, such as emergency response centers or network monitors, prioritize tasks to handle critical situations first.

---

### **📝 Tumhara Task**  
- Write your solution in **any programming language** (Python, C++, Java, etc.).  
- Save your file as `day51_priority_scheduler.[ext]` (for example, `day51_priority_scheduler.py`).

---

### **🌟 Motivational Quote**  
*"When every second counts, prioritize what matters. Let your code be the guiding force that ensures urgent alerts are never missed!"* 🚀

---

Your priority scheduler not only reinforces a key DSA concept but also simulates a real-world monitoring system. Tumhara code efficiently processes alerts, ensuring that the most critical issues are handled first.  
Ready for **Day 52**? Let's keep advancing through the multiverse!