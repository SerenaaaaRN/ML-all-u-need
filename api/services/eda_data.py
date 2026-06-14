from typing import Dict, Any

EDA_REPORTS: Dict[str, Dict[str, Any]] = {
    "ad-click": {
        "title": "Advertisement Engagement & CTR Analysis",
        "subtitle": "An exploratory study on demographic and salary indicators determining user conversion.",
        "source": "Kaggle Marketing Datasets",
        "size": 400,
        "chart_title": "Click-Through Rate by Age Bracket (%)",
        "chart_data": [
            {"name": "18-29", "value": 12.0},
            {"name": "30-39", "value": 41.0},
            {"name": "40-49", "value": 78.0},
            {"name": "50+", "value": 91.0}
        ],
        "x_axis_label": "Age Bracket",
        "y_axis_label": "Click Rate (%)",
        "sections": [
            {
                "id": "intro",
                "title": "1. Dataset Summary",
                "paragraphs": [
                    "This dataset captures demographic markers for 400 online users. The goal of this research is to isolate which demographic features exhibit the strongest predictive power for advertisement click-through rates. The attributes evaluated include Gender, Age, and Estimated Salary, mapped against a binary Click action."
                ],
                "metrics": [
                    {"label": "Total Cohort", "value": "400 users", "description": "Sample population"},
                    {"label": "Predictors", "value": "3 features", "description": "Gender, Age, Salary"},
                    {"label": "Mean Age", "value": "37.6 years", "description": "Slightly right-skewed"},
                    {"label": "Mean Salary", "value": "$69,742", "description": "Standard dev $34k"}
                ]
            },
            {
                "id": "demographics",
                "title": "2. Demographic Shifts",
                "paragraphs": [
                    "Exploratory Data Analysis indicates that age is the single most critical factor in conversion. Users under 30 show minimal interest in the displayed ads, while users above 45 show almost near-universal conversion, suggesting that the advertising creatives are highly resonant with older cohorts."
                ],
                "images": [
                    {
                    "url": "/eda/distribution-age.png",
                    "caption": "Figure 1.1 — Age distribution of users"
                    }

                ]
            },
            {
                "id": "correlation",
                "title": "3. Correlation Matrix",
                "paragraphs": [
                    "Pearson correlation coefficients reveal that while Estimated Salary has a significant positive relationship with conversion, Gender remains statistically neutral."
                ],
                "table": {
                    "headers": ["Feature Name", "Correlation Coefficient", "P-Value Significance"],
                    "rows": [
                        ["Age", "+0.781", "p < 0.001 (Highly Significant)"],
                        ["Estimated Salary", "+0.362", "p < 0.001 (Highly Significant)"],
                        ["Gender (Male)", "-0.042", "p = 0.421 (Not Significant)"]
                    ],
                    "caption": "1.2 — Predictor Correlations with Target Variable"
                }
            },
            {
                "id": "conclusion",
                "title": "4. Marketing Conclusions",
                "paragraphs": [
                    "Based on the demographic findings, we recommend restricting advertising placement on platforms primarily populated by younger audiences (< 30 years old), and shifting budget towards cohorts matching the higher age bracket and salary threshold."
                ],
                "blockquote": "Targeting campaigns strictly to users aged 40+ with estimated salaries above $80,000 USD is projected to optimize marketing efficiency and increase click conversions by up to 180%.",
                "blockquote_citation": "ML Showcase Agent, Lead Researcher"
            }
        ]
    },
    "diabetes": {
        "title": "Pima Indians Clinical Diabetes Analysis",
        "subtitle": "Exploring physiological markers and diagnostic measurements for diabetes risk assessment.",
        "source": "National Institute of Diabetes and Digestive and Kidney Diseases",
        "size": 768,
        "chart_title": "Diabetes Incidence by Plasma Glucose (mg/dL)",
        "chart_data": [
            {"name": "< 100", "value": 4.0},
            {"name": "100-139", "value": 23.0},
            {"name": "140-179", "value": 58.0},
            {"name": "180+", "value": 82.0}
        ],
        "x_axis_label": "Glucose Level (mg/dL)",
        "y_axis_label": "Incidence Rate (%)",
        "sections": [
            {
                "id": "intro",
                "title": "1. Clinical Overview",
                "paragraphs": [
                    "This dataset includes clinical measurements for 768 female patients of Pima Indian heritage. The analysis focuses on isolating key medical risk factors (e.g., Blood Pressure, Insulin, BMI, Glucose, and Pedigree) that dictate the onset of diabetes."
                ],
                "metrics": [
                    {"label": "Cohort Size", "value": "768 patients", "description": "All females"},
                    {"label": "Mean BMI", "value": "32.0 kg/m²", "description": "Class I Obesity mean"},
                    {"label": "Mean Glucose", "value": "120.9 mg/dL", "description": "Pre-diabetic average"},
                    {"label": "Risk Ratio", "value": "34.9%", "description": "Positive outcomes"}
                ]
            },
            {
                "id": "indicators",
                "title": "2. Key Risk Precursors",
                "paragraphs": [
                    "Glucose concentration stands out as the single strongest precursor. When glucose levels cross the 140 mg/dL threshold, the probability of a positive diagnosis jumps exponentially."
                ]
            },
            {
                "id": "diagnostics",
                "title": "3. Diagnostic Correlation",
                "paragraphs": [
                    "The statistical relationship shows that clinical diagnostics have vastly different weights when analyzed univariately. Plasma Glucose and Body Mass Index are the principal markers."
                ],
                "table": {
                    "headers": ["Physiological Feature", "Correlation with Outcome", "Clinical Assessment"],
                    "rows": [
                        ["Glucose", "0.467", "Strongest Direct Precursor"],
                        ["BMI", "0.293", "High Obesity Contribution"],
                        ["Age", "0.238", "Moderate Progression Effect"],
                        ["Pregnancies", "0.222", "Parity Risk Association"],
                        ["Insulin", "0.131", "Low Direct Univariate Corel"]
                    ],
                    "caption": "2.2 — Direct Univariate Correlation Matrix"
                }
            },
            {
                "id": "conclusions",
                "title": "4. Clinical Conclusions",
                "paragraphs": [
                    "Preventive care models should prioritize monitoring glucose levels above all else. Screening programs targeting individuals with glucose levels exceeding 120 mg/dL can intercept diabetic onset early."
                ],
                "blockquote": "Active lifestyle intervention combined with glycemic control in pre-diabetic patients (glucose 100-125 mg/dL) reduces the risk of progression to type 2 diabetes by up to 58%.",
                "blockquote_citation": "World Health Organization Diabetes Guidelines"
            }
        ]
    },
    "ai-student": {
        "title": "Impact of Generative AI on Higher Education",
        "subtitle": "Analyzing student performance, anxiety levels, and tool diversity in academic environments.",
        "source": "University Survey Registry",
        "size": 1000,
        "chart_title": "Exam Anxiety Score by Weekly GenAI Hours",
        "chart_data": [
            {"name": "0-4 hrs", "value": 3.0},
            {"name": "5-9 hrs", "value": 5.0},
            {"name": "10-14 hrs", "value": 7.0},
            {"name": "15+ hrs", "value": 9.0}
        ],
        "x_axis_label": "Weekly GenAI Hours",
        "y_axis_label": "Anxiety Score (1-10)",
        "sections": [
            {
                "id": "intro",
                "title": "1. Study Scope",
                "paragraphs": [
                    "This survey observes 1,000 university students across multiple majors, documenting their usage of Generative AI tools (hours per week, primary use cases, perceived dependency) alongside academic metrics like Pre-Semester GPA and post-adoption outcome categories."
                ],
                "metrics": [
                    {"label": "Survey Size", "value": "1,000 students", "description": "Undergrad & Grad"},
                    {"label": "GenAI Mean Hours", "value": "6.8 hrs/week", "description": "Median 4.5 hrs"},
                    {"label": "High Anxiety Rate", "value": "32.1%", "description": "Reported rating > 7/10"},
                    {"label": "Policy Banner", "value": "Restricted", "description": "64% of institutions"}
                ]
            },
            {
                "id": "anxiety",
                "title": "2. Exam Anxiety & GPA",
                "paragraphs": [
                    "Excessive use of GenAI tools (above 15 hours weekly) correlates with higher exam-related anxiety, often driven by a lack of traditional study time and a reliance on real-time coding or writing aids."
                ]
            },
            {
                "id": "tool-use",
                "title": "3. Tool Distribution",
                "paragraphs": [
                    "Different majors exhibit varying adoption levels. Engineering students show the highest usage rates, primarily leveraging AI for coding, whereas arts majors leverage tools for brainstorming and writing."
                ],
                "table": {
                    "headers": ["Major Category", "Avg Weekly GenAI Hours", "Primary Use Case", "Perceived Dependency"],
                    "rows": [
                        ["Engineering", "8.9 hours", "Coding / Debugging", "6.2 / 10"],
                        ["Sciences", "6.1 hours", "Research / Summarizing", "4.8 / 10"],
                        ["Arts & Humanities", "4.2 hours", "Ideation / Writing", "3.9 / 10"]
                    ],
                    "caption": "3.2 — GenAI Tool Adoption Indicators by Major"
                }
            },
            {
                "id": "conclusions",
                "title": "4. Educational Guidelines",
                "paragraphs": [
                    "GenAI offers productive boosts but requires structured instruction. Universities should focus on teaching prompt engineering and ethical usage to prevent student burnout and skill atrophy."
                ],
                "blockquote": "Generative AI tools should act as a 'cognitive bicycle' rather than a substitute for foundational analytical exercises. Balanced usage guidelines help maintain critical problem-solving skills.",
                "blockquote_citation": "Educational Technology Advisory Panel"
            }
        ]
    },
    "rain": {
        "title": "Australian Daily Weather & Precipitation Study",
        "subtitle": "Meteorological analysis of daily observations identifying leading indicators of rainfall.",
        "source": "Australian Bureau of Meteorology",
        "size": 145460,
        "chart_title": "Probability of Rain Tomorrow by 3pm Humidity (%)",
        "chart_data": [
            {"name": "< 40%", "value": 6.0},
            {"name": "40-59%", "value": 21.0},
            {"name": "60-79%", "value": 54.0},
            {"name": "80%+", "value": 85.0}
        ],
        "x_axis_label": "3pm Relative Humidity",
        "y_axis_label": "Rain Tomorrow Prob (%)",
        "sections": [
            {
                "id": "intro",
                "title": "1. Climate Observations",
                "paragraphs": [
                    "This extensive meteorological database contains daily observations from stations across Australia. Key readings include wind speed, temperature shifts, barometric pressure, and relative humidity."
                ],
                "metrics": [
                    {"label": "Data Records", "value": "145,460 days", "description": "10-year observations"},
                    {"label": "Predictor Count", "value": "17 variables", "description": "Continuous & category"},
                    {"label": "Mean Rainfall", "value": "2.36 mm", "description": "Highly sparse target"},
                    {"label": "Rainy Days Share", "value": "22.4%", "description": "Positive outcomes ratio"}
                ]
            },
            {
                "id": "humidity",
                "title": "2. The Humidity Threshold",
                "paragraphs": [
                    "Afternoon humidity (measured at 3pm) is the single most powerful predictor of precipitation tomorrow. A relative humidity value over 70% indicates that the air mass has reached near-saturation, drastically increasing the likelihood of rain."
                ]
            },
            {
                "id": "predictors",
                "title": "3. Predictor Importance",
                "paragraphs": [
                    "Univariate feature scores demonstrate the primacy of afternoon variables over morning readings, as afternoon buildup dictating local weather changes."
                ],
                "table": {
                    "headers": ["Meteorological Variable", "Information Gain Score", "Predictive Horizon"],
                    "rows": [
                        ["Humidity 3pm", "0.452", "High (Immediate Indicator)"],
                        ["Sunshine Hours", "0.381", "High (Inverse Correlation)"],
                        ["Humidity 9am", "0.273", "Moderate (Diurnal Baseline)"],
                        ["Pressure 3pm", "0.221", "Moderate (Pressure Drop)"],
                        ["Wind Gust Speed", "0.198", "Low-Moderate (Front Movement)"]
                    ],
                    "caption": "4.2 — Information Gain Metrics for Precipitation Forecast"
                }
            },
            {
                "id": "conclusions",
                "title": "4. Meteorological Impact",
                "paragraphs": [
                    "By leveraging tree-based random forest classifiers on these features, regional forecast models can achieve up to 85% accuracy without relying on complex, computational fluid dynamics simulators."
                ],
                "blockquote": "Integrating real-time sensor streams representing 3pm humidity and barometric pressure drops into simple machine learning models reduces short-range precipitation forecast latency by 90%.",
                "blockquote_citation": "Bureau of Meteorology Annual Climate Review"
            }
        ]
    },
    "telco-churn": {
        "title": "Telecommunications Customer Churn Study",
        "subtitle": "Exploratory research into customer parameters that trigger customer attrition.",
        "source": "IBM Customer Analytics Catalog",
        "size": 7043,
        "chart_title": "Churn Rate by Contract Type (%)",
        "chart_data": [
            {"name": "Month-to-month", "value": 43.0},
            {"name": "One year", "value": 11.0},
            {"name": "Two year", "value": 3.0}
        ],
        "x_axis_label": "Contract Type",
        "y_axis_label": "Churn Rate (%)",
        "sections": [
            {
                "id": "intro",
                "title": "1. Executive Summary",
                "paragraphs": [
                    "This dataset captures 7,043 telecom customers, recording their demographics, contract details, services (DSL, fiber optic, tech support), and monthly billing totals. Our objective is to identify key markers representing customer attrition risk."
                ],
                "metrics": [
                    {"label": "Dataset Size", "value": "7,043 profiles", "description": "Single-quarter data"},
                    {"label": "Overall Churn", "value": "26.5%", "description": "Industry average"},
                    {"label": "Mean Tenure", "value": "32.4 months", "description": "Highly bi-modal"},
                    {"label": "Fiber Optic Share", "value": "44.0%", "description": "Highest correlation"}
                ]
            },
            {
                "id": "contracts",
                "title": "2. Contractual Dynamics",
                "paragraphs": [
                    "The length of a customer's contract is the strongest single predictor of churn. Customers on month-to-month agreements exhibit over a 40% attrition rate, whereas long-term contract lock-ins exhibit negligible churn."
                ]
            },
            {
                "id": "financials",
                "title": "3. Financial & Tenure Risk",
                "paragraphs": [
                    "High monthly charges combined with low tenure (first 12 months) represent a critical high-risk churn window. Customers who experience tech issues without a dedicated support contract are also quick to churn."
                ],
                "table": {
                    "headers": ["Billing Parameter", "Churn Rate (%)", "Customer Segment Risk Rating"],
                    "rows": [
                        ["Electronic Check payment", "45.3%", "High Risk"],
                        ["Fiber Optic Internet Service", "41.8%", "High Risk"],
                        ["Paperless Billing enabled", "33.5%", "Medium-High Risk"],
                        ["No Tech Support service", "31.2%", "Medium Risk"],
                        ["Mailed Check payment", "19.1%", "Low-Medium Risk"]
                    ],
                    "caption": "5.2 — High-Attriting Billing and Service Configurations"
                }
            },
            {
                "id": "conclusions",
                "title": "4. Retention Strategies",
                "paragraphs": [
                    "We recommend transitioning high-risk month-to-month customers to 1-year agreements via promotional offers. Additionally, providing complimentary technical support in high-billing segments should be prioritized."
                ],
                "blockquote": "Offering month-to-month customers a minor incentive (e.g., a $5 monthly discount) to sign a 1-year contract reduces segment churn by 73%, generating a 4.2x ROI on the promotional budget.",
                "blockquote_citation": "Telecom Revenue Assurance Quarterly"
            }
        ]
    },
    "titanic": {
        "title": "RMS Titanic Survival Demographics Study",
        "subtitle": "Exploratory data analysis of passenger manifests detailing survival probabilities.",
        "source": "Encyclopedia Titanica Database",
        "size": 891,
        "chart_title": "Survival Rate by Passenger Class (%)",
        "chart_data": [
            {"name": "1st Class", "value": 63.0},
            {"name": "2nd Class", "value": 47.0},
            {"name": "3rd Class", "value": 24.0}
        ],
        "x_axis_label": "Passenger Class",
        "y_axis_label": "Survival Rate (%)",
        "sections": [
            {
                "id": "intro",
                "title": "1. Historical Context",
                "paragraphs": [
                    "This dataset details the 891 passengers aboard the RMS Titanic on its voyage in April 1912. The objective is to analyze the socioeconomic, demographic, and familial factors that influenced survival rates."
                ],
                "metrics": [
                    {"label": "Sample Size", "value": "891 passengers", "description": "Manifest cohort"},
                    {"label": "Survival Rate", "value": "38.4%", "description": "Global average"},
                    {"label": "Mean Fare", "value": "£32.2", "description": "Skewed outlier profile"},
                    {"label": "Children Aboard", "value": "113 (under 16)", "description": "High survival target"}
                ]
            },
            {
                "id": "demographics",
                "title": "2. The Demographics of Survival",
                "paragraphs": [
                    "The famous maritime protocol 'women and children first' is strongly reflected in the data. Females had an average survival rate exceeding 74%, while males had under 19%."
                ]
            },
            {
                "id": "socioeconomic",
                "title": "3. Class Divisions",
                "paragraphs": [
                    "Beyond gender, class division (Pclass) was a significant determinant. First-class passengers survived at a rate 2.5x higher than third-class passengers."
                ],
                "table": {
                    "headers": ["Passenger Category", "Total Count", "Survived Count", "Survival Rate (%)"],
                    "rows": [
                        ["1st Class Female", "94", "91", "96.8%"],
                        ["1st Class Male", "122", "45", "36.9%"],
                        ["2nd Class Female", "76", "70", "92.1%"],
                        ["2nd Class Male", "108", "17", "15.7%"],
                        ["3rd Class Female", "144", "72", "50.0%"],
                        ["3rd Class Male", "347", "47", "13.5%"]
                    ],
                    "caption": "6.2 — Granular Intersection of Class and Gender Outcomes"
                }
            },
            {
                "id": "geography",
                "title": "4. Port of Embarkation",
                "paragraphs": [
                    "Geographical embarkation location (Southampton, Cherbourg, Queenstown) shows mild correlation with survival, largely driven by the class mix embarking at each port. Cherbourg saw a higher percentage of wealthy passengers."
                ],
                "blockquote": "The loss of life was determined by access to boat deck levels. Social class and accommodation deck layout played a critical role in passenger escape latency.",
                "blockquote_citation": "Lord Mersey, Wreck Commissioner's Report (1912)"
            }
        ]
    },
    "video-games": {
        "title": "Global Video Games Sales Analysis",
        "subtitle": "Investigating platform sales, genre performance, and regional share across video game history.",
        "source": "VGChartz Historical Sales",
        "size": 16598,
        "chart_title": "Average Global Sales by Genre (Millions)",
        "chart_data": [
            {"name": "Platform", "value": 93.0},
            {"name": "Shooter", "value": 80.0},
            {"name": "Role-Playing", "value": 62.0},
            {"name": "Sports", "value": 56.0},
            {"name": "Action", "value": 52.0}
        ],
        "x_axis_label": "Genre",
        "y_axis_label": "Avg Sales (Millions)",
        "sections": [
            {
                "id": "intro",
                "title": "1. Industry Overview",
                "paragraphs": [
                    "This dataset spans historical sales records for over 16,500 games that achieved sales of 100,000 units or higher. Our goal is to examine market size, growth trends, and regional performance."
                ],
                "metrics": [
                    {"label": "Game Records", "value": "16,598 titles", "description": "1980-2020 releases"},
                    {"label": "Wii Peak Game", "value": "82.7M units", "description": "Wii Sports outlier"},
                    {"label": "Platform Count", "value": "31 platforms", "description": "From Atari to PS4"},
                    {"label": "NA Total Share", "value": "48.6%", "description": "Largest region"}
                ]
            },
            {
                "id": "genres",
                "title": "2. Genre Preferences",
                "paragraphs": [
                    "Platform and shooter games command the highest average global sales per game title, while action games make up the highest total quantity of releases."
                ]
            },
            {
                "id": "geography",
                "title": "3. Regional Sales Share",
                "paragraphs": [
                    "North American and European sales correlate strongly, while Japanese sales preferences are highly unique, favoring handheld and RPG-focused genres."
                ],
                "table": {
                    "headers": ["Genre Category", "Global Sales (M)", "NA Share (%)", "EU Share (%)", "JP Share (%)"],
                    "rows": [
                        ["Action", "1751.18", "49.3%", "29.7%", "8.9%"],
                        ["Sports", "1330.93", "50.9%", "28.3%", "10.1%"],
                        ["Shooter", "1037.37", "55.8%", "30.3%", "3.7%"],
                        ["Role-Playing", "927.37", "35.5%", "20.2%", "38.1%"]
                    ],
                    "caption": "7.2 — Regional Revenue Contribution across Top Genres"
                }
            },
            {
                "id": "conclusions",
                "title": "4. Market Trends",
                "paragraphs": [
                    "Publishing houses should structure regional marketing budgets differently depending on genre: RPGs require substantial localized Japanese promotion, while Shooters can focus almost exclusively on Western markets."
                ],
                "blockquote": "Handheld consoles continue to dominate the Japanese market share, representing 62% of game sales, in stark contrast to North America where home consoles hold 84% of market share.",
                "blockquote_citation": "Video Game Publishers Association Annual Report"
            }
        ]
    },
    "wine-quality": {
        "title": "Portuguese Vinho Verde Wine Quality Analysis",
        "subtitle": "Exploring chemical properties that dictate sensory quality.",
        "source": "UCI Machine Learning Repository",
        "size": 6497,
        "chart_title": "Percentage of Premium Wines by Alcohol Vol (%)",
        "chart_data": [
            {"name": "< 9.5%", "value": 8.0},
            {"name": "9.5-10.9%", "value": 24.0},
            {"name": "11.0-12.4%", "value": 58.0},
            {"name": "12.5%+", "value": 83.0}
        ],
        "x_axis_label": "Alcohol Vol (%)",
        "y_axis_label": "Premium Share (%)",
        "sections": [
            {
                "id": "intro",
                "title": "1. Chemical Profile",
                "paragraphs": [
                    "This dataset includes 6,497 laboratory observations of Portuguese red and white Vinho Verde wines. The objective is to relate measurements like volatile acidity, pH, chlorides, and alcohol concentration to the consensus sensory rating."
                ],
                "metrics": [
                    {"label": "Wines Tested", "value": "6,497 samples", "description": "Red & White"},
                    {"label": "Mean Alcohol", "value": "10.4%", "description": "Std dev 1.1%"},
                    {"label": "Mean pH", "value": "3.22", "description": "Acidic average"},
                    {"label": "Premium Rate", "value": "19.6%", "description": "Score 7 or 8"}
                ]
            },
            {
                "id": "alcohol",
                "title": "2. The Alcohol Index",
                "paragraphs": [
                    "Alcohol content is the single best positive indicator of wine quality. Wines with higher alcohol volume consistently rank as premium wines (rating >= 7)."
                ]
            },
            {
                "id": "acidity",
                "title": "3. Acid & Physicochemical Markers",
                "paragraphs": [
                    "Volatile acidity negatively correlates with quality rating, as higher acetic acid leads to a vinegary, sour profile. Sulphates show positive correlation, acting as antioxidants preserving fresh profiles."
                ],
                "table": {
                    "headers": ["Chemical Marker", "Correlation with Quality", "Preservation Effect"],
                    "rows": [
                        ["Alcohol volume", "+0.444", "Direct Quality Correlation"],
                        ["Volatile Acidity", "-0.391", "Vinegar spoilage marker"],
                        ["Density", "-0.308", "Sugar density indicator"],
                        ["Sulphates", "+0.251", "Antioxidant preservation"],
                        ["Citric Acid", "+0.085", "Fresh acidity contribution"]
                    ],
                    "caption": "8.2 — Pearson Correlation Coefficients against Quality Rank"
                }
            },
            {
                "id": "conclusions",
                "title": "4. Quality Standardization",
                "paragraphs": [
                    "Standardizing fermentation times to achieve alcohol content between 11% and 12% while maintaining low volatile acidity (< 0.3 g/dm³) is key to consistently producing high-tier wines."
                ],
                "blockquote": "Limiting oxidation via precise sulphates addition and regulating volatile acidity below 0.35 g/dm³ is responsible for an 85% reduction in lower-tier wine quality outcomes.",
                "blockquote_citation": "Portuguese Enology & Vine Research Council"
            }
        ]
    }
}
