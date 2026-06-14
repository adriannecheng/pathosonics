import streamlit as st
import streamlit.components.v1 as components # <--- Crucial module for HTML frames

# Page configuration
st.set_page_config(page_title=" Research Findings", page_icon="🔬", layout="centered")

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
    
    /* Main App Titles (Blue Lavender) */
    h1 { 
        font-family: 'Avenir', sans-serif !important; 
        color: #99acff !important; 
        font-weight: 700;
    }
    
    /* MAIN PAGE TITLE OVERRIDE ("PathoSonics Portfolio Carousel") */
    /* This rule forces your primary page headings to scale up beautifully */
    h1 { 
        font-family: 'Avenir', sans-serif !important; 
        color: #99acff !important; 
        font-weight: 700 !important;
        font-size: 3.0rem !important; /* Scaled up significantly for strong presentation weight */
        line-height: 1.2 !important;
        margin-bottom: 5px !important;
    }
        
    /* Secondary Section Subheaders */
    h2, h3, h4 {
        font-family: 'Avenir', sans-serif !important; 
        color: #CBD5E1 !important; /* Soft white/gray for balance */
        font-weight: 600;
    }
    
    .main { background-color: #0E1117; }
    
    /* Interactive Control Buttons Style Configuration */
    div.stButton > button:first-child {
        background-color: #99acff !important; 
        color: #0E1117 !important; /* Forces the text to a sharp, dark charcoal gray */
        font-weight: 700 !important; /* Makes the font bold and crisp */
        border-radius: 8px; 
        border: none; 
        padding: 0.5rem 2rem;
        font-family: 'Avenir', sans-serif !important;
        transition: all 0.2s ease-in-out; /* Smooth transition when hovering */
    }
    
    /* Hover State: When the cursor moves over the button */
    div.stButton > button:first-child:hover {
        background-color: #6b8cff !important; /* Darker Blue Lavender background */
        color: #FFFFFF !important; /* Flips the font text to crisp white for contrast */
        box-shadow: 0px 0px 12px rgba(0, 229, 255, 0.4); /* Subtle glowing accent */
    }

    </style>
""", unsafe_allow_html=True)

# Custom Sidebar Branding Logo (Matching Home)
import os
if os.path.exists("logo.png"):
    st.sidebar.image("logo.png", use_container_width=True)
    st.sidebar.markdown("<br>", unsafe_allow_html=True)

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
