## **Day 52: The Data Compressor – Optimize Transmission!** 📉💾

### **📜 Kahani / Story**  
The Glitch is flooding the multiverse with huge data packets, causing congestion in the network. In the communications hub, the engineers have devised a plan to reduce the load by compressing the data before transmission.  
   
Echo explains,  
*"Jab hum digital data transmit karte hain, bandwidth ka efficient use bahut zaroori hai. Data compression se hum repeated information ko condense kar sakte hain, jisse transmission fast ho jati hai. Aaj tumhara challenge hai run-length encoding (RLE) use karke data compress karna – bilkul waise hi, jaise real-world systems data loss ko kam karte hain."*  

Nariyal Bhai adds,  
*"Simple samjho, agar koi character bar-bar repeat ho raha ho, toh usko ek count ke saath represent karo. Isse hum network bandwidth bachate hain aur speed badhate hain!"*  

Mayur calmly concludes,  
*"Tumhara code efficient compression ka demonstration hoga, jo real-world applications mein file storage aur transmission efficiency badhata hai. Bas, focus karo aur apne algorithm ko optimize karo!"*

Iss tarah, tumhari coding journey ne DSA concept (run-length encoding) ko real-world data compression se link kar diya hai, ensuring the multiverse’s communication remains swift and efficient.

---

### **🎯 Challenge: Data Compressor Using Run-Length Encoding (RLE)**  
Write a program that:  
1. **Takes a string as input** (representing a data packet with repeated characters).  
2. **Compresses the string using run-length encoding.**  
   - For example, `"AAABBC"` should be encoded as `"3A2B1C"` (or a similar format).  
3. **Prints the compressed string.**

*Note:*  
- The encoding should represent consecutive occurrences of the same character as a count followed by the character.
- Handle both uppercase and lowercase letters, digits, and symbols.

---

### **🔍 Example Input/Output**

#### **Example 1**  
**Input:**  
```
Enter data packet: AAABBBCCDAA
```  
**Output:**  
```
Compressed Data: 3A3B2C1D2A
```

#### **Example 2**  
**Input:**  
```
Enter data packet: WWWWWBWWWW
```  
**Output:**  
```
Compressed Data: 5W1B4W
```

#### **Example 3**  
**Input:**  
```
Enter data packet: 112233
```  
**Output:**  
```
Compressed Data: 211223
```
*(This represents two 1's, two 2's, and two 3's.)*

---

### **💡 Hints**  
- **Iteration:**  
  - Loop through the string and keep a count of consecutive repeating characters.
- **String Manipulation:**  
  - Append the count and the character to the result as you traverse the string.
- **Edge Cases:**  
  - Handle empty strings and ensure the final set of characters is processed.
- **Real-World Connection:**  
  - Think of this as similar to compressing images or files to save space and improve transmission speed in networking.

---

### **📝 Tumhara Task**  
- Write your solution in **any programming language** (Python, C++, Java, etc.).  
- Save your file as `day52_data_compressor.[ext]` (e.g., `day52_data_compressor.py`).

---

### **🌟 Motivational Quote**  
*"Efficient communication requires smart compression. Let your code be the key that transforms bulky data into concise, powerful messages!"* 🚀

---

Your data compressor is now ready to optimize the multiverse’s data flow, linking DSA techniques with practical, real-world applications in network communication.  
Ready for **Day 53**? Let's continue our journey!