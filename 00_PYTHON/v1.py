
# https://docs.python.org/3/library/re.html. : One of the imp topic
emails = [
    "Hi Team I am facing an issue with the new feature implementation. Can someone assist me with this? and my email is example@example.com",
    "Hello, I wanted to follow up on the previous email regarding the project timeline.",
    "Dear Team, I have completed the initial testing phase. Please find the results attached.",
    "Congratulations! You won a gift voucher!",
    "Click here to claim your prize.",
]
x
def llm(prompt):
    return " working"

keywords = ['Congratulations!', 'voucher', 'prize', 'click here', 'offer', 'limited time', 'discount', 'free', 'win', 'urgent']


def check_email(email):
    SPAM_FLAG = False
    words = email.lower().split(' ')
    print(words)
    for keyword in keywords:
        if keyword.lower() in words:
            print(f"Found keyword '{keyword}' in email: {email}")
            SPAM_FLAG = True
            break
    return SPAM_FLAG


for i in emails:
    flag = check_email(i)
    if flag:
        print(f"Spam email detected: {i}")
    classification = llm(i)
    print(f"Email: {i}\nClassification: {classification}\n")

    #     for keyword in keywords:
    #         if keyword.lower() in words:
    #             print(f"Found keyword '{keyword}' in email: {email}")
    #             SPAM_FLAG = True
    #             break
    #     return SPAM_FLAG

# print(check_email("Congratulations! You won a gift voucher!"))

# print('Congratulations!'.lower())






# email = emails[2]
# print(email.split(' '))
# print('Click'.lower() in email.split(' '))
# click in ['click', 'here', 'to', 'claim', 'your', 'prize.'] ==> False/True