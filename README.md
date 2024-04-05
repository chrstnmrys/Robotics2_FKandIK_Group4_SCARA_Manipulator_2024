#  <p align="center">**Robotics 2: Forward and Inverse Kinematics of a**</p>
# <p align="center">$${\color{red}**SCARA**}‎~~{\color{red}**Manipulator**}$$</p>

##	I. Abstract of the Proj‎ect						

*<div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SCARA (Selective Compliance Assembly Robot Arm) Manipulators* represent a significant advancement in robotics, offering versatility and precision in various industrial applications. Initially developed for assembly tasks, SCARA robots feature a horizontal arm structure with articulated joints, providing precise movement in the X, Y, and Z axes while exhibiting selective compliance.This project aimed to develop a GUI (Graphical User Interface) Calculator to streamline forward kinematics and inverse kinematics calculations. Integrating a GUI calculator improves the usability and accessibility of SCARA manipulators by giving operators intuitive control over the robot's movements. The GUI calculator allows for real-time input of desired end-effector positions and orientations, which simplifies the process of generating suitable joint configurations. Using the kinematic equations that govern SCARA manipulators, the calculator converts user inputs into appropriate joint angle values using inverse kinematics computations. The GUI interface ensures smooth communication with the SCARA manipulator by providing interactive features including input fields, sliders, and visual feedback.We examine the calculation of Degrees of Freedom, followed by the formulation of D-H parameters and the construction of the D-H parametric table to represent the robot's kinematic chain. Homogeneous transformation matrices serve an important role in describing the relationship between consecutive links, allowing for a smooth transition between frames. The inverse kinematics problem, which is vital in maintaining the end-effector position and orientation, is handled utilizing graphical approaches for SCARA manipulators. Furthermore, advancements in sensor technology and control systems enhance their capabilities, enabling seamless integration into automated production lines. This abstract provides a comprehensive overview of SCARA manipulator kinematics and highlights the integration of computational tools for practical implementation in industrial automation.</div>

##  II. Introduction of the Project	
*<div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SCARA (Selective Compliance Assembly Robot Arm) Manipulators* are an essential advancement in the world ofrobotics, distinguished by their distinctive design and varied functionality. SCARA robots were developed in the 1980s and have since become vital components in a variety of industrial and production environments, providing accurate control and economical operation. At its core, a SCARA manipulator comprises articulated arms capable of movement in the horizontal plane, with a vertical axis of rotation for assembly tasks. This distinctive configuration grants SCARA robots exceptional speed and accuracy, making them ideal for tasks such as assembly, pick-and-place operations, packaging, and more.</div>



<div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The four-axis configuration of SCARA robots allows them to move along the X, Y, and Z planes. It also provides them with 360 degrees of rotational movement around the Z axis which allows for a cylindrical work envelope. The axes of SCARA robots feature a combination of dynamic and rigid movements. The X and Y axes of SCARA’s are flexible allowing for dynamic movements. This is where the “Selective Compliance” comes from in their name. Compliance refers to flexibility, but not all axes are flexible, so it is selective. The Z axis is the rigid axis since it is fixed. The Selective Compliance feature of SCARA refers to the ability to maintain rigidity and precision during operations while also providing controlled compliance or flexibility to particular directions. This feature allows SCARA robots to adapt to different workpieces and surroundings, resulting in consistent performance across a wide range of applications.</div>
<div align="justify">SCARA Manipulators are versatile beyond only their mechanical design. These robots, which have advanced control systems and programming interfaces, may easily be integrated into automated production lines and synced with other equipment, increasing productivity and efficiency.</div>

##  III. Degrees of Freedom of SCARA Manipulator 	

*<div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Degrees of Freedom* is define as the minimum number of independent parameters/variables/coordinates needed to describe a system completely. Consider a robotic arm. Its degrees of freedom are determined by each joint, which allows it to move in any direction, turn, and bend. For example, a simple arm with an elbow and shoulder joint may have two degrees of freedom, one for the movement of each joint.</div>

<div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;More generally, DoF is essential to comprehending the capabilities of a robot. A robot with more degrees of freedom can carry out more complex tasks and adjust to a larger variety of conditions. Higher DoF can, however, also lead to more complex programming since they usually call for more advanced control systems. A key component of robotics design is balancing the number of degrees of freedom with the particular tasks a robot has to perform.</div>

\
**Three Types of Manipulator based on the number of Degrees of Freedom**
1. Under-Actuated Manipulator
   - Either a spatial manipulator with less than 6-dof or a planar manipulator with less than 3-DoF.

