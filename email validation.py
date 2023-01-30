#You are given an integer  followed by  email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.

#email validation
#Valid email addresses must follow these rules:It must have the username@websitename.extension format type.The username can only contain letters, digits, dashes and underscores .The website name can only have letters and digits .The extension can only contain letters .The maximum length of the extension is .

def fun(s):
    if "@" in s and "." in s:
        pass
    else:
        return False
    a=0
    for i in range(0,s.index("@")):
        if ord(s[i])>64 and ord(s[i])<91:
            pass
        elif ord(s[i])>96 and ord(s[i])<123:
            pass
        elif ord(s[i])>47 and ord(s[i])<58:
            pass
        elif ord(s[i])==45 or ord(s[i])==95:
            pass
        else:
            return False
    if len(s)-1-s.index(".")==3:
        pass
    else:
        return False
    for q in range(s.index("@")+1,s.index(".")):
        if ord(s[q])>64 and ord(s[q])<91:
            pass
        elif ord(s[q])>96 and ord(s[q])<123:
            pass
        elif ord(s[q])>47 and ord(s[q])<58:
            pass
        else:
            return False
    return True
        
           
        
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
