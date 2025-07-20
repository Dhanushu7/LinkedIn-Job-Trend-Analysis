# LinkedIn Job Trend Analysis (Using Indeed for Educational Purposes)

---

## Project Overview

This project scrapes job postings from **Indeed.com** to analyze skill demand trends across cities and roles (since scraping LinkedIn directly is legally restricted). It then:
- Generates **Trend Analysis Visuals** (Top 10 Skills Chart).
- Creates a **Skill vs Role Matrix**.
- Provides **Job Demand Recommendations** based on real-time data.

---

## Tools Used

- Python 3.x
- Libraries:
  - `requests`
  - `beautifulsoup4`
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `openpyxl`

---

## Project Structure

| Folder/File                     | Description                                      |
|---------------------------------|--------------------------------------------------|
| `job_trend_analysis.py`         | Full project script (scraping, analysis, output) |
| `datasets/raw_jobs.csv`         | Raw scraped job postings                         |
| `outputs/cleaned_jobs.xlsx`     | Cleaned job data                                 |
| `outputs/skill_vs_role_matrix.xlsx` | Skill vs Role Matrix Excel report             |
| `outputs/skill_demand_chart.png` | Bar chart showing Top 10 skills                  |
| `outputs/job_recommendations.txt` | Suggested skills & locations for job seekers   |

---

## How to Run

1. **Install Python packages:**

```bash
pip install requests beautifulsoup4 pandas matplotlib seaborn openpyxl
```

2. **Run the project:**

```bash
python job_trend_analysis.py
```

3. **View Outputs:**
- Check `datasets/` and `outputs/` folders for:
   - Excel reports
   - Bar chart image
   - Job recommendations text file

---

## Deliverables Generated

-  **Trend Analysis Visuals:**  
  `outputs/skill_demand_chart.png`

-  **Skill vs Role Matrix:**  
  `outputs/skill_vs_role_matrix.xlsx`

-  **Job Demand Recommendations:**  
  `outputs/job_recommendations.txt`

---

## Notes

- This project scrapes **Indeed.com** public postings only, for **educational purposes**.
- For real projects, use the **LinkedIn API** (requires approval).
- Skills are extracted from job titles using basic keyword extraction (no advanced NLP).

---

## Contact

For project discussions or help, reach out to:

**Dhanushu V**  
Email: dhanushu77@gmail.com

---

**Disclaimer:**  
This project is for educational and personal portfolio use only. Data usage respects public website policies.
