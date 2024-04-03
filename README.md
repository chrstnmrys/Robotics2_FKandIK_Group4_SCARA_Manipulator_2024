#  <p align="center">**Robotics 2: Forward and Inverse Kinematics of a**</p>
# <p align="center">**SCARA Manipulator**</p>
##	I. Abstract of the Project														
##  II. Introduction of the Project	
***<div align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>SCARA (Selective Compliance Assembly Robot Arm) Manipulators</i>*** are an essential advancement in the world of robotics, distinguished by their distinctive design and varied functionality. SCARA robots were developed in the 1980s and have since become vital components in a variety of industrial and production environments, providing accurate control and economical operation. At its core, a SCARA manipulator comprises articulated arms capable of movement in the horizontal plane, with a vertical axis of rotation for assembly tasks. This distinctive configuration grants SCARA robots exceptional speed and accuracy, making them ideal for tasks such as assembly, pick-and-place operations, packaging, and more.</div>

<div align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The four-axis configuration of SCARA robots allows them to move along the X, Y, and Z planes. It also provides them with 360 degrees of rotational movement around the Z axis which allows for a cylindrical work envelope. The axes of SCARA robots feature a combination of dynamic and rigid movements. The X and Y axes of SCARA’s are flexible allowing for dynamic movements. This is where the “Selective Compliance” comes from in their name. Compliance refers to flexibility, but not all axes are flexible, so it is selective. The Z axis is the rigid axis since it is fixed. The Selective Compliance feature of SCARA refers to the ability to maintain rigidity and precision during operations while also providing controlled compliance or flexibility to particular directions. This feature allows SCARA robots to adapt to different workpieces and surroundings, resulting in consistent performance across a wide range of applications.</div>

***<div align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; SCARA Manipulators*** are versatile beyond only their mechanical design. These robots, which have advanced control systems and programming interfaces, may easily be integrated into automated production lines and synced with other equipment, increasing productivity and efficiency.</div>

##  III. Degrees of Freedom of SCARA Manipulator 	

***<div align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Degrees of Freedom*** is define as the minimum number of independent parameters/variables/coordinates needed to describe a system completely. Consider a robotic arm. Its degrees of freedom are determined by each joint, which allows it to move in any direction, turn, and bend. For example, a simple arm with an elbow and shoulder joint may have two degrees of freedom, one for the movement of each joint.</div>

<div align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; More generally, DoF is essential to comprehending the capabilities of a robot. A robot with more degrees of freedom can carry out more complex tasks and adjust to a larger variety of conditions. Higher DoF can, however, also lead to more complex programming since they usually call for more advanced control systems. A key component of robotics design is balancing the number of degrees of freedom with the particular tasks a robot has to perform.</div>

\
\
**The following are the Ideal Degrees of Freedom**
   
+ A point in 2D: 2-DoF ; 3D: 3-DoF
+ A rigid body in 3D: 6-DoF
+ Planar Manipulator: 3-DoF
+ Spatial Manipulator: 6-DoF

\
**Three Types of Manipulator based on the number of Degrees of Freedom**
1. ***Under-Actuated Manipulator***
   - Either a spatial manipulator with less than 6-dof or a planar manipulator with less than 3-DoF.

2. ***Ideal Manipulator***
   - Either a spatial manipulator with exactly 6-dof or a planar manipulator with exactly 3-DoF.

3. ***Redundant Manipulator***
   - Either a spatial manipulator with more than 6-dof or a planar manipulator with more than 3-DoF.
  
***Note:*** If the DOF of a manipulator is more than the Ideal Manipulator or based on your computation it is a Redundant Manipulator it is called ***Mobility***. 


***<div align="center">Grubler's Criterion for Mobility***</div>
<div align="center">
   
| ***Planar Manipulator***     | ***Spatial Manipulator***    |
|-----------------------       |--------------------------    |
|          ![Screenshot 2024-04-03 213346](https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/157685794/5f6fe03a-8da4-4929-ac3b-a4b415ec1c25) | ![Screenshot 2024-04-03 213815](https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/157685794/9bd2ba64-d4b3-4b3a-ab0f-ef4dbf30edbe)  |


</div>

***<p align="center">Mechanical Manipulator Anatomy***</p>
<div align="center">
   
