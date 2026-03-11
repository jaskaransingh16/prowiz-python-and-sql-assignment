import numpy as np
import pandas as pd
import requests

url="https://jsonplaceholder.typicode.com/posts"

response=requests.get(url)
data=response.json()

## Print all the Posts :

for i in data:
    print(i)

## convert to dataframe:

df=pd.DataFrame(data)
# print(df.head())

## Count Distinct Users 
distinct_user=df['userId'].nunique()
print("Distinct Users are :",distinct_user)

## User with Highest Post 
Highest_post=df['userId'].value_counts().idxmax()
print("User with highest number of posts:", Highest_post)


##average word length of tittle
def average_word_length(df):
    total_length = 0
    total_words = 0

    for title in df['title']:
        words = title.split()

        for word in words:
            total_length += len(word)
            total_words += 1

    return total_length / total_words


avg_length = average_word_length(df)
print("Average word length:", avg_length)
