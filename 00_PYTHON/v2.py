# user_input = "Hello, how can I assist you today?"
# question = "What is the weather like today?"
emails = ["Hello, I am facing the login issue",
          "I would like to know about my billing details",
          "Can you help me with my account settings?"]



# prompt = """
# You are a helpful assistant. Classify the email into one of the category
# - Billing
# - Technical Support
# - General Inquiry
# and here is the email 
# email : {email}
# """
# for email in emails:
#     prompt = f"""
#     You are a helpful assistant. Classify the email into one of the category
#     - Billing
#     - Technical Support
#     - General Inquiry
#     and here is the email 
#     email : {email}
#     """
#     print(prompt)
    
# print(user_input)
# print(question)

# print(prompt)

# print(prompt.format(user_input=user_input, question=question))

# list tuple ( reason when to what )

# prompt = "I am not happy"
# prompt[0] = "###"
# print(prompt[3])
# print(prompt[:5]) # access 


# set and dict

blog = """Most people's experience with LLMs and documents looks like RAG: 
you upload a collection of files, the LLM retrieves relevant chunks at query time, 
and generates an answer. This works, but the LLM is rediscovering knowledge from scratch 
on every question. There's no accumulation. Ask a subtle question that requires synthesizing 
five documents, and the LLM has to find and piece together the relevant fragments every time. 
Nothing is built up. NotebookLM, ChatGPT file uploads, and most RAG systems work this way."""

# words = blog.split(' ')
# word_set = set(words)
# print(len(words))
# print(len(word_set))

# a = [2,2,2,2,2,2]
# set_a = set(a)
# # print(len(a))
# print(len(set_a))



# print(len(blog.split(' '))) # list

# print(len((2,3,2,56,2)))

# output
# ['Most', "people's", 'experience', 'with', 'LLMs', 'and', 'documents', 
#  'looks', 'like', 'RAG:', '\nyou', 'upload', 'a', 'collection', 'of', 'files,', 'the', 
#  'LLM', 'retrieves', 'relevant', 'chunks', 'at', 'query', 'time,', '\nand', 'generates', 
#  'an', 'answer.', 'This', 'works,', 'but', 'the', 'LLM', 'is', 'rediscovering', 
#  'knowledge', 'from', 'scratch', '\non', 'every', 'question.', 
#  "There's", 'no', 'accumulation.', 'Ask', 'a', 'subtle', 'question', 'that', 
#  'requires', 'synthesizing', '\nfive', 'documents,', 'and', 'the', 'LLM', 'has', 'to', 
#  'find', 'and', 'piece', 'together', 'the', 'relevant', 'fragments', 'every', 'time.', '\nNothing', 
#  'is', 'built', 'up.', 'NotebookLM,', 
#  'ChatGPT', 'file', 'uploads,', 'and', 'most', 'RAG', 'systems', 'work', 'this', 'way.']


# city_a = {"test","v1","v2"}
# print(city_a[0])


# two table -->
col1 = set([1, 2, 3])
col2 = set([4, 5, 3])


# col1= [1, 2, 3]
# col2= [4, 5, 3]

# col1.extend(col2)
# print(len(col1))

# print(col1.intersection(col2))  # Output: {3}
# print(col1.difference(col2))    # Output: {1, 2}
# print(len(col1.union(col2)))         # Output: {1, 2, 3, 4, 5}

# print(3423 in col1)

set_a = {34,45,56,34,21}
set_b = {34,45,-1}

# https://docs.python.org/2/library/sets.html

#print(set_b.issubset(set_a))  # Output: True

# 
data = {"item1":"Tshirt",
        "item2":"Jeans",
        "item3":"Jacket",
        "item4":["Shirt","Trousers","Shorts"],
        "item5":{
            "color":"blue",
            "size":"M",
            "brand":"Nike",
            "price": 29.99,
            "stock": 100,
            "description": "A stylish blue Nike t-shirt."

        },
        2 : {
            "color":"red",
            "size":"L",
            "brand":"Adidas",
            "price": 34.99,
            "stock": 50,
            "description": "A trendy red Adidas t-shirt."
        },
        "rahul" : [1, 2, 3]
}
print(data[2]["description"])
# https://docs.python.org/3/c-api/dict.html