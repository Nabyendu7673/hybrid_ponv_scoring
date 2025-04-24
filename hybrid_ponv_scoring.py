import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Updated Hybrid PONV Scoring", layout="wide")

st.title("📋 Updated Hybrid PONV Scoring System")
st.markdown("""
This tool presents an updated PONV scoring system, integrating validated patient, surgical, drug-related, and postoperative factors.
Each cell includes the scoring with corresponding **clinical justification**.
""")

# Define the scoring data
data = {
    "Category": [
        "Patient-Specific Risk Factors", "", "", "", "", "", "", "",
        "Surgical and Anesthesia-Related Factors", "", "", "", "", "",
        "Postoperative Symptoms", "", "", "",
        "Drug-Related Factors (Dose-Based)", "", "", "", "", "", "", "", "", "", "", "", "", "", ""
    ],
    "Factor": [
        "Female gender", "Non-smoker", "History of PONV or Motion Sickness", "Age <50 years", "Preoperative Anxiety", "History of Migraine", "Obesity (BMI >30 kg/m²)", "",
        "Abdominal or Laparoscopic Surgery", "ENT, Neurosurgery, or Ophthalmic Surgery", "Gynecologic or Breast Surgery", "Surgery Duration >60 minutes", "Major Blood Loss >500 mL", "",
        "Nausea >30 minutes", ">2 episodes of vomiting", "Abdominal discomfort", "",
        "Ondansetron", "Midazolam", "Dexamethasone", "Glycopyrrolate", "Nalbuphine", "Fentanyl", "Butorphanol", "Pentazocine", "Propofol (TIVA)", "Propofol (Induction only)", 
        "Sevoflurane/Isoflurane/Desflurane", "Succinylcholine", "Atracurium", "Cisatracurium", "Vecuronium"
    ],
    "Score Range": [
        "1", "1", "2", "1", "1", "1", "1", "",
        "2", "1", "2", "1", "1", "",
        "1", "2", "1", "",
        "0 to –2", "0 to –2", "0 to –1", "0 to +1", "0 to +1", "0 to +3", "0 to +1", "0 to +3", "0 to –3", "0 to –1", "0 to +2", "0", "0", "0", "0"
    ],
    "Justification": [
        "Well-established independent risk factor",
        "Higher PONV risk compared to smokers",
        "Strongest predictor of PONV recurrence",
        "Younger patients have higher PONV risk",
        "Higher catecholamine levels contribute to nausea",
        "Increased serotonin sensitivity leads to PONV",
        "Delayed gastric emptying increases PONV risk", "",
        "Higher manipulation, insufflation—greater emetogenicity",
        "Moderate emetogenic risk",
        "Hormonal sensitivity & regional factors",
        "Longer exposure increases risk",
        "Hemodynamic instability increases risk", "",
        "Indicates ongoing emetogenic stimulation",
        "Severe emetogenic manifestation",
        "Often linked with emetogenic response", "",
        "≥4 mg IV effective; full dose (16–24 mg) offers maximum antiemetic effect",
        "Protective benefit increases with dose (meta-analysis support)",
        "≥4 mg effective for delayed PONV; high dose used for chemotherapy N/V",
        "At therapeutic doses, slows gastric emptying, increasing PONV risk slightly",
        "Mild to moderate emetogenicity at higher opioid doses",
        "Strongest dose-dependent PONV risk among opioids",
        "Partial agonist, less risky than fentanyl but still dose-sensitive",
        "Strongly emetogenic at higher doses due to kappa receptor stimulation",
        "Continuous infusion provides maximal protective benefit",
        "Induction effect only — volatile agents override antiemetic effect",
        "Strong dose-dependent increase in PONV above 1 MAC",
        "No evidence of dose-dependent effect on PONV",
        "No PONV association noted across dose spectrum",
        "No PONV effect observed clinically",
        "No impact on PONV, dose-independent"
    ]
}

df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

# Download section
st.markdown("### 📅 Download Table")
csv = df.to_csv(index=False).encode('utf-8')
buffer = BytesIO()
df.to_excel(buffer, index=False, engine='openpyxl')
buffer.seek(0)

col1, col2 = st.columns(2)
with col1:
    st.download_button("Download CSV", csv, "ponv_scoring.csv", "text/csv")
with col2:
    st.download_button("Download Excel", buffer, "ponv_scoring.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

# References
st.markdown("---")
st.markdown("### 📚 References")
st.markdown("""
- [Comparison of predictive models in postoperative nausea and vomiting in patients undergoing breast cancer surgery (2024)](https://pubmed.ncbi.nlm.nih.gov/39112678/)
- [Preventing Nausea and Vomiting After Bariatric Surgery: Is the Apfel Risk Prediction Score Enough to Guide Prophylaxis? (2020)](https://link.springer.com/article/10.1007/s11695-020-04682-2)
""")
