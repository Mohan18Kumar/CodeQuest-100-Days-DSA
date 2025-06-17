## **Day 45: The Packet Protector – Checksum Calculator** 📦🔍

### **📜 Kahani / Story**  
In the communications hub of the multiverse, data packets are constantly being transmitted to restore order against The Glitch’s corruption. Tum ab ek high-tech data center mein ho, jahan real-world data integrity ka challenge hai.  
   
Echo explains,  
*"Jab hum digital packets bhejte hain, toh data corruption se bachne ke liye hum checksum calculate karte hain. Yeh ek simple yet effective method hai to verify that the packet hasn’t been tampered with. Tumhara task hai ek packet ka checksum calculate karna – exactly how real-world systems ensure data integrity."*  

Nariyal Bhai adds,  
*"Bilkul waise hi jaise hum circuits ko test karte hain, tumhe packet ke characters ka ASCII sum lena hai, and then use modulo operation se ek checksum generate karna hai."*  

Iss tarah, tumhari coding journey direct link karti hai with real-world ECE applications – ensuring that every bit of data is verified before it moves forward.

---

### **🎯 Challenge: Checksum Calculator**  
Write a program that:  
1. **Takes a string as input** (representing a data packet).  
2. **Calculates the checksum** by summing the ASCII values of all characters in the string and taking the result modulo 256.  
3. **Prints the checksum value**.

*Note:*  
- The modulo operation ensures the checksum fits within a single byte (0–255), a common practice in real-world communications.

---

### **🔍 Example Input/Output**

#### **Example 1**  
**Input:**  
```
Enter packet data: Hello
```  
**Calculation:**  
- ASCII sum = 72 (H) + 101 (e) + 108 (l) + 108 (l) + 111 (o) = 500  
- Checksum = 500 % 256 = 244  
**Output:**  
```
Checksum: 244
```

#### **Example 2**  
**Input:**  
```
Enter packet data: Data123
```  
**Calculation:**  
- ASCII sum = 68 + 97 + 116 + 97 + 49 + 50 + 51 = 528  
- Checksum = 528 % 256 = 16  
**Output:**  
```
Checksum: 16
```

#### **Example 3**  
**Input:**  
```
Enter packet data: Secure
```  
**Calculation:**  
- ASCII sum = 83 + 101 + 99 + 117 + 114 + 101 = 615  
- Checksum = 615 % 256 = 103  
**Output:**  
```
Checksum: 103
```

---

### **💡 Hints**  
- **ASCII Conversion:** Use functions like `ord()` in Python (or equivalent in other languages) to convert each character to its ASCII value.  
- **Summing and Modulo:** Sum the ASCII values and then compute the modulo 256 to get the final checksum.  
- **Real-World Connection:** This method is similar to how many protocols ensure data integrity during transmission.

---

### **📝 Tumhara Task**  
- Write your solution in **any programming language** (Python, C++, Java, etc.).  
- Save your file as `day45_packet_protector.[ext]` (e.g., `day45_packet_protector.py`).

---

### **🌟 Motivational Quote**  
*"In the realm of data, every bit counts. Let your code be the guardian that ensures integrity and trust!"* 🚀

---

Your checksum calculator is now the shield that protects data packets from The Glitch’s corruption, blending practical ECE concepts with your coding prowess.  
Ready for the next challenge on **Day 46**? Let’s continue our journey into the multiverse!