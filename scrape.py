import requests  # Import the requests library for making HTTP requests
from bs4 import BeautifulSoup  # Import BeautifulSoup for parsing HTML
import re  # Import regular expressions to help extract the rating

# Define headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
list1=[]
# Initialize a list to store movie links
movie_links = []
x = input('enter the imdb you want to be higher : ')
y = input('enter numbet of pages that you want to explore : ')
# Loop through the first three pages
for page in range(1, int(y)+1):  # Pages 1 to 3
    # Send a GET request to the specified URL with the defined headers
    res = requests.get(f'https://www.f2mex.ir/page/{page}/', headers=headers)

    # Check if the request was successful
    if res.status_code == 200:  # If the status code indicates success (200)
        # Parse the response text using BeautifulSoup
        soup = BeautifulSoup(res.text, 'html.parser')

        # Select all movie rows
        movie_rows = soup.select('.imdb_row.d-flex.flex-wrap.align-items-center')

        # Loop through each movie row
        for row in movie_rows:
            # Find the rating span
            rating_span = row.select_one('.val')  # Adjust the selector if needed
            # Find the link to the movie
            link_tag = row.select_one('a')  # Assuming the movie link is in an anchor tag

            if rating_span and link_tag:  # Check if both elements exist
                # Use a regular expression to extract the rating number
                rating_text = rating_span.get_text(strip=True)
                rating_match = re.search(r'(\d+\.\d+)', rating_text)  # Match the pattern for a float

                if rating_match:
                    rating = float(rating_match.group(1))  # Convert the matched string to float
                    if rating > int(x):  # Filter based on the rating
                        movie_link = link_tag['href']  # Get the href attribute
                        movie_links.append(movie_link)  # Add the link to the list

        # Loop through each movie link and send a GET request to retrieve the page
        for link in movie_links:
            res2 = requests.get(link, headers=headers)  # Use 'link'
            soup2 = BeautifulSoup(res2.text, 'html.parser')

            # Select and print the desired movie data


            movie_rows2 = soup2.select('.hero__primary-text')  # Adjust the selector if needed
            for movie_row in movie_rows2:  # Iterate over the ResultSet
                list1.append(movie_row.get_text(strip=True))  # Print the text of each movie row

list2 = list(set(list1[::-1]))
print(*list2 , sep='\n')
# Print all movie links at the end
print(*movie_links, sep=' || ')