| ***Joint Type*** | ***DoF *f****|***Constraints c between two planar rigid <p align="center">bodies</p>***|***Constraints c between two spatailrigid <p align="center">bodies</p>***| 
| ------------------------| ------------------------   | ------------------------ | ------------------------ | 
|      Revolute (R)       | <p align="center">1</p>    |<p align="center">2</p>   |<p align="center">5</p>       |
|      Prismatic(P)       | <p align="center">1</p>    |<p align="center">2</p>   |<p align="center">5</p>       |
|      Helical (H)        | <p align="center">1</p>    |<p align="center">N/A</p> |<p align="center">5</p>       |
|      Cylindrical(c)     | <p align="center">2</p>    |<p align="center">N/A</p> |<p align="center">4</p>       |
|      Universal (U)      | <p align="center">2</p>    |<p align="center">N/A</p> |<p align="center">4</p>       |
|      Spherical (S)      | <p align="center">3</p>    |<p align="center">N/A</p> |<p align="center">3</p>       |

</div>

\
***<div align="center">STEP-BY-STEP COMPUTATION OF DEGREES OF FREEDOM (DoF)</div>***
<div align="center">
   
|      ***SOLUTION***     |
| ----------------------- |
|![Screenshot 2024-04-03 214722](https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/157685794/c4d38b69-7bb5-43e7-8b7b-d7dc2b0a67f3)  
***<div align="center">Therefore, this is an Under-Actuated Spatial Manipulator with 3-DoF.</div>***

</div>

##	IV. Kinematic Diagram and D-H Frame assignment of SCARA Manipulator 

***<div align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Kinematics*** the science of motion that treats the subject without regard to the forces that cause it. It includes the geometry, arrangement, and relative motion of the parts that make up a robot's mechanism. Understanding and managing the motion of manipulators, mobile robots, robotic arms, and other robotic systems requires an extensive knowledge of kinematics.</div>


<div align="center">
   
![Screenshot 2024-04-02 205748](https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/157685794/1b0ba79e-9911-4288-a779-0a653367c303)

</div>

\
***There are Two Main branches of Kinematics in Robotics***:

**<div align="justify">1. Forward Kinematics**: This branch deals with determining the position and orientation of the end-effector (the tool or device attached to the end of a robot arm) given the joint angles or lengths of the robot's links. In other words, it calculates the end position of the robot's tool given the joint configurations.</div>

**<div align="justify">2. Inverse Kinematics**: Inverse kinematics involves finding the joint angles or lengths required to position the end-effector at a desired location and orientation. It is essentially the reverse process of forward kinematics, where instead of finding the end position from joint configurations, it finds the joint configurations from the desired end position.</div>

***Kinematic Diagram*** is a diagram that shows how the links and joints are connected together when all of the joint variables have a value of zero.

***<div align="center">Joint Diagrams***</div>
<div align="center">
   
| ***Twisting/Revolute Joints***  |      ***Prismatic Linear/ Orthogonal Joints***    |
| ----------------------------    | ------------------------------------------------  |
|![Screenshot 2024-04-02 212344](https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/157685794/d42a9412-3313-4096-81ad-25342310c0cb) | ![Screenshot 2024-04-02 212412](https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/157685794/27feb30f-2dc5-4933-a7cb-3e5eae85bf54)

</div>

***Links*** θ, are the rigid parts of the mechanical manipulator, joints are also considered links and the values are constant.

- If revolute/twisting, links are drawn from the center of rotation.
- If prismatic either linear orthogonal, links are drawn from center of translation.
- If from base, links are drawn from center of gravity.

<div align="center">
   
![Screenshot 2024-04-02 080223](https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/157685794/5b674c17-e1cc-4ddd-8c10-b474bf63451c)

</div>


\
***<div align="center"> Joint Variables***</div>

<div align="center"> These are the values that change when the joints moves.</div>
<div align="center">
  
|                         | ***θn***                   |      ***dn***            |
|-------------------------| ---------------------------| -----------------------  |
|    Unit                 |  Degrees/Radian            |   m, mm, cm, in, etc.    |
|    Indicator            |  CounterClockwise(+)       |  displacement(d), always positive |
|    Joint                |  Twisting/Revolute Joints  |  Prismatic Joints        |

</div>

