import streamlit as st
import numpy as np
import time

# Custom CSS to hide the footer and the main menu
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Page config setup
st.set_page_config(page_title="PathoSonics Home", page_icon="logo.png", layout="wide")

# 2. Global Theme Styling Injection (Updated Color Hierarchy)
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    @import url('https://googleapis.com');

    /* Background and global body text styling (Slate Silver) */
    .main, p, div, label, span { 
        font-family: 'Avenir', sans-serif !important; 
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
        background-color: #9ea5f3 !important; /* Your current lavender blue shade */
        border-radius: 8px; 
        border: none; 
        padding: 0.5rem 2rem;
        font-family: 'Inter', sans-serif !important;
        transition: all 0.2s ease-in-out;
    }
    
    /* FORCE TEXT AND EMOJIS INSIDE BUTTON TO BE DARK CHARCOAL */
    /* This new targeting rule specifically overrides the text contrast issue you are seeing */
    div.stButton > button:first-child, 
    div.stButton > button:first-child p, 
    div.stButton > button:first-child div {
        color: #0E1117 !important; /* Ink-dark charcoal gray text */
        font-weight: 700 !important; /* Keeps the text crisp and bold */
    }
    
    /* Hover State Configuration */
    div.stButton > button:first-child:hover {
        background-color: #7b83df !important; /* Deepens background when hovered */
    }
    
    /* Keep text white on hover for sharp feedback styling */
    div.stButton > button:first-child:hover,
    div.stButton > button:first-child:hover p,
    div.stButton > button:first-child:hover div {
        color: #FFFFFF !important; /* Snaps text to white for ultimate contrast */
    }

# Custom Sidebar Text & Emoji Branding Logo
import os
import streamlit as st

# Explicitly calculate the absolute root directory of your app
root_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(root_dir, "logo.png")

if os.path.exists(logo_path):
    st.sidebar.image(logo_path, use_container_width=True)
    st.sidebar.markdown("<br>", unsafe_allow_html=True)

# 2. Correctly execute your text headers so raw HTML code does not print out
st.sidebar.markdown("""
    <div style='text-align: left; margin-bottom: 20px;'>
        <h1 style='font-size: 2.2rem; color: #00E5FF !important; margin-bottom: 0px;'>Patho Sonics</h1>
        <p style='font-size: 0.85rem; color: #94A3B8; text-transform: uppercase; letter-spacing: 2px;'>Educational Sonification Lab</p>
    </div>
    <hr style='margin-top: 0px; margin-bottom: 20px; border-color: #1F2937;'>
"", unsafe_allow_html=True)

# Master conversion dictionary mapping biochemical properties to MIDI pitches
protein_scale = {
    'I': 36, 'V': 38, 'L': 40, 'F': 43, 'C': 45, 'M': 48, 'A': 50, 'G': 52, 'T': 55, 'S': 57,
    'W': 60, 'Y': 62, 'P': 64, 'H': 67, 'E': 69, 'Q': 72, 'D': 74, 'N': 76, 'K': 79, 'R': 81
}

def midi_to_freq(midi_num):
    return 440.0 * (2.0 ** ((midi_num - 69.0) / 12.0))

def generate_audio_signal(sequence):
    sample_rate = 44100
    note_duration = 0.3
    full_audio = np.array([], dtype=np.float32)
    
    for letter in sequence:
        if letter in protein_scale:
            freq = midi_to_freq(protein_scale[letter])
            t = np.linspace(0, note_duration, int(sample_rate * note_duration), False)
            note_wave = np.sin(freq * t * 2 * np.pi)
            envelope = np.sin(np.linspace(0, np.pi, len(note_wave)))
            full_audio = np.concatenate((full_audio, note_wave * envelope))
            
    return full_audio, sample_rate

# Structural Carousel Database Array
carousel_data = [
    {
        "title": "🟢 Healthy Hemoglobin Subunit", "id": "RCSB 1A3N",
        "seq": "MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPK",
        "finding": "Maintains a bright, consonant, and high upward melodic trajectory in the 3rd and 4th octaves * Note: This is NOT a sample of the full sequence, not all residues are shown here for brevity. *"
    },
    {
        "title": "🔴 Sickle Cell Mutant Variant", "id": "MCHU HBB",
        "seq": "MVHLTPVEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPK",
        "finding": "Features an immediate, jarring downward displacement drop of approximately 5 scale degrees at the 7th node position. This is the critical mutation site where Glutamic Acid (E) is replaced by Valine (V), causing the sickle shape. * Note: This is NOT a sample of the full sequence, not all residues are shown here for brevity. *"
    },
    {
        "title": "🟡 Mutant p53 Cancer Variant", "id": "RCSB 2OCJ",
        "seq": "MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGP",
        "finding": "Densely clustered acoustic profile showing severe tonal variations indicative of systemic molecular distortion. * Note: This is NOT a sample of the full sequence, not all residues are shown here for brevity. *"
    }
]

# Track current card inside the browser session memory
if "card_index" not in st.session_state:
    st.session_state.card_index = 0

current_card = carousel_data[st.session_state.card_index]

st.title("🧬 PathoSonics Carousel")
st.caption("Shuffle through a few pre-loaded assests and explore what sonification is!")
st.markdown("---")

card_box = st.container(border=True)
with card_box:
    st.header(current_card["title"])
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric(label="Structural Registry ID", value=current_card["id"])
        st.metric(label="Total Sequence Length", value=f"{len(current_card['seq'])} Residues")
    with col_b:
        st.info(f"📋 **Sonifier Pattern Finding:** {current_card['finding']}")
    
    if st.button("🔊 Synthesize Profile Audio", key="btn_home_audio"):
        status = st.empty()
        pbar = st.progress(0)
        for msg, pct in [("🧬 Mapping genomic sequence strings...", 0.5), ("🎧 Processing wave transformations...", 1.0)]:
            status.text(msg)
            pbar.progress(pct)
            time.sleep(0.4)
            
        audio, sr = generate_audio_signal(current_card["seq"])
        status.empty()
        pbar.empty()
        st.audio(audio, sample_rate=sr)

# Navigation row alignment layout matrix
nav_col1, nav_col2, nav_col3 = st.columns(3)
with nav_col1:
    if st.button("⬅️ Previous Asset", key="btn_prev"):
        st.session_state.card_index = (st.session_state.card_index - 1) % len(carousel_data)
        st.rerun()
with nav_col3:
    if st.button("Next Asset ➡️", key="btn_next"):
        st.session_state.card_index = (st.session_state.card_index + 1) % len(carousel_data)
        st.rerun()

st.markdown("---")
st.info("💡 *Want to process completely unique custom data? Navigate to **2 🧪 Explore** inside your left sidebar menu panel!*")

