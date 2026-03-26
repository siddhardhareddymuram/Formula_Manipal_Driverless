x = 10
z=30
v=5
a=1
y=10
t=0.2
yaw_chang=10*0.2
import numpy as np
z_rad=np.radians(z+yaw_chang)
cosz=np.cos(z_rad)
sinz=np.sin(z_rad)
s_x=(v*cosz)*t+(0.5)*(a*cosz)*(t*t)
s_y=(v*sinz)*t+(0.5)*(a*sinz)*(t*t)
print("New Position of the DV Car is: ")
print(f"({x + s_x:.3f}, {y + s_y:.3f}, {z + yaw_chang:.1f})")

B1 = (12, 7)
B2 = (8, 6)
Y1 = (13, 4)
Y2 = (9, 3)
theta_rad = np.radians(z)
x_rel = B1[0] - x
y_rel = B1[1] - y
x_B1_init = x_rel * np.cos(theta_rad) + y_rel * np.sin(theta_rad)
y_B1_init = -x_rel * np.sin(theta_rad) + y_rel * np.cos(theta_rad)

x_rel = B2[0] - x
y_rel = B2[1] - y
x_B2_init = x_rel * np.cos(theta_rad) + y_rel * np.sin(theta_rad)
y_B2_init = -x_rel * np.sin(theta_rad) + y_rel * np.cos(theta_rad)

x_rel = Y1[0] - x
y_rel = Y1[1] - y
x_Y1_init = x_rel * np.cos(theta_rad) + y_rel * np.sin(theta_rad)
y_Y1_init = -x_rel * np.sin(theta_rad) + y_rel * np.cos(theta_rad)

x_rel = Y2[0] - x
y_rel = Y2[1] - y
x_Y2_init = x_rel * np.cos(theta_rad) + y_rel * np.sin(theta_rad)
y_Y2_init = -x_rel * np.sin(theta_rad) + y_rel * np.cos(theta_rad)

print("Cone positions in car frame (initial):")
print(f"B1: ({x_B1_init:.3f}, {y_B1_init:.3f})")
print(f"B2: ({x_B2_init:.3f}, {y_B2_init:.3f})")
print(f"Y1: ({x_Y1_init:.3f}, {y_Y1_init:.3f})")
print(f"Y2: ({x_Y2_init:.3f}, {y_Y2_init:.3f})")

theta_rad = np.radians(yaw_chang)


x_rel = B1[0] - s_x
y_rel = B1[1] - s_y
x_B1_new = x_rel * np.cos(theta_rad) + y_rel * np.sin(theta_rad)
y_B1_new = -x_rel * np.sin(theta_rad) + y_rel * np.cos(theta_rad)


x_rel = B2[0] -s_x
y_rel = B2[1] -s_y
x_B2_new = x_rel * np.cos(theta_rad) + y_rel * np.sin(theta_rad)
y_B2_new = -x_rel * np.sin(theta_rad) + y_rel * np.cos(theta_rad)


x_rel = Y1[0] - s_x
y_rel = Y1[1] - s_y
x_Y1_new = x_rel * np.cos(theta_rad) + y_rel * np.sin(theta_rad)
y_Y1_new = -x_rel * np.sin(theta_rad) + y_rel * np.cos(theta_rad)


x_rel = Y2[0] - s_x
y_rel = Y2[1] - s_y
x_Y2_new = x_rel * np.cos(theta_rad) + y_rel * np.sin(theta_rad)
y_Y2_new = -x_rel * np.sin(theta_rad) + y_rel * np.cos(theta_rad)

print("\nCone positions in car frame (new):")
print(f"B1: ({x_B1_new:.3f}, {y_B1_new:.3f})")
print(f"B2: ({x_B2_new:.3f}, {y_B2_new:.3f})")
print(f"Y1: ({x_Y1_new:.3f}, {y_Y1_new:.3f})")
print(f"Y2: ({x_Y2_new:.3f}, {y_Y2_new:.3f})")