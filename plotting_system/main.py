# plot with euler method
import os.path

from plotting_system.ball_movement_plotter import plot_ball
from plotting_system.difference_plotter import plot_differences

current_path = os.getcwd()
### Exercise 1

plot_ball(directory=current_path + '/csv_files/euler_generic.csv',
          name_of_file='euler_generic.png')

# plot with euler + collision account method
plot_ball(directory=current_path + '/csv_files/euler_collision.csv',
          name_of_file='euler_collision.png')

# plot with verlet method
plot_ball(directory=current_path + '/csv_files/verlet.csv',
          name_of_file='verlet.png')

### Exercise 2

# plot with c files
plot_ball(directory=current_path + '/csv_files/c_generic.csv',
          name_of_file='c_generic.png')

# plot difference between generic euler and c generic
plot_differences(directory1=current_path + '/csv_files/euler_generic.csv',
                 directory2=current_path + '/csv_files/c_generic.csv', name_of_file='c_vs_fortran_generic.png')

### Exercise 3


plot_ball(directory=current_path + '/csv_files/euler_generic_small_dt.csv',
          name_of_file='euler_generic_small_dt.png')

# plot with euler + collision account method
plot_ball(directory=current_path + '/csv_files/euler_collision_small_dt.csv',
          name_of_file='euler_collision_small_dt.png')

# plot with verlet method
plot_ball(directory=current_path + '/csv_files/verlet_small_dt.csv',
          name_of_file='verlet_small_dt.png')

### Exercise 4, plot all three methods with different velocity and position

plot_ball(directory=current_path + '/csv_files/euler_generic_new_v_x.csv',
          name_of_file='euler_generic_new_v_x.png')

plot_ball(directory=current_path + '/csv_files/euler_collision_new_v_x.csv',
          name_of_file='euler_collision_new_v_x.png')

plot_ball(directory=current_path + '/csv_files/verlet_new_v_x.csv',
          name_of_file='verlet_new_v_x.png')

### Exercise 5, plot all three methods with inelastic impact


plot_ball(directory=current_path + '/csv_files/euler_generic_inelastic.csv',
          name_of_file='euler_generic_inelastic.png')

plot_ball(directory=current_path + '/csv_files/euler_collision_inelastic.csv',
          name_of_file='euler_collision_inelastic.png')

plot_ball(directory=current_path + '/csv_files/verlet_inelastic.csv',
          name_of_file='verlet_inelastic.png')
