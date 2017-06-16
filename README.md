# A UI based translation of the gas transfer models. 
# Synopsis 
The project is about mathematical and computational modelling of the respiratory tree with the main focus on asthma.

Asthma is a respiratory system disorder which involves the whole respiratory tract. It is a reversible disease however
poor management of it could cause permanent airway remodelling and subsequently several complications.
It is a heterogeneous disease in which poor patient stratification leads to grouping different types together.
Therefore, it is very likely that two patients with exactly the same symptoms respond differently to the same medication. 
In this project, I am coupling three different models such that they could interact in real time. 

The final goal of the project is to find a novel biomarkers which could tackle the current hassles in 
distinguishing between different types of Asthma. We believe that the novel biomarker is going to efficiently 
categorise different phenotypes of asthma and could act as the perfect replacement for the current inefficient gold standard.
Our main code is in Fortran language, however most of my post processing is carried out in other languages 
such as MATLAB and Python. Forexample, as part of the debugging and compilation tasks, 
I have created a c++ file which could scan through all the source codes and create a makefile automatically 
by ordering all the file names required for compilation.

Please refer to this [link](https://github.com/arcisad/Automake) for an example. 

My goal for this project is to translate as much of the code as I can from old Fortran to new programming languages (specifically python for this project) and create a user interface to achieve a template for a potential user-friendly standalone application. The application is most efficient if it's multiplatform.  

Flowchart [link](https://github.com/arcisad/dssr2017ABI-a.rastar/blob/master/Digital.png).
