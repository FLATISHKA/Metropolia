import os


def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")


def generate_functions_list(module_file):
    module_name = os.path.splitext(os.path.basename(module_file))[0]
    module = __import__(module_name)
    function_list = [func for func in module.__dict__.values() if callable(func) and func.__module__ == module_name]
    return function_list


def function_driver(module_file, exceptions):
    try:
        functions = generate_functions_list(module_file)
        module_name = os.path.splitext(os.path.basename(module_file))[0]
        exe_i = 0
        for function in functions:
            function_name = function.__name__
            if function_name in exceptions:
                continue
            else:
                exe_i = exe_i + 1
            print_colored(f"Calling function: ({module_name}.{exe_i}) {function_name}", 32)
            try:
                function()
            except:
                print_colored("Function error!", 31)
    except:
        print_colored("\nDriver error!", 31)