## **Day 50: The Multiverse Monitor – System Health Checker** 🖥️🔍

### **📜 Kahani / Story**  
In the vast multiverse, every system's health must be vigilantly monitored to ensure smooth operation and avoid catastrophic failures. Today, you are in the central control room where a powerful dashboard—**The Multiverse Monitor**—displays real-time performance data from all critical subsystems.  
 
Echo explains,  
*"Yaar, har sensor se data aa raha hai, aur hum sab ko integrate karke system ki overall health check karna hai. Tumhara challenge hai ki tum collected sensor readings ka statistical analysis karo to determine the system's stability. Yeh bilkul waise hai jaise ECE labs mein signal processing ke through system performance evaluate karte hain, aur real-world industries mein quality control monitor hota hai."*

Nariyal Bhai adds,  
*"Dekho, jab multiple sensors se data milta hai, tab uska proper analysis karna bohot zaroori hai. Average, variance, aur standard deviation se pata chalta hai ki system kitna stable hai. Tumhara code is raw data ko ek integrated dashboard mein convert karega."*

Mayur, in his calm yet inspiring tone, chimes in,  
*"This challenge is the culmination of all your skills so far—data logging, filtering, and analysis. Tumhara solution batayega ki system health kaise maintain hoti hai, ensuring that every part of the multiverse runs seamlessly."*

Iss tarah, tumhari coding journey real-world data analytics aur ECE applications se judi hai, jahan raw numbers ko transform karke system performance monitor ki jati hai.

---

### **🎯 Challenge: System Health Checker**  
Write a program that:  
1. **Takes a series of sensor readings as input** (space-separated numbers representing system parameters, e.g., temperature, pressure, etc.).  
2. **Calculates and prints the following:**
   - **Average (mean) value**
   - **Variance**
   - **Standard Deviation**

*Note:*  
- Variance is the average of the squared differences from the mean.  
- Standard deviation is the square root of the variance.  
- This calculation simulates how real-world systems evaluate the consistency of their sensor data to ensure stability.

---

### **🔍 Example Inputs/Outputs**

#### **Example 1**  
**Input:**  
```
Enter sensor readings: 24 27 22 25 26
```  
**Calculation:**  
- Average = (24 + 27 + 22 + 25 + 26) / 5 = 24.8  
- Variance = [ (24-24.8)² + (27-24.8)² + (22-24.8)² + (25-24.8)² + (26-24.8)² ] / 5  
  ≈ (0.64 + 4.84 + 7.84 + 0.04 + 1.44) / 5 = 14.8 / 5 = 2.96  
- Standard Deviation ≈ √2.96 ≈ 1.72  
**Output:**  
```
Average: 24.8
Variance: 2.96
Standard Deviation: 1.72
```

#### **Example 2**  
**Input:**  
```
Enter sensor readings: 18.5 20.3 19.8 21.0 20.0
```  
**Calculation:**  
- Average ≈ 19.92  
- (Calculate variance and standard deviation accordingly)  
**Output:**  
```
Average: 19.92
Variance: [Calculated Value]
Standard Deviation: [Calculated Value]
```

#### **Example 3**  
**Input:**  
```
Enter sensor readings: 30 28 32 31 29 33
```  
**Calculation:**  
- Average = (30 + 28 + 32 + 31 + 29 + 33) / 6 = 30.5  
- (Calculate variance and standard deviation accordingly)  
**Output:**  
```
Average: 30.5
Variance: [Calculated Value]
Standard Deviation: [Calculated Value]
```

*Note:* For examples 2 and 3, you may perform similar calculations as in Example 1. Use appropriate rounding as needed.

---

### **💡 Hints**  
- **Calculating the Mean:**  
  - Sum all sensor readings and divide by the count.
- **Variance:**  
  - For each reading, compute the squared difference from the mean, sum these values, and divide by the count.
- **Standard Deviation:**  
  - Take the square root of the variance.
- **Real-World Connection:**  
  - This process is similar to how industrial systems monitor equipment performance to detect deviations and maintain quality control.

---

### **📝 Tumhara Task**  
- Write your solution in **any programming language** (Python, C++, Java, etc.).  
- Save your file as `day50_system_health_checker.[ext]` (e.g., `day50_system_health_checker.py`).

---

### **🌟 Motivational Quote**  
*"When you turn raw data into meaningful insights, you hold the key to reliability. Code with precision, and let every number guide you to perfection!"* 🚀

---

Your Multiverse Monitor is now complete—melding your coding acumen with real-world data analytics. Tumhara solution ensures that every system parameter is in check, keeping the multiverse safe from The Glitch.  
Ready to continue the journey? Let's move on to the next challenge!