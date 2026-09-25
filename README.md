# 📊 Automated Data Analyst

> **An AI-powered data analysis assistant that turns CSV and Excel datasets into meaningful insights using Python, Pandas, LangChain, and Groq.**

**Automated Data Analyst** is a Streamlit-based application that allows users to upload a dataset, automatically perform exploratory data analysis, and ask questions about the data using natural language.

Instead of manually inspecting rows, calculating statistics, checking missing values, and identifying relationships between columns, the application combines **Pandas-based data analysis with an LLM-powered analysis layer** to provide a simple conversational experience.

---

## 🌐 Live Demo: https://automated-data-analyst.onrender.com/

> **Note:** Since the application is hosted on Render's free tier, the first request may take 30–60 seconds while the server wakes up.

---
## 🚀 Features

### 📂 Dataset Upload

Upload your own datasets directly through the Streamlit interface.

Supported formats:

* `.csv`
* `.xlsx`

The application automatically loads the dataset using Pandas.

---

### 🔎 Automated Exploratory Data Analysis

Once a dataset is uploaded, the application automatically generates useful dataset information, including:

* Number of rows
* Number of columns
* Numerical columns
* Categorical columns
* Missing values
* Duplicate rows
* Descriptive statistics
* Correlation between numerical variables

This provides an immediate overview of the dataset before asking questions.

---

### 🤖 Natural Language Data Analysis

Users can ask questions about their dataset using normal language.

For example:

```text
What are the major patterns in this dataset?
```

```text
Which variables are strongly correlated?
```

```text
What problems do you see in this dataset?
```

The application sends the question together with the calculated EDA results to the LLM and generates a concise analytical response.

---

### 🧠 LLM-Powered Insights

The project uses **LangChain + Groq** to provide natural-language interpretation of the calculated statistics.

The LLM is instructed to:

* Use the provided EDA results
* Avoid inventing numbers
* Answer the user's question clearly
* Focus on the available dataset information

This separates the **numerical computation layer** from the **natural-language interpretation layer**.

---

### 📊 Interactive Streamlit Interface

The application provides a simple interface for:

1. Uploading a dataset
2. Previewing the data
3. Viewing dataset statistics
4. Exploring EDA results
5. Asking analytical questions
6. Receiving AI-generated insights

---

## 🏗️ Architecture

The application follows a simple and modular pipeline:

```text
              ┌──────────────────┐
              │   User Dataset   │
              │   CSV / XLSX     │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │   Streamlit UI   │
              │     app.py       │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │   Data Loading   │
              │  data_analysis.py│
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │   Basic EDA      │
              │                  │
              │ • Data Types     │
              │ • Missing Values │
              │ • Duplicates     │
              │ • Statistics     │
              │ • Correlation    │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │  User Question   │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ LangChain + Groq │
              │      LLM         │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ AI Analysis      │
              │ & Insights       │
              └──────────────────┘
```

### Design Principle

The project follows a simple principle:

> **Python calculates the data. The LLM explains the data.**

Pandas is responsible for numerical analysis and statistics, while the LLM is used for natural-language interpretation.

---

## 🛠️ Tech Stack

| Technology        | Purpose                                      |
| ----------------- | -------------------------------------------- |
| **Python**        | Core programming language                    |
| **Streamlit**     | Web application and UI                       |
| **Pandas**        | Data loading and analysis                    |
| **NumPy**         | Numerical operations                         |
| **LangChain**     | LLM integration                              |
| **Groq**          | LLM inference                                |
| **OpenPyXL**      | Excel file processing                        |
| **Plotly**        | Data visualization support                   |
| **python-dotenv** | Environment variable management              |
| **uv**            | Python dependency and environment management |

The project currently targets **Python 3.14+** and declares its dependencies in `pyproject.toml`.

---

## 📁 Project Structure

```text
Automated-Data-Analyst/
│
├── app.py                  # Streamlit application
│
├── data_analysis.py        # Data loading and EDA logic
│
├── llm.py                  # Groq LLM configuration and analysis
│
├── pyproject.toml          # Project configuration and dependencies
├── requirements.txt        # Python dependencies
├── uv.lock                 # Locked dependency versions
│
├── .python-version         # Python version configuration
├── .gitignore              # Ignored files
│
└── README.md               # Project documentation
```

### Core Components

#### `app.py`

Responsible for the application interface and workflow.

It handles:

* Streamlit configuration
* File upload
* Dataset preview
* Dataset metrics
* EDA display
* User questions
* LLM analysis
* Error handling

The current UI exposes metrics such as rows, columns, missing values, and duplicate records.

#### `data_analysis.py`

Contains the core data-analysis functionality.

Responsibilities include:

* Loading CSV/XLSX files
* Detecting numerical columns
* Detecting categorical columns
* Calculating missing values
* Detecting duplicate rows
* Generating descriptive statistics
* Calculating correlations

The EDA layer is implemented using Pandas and NumPy.

#### `llm.py`

Handles the LLM integration.

The application:

1. Loads the Groq API key from environment variables.
2. Creates a `ChatGroq` model through LangChain.
3. Receives the user's question.
4. Passes the EDA results to the LLM.
5. Generates the final analytical response.

The current implementation uses the `qwen/qwen3.8-27b` Groq model with deterministic temperature settings.

---

# ⚙️ Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/Swainakash0799/Automated-Data-Analyst.git

