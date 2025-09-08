#Amanda Eng Book Recomendation System code. 7/9/2025.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#dtype making sure that datatypes correct
dtype_specs = {
    "Year-Of-Publication" : int,
    "Book-Rating" : int,
    "User-ID" : str,
    "Age" : str,
    "ISBN" : str,
    "Book-Title": str,
    "Book-Author": str,
    "Publisher": str,
    "Image-URL-S": str,
    "Image-URL-M": str,
    "Image-URL-L": str,
    "Location" : str,
    "Age": str
}




#Read the information from the books dataset
books = pd.read_csv('C:/Users/onetw/Projects/reccSystem/reccSystem/bookDataset/books_data/books.csv',sep=';', on_bad_lines='skip', encoding="latin-1")
books = pd.read_csv('C:/Users/onetw/Projects/reccSystem/reccSystem/bookDataset/books_data/books.csv', sep=';', on_bad_lines='skip', encoding="latin-1")
books.columns = ['ISBN','Book-Title','Book-Author','Year-Of-Publication','Publisher','Image-URL-S','Image-URL-M','Image-URL-L']

#Read users dataset
users = pd.read_csv('C:/Users/onetw/Projects/reccSystem/reccSystem/bookDataset/books_data/users.csv', sep=';', on_bad_lines='skip', encoding="latin-1")
users.columns = ['User-ID','Location','Age']

#Read the Ratings dataset
ratings = pd.read_csv('C:/Users/onetw/Projects/reccSystem/reccSystem/bookDataset/books_data/ratings.csv', sep=';', on_bad_lines='skip', encoding="latin-1")
ratings.columns = ['User-ID','ISBN','Book-Rating']

#verifuying the datasets are read
print(books.shape)
print(list(books.columns))

print(ratings.shape)
print(list(ratings.columns))


#generate histogram of user ages (0-100)

users.Age.hist(bins=range(0,100))
plt.title('User Age Group')
plt.xlabel('Age')
plt.ylabel('Number of Users')

plt.show()

#Combined ratings of all books on pie chart (using [] becvause python doesn't accept '-' as a colunm name)

ratings['Book-Rating'].value_counts().plot(kind='pie')
plt.title('Combined Rating of All Books')
plt.xlabel('Rating')

plt.show()


#recomended books by rating to users based on book's ISBN and sort in best to worst order

recommender_byRating = pd.DataFrame(ratings.groupby('ISBN')['Book-Rating'].count())
top_books = recommender_byRating.sort_values('Book-Rating', ascending=False).head()

print(top_books)

#merge books and ratings datasets
overall_rating = pd.merge(ratings, books, on='ISBN')

#Find most popular book in the data by rating and show the title
book_rated = (overall_rating.
              groupby(by = ['Book-Title'])['Book-Rating'].
              count().reset_index())

book_ratingCount= (book_rated.head())
print(book_ratingCount)



#Demographic based recommendation of users living in spain and austrilia 

#Merge books, users, and rating datasets
overall_ratingCount = overall_rating.merge(book_ratingCount, left_on = 'Book-Title', right_on = 'Book-Title', how = 'left')
bookUser = overall_ratingCount.merge(users, left_on = 'User-ID', right_on = 'User-ID', how = 'left')

#filter by locations
demographic = bookUser[bookUser['Location'].str.contains("australia|spain")]
print(demographic.head())