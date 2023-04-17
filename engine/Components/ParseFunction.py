# Global Variables
left_brackets = "({["
right_brackets = ")}]"
binary_connectives = ['^', 'v', '->', '<->']
unary_connectives = ['!']


# START HERE
def parse_statements(statement, elements, variables):

    # print("statement=" + statement)
    # print("variables=" + str(variables))
    # print("elements=" + str(elements) + '\n')

    # print("calling parse()")
    returned_arr = parse(elements)

    # print("print returned_arr in parse_statement=" + str(returned_arr))

    # print("exit build_statements()")
    return returned_arr


# takes a new analyzed statement as array and
# returns an array of the parsed statement with individual blocks
def parse(arr):
    # is_parsable = False
    is_parsable = count_brackets(arr)

    if is_parsable:
        temp_arr = []

        # remove brackets
        arr = remove_brackets(arr)
        # parse the binary/unary into left, middle, and right
        if arr[0] in unary_connectives:
            temp_arr.append(arr[0])
            temp_arr.append(arr[1])
            return temp_arr

        middle, position_middle = find_connective(arr)

        # left
        left = []
        arr_left = arr[:position_middle]
        if len(arr_left) > 1:
            # print("left")
            if arr_left[0] in left_brackets:
                left = parse(arr_left)
        elif len(arr_left) == 1:
            left.append(arr_left[0])

        # right
        right = []
        arr_right = arr[position_middle + 1:]
        if len(arr_right) > 1:
            # process right side
            # print("right")
            if arr_right[0] in left_brackets:
                right = parse(arr_right)
        elif len(arr_right) == 1:
            right.append(arr_right[0])

        temp_arr.append(left)
        temp_arr.append(middle)
        temp_arr.append(right)

        return temp_arr


# does a check to see whether there is a matching number of opening
# and closing brackets
# returns bool
def count_brackets(array):
    count = 0
    for i in range(len(array)):
        if array[i] in left_brackets:
            count += 1
        elif array[i] in right_brackets:
            count -= 1

    if count == 0:
        return True

    return False


# checks whether the open brackets have matching closing brackets
# def check_brackets(array):
#     inBracket = False
#     clear_array = []
#     i = 0
#     while i < len(array):
#         # for i in range(len(array)):
#         if array[i] in left_brackets:
#             # if we are already in brackets
#             if inBracket:
#                 clear = check_brackets(array[i:])
#                 i += 1
#             inBracket = True
#             i += 1
#             continue
#         elif array[i] in right_brackets and inBracket:
#             # found matching closing bracket
#             inBracket = False
#             return not inBracket
#         else:
#             clear_array.append(array[i])
#             print("clear_array=" + str(clear_array))
#             i += 1


# removes the outer brackets and returns new array
# returns a new array with the outer brackets removed
def remove_brackets(array):
    len_of_array = len(array)
    array.pop(0)
    array.pop(len_of_array - 2)

    return array


# returns an integer of the position of the closing bracket
def find_pos_close(array):
    # print("in find_pos_close()")

    # print("debug in find_pos_close(): array=" + str(array))
    for i in range(len(array)):
        if array[i] in right_brackets:
            # print("exit find_pos_close()")
            return i


# given an array without outer brackets, find the connective between
# left section and right section
# (left) conn (right)
# returns a string with the connective and position in array
def find_connective(arr):
    temp_string = ''
    count = 0
    in_bracket = False

    for i in range(len(arr)):
        j = 0
        elem = arr[i]
        if elem in left_brackets:
            in_bracket = True
            count += 1
        if elem in right_brackets and in_bracket:
            if count == 1:
                in_bracket = False
            count -= 1
        if elem in binary_connectives and not in_bracket and count == 0:
            # print("debug")
            return elem, i

    return temp_string
