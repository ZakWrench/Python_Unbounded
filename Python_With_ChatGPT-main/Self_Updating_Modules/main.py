import my_module
import update_module

# Call the update_func1 and update_variable functions from the update_module script
update_module.update_func1()
update_module.update_variable()

# Call the updated functions and variables from the my_module module
print(my_module.func1())  # prints "Updated Function 1"
print(my_module.func2())  # prints "Function 2"
print(my_module.my_variable)  # prints "Updated value"
