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
    real :: x, v, g, t, dt
    
    x = 1.0	! initial height of the ball
    v = 0.0	! initial velocity of the ball
    g = 9.8	! gravitational acceleration
    t = 0.0	! initial time
    dt = 0.01	! size of time step
    
    open(10,file='euler_generic_inelastic.csv')   ! open data file
    
    do steps = 1, 300    ! loop for 300 timesteps
      t = t + dt
      x = x + v*dt
      v = v - g*dt



      if(x.lt.0) then		! reflect the motion of the ball
        x = -x
        v = -v
        v = v - v*0.1 !reduce velocity by 10%



   
      endif

      write(10,*) t, x, v	! write out data at each time step
    
    enddo
    
end program bouncing_balls
    