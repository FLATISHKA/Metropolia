import os


def print_colored(text_left, color_left, text_right="", color_right=0):
    colored_left = f"\033[{color_left}m{text_left}\033[0m"
    colored_right = f"\033[{color_right}m{text_right}\033[0m"
    left = colored_left if color_left else text_left
    right = colored_right if color_right else text_right
    print(left + right)


def generate_functions_list(module_file):
    module_name = os.path.splitext(os.path.basename(module_file))[0]
    module = __import__(module_name)

    function_list = [
        func for func in module.__dict__.values()
        if callable(func) and func.__module__ == module_name and func.__name__ != "Exc"
    ]
    return function_list


def function_driver(module_file):
    try:
        functions = generate_functions_list(module_file)
        module_name = os.path.splitext(os.path.basename(module_file))[0]
        for i, function in enumerate(functions):
            function_name = function.__name__
            function_info = f"({module_name}.{i + 1}) {function_name}"
            print_colored("Function: ", 0, function_info, 32)  # White color

            try:
                function()
            except:

                print_colored("\nFunction error!", 31)
    except:
        print_colored("\nDriver error!", 31)
