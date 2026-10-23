from business_logic import (
    classify_with_cot,
    classify_with_self_consistency,
    draft_response_with_tot
)


def is_enterprise_customer(sender):
    enterprise_domains = ["bigclient.com", "enterprise.com", "corp.com"]
    domain = sender.split('@')[-1]
    if domain in enterprise_domains:
        return True
    return False



def process_email(email):
    # step 1    : classify the email using COT
    initial = classify_with_cot(email['subject'], email['body'], email['sender'])

    # step 2 : check for high stakes customer
    is_high_stakes = is_enterprise_customer(email['sender'])

    # step 3 : if high stakes, use self consistency to classify
    if is_high_stakes:
        final = classify_with_self_consistency(email['subject'], email['body'], email['sender'])
    else:
        final = initial

    # step 4 : routing
    routing = {
        "Billing"        : "billing-team@company.com",
        "Technical"      : "tech-support@company.com",
        "Feature Request": "product@company.com",
        "Spam"           : None,
    }

    routed_to = routing.get(final['category'], 'support@company.com')

    # step Tot for churn risk : in production application ==> churn risk will be calculated using Machine learning model
    is_churn = ("cancel" in email['body'].lower()
                or "not satisfied"  in email['body'].lower())
    

    drafted_response = None
    if is_churn:
        drafted_response = draft_response_with_tot(email['subject'], email['body'], final['category'])


    return {
        "email_id": email.get("sender"),
        "classification": final['category'],
        "routed_to": routed_to,
        "drafted_response": drafted_response,
    }


# print(is_enterprise_customer(email['sender']))

# here email is a dict
emails = [{
    "subject": "Login issue",
    "body": "I'm unable to log into my account. I paid but not sure payment done or not.",
    "sender": "user@enterprise.com"
},
{
    "subject": "Feature request",
    "body": "I'd like to request a new feature for the product.",
    "sender": "user@bigclient.com"
},
{
    "subject": "Account cancellation",
    "body": "I want to cancel my account.",
    "sender": "user@enterprise.com"
}
]


for email in emails:
    print(process_email(email))
