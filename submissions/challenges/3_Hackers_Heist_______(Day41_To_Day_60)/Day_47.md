## **Day 47: The Interference Eliminator – Noise Reduction Challenge** 📡🔇

### **📜 Kahani / Story**  
In the heart of the multiverse’s communications hub, The Glitch is causing havoc by injecting unwanted noise into the transmitted signals. Tum ab ek high-tech lab mein ho jahan ECE engineers real-time signal filtering karte hain to eliminate interference.  
  
Echo explains,  
*"Jab signal mein interference hota hai, toh accurate data transmission mushkil ho jati hai. Tumhara challenge hai ek moving average filter implement karna – ek basic yet powerful technique to smooth out noise from digital signals. Isse tum dekh sakte ho ki kaise real-world systems unwanted disturbances ko filter karte hain."*  

Nariyal Bhai kehta hai,  
*"Yeh bilkul waise hi hai jaise hum signal processing labs mein noisy measurements ko clean karte hain. Tumhara code bhi is noise ko hata ke signal ko clear karega."*  

Mayur adds,  
*"Tumhara solution not only improves the signal quality but also simulates how advanced communication systems maintain clarity despite interference. Let’s eliminate that noise and let the true signal shine through!"*

Iss tarah, tumhari coding journey directly link hoti hai real-world ECE applications, jahan noise reduction is crucial for reliable communication.

---

### **🎯 Challenge: Moving Average Filter (Noise Reduction)**  
Write a program that:  
1. **Takes a list of integers as input** (each representing signal amplitude over time with noise).  
2. **Takes an integer \( W \) as input**, which is the window size for the moving average filter.  
3. **Calculates the moving average** for the signal using the given window size.  
4. **Prints the smoothed signal** as a list of averaged values.

*Note:*  
- For a window size \( W \), the moving average for a position is the average of \( W \) consecutive elements.  
- If there are fewer than \( W \) elements remaining at the end, you may handle it by computing the average for the remaining elements or stop processing.

---

### **🔍 Example Input/Output**

#### **Example 1**  
**Input:**  
```
Enter signal (space-separated): 10 20 30 40 50 60
Enter window size (W): 3
```  
**Calculation:**  
- Moving averages:  
  - (10+20+30)/3 = 20  
  - (20+30+40)/3 = 30  
  - (30+40+50)/3 = 40  
  - (40+50+60)/3 = 50  
**Output:**  
```
Smoothed Signal: 20 30 40 50
```

#### **Example 2**  
**Input:**  
```
Enter signal (space-separated): 5 15 25 35 45
Enter window size (W): 2
```  
**Calculation:**  
- Moving averages:  
  - (5+15)/2 = 10  
  - (15+25)/2 = 20  
  - (25+35)/2 = 30  
  - (35+45)/2 = 40  
**Output:**  
```
Smoothed Signal: 10 20 30 40
```

#### **Example 3**  
**Input:**  
```
Enter signal (space-separated): 100 80 60 40 20
Enter window size (W): 4
```  
**Calculation:**  
- Moving average:  
  - (100+80+60+40)/4 = 70  
  - (80+60+40+20)/4 = 50  
**Output:**  
```
Smoothed Signal: 70 50
```

---

### **💡 Hints**  
- **Sliding Window Technique:**  
  - Use a loop to iterate over the signal list and compute the average for each window of size \( W \).  
- **Edge Handling:**  
  - Decide whether to process the last window if it has fewer than \( W \) elements or stop before it.  
- **Real-World Connection:**  
  - Yeh process bilkul waise hi hai jaise signal processors real-time measurements ko smooth karte hain to eliminate noise and ensure clear communication.

---

### **📝 Tumhara Task**  
- Write your solution in **any programming language** (Python, C++, Java, etc.).  
- Save your file as `day47_interference_eliminator.[ext]` (e.g., `day47_interference_eliminator.py`).

---

### **🌟 Motivational Quote**  
*"Clear signals are the foundation of reliable communication. Apne code ke through noise ko hatao, aur asli data ko shine karne do!"* 🚀

---

Your moving average filter is the shield that protects digital signals from interference – just like real-world ECE systems maintain clarity amid chaos.  
Ready for the next challenge on **Day 48**? Let's continue our journey through the multiverse!