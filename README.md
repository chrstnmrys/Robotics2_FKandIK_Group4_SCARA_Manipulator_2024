#  <p align="center">**Robotics 2: Forward and Inverse Kinematics of a**</p>
# <p align="center">**SCARA Manipulator**</p>
##	I. Abstract of the Project														
##  II. Introduction of the Project	
***<div align="justify"> SCARA (Selective Compliance Assembly Robot Arm) Manipulators*** are an essential advancement in the world of robotics, distinguished by their distinctive design and varied functionality. SCARA robots were developed in the 1980s and have since become vital components in a variety of industrial and production environments, providing accurate control and economical operation. At its core, a SCARA manipulator comprises articulated arms capable of movement in the horizontal plane, with a vertical axis of rotation for assembly tasks. This distinctive configuration grants SCARA robots exceptional speed and accuracy, making them ideal for tasks such as assembly, pick-and-place operations, packaging, and more.</div>

<div align="justify">The four-axis configuration of SCARA robots allows them to move along the X, Y, and Z planes. It also provides them with 360 degrees of rotational movement around the Z axis which allows for a cylindrical work envelope. The axes of SCARA robots feature a combination of dynamic and rigid movements. The X and Y axes of SCARA’s are flexible allowing for dynamic movements. This is where the “Selective Compliance” comes from in their name. Compliance refers to flexibility, but not all axes are flexible, so it is selective. The Z axis is the rigid axis since it is fixed. The Selective Compliance feature of SCARA refers to the ability to maintain rigidity and precision during operations while also providing controlled compliance or flexibility to particular directions. This feature allows SCARA robots to adapt to different workpieces and surroundings, resulting in consistent performance across a wide range of applications.</div>

***<div align="justify">SCARA Manipulators*** are versatile beyond only their mechanical design. These robots, which have advanced control systems and programming interfaces, may easily be integrated into automated production lines and synced with other equipment, increasing productivity and efficiency.</div>

##  III. Degrees of Freedom of SCARA Manipulator 	

***<div align="justify">Degrees of Freedom*** is define as the minimum number of independent parameters/variables/coordinates needed to describe a system completely. Consider a robotic arm. Its degrees of freedom are determined by each joint, which allows it to move in any direction, turn, and bend. For example, a simple arm with an elbow and shoulder joint may have two degrees of freedom, one for the movement of each joint.</div>

<div align="justify">More generally, DoF is essential to comprehending the capabilities of a robot. A robot with more degrees of freedom can carry out more complex tasks and adjust to a larger variety of conditions. Higher DoF can, however, also lead to more complex programming since they usually call for more advanced control systems. A key component of robotics design is balancing the number of degrees of freedom with the particular tasks a robot has to perform.</div>


\
The following are the Ideal Degrees of Freedom
+ A point in 2D: 2-DoF ; 3D: 3-DoF
+ A rigid body in 3D: 6-DoF
+ Planar Manipulator: 3-DoF
+ Spatial Manipulator: 6-DoF

Three Types of Manipulator based on the number of Degrees of Freedom
1. Under-Actuated Manipulator
   - Either a spatial manipulator with less than 6-dof or a planar manipulator with less than 3-DoF.

2. Ideal Manipulator
   - Either a spatial manipulator with exactly 6-dof or a planar manipulator with exactly 3-DoF.

3. Redundant Manipulator
   - Either a spatial manipulator with more than 6-dof or a planar manipulator with more than 3-DoF.
  
***Note:*** If the DOF of a manipulator is more than the Ideal Manipulator or based on your computation it is a Redundant Manipulator it is called ***Mobility***. 


***Grubler's Criterion for Mobility***

| ***Planar Manipulator***  | ***Spatial Manipulator***|
| ------------------------- | ------------------------ |
|                           |                          |

***Mechanical Manipulator Anatomy***

| ***Joint Type*** | ***DoF *f****|***Constraints c between two planar rigid <p align="center">bodies</p>***|***Constraints c between two spatailrigid <p align="center">bodies</p>***| 
| ------------------------- | ------------------------ | ------------------------ | ------------------------ | 
|      Revolute (R)       |                  1         |<p align="center">2</p>          |<p align="center">5</p>       |
|      Prismatic(P)       |                  1         |<p align="center">2</p>          |<p align="center">5</p>       |
|      Helical (H)        |                  1         |<p align="center">N/A</p>        |<p align="center">5</p>       |
|      Cylindrical(c)     |                  2         |<p align="center">N/A</p>        |<p align="center">4</p>       |
|      Universal (U)      |                  2         |<p align="center">N/A</p>        |<p align="center">4</p>       |
|      Spherical (S)      |                  3         |<p align="center">N/A</p>        |<p align="center">3</p>       |
##	IV. Kinematic Diagram and D-H Frame assignment of SCARA Manipulator 													
##	V. D-H Parametric Table of SCARA Manipulator														
##	VI. HTM of SCARA Manipulator													
##	VII. Inverse Kinematics of SCARA Manipulator													
##	VIII. Forward and Inverse Kinematics GUI calculator of SCARA Manipulator									
##	IX. References														
