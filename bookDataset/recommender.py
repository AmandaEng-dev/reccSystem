#Amanda Eng Book Recomendation System code. 7/9/2025.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read the information from the books dataset
books = pd.read_csv('C:/Users/onetw/Projects/reccSystem/reccSystem/bookDataset/books_data/books.csv',sep=';', dtype=str, on_bad_lines='skip', encoding="latin-1")
books = pd.read_csv('C:/Users/onetw/Projects/reccSystem/reccSystem/bookDataset/books_data/books.csv', sep=';',dtype=str, on_bad_lines='skip', encoding="latin-1")
books.columns = ['ISBN','Book-Title','Book-Author','Year-Of-Publication','Publisher','Image-URL-S','Image-URL-M','Image-URL-L']

# #Read users dataset
users = pd.read_csv('C:/Users/onetw/Projects/reccSystem/reccSystem/bookDataset/books_data/users.csv', sep=';',dtype=str, on_bad_lines='skip', encoding="latin-1")
users.columns = ['User-ID','Location','Age']

# #Read the Ratings dataset
ratings = pd.read_csv('C:/Users/onetw/Projects/reccSystem/reccSystem/bookDataset/books_data/ratings.csv', sep=';',dtype=str, on_bad_lines='skip', encoding="latin-1")
ratings.columns = ['User-ID','ISBN','Book-Rating']


