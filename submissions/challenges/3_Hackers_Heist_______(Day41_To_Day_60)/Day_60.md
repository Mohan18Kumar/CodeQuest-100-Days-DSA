## **Day 60: The Firewall Protector – Trie-Based URL Blocker** 🔥🔐

### **📜 Kahani / Story**  
In the depths of Hacker’s Hideout, The Glitch is trying to infiltrate the system by sending malicious URLs into the network. To counter this threat, the Debuggers have set up a digital firewall that blocks harmful web addresses.  
   
Echo explains,  
*"Jab network ko secure rakhna ho, tab fast lookup ki zaroorat padti hai. Isliye hum Trie (prefix tree) ka use karte hain to quickly detect malicious URLs. Tumhara challenge hai ek Trie implement karna jismein ek list of banned URLs store ho, aur phir input URL check karo – agar match milta hai, toh usse block karo."*  

Nariyal Bhai adds,  
*"Bilkul, jaise real-world firewalls known malicious addresses ko filter karte hain, tumhara code bhi same karega. Yeh ek efficient way hai to check for harmful patterns in data."*  

Mayur concludes,  
*"Is challenge se tum DSA ke Trie data structure ko samjhoge aur real-world network security ke application ka bhi practical experience paoge. Let your code be the shield that protects the multiverse from cyber threats!"*

Iss tarah, tumhari coding journey advanced DSA techniques ko real-world cybersecurity applications se seamlessly connect karti hai.

---

### **🎯 Challenge: Trie-Based URL Blocker**  
Write a program that:  
1. **Stores a list of malicious URLs (or URL prefixes)** using a Trie.  
2. **Takes a URL as input** and checks whether it starts with any of the stored malicious prefixes.  
3. **Prints a message:**  
   - If a malicious prefix is found, print `"Blocked: Malicious URL detected."`  
   - Otherwise, print `"Safe: URL is clean."`

*Note:*  
- The Trie should efficiently support insertion and prefix search.  
- Assume all URLs are in lowercase for consistency.

---

### **🔍 Example Input/Output**

#### **Example 1**  
**Malicious URL List (stored in the Trie):**  
```
["badsite.com", "malware", "phishing"]
```  
**Input:**  
```
Enter URL: badsite.com/login
```  
**Output:**  
```
Blocked: Malicious URL detected.
```

#### **Example 2**  
**Malicious URL List:**  
```
["badsite.com", "malware", "phishing"]
```  
**Input:**  
```
Enter URL: securebank.com
```  
**Output:**  
```
Safe: URL is clean.
```

#### **Example 3**  
**Malicious URL List:**  
```
["badsite.com", "malware", "phishing"]
```  
**Input:**  
```
Enter URL: phishingattack.net
```  
**Output:**  
```
Blocked: Malicious URL detected.
```

---

### **💡 Hints**  
- **Trie Structure:**  
  - Create a Trie node class/structure with attributes for children and an end-of-word flag.
- **Insertion:**  
  - Insert each malicious URL or prefix into the Trie.
- **Prefix Search:**  
  - For a given input URL, traverse the Trie to check if any stored prefix matches the beginning of the URL.
- **Real-World Connection:**  
  - This technique is used in many security systems to quickly block known malicious patterns, ensuring efficient and fast URL filtering.

---

### **📝 Tumhara Task**  
- Write your solution in **any programming language** (Python, C++, Java, etc.).  
- Save your file as `day60_firewall_protector.[ext]` (for example, `day60_firewall_protector.py`).

---

### **🌟 Motivational Quote**  
*"Secure your network, secure your future. Build your firewall with precision, and let every line of code fortify the digital realm!"* 🚀

---

Your Firewall Protector challenge perfectly merges advanced DSA (Trie) concepts with real-world cybersecurity applications. Tumhara solution will act as a digital shield, blocking malicious URLs and protecting the multiverse from The Glitch's attacks.  
Ready for **Day 61**? Let's move forward and keep the defenses strong!