## Inspiration
The idea for **OceanTrack** began when we started thinking about the journey of plastic waste in our oceans. We wondered: what happens to these plastics once they’re dumped into the sea? How far do they travel, and can we predict where they will end up? With the devastating impact of plastic pollution on marine life and ecosystems, we realized that if we could pinpoint heavily concentrated plastic dumps, we might be able to target these areas for clean-up efforts and significantly reduce pollution. This curiosity and a strong desire to make a tangible difference inspired us to create OceanTrack, a tool to track and predict the path of ocean plastic waste.

## What it does
OceanTrack is a powerful machine learning tool that predicts the movement of plastic waste in the ocean. By analyzing environmental data such as Sea Level Pressure and Sea Surface Temperature, OceanTrack forecasts the changes in longitude and latitude of plastic debris over time. This enables us to map out the future journey of plastic waste and identify areas where it is most likely to accumulate, allowing for targeted clean-up efforts and better resource allocation to combat ocean pollution.

## How we built it
- Found a dataset that contained info regarding longtitude and latitude and SST and SLP
- Created a lightGBM model 
- After trying out multiple models, lightgbm was best
- It learns the correlation between SST and SLP with the change in Latitude and Longitude 
- Fine tuning the hyperparameters, we trained the model
- The dataset found was not in the built in the best quality, we had to handle missing values with the dataset
- Using the previous longitude and latitude, you can predict the change in the longitude and latitude overtime with the initial SST and SLP values. 

## Challenges we ran into
- Finding the right problem for the model
- Finding the right dataset
- Optimizing the model
One of the biggest challenges we faced was dealing with the complexity of ocean currents and environmental factors that affect the movement of plastic waste. The ocean is a dynamic environment, with countless variables influencing how and where plastics travel. Another challenge was finding the right dataset that accurately reflected these conditions. We also had to fine-tune our model extensively to ensure it could handle the nuances of different oceanographic data while still providing reliable predictions.

## Accomplishments that we're proud of
We are incredibly proud of the accuracy and efficiency of OceanTrack. By leveraging the LightGBM model, we were able to develop a predictive tool that not only provides valuable insights into the journey of ocean plastics but also contributes to the larger fight against ocean pollution. We’re proud of how our diverse skill set came together to tackle a complex problem and build a tool that can make a real-world impact.

## What we learned
Throughout this project, we learned a great deal about the complexities of oceanography and the various factors that contribute to plastic waste movement. We deepened our understanding of machine learning, particularly in selecting and fine-tuning models to optimize performance for specific applications. 

## What's next for OceanTrack: Predictive Modeling for Plastic Waste Migration
Looking ahead, we plan to enhance OceanTrack by incorporating more diverse datasets and improving its predictive capabilities. We aim to integrate real-time data feeds to provide up-to-date tracking of plastic waste. Additionally, we want to expand the model to predict the impact of seasonal changes and extreme weather events on plastic migration. Our ultimate goal is to make OceanTrack a comprehensive tool that can be used by environmental organizations and policymakers worldwide to effectively combat ocean plastic pollution.
