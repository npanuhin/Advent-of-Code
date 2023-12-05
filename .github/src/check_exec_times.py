# from sys import path as sys_path
# import os

# sys_path.append("../")

# from readme_exec import count_time
# from utils import mkpath


# result = []
# for year in range(2000, 3000):
#     for path, folders, files in os.walk(mkpath("../../", year)):
#         cur_path = os.getcwd()
#         os.chdir(path)

#         for filename in files:
#             if os.path.splitext(filename)[1] != ".py":
#                 continue

#             with open(filename, encoding='utf-8') as file:
#                 code = file.read().strip()

#             time = round(count_time(code))

#             if time >= 1000:
#                 result.append((mkpath(path, filename), time))

#         os.chdir(cur_path)

#         with open("exec_time_result.txt", 'w') as file:
#             for path, time in result:
#                 print(path, str(time) + "ms", file=file)


# path = "../../2020/Day 23/"
# filename = "part2.py"

# cur_path = os.getcwd()
# os.chdir(path)

# with open(filename, encoding='utf-8') as file:
#     code = file.read().strip()

# print(mkpath(path, filename), str(round(count_time(code))) + "ms")

# os.chdir(cur_path)
