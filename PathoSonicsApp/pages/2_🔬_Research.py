import streamlit as st
import streamlit.components.v1 as components # <--- Crucial module for HTML frames

# Page configuration
st.set_page_config(page_title=" Research Findings", page_icon="🔬", layout="wide")

# 2. Global Theme Styling Injection (Updated Color Hierarchy)
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    @import url('https://googleapis.com');

    /* Background and global body text styling (Slate Silver) */
    .main, p, div, label, span { 
        font-family: 'Microsoft', sans-serif !important; 
        font-size: 1.05rem;
        color: #94A3B8 !important; /* Premium silver text */
    }
    
    /* Main App Titles (Vibrant Electric Cyan) */
    h1 { 
        font-family: 'Avenir', serif !important; 
        color: #99acff !important; 
        font-weight: 700;
    }
    
    /* Secondary Section Subheaders */
    h2, h3, h4 {
        font-family: 'Avenir', serif !important; 
        color: #CBD5E1 !important; /* Soft white/gray for balance */
        font-weight: 600;
    }
    
    .main { background-color: #0E1117; }
    
    /* Interactive Control Buttons (Lavender Blue) */
    div.stButton > button:first-child {
        background-color: #99acff !important; 
        color: #0E1117 !important; 
        font-weight: bold;
        border-radius: 8px; 
        border: none; 
        padding: 0.5rem 2rem;
        font-family: 'Microsoft', sans-serif !important;
    }
    div.stButton > button:first-child:hover {
        background-color: #00B2CC !important; 
        color: #FFFFFF !important;
    }
    </style>
    """, unsafe_allow_html=True)


# Custom Sidebar Branding Logo (Matching Home)
try:
    st.sidebar.image("logo.png", use_container_width=True)
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
except Exception:
    st.sidebar.warning("⚠️ logo.png asset not detected.")
st.sidebar.markdown("""
    <div style='text-align: center; margin-bottom: 20px;'>
        <h1 style='font-size: 2.2rem; color: #00D2C4 !important; margin-bottom: 0px;'>🧬 PathoSonics</h1>
        <p style='font-size: 0.85rem; color: #888888; text-transform: uppercase; letter-spacing: 2px;'>Educational Sonification Lab</p>
    </div>
    <hr style='margin-top: 0px; margin-bottom: 20px; border-color: #1F2937;'>
""", unsafe_allow_html=True)

# 3. Primary Workspace Elements
st.title("🔬 Research Manuscript Portal")
st.caption("Review the live, cloud-synchronized academic literature sheet below.")
st.markdown("---")

google_doc_url = "https://docs.google.com/document/d/e/2PACX-1vSDnDcB-2vzNMKUAr0YvjBpWDT6GRuysGffC58VIfRs3ICJbaurEZw6cSG9cSat34IU11oH69oAOsyQ/pub?embedded=true"

# 4. Embedded Cloud Frame Generator
# This natively draws a 1000-pixel-high document window right on your screen
components.html(
    f"""
    <iframe src="{google_doc_url}" 
            style="width:100%; height:1000px; border:1px solid #1F2937; background-color:#FFFFFF; border-radius:8px;">
    </iframe>
    """,
    height=1010
)