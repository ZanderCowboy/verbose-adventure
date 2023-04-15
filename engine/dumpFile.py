# i, j = 0, 0
# add_braces = True
# new_elements_array = []
# # copy_elements = elements.copy()
# for e in range(0, len(elements)):
# 	if e == len(elements):
# 		break
# 	if elements[e] == '!':
# 		right = elements[e + 1]
# 		if right in ")}]":
# 			print("Syntax error, break")
# 			break
# 		elif right in "({[":
# 			print("Call negate bracket section")
# 			break
# 		elif right in variables:
# 			connective_statement = "(" + elements[e] + str(right) + ")"
# 			# print(connective_statement)
# 			# print(elements)
# 			elements.pop(e)
# 			# print(elements)
# 			elements.pop(e)
# 			# print(elements)
# 			elements.insert(e, connective_statement)
# 			# j += 1
# 			# print(elements)
#
# print(elements)
# while i < len(elements):
# 	left = ''
# 	right = ''
# 	if elements[i] in variables:
# 		i += 1
# 		continue
# 	elif elements[i] in "(){}[]":
# 		print("Evaluate brackets")
# 	else:
# 		# index = statement.find(elements[i])
# 		index = i
# 		if index > 0:
# 			# todo check to see if braces is needed
#
# 			# todo check to see if left or right is not a variable
# 			if elements[index] != '!':  # todo add comment
# 				left = elements[index - 1]
# 				right = elements[index + 1]
# 				print("Debug: left=" + left + ", right=" + right)
# 				# if right in "({[":  # if open bracket is found, find close bracket and continue
# 				#     temp_array = []
# 				#
# 				#     # todo call function to search for closing bracket
# 				#     print("in right if")
# 				#     for u in range(index+1, len(elements)):
# 				#         temp = elements[u]
# 				#         print(str(u) + '\t' + temp)
# 				#         # print(elements[u])
# 				#         if elements[u] in ")}]":
# 				#             left = elements[u-3]
# 				#             middle = elements[u-2]
# 				#             right = elements[u-1]
# 				#             element = concatenate(left, middle, right)
# 				#             print("print element=" + element)
# 				#             print("print u:" + str(u))
# 				#             break
# 				#     #
# 				# if right in "({[":
# 				# find closing brackets
#
#
# 				if add_braces == True:
# 					connective_statement = "(" + str(left) + elements[index] + str(right) + ")"
# 				print(left + ' + ' + connective_statement + ' + ' + right)
# 				elements.pop(i - 1)
# 				elements.pop(i - 1)
# 				elements.pop(i - 1)
# 				new_elements_array.append(connective_statement)
# 				# elements.insert(i - 1, connective_statement)
# 				j += 1
# 				i -= 1
# 				print("elements=\t" + str(elements))
# 				print("new_ele=\t" + str(new_elements_array))
# 				print()
#
# 			# elif elements[index] == '!':  # in case of negation
# 			#     right = elements[index + 1]
# 			#     connective_statement = "(" + elements[index] + str(right) + ")"
# 			#     print(connective_statement)
# 			#     print(elements)
# 			#     elements.pop(index)
# 			#     print(elements)
# 			#     elements.pop(index)
# 			#     print(elements)
# 			#     elements.insert(index, connective_statement)
# 			#     j += 1
# 			#     print(elements)
#
# 	i += 1
#
# print("final_elements=" + str(new_elements_array))
#
# for e in range(len(new_elements_array)):
# 	elem = new_elements_array[e]
# 	print(elem)
#
# 	if '()' in elem:
# 		# print("yes")
# 		found = elem.find('()')
# 		if found != -1:
# 			print()
# 		# print(elem[2])
#
#
# print("Out build_statements():")
# return elements