2. Ideal Manipulator
   - Either a spatial manipulator with exactly 6-dof or a planar manipulator with exactly 3-DoF.

3. Redundant Manipulator
   - Either a spatial manipulator with more than 6-dof or a planar manipulator with more than 3-DoF.

 > [!NOTE] 
 >If the DOF of a manipulator is more than the Ideal Manipulator or based on your computation it is a Redundant Manipulator it is called ***Mobility***. 


***<div align="center">Grubler's Criterion for Mobility***</div>
<div align="center">
   
| **Planar Manipulator**     |
|-----------------------       |
|     ![Screenshot 2024-04-03 225206](https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/157685794/cb7808ee-a47d-4b59-b153-5fbb6376f385) |

</div>

<div align="center">
   
| **Spatial Manipulator**    |
|--------------------------    |
|![Screenshot 2024-04-03 225248](https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/157685794/3f28d81a-8349-495a-a5f6-568c1845f007) |

</div>


***<div align="center">STEP-BY-STEP COMPUTATION OF DEGREES OF FREEDOM (DoF)</div>***
<div align="center">
   
|      ***COMPUTATION***     |
| ----------------------- |
|![Screenshot 2024-04-03 214722](https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/157685794/c4d38b69-7bb5-43e7-8b7b-d7dc2b0a67f3)  
***<div align="center">Therefore, this is an Under-Actuated Spatial Manipulator with 3-DoF.</div>***

</div>

##	IV. Kinematic Diagram and D-H Frame assignment of SCARA Manipulator 

*<div align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Kinematics* the science of motion that treats the subject without regard to the forces that cause it. It includes the geometry, arrangement, and relative motion of the parts that make up a robot's mechanism. Understanding and managing the motion of manipulators, mobile robots, robotic arms, and other robotic systems requires an extensive knowledge of kinematics.</div>

\
**There are Two Main branches of Kinematics in Robotics**:

**<div align="justify">1. Forward Kinematics**: This branch deals with determining the position and orientation of the end-effector (the tool or device attached to the end of a robot arm) given the joint angles or lengths of the robot's links. In other words, it calculates the end position of the robot's tool given the joint configurations.</div>

**<div align="justify">2. Inverse Kinematics**: Inverse kinematics involves finding the joint angles or lengths required to position the end-effector at a desired location and orientation. It is essentially the reverse process of forward kinematics, where instead of finding the end position from joint configurations, it finds the joint configurations from the desired end position.</div>

**Kinematic Diagram** is a diagram that shows how the links and joints are connected together when all of the joint variables have a value of zero.


Links, are the rigid parts of the mechanical manipulator, joints are also considered links and the values are constant.

- If revolute/twisting, links are drawn from the center of rotation.
- If prismatic either linear orthogonal, links are drawn from center of translation.
- If from base, links are drawn from center of gravity.


<div align="center"> Joint Variables</div>

<div align="center"> These are the values that change when the joints moves.</div>
<div align="center">
  
|                         | ***θn***                   |      ***dn***            |
|-------------------------| ---------------------------| -----------------------  |
|    Unit                 |  Degrees/Radian            |   m, mm, cm, in, etc.    |
|    Indicator            |  CounterClockwise(+)       |  displacement(d), always positive |
|    Joint                |  Twisting/Revolute Joints  |  Prismatic Joints        |

</div>


DENAVIT-HARTENBERG NOTATION


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In 1955, Jacques Denavit and Richard Hartenberg introduced this convention in order to standardize the coordinate frames for spatial linkages.   D-H Notationbuse to solve the forward kinematics of a mechanical manipulator. 

***<div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Denavit***, a French engineer, and ***Hartenberg***, a German-born Canadian engineer, collaborated on developing a systematic method to describe the geometry and kinematics of robotic manipulators. Their work was motivated by the increasing interest in using robots for various industrial applications, particularly in manufacturing. The development of DH notation was a significant advancement in the field of robotics because it provided a unified framework for describing the motion of robotic manipulators, regardless of their specific configuration or number of degrees of freedom. This notation simplified the analysis and control of robotic systems and became widely adopted in both academia and industry.</div>

Frames:
\
In a mechanical manipulator a coordinate system that the manipulator uses to know where it is and where to go. 

**Three types of Frames**
+ Base (world) Frame
+ User Frame
+ Tool Frame

D-H Frame Rules use to assign frames in a kinematic diagram for applying D-H Notation. These rules help to establish a standardized framework for describing the geometry and kinematics of the manipulator. Here are the D-H frame rules:

