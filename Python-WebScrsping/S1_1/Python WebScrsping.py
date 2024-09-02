import os
import re
import requests

# Define menu categories with their URLs
menu_urls = {
    "Breakfast": "https://mcdonalds.com.pk/full-menu/breakfast/",
    "Beef": "https://mcdonalds.com.pk/full-menu/beef/",
    "Chicken and Fish": "https://mcdonalds.com.pk/full-menu/chicken-and-fish/",
    "Crispy Chicken": "https://mcdonalds.com.pk/full-menu/crispy-chicken/",
    "Wraps": "https://mcdonalds.com.pk/full-menu/wraps/",
    "Happy Meal": "https://mcdonalds.com.pk/full-menu/happy-meal/",
    "Extra Value Meals": "https://mcdonalds.com.pk/full-menu/extra-value-meals/",
    "Value Meals": "https://mcdonalds.com.pk/full-menu/value-meals/",
    "Desserts": "https://mcdonalds.com.pk/full-menu/desserts/",
    "Beverages": "https://mcdonalds.com.pk/full-menu/beverages/",
    "Mc Cafe": "https://mcdonalds.com.pk/full-menu/mccafe/",
    "Fries and Sides": "https://mcdonalds.com.pk/full-menu/fries-and-sides/"
}

# Create a directory to store the menu files
output_dir = "scraped_menus"
os.makedirs(output_dir, exist_ok=True)
print(f"Created directory: {output_dir}")

# Function to check if a string is a palindrome
def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]

# Loop through each menu category
for category_name, url in menu_urls.items():
    print(f"Processing category: {category_name}")

    # Fetch the webpage content
    response = requests.get(url)
    webpage_content = response.text

    # Check if the menu category is found on the webpage
    if category_name.lower() in webpage_content.lower():
        # Sanitize the file name by removing special characters
        sanitized_name = re.sub(r'[^A-Za-z0-9]', '', category_name)

        # Extract item names
        extracted_items = re.findall(r'<span class="categories-item-name">([^<]+)</span>', webpage_content)

        # Save the extracted items to a file with line numbers
        output_file = os.path.join(output_dir, f"{sanitized_name}.txt")
        with open(output_file, 'w') as f:
            for idx, item in enumerate(extracted_items, 1):
                f.write(f"{idx}. {item}\n")

        print(f"Successfully saved items for {category_name} to {output_file}")
    else:
        print(f"Warning: {category_name} not found on the webpage.")

print("Script execution completed.")
