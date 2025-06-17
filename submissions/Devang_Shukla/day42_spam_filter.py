def filter_spam_emails(emails, spam_keywords):
    filtered_emails = []
    spam_keywords = [word.lower().strip() for word in spam_keywords]

    for email in emails:
        email_lower = email.lower()
        if not any(spam_word in email_lower for spam_word in spam_keywords):
            filtered_emails.append(email.strip())
    
    return filtered_emails

emails_input = input("Enter email subjects (comma-separated): ")
spam_input = input("Enter spam keywords (comma-separated): ")
emails = emails_input.split(",")
spam_keywords = spam_input.split(",")
clean_emails = filter_spam_emails(emails, spam_keywords)
print("\nFiltered Emails:")
for email in clean_emails:
    print(f"- {email}")