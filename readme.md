# LDCE Resume Builder Automation

## Introduction

This is a Python script created to automate the form filling of the [LDCE Resume Builder](https://resume-builder-v1-ldce.netlify.app/) in Chrome. It uses Selenium to automate the browser.

## How to Use

1. **Install ChromeDriver**

    First, if your chrome version is greater than 114 download ChromeDriver from [here](https://developer.chrome.com/docs/chromedriver/downloads), else download from [here](https://chromedriver.storage.googleapis.com/index.html).

    Extract the zip file.

    Add [path/to/your/chromedriver.exe]() in Environment Variables.

2. **Virtual Environment setup (Optional)**

    Create virtual environment:

    ```
    python -m venv venv
    ```

    Activate virtual environment (cmd)

    ```
    .\venv\Scripts\activate
    ```

3. **Install the dependencies**

    ```
    pip install -r r.txt
    ```

4. **Modify Data**

    Change the data in the `src/Data.py` file according to your requirements.

5. **Run the Script**

    Run the `src/App.py` file using the following Python command:

    ```bash
    python src/App.py
    ```
