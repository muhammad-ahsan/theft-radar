# Bike Theft Radar

Welcome to Bike Theft Radar, a radar application to visualize bike theft trends.

## Overview

Bike theft is a common issue in urban areas, and understanding its trends can help cyclists and authorities take preventive measures. Bike Theft Radar provides a user-friendly interface to explore bike theft data. The application visualizes the locations of reported bike theft incidents, helping users identify high-risk areas and trends over time.

## Features

- Interactive map visualization of bike theft incidents
- Insightful analysis of theft trends by neighborhood.
- Data sourced from the regional government website [www.govdata.de](https://www.govdata.de).

## Usage

To access the application, simply click on the following link: [Bike Theft Radar](https://theft-radar.streamlit.app/)

### Note

- Exact geo-locations of theft incidents might be error-prone due to various factors.
- However, neighborhood-level trends remain robust and can provide valuable insights.

## How to Build Docker

``` 
docker build -t theft-radar .
```

## Run Docker
```
docker run -p 8000:8000 theft-radar
```
## Feedback and Contribution

Your feedback is valuable in improving Bike Theft Radar. If you encounter any issues, have suggestions for improvement, or would like to contribute to the project, please feel free to reach out.

## Contact

For inquiries or support, please contact us at [muhammad.ahsan@gmail.com](mailto:muhammad.ahsan@gmail.com).







