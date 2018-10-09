import numpy as np  # 一次方程组
num = int(input('请输入参数（方程）个数：'))
A, B, C = [eval(input("请输入第%d行系数列表：" % i)) for i in range(1, num+1)], eval((input('请输入含%d个常量的列表：' % num))), eval(str((input('请输入含%d个参数的列表：' % num)).split(',')))
print('\n'.join(str(a) for a in [str(C[i]) + '=' + str(np.linalg.solve(A, B)[i]) for i in range(len(np.linalg.solve(A, B)))]))