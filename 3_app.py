import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. Page Configuration (Pure Streamlit)
st.set_page_config(
    page_title="Palo Alto HR Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Load Data Function
@st.cache_data
def load_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "Processed_HR_Data.csv")
    return pd.read_csv(file_path)

df = load_data()

# 3. Native Streamlit Header
st.title(" Palo Alto Networks: HR Retention Intelligence")
st.caption("Advanced AI-Powered Workforce Analytics & Risk Simulator (Pure Python Edition)")
st.divider()

# 4. Native Sidebar Controls
st.sidebar.title(" Control Center")
st.sidebar.info("Use these filters to slice the dataset dynamically.")

dept_filter = st.sidebar.multiselect(
    "Select Department:",
    options=df['Department'].unique(),
    default=df['Department'].unique()
)

cluster_filter = st.sidebar.multiselect(
    "Select Career Cluster:",
    options=df['Cluster_Name'].unique(),
    default=df['Cluster_Name'].unique()
)

risk_filter = st.sidebar.multiselect(
    "Select Promotion Risk Level:",
    options=['Low', 'Medium', 'High'],
    default=['Low', 'Medium', 'High']
)

# Apply dynamic filters
filtered_df = df[
    (df['Department'].isin(dept_filter)) &
    (df['Cluster_Name'].isin(cluster_filter)) &
    (df['Promotion_Gap_Risk'].isin(risk_filter))
]

# 5. Native Metric Components (No CSS needed)
col1, col2, col3, col4 = st.columns(4)

total_emp = len(filtered_df)
attr_rate = (filtered_df['Attrition'].mean() * 100) if total_emp > 0 else 0
high_risk_count = len(filtered_df[filtered_df['Promotion_Gap_Risk'] == 'High'])
actionable_targets = len(filtered_df[filtered_df['Retention_Opportunity'] == 'High Priority'])

# Streamlit's built-in metric component is naturally clean and professional
col1.metric(label="Filtered Workforce", value=f"{total_emp:,}")
col2.metric(label="Historical Attrition Rate", value=f"{attr_rate:.1f}%")
col3.metric(label="High Promotion Risk", value=f"{high_risk_count:,}")
col4.metric(label="Actionable Retention Targets", value=f"{actionable_targets:,}")

st.divider()

# 6. Advanced Interactive Tabs (Native)
tab1, tab2, tab3, tab4 = st.tabs([
    " Predictive Visuals", 
    " Hierarchy Risk Map", 
    " Retention Simulator", 
    " Target Export"
])

# TAB 1: Advanced Plotly Visuals
with tab1:
    c1, c2 = st.columns(2)
    
    with c1:
        # Complex Bar Chart
        fig_cluster = px.bar(
            filtered_df['Cluster_Name'].value_counts().reset_index(),
            x='Cluster_Name', y='count',
            color='Cluster_Name',
            title="Career Segment Distribution",
            labels={'Cluster_Name': 'Segment', 'count': 'Employee Count'}
        )
        st.plotly_chart(fig_cluster, use_container_width=True)
        
    with c2:
        # Advanced 3D Scatter Plot (Purely analytical, no CSS)
        fig_3d = px.scatter_3d(
            filtered_df,
            x='YearsAtCompany',
            y='Promotion_Gap_Ratio',
            z='Role_Stagnation_Index',
            color='Promotion_Gap_Risk',
            title="3D Stagnation & Experience Mapping",
            opacity=0.7
        )
        st.plotly_chart(fig_3d, use_container_width=True)

# TAB 2: Drill-down Sunburst
with tab2:
    st.subheader("Department & Role Hierarchy Risk Map")
    st.write("Click on any sector to drill down into Department -> Job Role -> Attrition Risk.")
    
    # Sunburst chart is a highly advanced visualization native to Plotly
    fig_sunburst = px.sunburst(
        filtered_df,
        path=['Department', 'JobRole', 'Promotion_Gap_Risk'],
        color='Attrition',
        color_continuous_scale='Reds',
        title="Workforce Hierarchy Attrition Breakdown"
    )
    fig_sunburst.update_layout(height=600)
    st.plotly_chart(fig_sunburst, use_container_width=True)

# TAB 3: Interactive Math/Logic Simulator
with tab3:
    st.subheader(" What-If Promotion Intervention Simulator")
    st.write("Simulate the analytical impact of promoting stagnant employees.")
    
    sim_col1, sim_col2 = st.columns([1, 2])
    
    with sim_col1:
        # Native interactive slider
        promotion_budget = st.slider(
            "Select % of High-Risk Employees to Promote:", 0, 100, 25, step=5
        )
        
        simulated_mitigation = int(high_risk_count * (promotion_budget / 100))
        remaining_high_risk = high_risk_count - simulated_mitigation
        
        st.success(f"**Simulation Output:**\nPromoting **{simulated_mitigation}** high-risk employees will reduce total high-risk exposure down to **{remaining_high_risk}**.")
    
    with sim_col2:
        # Live updating chart based on simulator math
        sim_data = pd.DataFrame({
            'Category': ['Current High Risk', 'Simulated Mitigated', 'Remaining Risk'],
            'Count': [high_risk_count, simulated_mitigation, remaining_high_risk]
        })
        fig_sim = px.bar(
            sim_data, x='Category', y='Count',
            color='Category',
            title="Risk Exposure Mitigation Profile"
        )
        st.plotly_chart(fig_sim, use_container_width=True)

# TAB 4: Data Rendering and Export
with tab4:
    st.subheader(" Actionable Target Roster")
    
    target_df = filtered_df[filtered_df['Retention_Opportunity'] == 'High Priority']
    
    cols_to_show = [
        'Age', 'Department', 'JobRole', 'MonthlyIncome', 
        'YearsAtCompany', 'YearsSinceLastPromotion', 'Promotion_Gap_Ratio', 'Cluster_Name'
    ]
    
    # Native interactive dataframe
    st.dataframe(
        target_df[cols_to_show].sort_values(by='Promotion_Gap_Ratio', ascending=False),
        use_container_width=True
    )
    
    # Native download button
    csv_data = target_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label=" Export High-Priority Retention Roster (CSV)",
        data=csv_data,
        file_name="Palo_Alto_High_Priority_Retention_Targets.csv",
        mime="text/csv"
    )