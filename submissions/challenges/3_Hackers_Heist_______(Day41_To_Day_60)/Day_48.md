## **Day 48: The Sensor Simulator – Concurrent Data Streams** ⏱️🌡️

### **📜 Kahani / Story**  
In the multiverse, remote outposts rely on sensors to monitor critical parameters. Today, you are tasked with simulating two independent sensors that work concurrently in a real-world scenario.  

Echo explains,  
*"Imagine a remote station where one sensor measures temperature and another measures humidity. In the real world, these sensors send data simultaneously. Tumhara challenge hai in data streams ko concurrently simulate karna using multi-threading – just like real systems do!"*

Nariyal Bhai adds,  
*"Simple sensor data can help us understand the importance of real-time monitoring without any complicated interference. Bas, do threads banao aur unme sensor readings print karo."*

Mayur concludes,  
*"Focus on the task at hand – simulate two data streams concurrently. Yeh challenge tumhe multi-threading ka basic idea dega, which is essential for real-world applications."*

Iss tarah, tumhari coding journey real-world simulation se judi hai, jahan multi-threading ka use karke hum sensor data ko ek saath process karte hain.

---

### **🎯 Challenge: Sensor Data Simulator**  
Write a program that:  
1. **Spawns two threads concurrently:**
   - **Thread 1 (Temperature Sensor):** Simulates a temperature sensor by printing temperature readings (e.g., random integers between 20°C to 30°C) every second.
   - **Thread 2 (Humidity Sensor):** Simulates a humidity sensor by printing humidity readings (e.g., random integers between 40% to 60%) every second.
2. **Ensures both threads run concurrently** for a set duration (e.g., 10 seconds) before the program ends.
3. **Prints a final message**:  
   ```
   Sensor simulation complete.
   ```

*Note:*  
- Use multi-threading constructs available in your language (e.g., `threading` module in Python, `Thread` class in Java, or `std::thread` in C++).
- Use delays (e.g., sleep for 1 second) to simulate real-time data generation.

---

### **🔍 Example Outputs**

#### **Example 1**  
```
[Temperature Sensor] Temperature: 24°C
[Humidity Sensor] Humidity: 52%
[Temperature Sensor] Temperature: 27°C
[Humidity Sensor] Humidity: 47%
...
Sensor simulation complete.
```

#### **Example 2**  
```
[Temperature Sensor] Temperature: 22°C
[Humidity Sensor] Humidity: 55%
[Temperature Sensor] Temperature: 25°C
[Humidity Sensor] Humidity: 50%
[Temperature Sensor] Temperature: 28°C
[Humidity Sensor] Humidity: 58%
...
Sensor simulation complete.
```

#### **Example 3**  
```
[Temperature Sensor] Temperature: 30°C
[Humidity Sensor] Humidity: 45%
[Temperature Sensor] Temperature: 29°C
[Humidity Sensor] Humidity: 60%
[Temperature Sensor] Temperature: 26°C
[Humidity Sensor] Humidity: 42%
...
Sensor simulation complete.
```

*Note:* The exact sensor readings will vary each run due to randomness and concurrent thread scheduling.

---

### **💡 Hints**  
- **Threading:**  
  - In Python, consider using the `threading.Thread` class and `time.sleep(1)` for delays.
- **Random Data:**  
  - Use a random number generator (e.g., `random.randint`) to simulate sensor readings.
- **Synchronization:**  
  - Ensure the main thread waits for both sensor threads to finish (using join operations).

---

### **📝 Tumhara Task**  
- Write your solution in **any programming language** (Python, C++, Java, etc.).  
- Save your file as `day48_sensor_simulator.[ext]` (for example, `day48_sensor_simulator.py`).

---

### **🌟 Motivational Quote**  
*"Real-world systems rely on timely data. Simulate, observe, and learn—let every sensor reading guide you to mastery!"* 🚀

---

Your sensor simulator bridges basic multi-threading concepts with real-world data processing. Tumhara code aise data streams ko effortlessly handle karega, just like in modern monitoring systems.  
Ready for **Day 49**? Let's continue our journey!