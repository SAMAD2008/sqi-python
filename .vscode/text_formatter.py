text = " tHe BoY is haPpy "
#print(dir(str))
formatted_string = text.strip()
print(formatted_string)
contain = formatted_string.capitalize()
print(contain)
print(f"{contain}.")


book_info = "john doe ; the art of programming ; 2020 ; ISN 978-3-16-148410-0 ; 350 ; 2500"
formatted_bookinfo = book_info.split(" ; ")
print(formatted_bookinfo)
name, title, year, ISBN, price, totalpages = formatted_bookinfo 
formatted_title = title.strip()
print(formatted_title)        
float_price = float(price)
str_name = name.title()

formatted_book_info = (f"The book {formatted_title} was written by {str_name} and published in {year}. It has {totalpages} pages and {ISBN.replace("ISB", "ISBN")} and costs {"float_price"} ")

print(formatted_book_info) 






