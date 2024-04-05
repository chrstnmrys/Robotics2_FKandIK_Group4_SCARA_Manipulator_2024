#  <p align="center">**Robotics 2: Forward and Inverse Kinematics of a**</p>
# <p align="center">**SCARA Manipulator**</p>
##	I. Abstract of the Project						

<div align="justify">SCARA (Selective Compliance Assembly Robot Arm) Manipulators represent a significant advancement in robotics, offering versatility and precision in various industrial applications. Initially developed for assembly tasks, SCARA robots feature a horizontal arm structure with articulated joints, providing precise movement in the X, Y, and Z axes while exhibiting selective compliance.This project aimed to develop a GUI (Graphical User Interface) Calculator to streamline forward kinematics and inverse kinematics calculations. Integrating a GUI calculator improves the usability and accessibility of SCARA manipulators by giving operators intuitive control over the robot's movements. The GUI calculator allows for real-time input of desired end-effector positions and orientations, which simplifies the process of generating suitable joint configurations. Using the kinematic equations that govern SCARA manipulators, the calculator converts user inputs into appropriate joint angle values using inverse kinematics computations. The GUI interface ensures smooth communication with the SCARA manipulator by providing interactive features including input fields, sliders, and visual feedback.We examine the calculation of Degrees of Freedom, followed by the formulation of D-H parameters and the construction of the D-H parametric table to represent the robot's kinematic chain. Homogeneous transformation matrices serve an important role in describing the relationship between consecutive links, allowing for a smooth transition between frames. The inverse kinematics problem, which is vital in maintaining the end-effector position and orientation, is handled utilizing graphical approaches for SCARA manipulators.</div>


<div align="justify">Furthermore, advancements in sensor technology and control systems enhance their capabilities, enabling seamless integration into automated production lines. This abstract provides a comprehensive overview of SCARA manipulator kinematics and highlights the integration of computational tools for practical implementation in industrial automation.</div>

##  II. Introduction of the Project	
***<div align="justify"><i>SCARA (Selective Compliance Assembly Robot Arm) Manipulators</i>*** are an essential advancement in the world of robotics, distinguished by their distinctive design and varied functionality. SCARA robots were developed in the 1980s and have since become vital components in a variety of industrial and production environments, providing accurate control and economical operation. At its core, a SCARA manipulator comprises articulated arms capable of movement in the horizontal plane, with a vertical axis of rotation for assembly tasks. This distinctive configuration grants SCARA robots exceptional speed and accuracy, making them ideal for tasks such as assembly, pick-and-place operations, packaging, and more.</div>

<div align="justify">The four-axis configuration of SCARA robots allows them to move along the X, Y, and Z planes. It also provides them with 360 degrees of rotational movement around the Z axis which allows for a cylindrical work envelope. The axes of SCARA robots feature a combination of dynamic and rigid movements. The X and Y axes of SCARA’s are flexible allowing for dynamic movements. This is where the “Selective Compliance” comes from in their name. Compliance refers to flexibility, but not all axes are flexible, so it is selective. The Z axis is the rigid axis since it is fixed. The Selective Compliance feature of SCARA refers to the ability to maintain rigidity and precision during operations while also providing controlled compliance or flexibility to particular directions. This feature allows SCARA robots to adapt to different workpieces and surroundings, resulting in consistent performance across a wide range of applications.</div>

***<div align="justify">SCARA Manipulators*** are versatile beyond only their mechanical design. These robots, which have advanced control systems and programming interfaces, may easily be integrated into automated production lines and synced with other equipment, increasing productivity and efficiency.</div>

##  III. Degrees of Freedom of SCARA Manipulator 	

***<div align="justify">Degrees of Freedom*** is define as the minimum number of independent parameters/variables/coordinates needed to describe a system completely. Consider a robotic arm. Its degrees of freedom are determined by each joint, which allows it to move in any direction, turn, and bend. For example, a simple arm with an elbow and shoulder joint may have two degrees of freedom, one for the movement of each joint.</div>

<div align="justify">More generally, DoF is essential to comprehending the capabilities of a robot. A robot with more degrees of freedom can carry out more complex tasks and adjust to a larger variety of conditions. Higher DoF can, however, also lead to more complex programming since they usually call for more advanced control systems. A key component of robotics design is balancing the number of degrees of freedom with the particular tasks a robot has to perform.</div>

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
   
| ***Planar Manipulator***     |
|-----------------------       |
|     ![Screenshot 2024-04-03 225206](https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/157685794/cb7808ee-a47d-4b59-b153-5fbb6376f385) |

</div>

<div align="center">
   
| ***Spatial Manipulator***    |
|--------------------------    |
|![Screenshot 2024-04-03 225248](https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/157685794/3f28d81a-8349-495a-a5f6-568c1845f007) |

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
   
|      ***COMPUTATION***     |
| ----------------------- |
|![Screenshot 2024-04-03 214722](https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/157685794/c4d38b69-7bb5-43e7-8b7b-d7dc2b0a67f3)  
***<div align="center">Therefore, this is an Under-Actuated Spatial Manipulator with 3-DoF.</div>***

</div>

##	IV. Kinematic Diagram and D-H Frame assignment of SCARA Manipulator 

