import my_module


def update_func1():
    # Modify the func1 function in the my_module module
    def new_func1():
        return "Updated Function 1"
    my_module.func1 = new_func1


def update_variable():
    # Modify the my_variable variable in the my_module module
    my_module.my_variable = "Updated value"