\
**DENAVIT-HARTENBERG NOTATION**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; In 1955, Jacques Denavit and Richard Hartenberg introduced this convention in order to standardize the coordinate frames for spatial linkages.   ***D-H Notation*** use to solve the forward kinematics of a mechanical manipulator. 

***<div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Denavit***, a French engineer, and ***Hartenberg***, a German-born Canadian engineer, collaborated on developing a systematic 
method to describe the geometry and kinematics of robotic manipulators. Their work was motivated by the increasing interest in using robots for various industrial applications, particularly in manufacturing. The development of DH notation was a significant advancement in the field of robotics because it provided a unified framework for describing the motion of robotic manipulators, regardless of their specific configuration or number of degrees of freedom. This notation simplified the analysis and control of robotic systems and became widely adopted in both academia and industry.</div>

***Frames***
\
In a mechanical manipulator a coordinate system that the manipulator uses to know where it is and where to go. 

**Three types of Frames**
+ Base (world) Frame
+ User Frame
+ Tool Frame

***&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; D-H Frame Rules*** use to assign frames in a kinematic diagram for applying D-H Notation. These rules help to establish a standardized framework for describing the geometry and kinematics of the manipulator. Here are the D-H frame rules:

**D-H Frame Rules**

Rule 1: The Z axis must be the axis of rotation for the revolute/twisting, on the direction of translation for a prismatic joint.
\
\
Rule 2: The X axis must be perpendicular both it’s own Z axis, and the Z axis of the frame before it.
\
\
Rule 3: Each X axis must intersect the Z axis of the frame before it.
+ Rules for complying Rule 3:
  + Rotate the axis until it hits the other
  + Translate the axis until it hits the other

Rule 4: All frames must follow the right hand rule, used to draw Y axis.

**<div align="center">Applying D-H Frame Rules**</div>
<div align="center">
   
| ***SCARA MANIPULATOR***         |   
| ----------------------------    | 
|![Screenshot 2024-04-01 223347](https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/157685794/7607a58e-c2eb-46ab-abe6-7efd68b1ab7a) |

</div>

##	V. D-H Parametric Table of SCARA Manipulator		

***<div align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The Denavit-Hartenberg (D-H) Parameter Table*** is a systematic way to organize the D-H parameters for each joint of a robotic manipulator. It helps to define the geometric and kinematic relationships between adjacent links and joints in the manipulator. The D-H parameter table typically consists of rows corresponding to each joint, with columns representing the D-H parameters: θ, α, d, and r.</div>

**Denavit-Hartenberg Notation**

Step 1: Assign frames according to the four D-H Frame Rules
\
Step 2: Fill out the D-H Parametric Table
\
Step 3: Plug the table into the Homogeneous Transformation Matrix form
\
Step 4: Multiply the matrices together

**<div align="center">Denavit-Hartenberg Table**</div>
<div align="center">
   
|  ***n***  |  ***θ***  |  ***α***  |  ***d***  |  ***r***  |       
| ----------| ----------|-----------|-----------|-----------|
|   1       |           |           |           |           |
|   2       |           |           |           |           |
|   3       |           |           |           |           |
|   4       |           |           |           |           |

</div>

***Notes:*** 
\
\
Columns = number of paramters
\
Rows = number of frames - 1

<div align="center">
   
| ***θ and α***  |      ***d and r***     |
| ---------------------------- | ----------------------- |
|  Rotational Parameters/ Orientation Parameters   |      Position Parameters/ Translation Parameters                   |
|  Unit: Radian/ Degree          |                     Unit: cm, mm, m, ft, in and etc.   |

</div>


***<div align="center">Denavit-Hartenberg Parameters***</div>
<div align="center">
   
|  ***θ***  |  ***α***  |  ***d***  |  ***r***  |
| ----------|-----------|-----------|-----------|
| Rotation around Zn-1, that is required to get Xn-1 to match Xn, with the joint variable θ if the joint is twisting/revolute joint. | Rotation around Xn that is required to match Zn-1 to Zn. | The distance from the origin of n-1 and n, frames along the Zn-1 direction with joint variable (d) if joint is prismatic. | The distance from the origin of n-1 and n frames along the Xn direction. |

</div>

##	VI. HTM of SCARA Manipulator													
##	VII. Inverse Kinematics of SCARA Manipulator													
##	VIII. Forward and Inverse Kinematics GUI calculator of SCARA Manipulator									
##	IX. References														
