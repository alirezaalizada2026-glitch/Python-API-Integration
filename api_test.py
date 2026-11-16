import requests
import json

# API URL
url = "https://jsonplaceholder.typicode.com/posts"

try:
    # Send GET request
    response = requests.get(url, timeout=10)

    # Check HTTP errors
    response.raise_for_status()

    # Convert JSON response to Python data
    posts = response.json()

    print("Total posts from API:", len(posts))

    # Get number of posts from user
    try:
        limit = int(input("Enter the number of posts to retrieve: "))

        if limit <= 0:
            print("Please enter a positive integer.")

        elif limit > len(posts):
            print("Only", len(posts), "posts are available.")

        else:
            # Select requested posts
            selected_posts = posts[:limit]

            # Save posts to JSON file
            with open("posts.json", "w", encoding="utf-8") as file:
                json.dump(selected_posts, file, indent=4)

            print("\n----- Retrieved Posts -----")
            for post in selected_posts:
                print("\nPost ID : ", post['id'])
                print("Title : ", post['title'])
                print("Body : ", post['body'])
                print("------------------------")
            print('Requested Posts : ', limit)
            print("Retrieved Posts : ", len(selected_posts))
            print("Data saved successfully.")

    except ValueError:
        print("Invalid input! Please enter a number.")

except requests.exceptions.Timeout:
    print("Error: The request timed out.")

except requests.exceptions.ConnectionError:
    print("Error: Please check your internet connection.")

except requests.exceptions.HTTPError as error:
    print("HTTP Error:", error)

except requests.exceptions.RequestException as error:
    print("API Error:", error)

except json.JSONDecodeError:
    print("Error: Invalid JSON response.")