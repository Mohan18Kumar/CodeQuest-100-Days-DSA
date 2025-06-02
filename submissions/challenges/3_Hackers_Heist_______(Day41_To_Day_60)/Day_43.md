## **Day 43: The Signal Decoder – Parity Check for Reliable Communication** 📡💻

### **📜 Kahani / Story**  
Tum ab college ke Electronics lab mein ho, jahan real-world communication systems ka demonstration chal raha hai. Aaj tumhein ek aisa challenge diya gaya hai jo directly ECE ke concepts se linked hai.  
 
Echo softly explains,  
*"Yaar, jab hum digital signals transmit karte hain, toh interference ya noise se errors ho sakte hain. Isiliye, hum parity check ka use karte hain – ek simple method to ensure data integrity. Tumhara challenge hai ek binary signal ka parity check karna. Yeh concept na sirf coding ke liye, balki electronics mein bhi bahut important hai."*  

Nariyal Bhai adds,  
*"Jaise hum circuit labs mein measurements karte hain aur signals ko verify karte hain, waise hi tumhe yahan har bit ko count karna hai. Agar total 1's even hain, signal sahi hai; agar odd hain, toh error detected!"*  

Mayur, thoda dramatic tone mein, kehta hai,  
*"Socho, yeh parity check ek chhoti si inspection jaisa hai – jaise hum ek phone call ya data transmission mein guarantee karte hain ki sab kuch sahi ja raha hai. Tumhara kaam hai verify karna ki tumhara signal error-free hai."*  

Is tarah, tum gradually apne coding skills ko real-world ECE application se link karte hue, ek reliable communication system ka simulation karoge.

---

### **🎯 Challenge: Even Parity Checker**  
Write a program that:  
1. **Takes a binary string as input** (representing a digital signal).  
2. **Counts the number of 1’s** in the signal.  
3. **Checks if the count is even or odd.**  
4. **Prints "Even Parity"** if the number of 1’s is even; otherwise, **prints "Odd Parity – Error Detected!"**.

*Note:* Even parity is used in communication systems to detect errors in transmitted data.

---

### **🔍 Example Input/Output**

#### **Example 1**  
**Input:**  
```
Enter binary signal: 1101001
```  
**Output:**  
```
Even Parity
```  
*(Explanation: 1’s count is 4, which is even.)*

#### **Example 2**  
**Input:**  
```
Enter binary signal: 1011010
```  
**Output:**  
```
Even Parity
```  
*(Explanation: 1’s count is 4, which is even.)*

#### **Example 3**  
**Input:**  
```
Enter binary signal: 1110001
```  
**Output:**  
```
Odd Parity – Error Detected!
```  
*(Explanation: 1’s count is 5, which is odd.)*

---

### **💡 Hints**  
- **Counting Bits:** Convert the input into a string and iterate over each character to count '1's.  
- **Parity Check:** Use the modulo operator (`%`) to determine if the count is even.  
- **Real-World Connection:** Yeh process bilkul waise hi hai jaise digital systems mein parity bits ka use hota hai for error detection.

---

### **📝 Tumhara Task**  
- Write your solution in **any programming language** (Python, C++, Java, etc.).  
- Save your file as `day43_parity_check.[ext]` (e.g., `day43_parity_check.py`).

---

### **🌟 Motivational Quote**  
*"Precision in communication is key – chahe woh data transmission ho ya tumhara code. Har bit ka hisaab rakho, aur apni duniya sudharo!"* 🚀

---

Your signal has been thoroughly checked for errors, bridging the gap between coding and real-world ECE applications. Tumhari coding journey ab aur bhi practical ho gayi hai.  
Ready for the next challenge on **Day 44**? Let's move forward!