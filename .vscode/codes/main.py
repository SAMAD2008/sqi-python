from data_processing.file_reader import read_data
# from data_processing.web_fetcher import fetch_user_data
from data_processing.web_fetcher import fetch_user_zip_and_website


# result = read_data('data.txt')

# print(result)

# users_usernames = fetch_user_data()

# print(users_usernames)




users_zip_and_website = fetch_user_zip_and_website()

print(users_zip_and_website)