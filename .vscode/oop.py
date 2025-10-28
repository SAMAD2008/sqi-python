# # class Car:
# #         def __init__(self, brand, make_year):
# #          print('Car brand:', brand)
# #          print('year:', make_year)

# # Car_details1 = Car('Toyota', '1999')        
# # Car_details2 = Car('Nissan', '2000')        

# class Line:
#     def __init__(self, coor1, coor2): 
#         self.x1, self.y1 = coor1
#         self.x2, self.y2 = coor2

#     def distance(self):
#          distance_result = ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5
#          return distance_result
    
#     def slope(self):
#         slope_result = (self.y2 - self.y1) / (self.x2 - self.x1)
#         return slope_result

# coor1 = (2, 5)
# coor2 = (8, 9)
# line1 = Line(coor1, coor2)       
# print(line1.distance())
# print(line1.slope())
# line2 = Line((7, 8), (9, 2))
# print(line2.distance())
# print(line2.slope())



# Handle Multiple Exceptions:
# Write a function safe_divide(a, b) that performs division.
# Handle ZeroDivisionError if the divisor is zero.
# Handle TypeError if the inputs are not numbers.
# Handle ValueError if the inputs are not convertible to floats.
# def safe_divide(a, b):
#     try:
#         result = a / b
#         return result
#     except ZeroDivisionError:
#         return "Error: Division by zero is not allowed."
#     except TypeError:  
#         return "Error: Inputs must be numbers."
#     except ValueError:
#         return "Error: Inputs must be convertible to floats."
#     except Exception:
#         return "An error occured. Please, check your inputs well."
    
# print(safe_divide(2, 6))

class NegativeNumberError(Exception):
    def __init__(self, message = "The provided number is less than zero"):
        self.message = message
        super().__init__(self.message)

def check_positive(number):
    if number < 0:
        raise NegativeNumberError
    return number




