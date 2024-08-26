![BRO](https://github.com/RishiShah99/OceanTrack/blob/main/tn.png?raw=true)


## Inspiration 💡
The idea for **OceanTrack** began when we started thinking about the journey of plastic waste in our oceans. We wondered: what happens to these plastics once they’re dumped into the sea? How far do they travel, and can we predict where they will end up? With the devastating impact of plastic pollution on marine life and ecosystems, we realized that if we could pinpoint heavily concentrated plastic dumps, we might be able to target these areas for clean-up efforts and significantly reduce pollution. This curiosity and a strong desire to make a tangible difference inspired us to create OceanTrack, a tool to track and predict the path of ocean plastic waste.

## What it does 💻
OceanTrack is a powerful machine learning tool that predicts the movement of plastic waste in the ocean. By analyzing environmental data such as Sea Level Pressure and Sea Surface Temperature, OceanTrack forecasts the changes in longitude and latitude of plastic debris over time. This enables us to map out the future journey of plastic waste and identify areas where it is most likely to accumulate, allowing for targeted clean-up efforts and better resource allocation to combat ocean pollution.

## How we built it 🛠️
To build **OceanTrack**, we started by sourcing a dataset that included crucial information such as longitude, latitude, Sea Surface Temperature (SST), and Sea Level Pressure (SLP). This data provided the foundation for our model by capturing the environmental conditions that affect plastic movement in the ocean. We experimented with various machine learning models to find the most effective approach for our needs. After thorough testing, we chose the LightGBM model due to its superior performance and ability to learn the correlation between SST, SLP, and the changes in latitude and longitude.

The development process involved several key steps:

- **Data Preparation**: We addressed the dataset’s quality issues by handling missing values and ensuring the data was clean and ready for modeling.
- **Model Selection**: Through experimentation, we determined that LightGBM was the most effective model for our application.
- **Hyperparameter Tuning**: We fine-tuned the hyperparameters of the LightGBM model to optimize its predictive performance.
- **Predictive Modeling**: Using the processed dataset, we trained the model to predict changes in longitude and latitude based on initial SST and SLP values.

## Challenges we ran into ❌
Throughout the development of OceanTrack, we encountered several challenges:

- **Identifying the Right Problem**: One of the initial hurdles was defining a clear and actionable problem that our model could solve.
- **Data Acquisition**: Finding a suitable dataset that accurately represented the oceanic conditions and plastic waste distribution was a significant challenge.
- **Model Optimization**: Ensuring the model performed well involved extensive testing and fine-tuning to handle the complex dynamics of ocean currents and environmental factors.

Despite these challenges, our team's perseverance and collaboration enabled us to develop a robust and effective tool for predicting the movement of plastic waste in the ocean.

## Accomplishments that we're proud of 🏆
We are incredibly proud of the accuracy and efficiency of OceanTrack. By leveraging the LightGBM model, we were able to develop a predictive tool that not only provides valuable insights into the journey of ocean plastics but also contributes to the larger fight against ocean pollution. We’re proud of how our diverse skill set came together to tackle a complex problem and build a tool that can make a real-world impact.

## What we learned 📝
Throughout this project, we learned a great deal about the complexities of oceanography and the various factors that contribute to plastic waste movement. We deepened our understanding of machine learning, particularly in selecting and fine-tuning models to optimize performance for specific applications. 

## What's next for OceanTrack 🚀
Looking ahead, we plan to enhance OceanTrack by incorporating more diverse datasets and improving its predictive capabilities. We aim to integrate real-time data feeds to provide up-to-date tracking of plastic waste. Additionally, we want to expand the model to predict the impact of seasonal changes and extreme weather events on plastic migration. Our ultimate goal is to make OceanTrack a comprehensive tool that can be used by environmental organizations and policymakers worldwide to effectively combat ocean plastic pollution.