import streamlit as st
import networkx as nx

st.markdown("""
<style>
/* Base graph-paper grid */
.stApp {
  background-image:
    linear-gradient(rgba(255,255,255,0.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.04) 1px, transparent 1px),
    linear-gradient(rgba(255,255,255,0.08) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.08) 1px, transparent 1px);
  background-size:
    24px 24px,
    24px 24px,
    120px 120px,
    120px 120px;
  background-position: -1px -1px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
/* Make expander a solid surface, not a wireframe */
div[data-testid="stExpander"] {
  background: linear-gradient(
    180deg,
    rgba(15, 23, 42, 0.94),
    rgba(17, 24, 39, 0.94)
  );
  border-radius: 14px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.35);
  border: none;
  overflow: hidden;
}

/* Remove default expander border */
div[data-testid="stExpander"] > details {
  border: none;
}

/* Header styling */
div[data-testid="stExpander"] summary {
  padding: 12px 16px;
  font-weight: 500;
}         
</style>
""", unsafe_allow_html=True)

algo_simulator = st.Page("pages/1_Algorithm_Simulator.py", title="Algorithm Simulator", icon="📺")
algo_comparison = st.Page("pages/2_Algorithm_Comparison.py", title="Algorithm Comparison", icon="📊")

pg = st.navigation([algo_simulator, algo_comparison])

pg.run()

# Initialize session state if not already done (for shared graph)
if 'graph' not in st.session_state:
    st.session_state['graph'] = None