***<div align="justify"> Kinematics*** the science of motion that treats the subject without regard to the forces that cause it. It includes the geometry, arrangement, and relative motion of the parts that make up a robot's mechanism. Understanding and managing the motion of manipulators, mobile robots, robotic arms, and other robotic systems requires an extensive knowledge of kinematics.</div>

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
In 1955, Jacques Denavit and Richard Hartenberg introduced this convention in order to standardize the coordinate frames for spatial linkages.   ***D-H Notation*** use to solve the forward kinematics of a mechanical manipulator. 

***<div align="justify">Denavit***, a French engineer, and ***Hartenberg***, a German-born Canadian engineer, collaborated on developing a systematic 
method to describe the geometry and kinematics of robotic manipulators. Their work was motivated by the increasing interest in using robots for various industrial applications, particularly in manufacturing. The development of DH notation was a significant advancement in the field of robotics because it provided a unified framework for describing the motion of robotic manipulators, regardless of their specific configuration or number of degrees of freedom. This notation simplified the analysis and control of robotic systems and became widely adopted in both academia and industry.</div>

***Frames***
\
In a mechanical manipulator a coordinate system that the manipulator uses to know where it is and where to go. 

**Three types of Frames**
+ Base (world) Frame
+ User Frame
+ Tool Frame

***D-H Frame Rules*** use to assign frames in a kinematic diagram for applying D-H Notation. These rules help to establish a standardized framework for describing the geometry and kinematics of the manipulator. Here are the D-H frame rules:

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

***<div align="justify">The Denavit-Hartenberg (D-H) Parameter Table*** is a systematic way to organize the D-H parameters for each joint of a robotic manipulator. It helps to define the geometric and kinematic relationships between adjacent links and joints in the manipulator. The D-H parameter table typically consists of rows corresponding to each joint, with columns representing the D-H parameters: θ, α, d, and r.</div>

**Denavit-Hartenberg Notation**

**Denavit-Hartenberg Table**

   
|  ***n***  |  ***θ***  |  ***α***  |  ***d***  |  ***r***  |       
| ----------| ----------|-----------|-----------|-----------|
|   1       |           |           |           |           |
|   2       |           |           |           |           |
|   3       |           |           |           |           |
|   4       |           |           |           |           |


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
   
***θ*** 
Rotation around Zn-1, that is required to get Xn-1 to match Xn, with the joint variable θ if the joint is twisting/revolute joint. 

***α*** 
Rotation around Xn that is required to match Zn-1 to Zn.

***d*** 
The distance from the origin of n-1 and n, frames along the Zn-1 direction with joint variable (d) if joint is prismatic.

***d*** 
The distance from the origin of n-1 and n frames along the Xn direction.



<div align="center">
   
|      ***COMPUTATION***     |
| ----------------------- |
| ![Screenshot 2024-04-04 144101](https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/157685794/270a2967-26c4-4c62-9f83-d8f3753c09eb) |

</div>

##	VI. HTM of SCARA Manipulator			

***<div align="justify"> Homogeneous Transformation Matrices*** are fundamental concepts in robotics and computer graphics, particularly in the context of describing transformations in 3D space. These matrices are used to represent both rotation and translation transformations in a single, unified framework. In robotics, homogeneous transformation matrices are particularly important for representing the position and orientation of objects or coordinate frames relative to each other within a robotic system. They are commonly used to describe the pose of robot links or end-effectors with respect to a base coordinate frame.</div>

<div align="justify"> Homogeneous Transformation Matrix is a 4x4 matrix, consisting of a 3x3 rotation matrix combined with a 3x1 position vector along with an augmentation column, that describes the transformation of a manipulator in a coordinate system.</div>


##	VII. Inverse Kinematics of SCARA Manipulator	

***<div align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Kinematics*** the science of motion that treats the subject without regard to the forces that cause it. It includes the geometry, arrangement, and relative motion of the parts that make up a robot's mechanism. Understanding and managing the motion of manipulators, mobile robots, robotic arms, and other robotic systems requires an extensive knowledge of kinematics.</div>

***There are Two Main branches of Kinematics in Robotics***:

**<div align="justify">1. Forward Kinematics**: This branch deals with determining the position and orientation of the end-effector (the tool or device attached to the end of a robot arm) given the joint angles or lengths of the robot's links. In other words, it calculates the end position of the robot's tool given the joint configurations.</div>

**<div align="justify">2. Inverse Kinematics**: Inverse kinematics involves finding the joint angles or lengths required to position the end-effector at a desired location and orientation. It is essentially the reverse process of forward kinematics, where instead of finding the end position from joint configurations, it finds the joint configurations from the desired end position.</div>


***<div align="center">STEP-BY-STEP SOLUTION USING GRAPHICAL METHOD***</div>
<div align="center">
   
|      ***TOP VIEW***     |  ***EQUATIONS***     |
| ----------------------- | -------------------- |
|![Screenshot 2024-04-04 182149](https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/157685794/36e12b54-21c4-4045-91af-491d0e32d2eb) |![Screenshot 2024-04-04 182455](https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/157685794/41b5e677-7a5f-41a5-8c5c-b5c5bf5f437d) |

|      ***FRONT VIEW***     |  ***EQUATIONS***     |
| ----------------------- | -------------------- |
| ![Screenshot 2024-04-04 182212](https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/157685794/5863161c-b5c8-4646-8467-288d2dbcf091) |![Screenshot 2024-04-04 182957](https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/157685794/5253b075-29cc-4661-809f-8f9f428015ed) |

</div>

##	VIII. Forward and Inverse Kinematics GUI calculator of SCARA Manipulator									
##	IX. References												
https://robotsdoneright.com/Articles/what-is-a-scara-robot.html


