A system that automatically calculates the optimal angle of inclination by
incorporating real-time factors can significantly improve the accuracy and
reliability of artillery targeting. By using a Deep Neural Network (DNN) model
trained on a dataset tailored to these scenarios, we can create a predictive system
that reduces error margins, ensures safer operations, and enhances overall
mission success.
model used: DNN(Deep Neural Network)
Features used: Distance_to_Target_m,Initial_Velocity_m_s,Wind_Speed_m_s,Wind_Direction_deg,Firing_Angle_deg
considered system: M777 Howitzer
Dataset size: 50000 samples (synthetic dataset using python script)
predicted output: Firing_Angle_deg
Obtained accuracy: 96.65%
