import os


def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")


def generate_functions_list(module_file):
    module_name = os.path.splitext(os.path.basename(module_file))[0]
    module = __import__(module_name)
    function_list = [func for func in module.__dict__.values() if callable(func) and func.__module__ == module_name]
    return function_list


def function_driver(module_file):
    functions = generate_functions_list(module_file)
    module_name = os.path.splitext(os.path.basename(module_file))[0]
    for index, function in enumerate(functions):
        function_name = function.__name__
        print_colored(f"Calling function: ({module_name}.{index + 1}) {function_name}", 32)
        try:
            function()
        except:
            print_colored("Function error!", 31)