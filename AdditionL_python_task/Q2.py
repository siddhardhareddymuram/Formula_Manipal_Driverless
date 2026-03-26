import numpy as np
from scipy.optimize import minimize


x_car = 0.1
y_car = 3.1
v = 5.5
v_des = 10
a = 1.3
yaw_rate = 0.23
psi = 0.0 
dt = 0.02
N = 3  


x_prev, y_prev = 0.9, 3
x_next, y_next = 1.4, 4.1


w_theta = 1.0
w_cte = 1.0
w_v = 1.0


def cost(steering_angle):
    x, y, psi_t, v_t = x_car, y_car, psi, v
    J = 0
    for _ in range(N):
       
        x += v_t * np.cos(psi_t) * dt
        y += v_t * np.sin(psi_t) * dt
        psi_t += yaw_rate * dt + steering_angle 
        v_t += a * dt
        
    
        cte = abs((y_next - y_prev)*x - (x_next - x_prev)*y + x_next*y_prev - y_next*x_prev) / \
              np.sqrt((y_next - y_prev)**2 + (x_next - x_prev)**2)
        
      
        path_angle = np.arctan2(y_next - y_prev, x_next - x_prev)
        theta_err = psi_t - path_angle
   
        v_err = v_des - v_t
        
     
        J += w_theta*(theta_err**2) + w_cte*(cte**2) + w_v*(v_err**2)
        
    return J


res = minimize(cost, x0=0.0, bounds=[(-0.5, 0.5)]) 
print("Optimal steering angle:", res.x[0])
print("Minimum cost:", res.fun)