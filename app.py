import streamlit as st
import networkx as nx

algo_simulator = st.Page("pages/1_Algorithm_Simulator.py", title="Algorithm Simulator", icon="🧠")
algo_comparison = st.Page("pages/2_Algorithm_Comparison.py", title="Algorithm Comparison", icon="📊")

pg = st.navigation([algo_simulator, algo_comparison])

pg.run()

# Initialize session state if not already done (for shared graph)
if 'graph' not in st.session_state:
    st.session_state['graph'] = None