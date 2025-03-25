#多次多项式拟合
# 构造三次多项式设计矩阵
import numpy as np

# 新的数据点
voltage =     [0, 3, 6, 9, 12, 16, 19, 22, 25, 28, 32, 72, 112, 151, 192, 232, 271, 312, 352, 392, 472, 552, 632, 711, 791, 871, 951, 1030, 1113, 1190, 1270, 1351, 1389, 1430, 1470, 1509, 1549, 1589, 1629, 1670, 1709, 1749, 1789, 1829]
standardAdc = [0, 1, 2, 3, 4,  5,  6,  7,  8,  9,  10, 20, 30,  40,  50,  60,  70,  80,  90,  100, 120, 140, 160, 180, 200, 220, 240, 260,  280,  300,  320,  340,   350,  360,  370,  380,  390,  400, 410,  420,  430,  440,  450,  460]

# 构造三次多项式设计矩阵
A = np.vstack([np.ones(len(voltage)), voltage, np.array(voltage)**2, np.array(voltage)**3]).T
B = np.array(standardAdc)

# 使用最小二乘法求解
X = np.linalg.lstsq(A, B, rcond=None)[0]

# 输出拟合参数
print("Fitted polynomial coefficients:")
print("a0 = {:.6f}".format(X[0]))
print("a1 = {:.6f}".format(X[1]))
print("a2 = {:.6f}".format(X[2]))
print("a3 = {:.6f}".format(X[3]))

a0 = 1.161132 
a1 = 0.253701 
a2 = -0.000004
a3 = 0.000000 
x = 1829.000000
result = a0 + a1 * x + a2 * x**2 + a3 * x**3
print(f"P(1829) = {result:.6f}")
# 计算预测值并验证
predictedAdc = X[0] + X[1] * np.array(voltage) + X[2] * np.array(voltage)**2 + X[3] * np.array(voltage)**3
print("predictedAdc:", predictedAdc)
# 输出预测值和实际值
print("\nValidation:")
for i in range(len(voltage)):
    print(f"Voltage: {voltage[i]}, Predicted ADC: {predictedAdc[i]:.2f}, Actual ADC: {standardAdc[i]}")





# 二次多项式拟合
# import numpy as np

# # 新的数据点
# voltage =     [0, 3, 6, 9, 12, 16, 19, 22, 25, 28, 32, 72, 112, 151, 192, 232, 271, 312, 352, 392, 472, 552, 632, 711, 791, 871, 951, 1030, 1113, 1190, 1270, 1351, 1389, 1430, 1470, 1509, 1549, 1589, 1629, 1670, 1709, 1749, 1789, 1829]
# standardAdc = [0, 1, 2, 3, 4,  5,  6,  7,  8,  9,  10, 20, 30,  40,  50,  60,  70,  80,  90,  100, 120, 140, 160, 180, 200, 220, 240, 260,  280,  300,  320,  340,   350,  360,  370,  380,  390,  400, 410,  420,  430,  440,  450,  460]

# # 构造设计矩阵 A 和向量 B
# A = np.vstack([np.ones(len(voltage)), voltage, np.array(voltage)**2]).T
# B = np.array(standardAdc)

# # 使用最小二乘法求解
# X = np.linalg.lstsq(A, B, rcond=None)[0]

# # 输出拟合参数
# print("Fitted polynomial coefficients:")
# print("a0 = {:.6f}".format(X[0]))
# print("a1 = {:.6f}".format(X[1]))
# print("a2 = {:.6f}".format(X[2]))

# # 计算预测值并验证
# predictedAdc = X[0] + X[1] * np.array(voltage) + X[2] * np.array(voltage)**2

# # 输出预测值和实际值
# print("\nValidation:")
# for i in range(len(voltage)):
#     print(f"Voltage: {voltage[i]}, Predicted ADC: {predictedAdc[i]:.2f}, Actual ADC: {standardAdc[i]}")
# a0 = 1.300701
# a1 = 0.251663
# a2 = -0.000001

# # 计算 x = 5 时的值
# x = 1709.000000
# result = a0 + a1 * x + a2 * x**2
# print(f"P(16) = {result:.6f}")

