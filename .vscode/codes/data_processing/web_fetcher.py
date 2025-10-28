import requests as req

# def fetch_user_data():
#     url = "https://jsonplaceholder.typicode.com/users"
#     usernames_list = []
#     try:
#         users = req.get(url).json()

#         for user in users:
#             username = user['username']
#             usernames_list.append(username)

#             # zip code 
#             # website
#         return usernames_list

#     except req.exceptions.SSLError:
#         print("An SSL Error has occured.")

#         return usernames_list
#     except req.exceptions.ConnectionError:
#         print("Internet connection not found! Please connect to a strong network and try again.")
#         return usernames_list

   




def fetch_user_zip_and_website():
    url = "https://jsonplaceholder.typicode.com/users"
    user_data = []
    try:
        users = req.get(url).json()

        for user in users:
            zipcode = user['address']['zipcode']
            website = user['website']
            user_data.append({"zip": zipcode, "site": website})

        return user_data

    except req.exceptions.SSLError:
        print("An SSL Error has occured.")

        return user_data
    except req.exceptions.ConnectionError:
        print("Internet connection not found! Please connect to a strong network and try again.")
        return user_data

   
















