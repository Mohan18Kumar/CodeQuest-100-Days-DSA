## **Day 42: The Spam Filter – Real-World Email Sorting System** 📧🔍

### **📜 Kahani / Story**  
Ab tum Hacker’s Hideout se nikal kar ek real-world scenario mein aa gaye ho – ek busy IT department jahan college ke interns bhi kaam kar rahe hain.  
Echo kehta hai,  
*"Office ke inbox mein spam emails ki bauchhaar ho rahi hai. Tumhara kaam hai un spam messages ko filter out karke, genuine emails ko alag dikhana. Yeh bilkul waise hi hai jaise apne assignments mein relevant information ko choose karna!"*  

Nariyal Bhai thoda samjhaata hai,  
*"Yaar, real world mein emails filter karna bahut important hai – bina spam ke productivity badh jaati hai!"*

---

### **🎯 Challenge: Spam Filter Implementation**  
Write a program that:  
1. **Takes a list of email subjects (or messages) as input.**  
2. **Takes a list of spam keywords as input.**  
3. **Filters out emails containing any of the spam keywords** (case-insensitive match).  
4. **Prints the clean (non-spam) emails.**

*Example Scenario:*  
- Input email subjects might include phrases like "Win a free iPhone now!" or "Meeting update for project X."  
- Spam keywords could be: "win", "free", "prize", etc.

---

### **🔍 Example Input/Output**

#### **Example 1**  
**Input:**  
```
Enter email subjects (comma-separated): "Win a free iPhone", "Project meeting at 3 PM", "Congratulations, you've won a prize", "Team outing tomorrow"
Enter spam keywords (comma-separated): free, win, prize
```  
**Output:**  
```
Filtered Emails:
- Project meeting at 3 PM
- Team outing tomorrow
```

#### **Example 2**  
**Input:**  
```
Enter email subjects (comma-separated): "Discounts on laptops", "Urgent: account update", "Free gift with purchase", "Office party invitation"
Enter spam keywords (comma-separated): free, discount, gift
```  
**Output:**  
```
Filtered Emails:
- Urgent: account update
- Office party invitation
```

---

### **💡 Hints**  
- **String Manipulation:** Convert both the email subject and spam keywords to lowercase for case-insensitive matching.  
- **Filtering:** Loop through each email subject and check if any spam keyword is a substring.  
- **Data Structures:** Use arrays or lists to store email subjects and keywords.

---

### **📝 Tumhara Task**  
- Write your solution in **any programming language** (Python, C++, Java, etc.).  
- Save your file as `day42_spam_filter.[ext]` (e.g., `day42_spam_filter.py`).

---

### **🌟 Motivational Quote**  
*"Real-world problems demand real-world solutions. Filter out the noise, focus on what matters, and let your code shine!"* 🚀

---

The IT department's inbox is now under control thanks to your spam filter. Tumhari coding skills ne real-world application ka mazaa dikhaya hai!  
Ready for **Day 43**? Let’s continue our adventure!