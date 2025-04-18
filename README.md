# 📊 Ukrainian NPPs: Open Data Analysis 

This project explores open datasets on radioactive emissions and discharges from  
nuclear power plants (NPPs) in Ukraine. Using Python, Pandas, and Plotly, we  
analyze environmental indicators across several stations and visualize quarterly  
changes over time.

The goal is to better understand trends in emission levels and present the data  
in an accessible, interactive format. All data is retrieved from publicly  
available government sources.

🧪 **Technologies:** Python, Poetry, Pandas, Plotly, Jupyter Notebook, Pytest

📈 **Focus:** Data analysis, API integration, interactive visualizations 

📂 **Data Source:** [Open data portal][1]

📦 **Dataset Page:** [Ecological and radiation situation in the area of ​​nuclear power plants][2]

🔌 **API docs:** [How to retrieve a dataset (API)?][3]

[1]: https://data.gov.ua/en/

[2]: https://data.gov.ua/en/dataset/4a9d3d56-bd95-4c3e-97e7-1cdc7bcbd445/resource/d55eebcf-4660-4919-96b3-4894be5a6cda

[3]: https://data.gov.ua/pages/aboutuser2#:~:text=%D0%AF%D0%BA%C2%A0%D0%B7%D0%B0%D0%B1%D1%80%D0%B0%D1%82%D0%B8%20%D0%BD%D0%B0%D0%B1%D1%96%D1%80%20%D0%B4%D0%B0%D0%BD%D0%B8%D1%85%20(API)%3F

## 🔍 Key Features

🛰️ Fetch real-time datasets 

📥 Process Excel reports into structured DataFrames

📊 Build interactive, filterable visualizations (Plotly)

📈 Analyze radioactive emissions, discharges, and thresholds

🧩 Modular structure and reusable components

## 📈 Use Case

This notebook allows researchers and developers to explore environmental metrics  
such as:

* Inert radioactive gas emissions (IRG)

* Iodine radionuclides index

* Long-living isotopes

* Cs-137 and Co-60 emissions/discharges

* Quarterly and annual release indexes

## 🚀 Quickstart

Requires Poetry and Jupyter

```bash
# Clone the repo
git clone https://github.com/Asbuga/Ukrainian-NPPs.git
cd Ukrainian-NPPs

# Install dependencies and activate virtual environment
poetry install
poetry shell
```

## 🧠 Project Structure

```bash
.
├── src/                 
│   └── client.py       # API client module
├── notebooks/
│   └── analysis.ipynb  # Main notebook (interactive dashboard)
├── tests/              # Unit tests for modules
├── pyproject.toml      # Poetry config
└── README.md
```

# Run the notebook

```bash
jupyter notebook
```

## 🧪 Testing

```bash
poetry run pytest
```

## ⚠️ License & Data Usage

All datasets are sourced from data.gov.ua and distributed under the Creative  
Commons Attribution 4.0 License (CC BY 4.0).  
Make sure to attribute the original source if you reuse the data.  

## 👨‍💻 Author

Andrii Buha – Python Backend Developer | Django & FastAPI | Data Processing 

📬 [LinkedIn](https://www.linkedin.com/in/andrii-buha/)  
💻 [GitHub](https://github.com/Asbuga)  
