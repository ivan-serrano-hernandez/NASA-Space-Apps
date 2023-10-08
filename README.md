# NASA-Space-Apps
**DELFOS**'s repository for Nasa Space Apps Challenge 2023 <br/>

Link web

imagen

## :scroll: Table of Contents
- [:question: What is our project](https://github.com/ivan-serrano-hernandez/NASA-Space-Apps/blob/main/README.md#hackupc2023)
- [:computer: Technology Used](https://github.com/ivan-serrano-hernandez/NASA-Space-Apps/blob/main/README.md#computer-Technology-Used)
- [🤗 MLheads 🤯](https://github.com/ivan-serrano-hernandez/NASA-Space-Apps#-mlheads-)

## :question: What is our project
### Abastract

The main objective of this project is the creation of a tool that facilitates decision-making related to the protection of space satellites. **Recurrent neural networks** have been implemented, whose output consists of future values of the geomagnetic activity *index Kp*. Through a rigorous treatment of input and output data, efficient and easy-to-understand graphical elements have been created in terms of this value.


### Introduction to the problem

Since the early launches of space satellites, the quality of life for people has increased exponentially. These devices have enabled the implementation of nearly instantaneous remote communication in everyday life. Multiple advancements have arisen as a direct consequence of this fact, such as wireless mobile phone networks, GPS satellite control that allows for flight synchronization of airplanes, improved cartography, the study of Earth's terrain, the detection and prevention of natural disasters, assistance in search and rescue operations, and more. However, despite being in space, where the environment can be modeled as a vacuum, satellites are not exempt from danger. Specifically, extreme solar winds and geomagnetic storms continuously affect the numerous satellites that humans have managed to put into orbit. Elon Musk has confirmed the loss of 40 out of 49 satellites (belonging to Starlink) due to geomagnetic storms. Due to the effort this process entails, both technically and economically, it is advisable to present methods for predicting and preventing storms. This idea forms the cornerstone of the project, in which machine learning technologies have been applied to design a predictive model for storms, aiming to facilitate preventive decision-making.


### Solving the problem

The **neural network model** has been trained with a dataset of 3 million data points. Since the percentage of missing values was very high, a meticulous treatment of these has been attempted. NaN imputation techniques such as KNN, data scaling, and dimensionality reduction through techniques like PCA have been implemented. Additionally, merges have been created to group the datasets according to the frequency of Kp data, once again adjusting the dimensionality of the values. Regarding the architecture of deep learning, the use of various models is proposed, taking into account different dimensionalities as well as layers of learning (LSTM, dense, and dropout layers have generally been used). The work was done in Python, with the assistance of libraries such as Keras, TensorFlow, NumPy, Pandas, Matplotlib, Scikit-Learn, etc.

## :computer: Technology Used
- Technologies: `Recurrent Neural Networks (*RNN*)`
- Datasets: [Geomagnetic Observatory Niemegk, GFZ German Research Centre for Geosciences](https://kp.gfz-potsdam.de/app/files/Kp_ap_since_1932.txt), [DSCOVR PlasMAG instrument suite](https://www.spaceappschallenge.org/develop-the-oracle-of-dscovr-experimental-data-repository/), [CARISMA Magnetometer Network](https://donnees-data.asc-csa.gc.ca/dataset/06f5e364-6e2c-4d1c-95c2-9fb7d871ca20)

## 🤗 DELFOs 🤯
- Iván Serrano Hernandez
- Lluís Llull Riera
- Lluc Campins Sastre
- Javier Lalueza Puertolas