cd Automated-Data-Analyst
```

---

## 2. Create a Virtual Environment

### Using `uv`

```bash
uv venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Or on macOS/Linux:

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

Using `uv`:

```bash
uv sync
```

The repository also includes a `uv.lock` file for reproducible dependency management.

---

## 4. Configure the Groq API Key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

The application reads the API key using `python-dotenv`.

> ⚠️ Never commit your `.env` file or expose your API key publicly.

---

## 5. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 💡 Example Workflow

### Step 1 — Upload Data

Upload a CSV or Excel file.

Example:

```text
retail_customer_shopping_behaviour.csv
```

### Step 2 — Inspect the Dataset

The application displays:

```text
Rows
Columns
Missing Values
Duplicates
```

along with a dataset preview.

### Step 3 — Explore EDA

View:

* Numerical columns
* Categorical columns
* Missing values
* Descriptive statistics
* Correlation matrix

### Step 4 — Ask a Question

Example:

```text
What are the main patterns in this dataset?
```

### Step 5 — Get AI Analysis

The application combines the calculated EDA information with your question and generates an easy-to-understand response.

---

# 🔐 Environment Variables

The project currently requires:

| Variable       | Description                         |
| -------------- | ----------------------------------- |
| `GROQ_API_KEY` | API key used to access the Groq LLM |

Example:

```env
GROQ_API_KEY=xxxxxxxxxxxxxxxx
```

---

# 🎯 Example Questions

You can ask questions such as:

### Dataset Understanding

```text
What are the main characteristics of this dataset?
```

### Data Quality

```text
Are there any missing values or duplicate records?
```

### Relationships

```text
Which numerical variables appear to be correlated?
```

### Business Insights

```text
What are the most important patterns in this dataset?
```

### Data Problems

```text
What potential data quality issues should I investigate?
```

> The quality of the response depends on the information available in the generated EDA results.

---

# 🔄 How the Application Works

The complete workflow is:

```text
Upload Dataset
      ↓
Load CSV / Excel
      ↓
Inspect Dataset
      ↓
Identify Numerical & Categorical Columns
      ↓
Calculate Missing Values
      ↓
Detect Duplicates
      ↓
Generate Statistics
      ↓
Calculate Correlations
      ↓
User Asks Question
      ↓
EDA Results + Question
      ↓
Groq LLM
      ↓
Natural Language Analysis
```

This approach keeps data computation deterministic while using the LLM primarily for interpretation.

---

# 🧩 Key Implementation Concepts

### 1. Automated Data Profiling

The application automatically determines the basic structure of the uploaded dataset without requiring the user to manually specify column types.

### 2. Deterministic EDA

Core numerical calculations are performed using Pandas rather than relying on the LLM.

For example:

```python
df.describe()
```

and:

```python
df[numerical_columns].corr()
```

This helps keep numerical results grounded in the actual dataset.

### 3. LLM-Assisted Interpretation

The LLM receives the generated EDA information together with the user's question.

The prompt explicitly instructs the model:

```text
Use only the provided EDA results.
Do not invent numbers.
```

This reduces the risk of unsupported numerical claims.

---

# 📌 Current Scope

The current version focuses on:

* CSV/XLSX analysis
* Automated basic EDA
* Data-quality inspection
* Correlation analysis
* Natural-language questions
* LLM-generated explanations

It is intentionally kept lightweight and modular so additional analytical capabilities can be added later.

---

# 🚧 Future Improvements

Planned improvements could include:

* [x] Automated data cleaning
* [ ] Interactive Plotly dashboards
* [ ] KPI generation
* [ ] Advanced visualizations
* [ ] Natural-language chart generation
* [ ] Statistical hypothesis testing
* [x] Outlier detection
* [ ] Time-series analysis
* [ ] Forecasting
* [ ] Automated business reports
* [x] Downloadable analysis reports
* [ ] Conversation history
* [ ] Multiple LLM provider support
* [ ] Better prompt grounding
* [x] Dataset-aware question answering
* [ ] Production deployment
* [x] Automated testing and CI/CD

---

# 🎓 What This Project Demonstrates

This project demonstrates practical experience with:

* **Python development**
* **Data analysis with Pandas**
* **Exploratory Data Analysis**
* **Data preprocessing**
* **Data-quality analysis**
* **Natural Language Processing**
* **LLM integration**
* **LangChain**
* **Groq API**
* **Prompt engineering**
* **Streamlit application development**
* **Environment and dependency management**

---

# 📈 Why This Project?

Traditional data analysis often requires users to:

```text
Load Data
   ↓
Inspect Data
   ↓
Clean Data
   ↓
Calculate Statistics
   ↓
Create Analysis
   ↓
Interpret Results
```

Automated Data Analyst simplifies this workflow by providing a conversational interface on top of the analytical pipeline:

```text
Upload Data
      ↓
Automatic EDA
      ↓
Ask a Question
      ↓
AI-Assisted Analysis
```

The goal is not to replace the underlying data-analysis process, but to make it **faster and easier to interact with**.

---

# 🤝 Contributing

Contributions and suggestions are welcome.

If you would like to improve the project:

```bash
git clone https://github.com/Swainakash0799/Automated-Data-Analyst.git
cd Automated-Data-Analyst
```

Create a feature branch:

```bash
git checkout -b feature/your-feature
```

Make your changes, test them locally, and open a pull request.

---

# 👨‍💻 Author

**Akash Swain**

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
