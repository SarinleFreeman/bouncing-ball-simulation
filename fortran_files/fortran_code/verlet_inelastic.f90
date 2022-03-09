! --------------------------------
! Name: Mohamed Yusuf
! Assignment: 1
!----------------------------------

program bouncing_balls
    implicit none
    
    ! Use the Euler method to compute the trajectory of a bouncing
    ! ball assuming perfect reflection at the surface x = 0.
    ! Use SI units (meters and seconds)
    
    integer :: steps
    real :: x, v, g, t, dt,v_half,dt_temp,next_v,next_x,next_v_half
    
    x = 1.0	! initial height of the ball
    v = 0.0	! initial velocity of the ball
    g = 9.8	! gravitational acceleration
    t = 0.0	! initial time
    dt = 0.01	! size of time step
    
    open(10,file='verlet_inelastic.csv')   ! open data file
    
    do steps = 1, 300    ! loop for 300 timesteps
      t = t + dt
      v_half = v - g*(dt/2)
      x = x + v_half*dt
      v = v_half -g*(dt/2)

      next_v_half = v - g*(dt/2)
      next_x = x + v_half*dt
      next_v = v_half -g*(dt/2)



      if(next_x.lt.0) then		! reflect the motion of the ball
        dt_temp  = -x/v ! calculate time ball takes to hit floor
        v = -(v- g*dt_temp) ! calculate velocity at ground
        v = v - v*0.1 !reduce velocity by 10%
        x = 0 ! set time at 0
        t = t + dt_temp ! update the time correspondingly
   
      endif

      write(10,*) t, x, v	! write out data at each time step
    
    enddo
    
end program bouncing_balls
    