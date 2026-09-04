############################################################
# [11-13] try ~ except
############################################################

# try :
#     a = 200
# except NameError :
#    print('NameError 1')
# 
# try :
#     a = b
# except NameError :
#     print('NameError 2')
#     b = 50
#     a = b
# 
# print(a, b)

############################################################
# [11-14-1] 오류 이름이 맞지 않는 경우
############################################################

# try :
#     a = b
# except TypeError : 
#     print('TypeError')
#     b = 50

############################################################
# [11-14-2] Exception: 모든 오류에 대응
############################################################

# try :
#     a = b
# except Exception : 
#     print('Error')
#     b = 50
#     a = b
# 
# print(a, b)

############################################################
# [11-15] Error Object와 오류 내용의 인쇄
############################################################

# try :
#     a = int('3.14')
# except Exception as e :
#     print(type(e))
#     print(type(e).__name__, e)
#     a = int(3.14)
# 
# print(a)

############################################################
# [11-16-1] else
############################################################

# try :
#     a = 10
# except NameError :
#     print('NameError')
#     a += 20
# else :
#     a += 30
#     
# print(a)

############################################################
# [11-16-2] finally
############################################################

# try :
#     a = 10
#     a = b
# except NameError :
#     print('NameError')
#     a = 0
# else :
#     a += 30
# finally :
#     a += 40

# print(a)

############################################################
# [11-17-1] 다양한 오류 대응
############################################################

# n = int(input())
# t = (1, 'kim', 2)
# 
# try :
#     if n == 2 :
#         a = b
#     else :
#         a = t[n] + 1
# except TypeError as e : # 1
#     print(type(e).__name__, e)
#     a = 10
# except NameError as e : # 2
#     print(type(e).__name__, e)    
#     a = 20
# except IndexError as e : # 3
#     print(type(e).__name__, e)    
#     a = 30
# finally :
#     print(a)

############################################################
# [11-17-2] 발생 오류 무시
############################################################

# a = 10
# 
# try :
#     a = b
# except Exception :
#     pass
# 
# print(a)

############################################################
# [11-18] 모듈 import
############################################################

# def add(a, b):
# 	return 'add?'
# 
# import my_module
# print(add(3,4), my_module.add(3,4), my_module.sub(3,4))

# import my_module as mm
# print(mm.add(3,4), mm.sub(3,4))

# import my_module as mm, your_module as ym
# print(mm.add(3,4), mm.sub(3,4))
# print(ym.mul(3,4), ym.div(3,4))

############################################################
# [11-19] 모듈의 특정 이름(name) import
############################################################

# def add(a, b):
#     return 'add?'
# 
# import my_module as mm
# from my_module import add
# 
# print(add(3,4))
# print(mm.add(3,4), mm.sub(3,4))

# from my_module import add, sub
# print(add(3,4), sub(3,4))

# from my_module import *
# print(add(3,4), sub(3,4))

############################################################
# [11-20] Module import와 Name import의 차이
############################################################

# import pprint as pp
# 
# import my_module as mm
# from my_module import add
# 
# pp.pprint(globals())

############################################################
# [11-21] 패키지 import
############################################################

# import my_package.my_module as mm
# print(mm.add(3,4), mm.sub(3,4))
# 
# from my_package import my_module as mm
# print(mm.add(3,4), mm.sub(3,4))
# 
# from my_package.my_module import add, sub
# print(add(3,4), sub(3,4))
# 
# from my_package.my_module import *
# print(add(3,4), sub(3,4))
# 
# import sys
# sys.path.append(r'.\my_package\files')
# 
# import my_module2 as mm2
# sys.path.pop()
# 
# print(mm2.add(3,4), mm2.sub(3,4))