> [!IMPORTANT]
>**D-H Frame Rules**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Rule 1: The Z axis must be the axis of rotation for the revolute/twisting, on the direction of translation for a prismatic joint.
\
\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Rule 2: The X axis must be perpendicular both it’s own Z axis, and the Z axis of the frame before it.
\
\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Rule 3: Each X axis must intersect the Z axis of the frame before it.
\
\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Rules for complying Rule 3:
   + Rotate the axis until it hits the other
   + Translate the axis until it hits the other

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Rule 4: All frames must follow the right hand rule, used to draw Y axis.

**<div align="center">Applying D-H Frame Rules**</div>
<div align="center">
   
| ***SCARA MANIPULATOR***         |   
| ----------------------------    | 
|![Screenshot 2024-04-01 223347](https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/157685794/7607a58e-c2eb-46ab-abe6-7efd68b1ab7a) |

</div>

##	V. D-H Parametric Table of SCARA Manipulator		

<div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The Denavit-Hartenberg (D-H) Parameter Table is a systematic way to organize the D-H parameters for each joint of a robotic manipulator. It helps to define the geometric and kinematic relationships between adjacent links and joints in the manipulator. The D-H parameter table typically consists of rows corresponding to each joint, with columns representing the D-H parameters: θ, α, d, and r.</div>

**Denavit-Hartenberg Notation**

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

*<div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Homogeneous Transformation Matrices* are fundamental concepts in robotics and computer graphics, particularly in the context of describing transformations in 3D space. These matrices are used to represent both rotation and translation transformations in a single, unified framework. In robotics, homogeneous transformation matrices are particularly important for representing the position and orientation of objects or coordinate frames relative to each other within a robotic system. They are commonly used to describe the pose of robot links or end-effectors with respect to a base coordinate frame.</div>

<div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Homogeneous Transformation Matrix is a 4x4 matrix, consisting of a 3x3 rotation matrix combined with a 3x1 position vector along with an augmentation column, that describes the transformation of a manipulator in a coordinate system.</div>

<div align="center">
   
|      **ROTATION MATRICES OF SCARA MANIPULATOR**  |
| ----------------------- | 
| ![Screenshot 2024-04-05 152003](https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/157685794/82a31d92-7d2b-41e1-8153-db53d4ae8241) |

![434243129_764966829073591_8296782512713456778_n](https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/157685794/93f0b719-dcc7-40f6-afa6-a4d0c7ecba74)

</div>

<div align="center">
   
|      **POSITION VECTORS OF SCARA MANIPULATOR**    |
| ----------------------- | 
|![434199899_1578215076365522_3786866650023595446_n](https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/157685794/6a35193d-0c61-40b5-b3f7-9ff52cf83f70)|

![Screenshot 2024-04-05 152031](https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/157685794/e654c9d2-bcfa-470c-8cf3-302a3bdf6d52)

![Screenshot 2024-04-05 152108](https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/157685794/7a96ce74-c49f-4927-8544-61b848103f3e)

</div>


##	VII. Inverse Kinematics of SCARA Manipulator	

*<div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Kinematics* the science of motion that treats the subject without regard to the forces that cause it. It includes the geometry, arrangement, and relative motion of the parts that make up a robot's mechanism. Understanding and managing the motion of manipulators, mobile robots, robotic arms, and other robotic systems requires an extensive knowledge of kinematics.</div>

**There are Two Main branches of Kinematics in Robotics**:

**<div align="justify">1. Forward Kinematics**: This branch deals with determining the position and orientation of the end-effector (the tool or device attached to the end of a robot arm) given the joint angles or lengths of the robot's links. In other words, it calculates the end position of the robot's tool given the joint configurations.</div>

**<div align="justify">2. Inverse Kinematics**: Inverse kinematics involves finding the joint angles or lengths required to position the end-effector at a desired location and orientation. It is essentially the reverse process of forward kinematics, where instead of finding the end position from joint configurations, it finds the joint configurations from the desired end position.</div>


<div align="center">STEP-BY-STEP SOLUTION USING GRAPHICAL METHOD</div>
<div align="center">
   
|      TOP VIEW   |  FRONT VIEW     |
| ----------------------- | -------------------- |
|![Screenshot 2024-04-04 182149](https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/157685794/36e12b54-21c4-4045-91af-491d0e32d2eb) |![Screenshot 2024-04-04 182212](https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/157685794/5863161c-b5c8-4646-8467-288d2dbcf091) |

|      EQUATIONS    |
| ----------------------- | 
| ![Screenshot 2024-04-04 182455](https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/157685794/4086f258-8cc6-49dc-ad42-91d1c4b6bf43) |

 ![Screenshot 2024-04-04 182957](https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/157685794/5253b075-29cc-4661-809f-8f9f428015ed) 

 </div>

