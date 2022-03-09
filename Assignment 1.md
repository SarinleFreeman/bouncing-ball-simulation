### Assignment 1
****


**Basic Theoretical Model**:

The problem is associated with the dynamics of a ball released from a certain height. The situation can be mathematically encapsulated through the below formulas:

$$x(0) = c\\\ , v(0) = b : c,b \in R$$
$$v(t) = \frac {dx}{dt}$$
$$a(t) = \frac {dv}{dt} = -g$$

It is trivial to see that the above then induce the solutions:

$$\int a(t)dt = v(t)  =  -gt + A $$

$$\int v(t)dt = \frac {-gt^2}{2} + At + B$$

where $A,B$ are constants that can be shown to be equivalent to:

$$B = x(0) , A = v(0)$$

**Numerical  Model**:

I will utilize the euleur method to discretize our system:

$$v(t) = \frac{x(t+\Delta t) - x(t)}{\Delta t}  $$

$$a(t) = -g = \frac{v(t+\Delta t) - v(t)}{\Delta t}  $$

Thus acquiring the following:

$$x(t+\Delta t) = v(t)\Delta t + x(t)$$

$$v(t+\Delta t) = -g\Delta t +v(t)  $$


## Exercise 1 

After running the code given i get the current output:

![[c_generic.png]]
*Figure 1: Generic Euler method*

Figure 1 displays various parameters (position,velocity and energy) over time. The initial maximum values are viewed through a dotted red line, one notices that the energy of our isolated system is increasing!

This error stems from eulers method assuming constant velocity between time steps. This is incorrect generally and is especially incorrect at the ground discontinuity where the velocity is flipped.

One way to minimize this iis to perform the euler method over a smaller step for the time before it hits 0 (*see euler_collision.f90 file for more details*)

$$\Delta t_0 = \frac{x(t)}{v(t)}$$
$$x(t+\Delta t_0) = 0$$

$$v(t+\Delta t_0) = -(-g\Delta t_0 +v)  $$

This gives us the following plot:

![[euler_collision.png]]
*Figure 1: Collision handling Euler method*

However this , still , isn't accurate enough. Thus to handle this lack of energy conservation in our system i can utilize the drift-kick-drift method. This method unlike the Euler method is time reversible thus leading to energy conservation. 

$$v(t+\frac {\Delta t} {2}) = v(t) - g\frac {\Delta t} {2}$$

$$x(t+\Delta t) = x(t) +v(t+\frac {\Delta t} {2})\Delta t $$

$$v(t+\Delta t) = v(t+\frac {\Delta t} {2}) - g\frac {\Delta t} {2}  $$


Below is a plot utilizing the above method combined with the discontinuity handling method shown before:


![[verlet.png]]
*Figure 3: Drift - Kick -Drift method*

As you can see energy is conserved in this situation and the mechanics of the ball are more accurate.



## Exercise 2

To analyse the impact of running c-code i viewed the difference between all three parameters over time

![[c_vs_fortran_generic.png]]
*Figure 4: C-code vs Fortran code with generic euler method*

As you can see the differences are not significant and seem to be mainly caused by random error fluctuations.

## Exercise 3

In this exercise i reduced the time step by 100 and increased the total run time by 100 as well. I then ran the system for all three methods

![[euler_generic_small_dt.png]]
![[euler_collision_small_dt.png]]
![[verlet_small_dt.png]]
*Figure 5: Smaller time differential: generic euler, euler+collision and drift-kick-drift methods in that order.*

As we can see all three systems are more accurate.To understand why, we must understand the simulated Euler method derived variables, $E_s$, are correct when we take the limit $\Delta t$ to 0.


$$E_{true} = lim_{\Delta t \rightarrow 0}\\\ E_s(\Delta t)$$

Thus as we reduce the time_step we converge to the actual value at higher and higher levels of approximations.


## Exercise 4

In this exercise i increased the initial velocity and position by 10 units.

The following plots are for all three methods:


![[euler_generic_new_v_x 2.png]]
![[euler_collision_new_v_x 1.png]]
![[verlet_new_v_x 1.png]]
*Figure 6: v_0 = 10 and x_0 = 10 : generic euler, euler+collision and drift-kick-drift methods in that order.*

We quickly notice that the position,velocity and energy waves are  characterised by a higher frequency. This makese sense as the velocity of the ball impacts reaches the ground quicker and correspondingly reaches it peak quicker.

We also notice, unlike the previous cases, the balls position goes upwards initially instead of downwards. This is due to the initial velocity propelling it upwards. Moreover the maximum height also increases relative to the previous cases as the ball is given more initial propulsion.

We also notice that the energy of the system is higher then our previous cases , this makes sense as the total energy of our isolated system is characterised by:

$$E = \frac 12 m v_0^2 + mgh_0$$

Finally the error associated with energy also seems to take longer to manifest, this is due to the added energy being miniscule relative to the total energy. Hence we only begin to see its impacts at later times.


## Exercise 5
In this exercise i increased the initial velocity and position by 10 units.

The following plots are for all three methods:

![[euler_collision_inelastic.png]]
![[euler_generic_inelastic.png]]
![[verlet_inelastic.png]]
*Figure 7: Inelastic collisions : generic euler, euler+collision and drift-kick-drift methods in that order.*

The plots show the balls height decreasing slowly over time as well as it's energy also decreasing over time.

This makes sense as after every collision with the ground the ball loses 10% of its velocity and correspondingly its total energy decreases to 81% of its previous value:

$$E_{new} = \frac 1 2 m(0.9v)^2 = 0.81\frac 1 2 m(v)^2 = 0.81 E_{old} $$

Hence we are noticing a 19% loss of energy after every collision, Which inturn means the maximum height the ball can reach decreases by the same amount.

We finally notice , due to the error in euler methods, the rate of decrease seems to be faster in the drift-kick-drift method. This leads to their peaks slowly being out of sync.


