# NIME Paper Search

A simple Python script to fetch the NIME conference proceedings metadata and search paper titles, abstracts, and keywords for user-defined terms. Matching papers are printed to the console and saved to a text file named after the keywords.

## Features

* Automatically discovers the latest CSV feed of NIME papers from the official GitHub Pages.
* Searches across **title**, **abstract**, and **keywords** fields.
* Generates DOI links (e.g., `https://doi.org/<DOI>`).
* Saves results to `<keyword1>_<keyword2>_... .txt`.

## Prerequisites

* **Python** 3.7 or higher
* **pip** (Python package installer)
* Internet connection (to fetch the CSV and landing page)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/<username>/NIME_Paper_Search.git
   cd NIME_Paper_Search
   ```

2. **(Optional) Create and activate a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate      # On macOS/Linux
   venv\Scripts\activate       # On Windows
   ```

3. **Install dependencies**:

   You can install directly:

   ```bash
   pip install requests beautifulsoup4
   ```

   Or using a `requirements.txt` file (create one with the following lines):

   ```txt
   requests>=2.25.1
   beautifulsoup4>=4.9.3
   ```

   Then:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Edit search keywords** in the script:

   Open `Paper_Search.py` and modify the `KEYWORDS` list at the top:

   ```python
   # Top of Paper_Search.py
   KEYWORDS = ["Ableton", "machine learning"]
   ```

2. **Run the script**:

   ```bash
   python Paper_Search.py
   ```

3. **View results**:

   * Matching papers will be printed in the terminal with their year, title, DOI link, and matched keyword.
   * A text file named after your keywords (e.g., `Ableton_machine_learning.txt`) will be created in the same directory, containing the same information.

## Example

```bash
$ python Paper_Search.py
Found 3 matching papers:

2022 — Automating Workflows in Ableton Live with MediaPipe Facial Controls
  DOI link: https://doi.org/10.5281/zenodo.1234567
  Matched on: Ableton

2021 — Gesture-Based Interaction in Live Coding Environments
  DOI link: https://doi.org/10.5281/zenodo.2345678
  Matched on: Ableton

2020 — Machine Learning Techniques for Audio Classification
  DOI link: https://doi.org/10.5281/zenodo.3456789
  Matched on: machine learning
```

## License

This project is released under the [MIT License](LICENSE). Feel free to use and modify as needed.