##	VIII. Forward and Inverse Kinematics GUI calculator of SCARA Manipulator	

<div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The development of a Graphical User Interface (GUI) calculator for the Forward Kinematics of a SCARA (Selective Compliance Assembly Robot Arm) Manipulator represents a significant stride in enhancing accessibility and usability in robotics. By leveraging programming languages such as Python and GUI frameworks like Tkinter, engineers and enthusiasts can now seamlessly interact with complex robotic systems,
understanding their spatial configurations with ease. </div>
<div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </div>
<p align="center">
   <img src = "https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/158394790/3ab5cf4b-78b0-43ba-8165-6d0e32a9bfa1)" />
</p>

<div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The GUI calculator fosters innovation and comes with a user-friendly interface
In essence, the Forward Kinematics GUI calculator for SCARA manipulators maximizes the fusion of technology and accessibility, empowering users to unravel the intricacies of robotic motion effortlessly. </div>

<div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </div>
<div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </div>

> In this GUI calculator, the students incorporate various functions:
1. **Forward Function**
   - <div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;Forward Button of the GUI calculator solves the Forward Kinematics of a SCARA Manipulator, as well as the Homogeneous Transformation Matrices, and shows a representation of the transformation of the robotic arm. </div>
<div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </div>
<p align="center">
<img src = "https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/158394790/76fbfcb9-0f24-40cb-b38f-b82e9ae826ee" />
</p>
<div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </div>

2. **Inverse Function**
   - <div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;Inverse Button of the GUI calculator solves the Inverse Kinematics of a SCARA Manipulator and shows a representation of the transformation of the robotic arm.</div>
<div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </div>
<p align="center">
<img src = "https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/158394790/f749af7e-a1f8-4ee5-af93-7bb16545ea70" />
</p>
<div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </div>

3. **Reset Function**
   - <div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;Reset Button of the GUI calculator resets the values processed in the calculator and deletes all of the entries.</div>
<div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </div>
<p align="center">
<img src = "https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/158394790/a1ab3488-1e09-4b4e-9c7b-65965a611de1" />
</p>
<div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </div>

4. **About SCARA Manipulator Function**
   - <div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;SCARA Manipulator Button of the GUI calculator ultimately transcends mere convenience; it presents a brief information about the SCARA Manipulator.</div>
 <div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </div>  
<p align="center">
<img src = "https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/158394790/d48af3b0-45ae-426b-9956-3058678c940a" />
</p>
<div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </div>

5. **Degrees of Freedom Function**
   - <div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;SCARA DOF Button of the GUI calculator presents the computation of the Degrees of Freedom of the SCARA Manipulator.</div>
<p align="center">
<img src = "https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/158394790/d2cd61b3-2de4-4652-9eaf-f81f394692f6" />
</p>
<div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </div>

6. **DH Assigned Frames Function**
   - <div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;DH Frames Button of the GUI calculator shows the assigned DH frames using the Kinematic Diagram of the SCARA MANIPULATOR.</div>
<p align="center">
<img src = "https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/158394790/36a62231-3b30-490e-a317-39465ef2b494" />
</p>
<div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </div>

7. **Parametric Table Function**
    - <div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;Parametric Table Button of the GUI calculator shows the organized parameters generated using the D-H frame assignment rules.</div>
<p align="center">
<img src = "https://github.com/chrstnmrys/Robotics2_FKandIK_Group4_SCARA_Manipulator_2024/assets/158394790/8fa62eac-5056-4423-be25-81a5c1e23ac9" />
</p>
<div align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </div>



## IX. Video Presentations

+ Degrees of Freedom of SCARA Manipulator
   - https://youtu.be/mOepO-KTVWM?si=8isQdyEZ3a9oyO8O
+ Kinematic Diagram and D-H Frame assignment of SCARA Manipulator 
   - https://youtu.be/TOnIAo2py4s?si=EEIDet8OALfZ9fKo
   - https://youtu.be/3qmJ3NAQ5-E?si=PFwaCPd2xF_aSlk-
+ D-H Parametric Table of SCARA Manipulator
   - https://youtu.be/dzJ9iJEPGoE?si=2KAdAG3UHAjDmigJ
+ HTM of SCARA Manipulator			
   - https://youtube.com/watch?v=7g6c-o29TvI
+ Inverse Kinematics of SCARA Manipulator
   - https://youtube.com/watch?v=mifuxa4e4-Y
##	X. References												
https://robotsdoneright.com/Articles/what-is-a-scara-robot.html


