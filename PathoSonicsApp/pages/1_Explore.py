import streamlit as st
import numpy as np
import time

# Page configuration
st.set_page_config(page_title="Custom Sequencing Exploration", page_icon="🧪", layout="wide")

    # 2. Global Theme Styling Injection (Updated Header Font Sizes)
st.markdown("""
    <style>
        /* TARGET AND BANISH THE KEYBOARD DOUBLE ARROW NAV GLITCH */
    /* This rule searches for the broken material icon label and hides it entirely */
    [data-testid="stSidebarCollapseButton"] button div,
    span:contains("keyboard_double_arrow") {
        display: none !important;
        visibility: hidden !important;
    }
    
    /* Optional: If the button container frame itself is still making an empty box, use this */
    .st-emotion-cache-16ids9p, [data-markdown-target="true"] {
        font-size: 0px !important;
        color: transparent !important;
    }

    @import url('https://googleapis.com');
    @import url('https://googleapis.com');

    .main, p, div, label, span { 
        font-family: 'Spot Mono', sans-serif !important; 
        font-size: 1.05rem;
        color: #94A3B8 !important; 
    }
    
    /* 1. PRIMARY PAGE TITLES OVERRIDE (e.g., "Custom Sequencing Exploration") */
    /* This rule forces your absolute largest page headers to scale up significantly */
    h1 { 
        font-family: 'Spot Mono', sans-serif !important; 
        color: #00E5FF !important; 
        font-weight: 700 !important;
        font-size: 3.5rem !important; /* Increased from 3.0rem to 3.5rem for maximum command */
        line-height: 1.2 !important;
        margin-bottom: 5px !important;
    }
    
    /* 2. SECONDARY CONTAINER AND SECTION HEADERS OVERRIDE */
    /* This rule targets secondary module headers across your app layout */
    h2 {
        font-family: 'Spot Mono', sans-serif !important; 
        color: #CBD5E1 !important; 
        font-weight: 700 !important;
        font-size: 2.4rem !important; /* Scaled up from 2.1rem for higher visibility */
        margin-bottom: 15px !important;
    }

    h3, h4 {
        font-family: 'Spot Mono', sans-serif !important; 
        color: #CBD5E1 !important; 
        font-weight: 600;
        font-size: 1.7rem !important; /* Scaled up from 1.5rem for visual balance */
    }
    
    .main { background-color: #0E1117; }
    
    /* Interactive Control Button Style Configuration */
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
    </style>
    """, unsafe_allow_html=True)

# Custom Sidebar Branding Logo (Matching Home)
import os
import streamlit as st

# Calculates the subpage location, then safely steps backward to the root path
pages_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.abspath(os.path.join(pages_dir, "..", "logo.png"))

if os.path.exists(logo_path):
    st.sidebar.image(logo_path, use_container_width=True)
    st.sidebar.markdown("<br>", unsafe_allow_html=True)


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

st.title("🔎 Custom Sequencing Exploration")
st.write("Input raw uppercase FASTA strings below to evaluate custom biometric sonic signals!")
st.markdown("---")

user_input = st.text_area("Paste custom uppercase sequence markers here:", value="MARV")

if st.button("⚙️ Synthesize Custom Matrix", key="btn_sandbox_run"):
    clean_input = "".join(user_input.split()).upper()
    
    if len(clean_input) == 0:
        st.warning("Input canvas cannot be left blank.")
    else:
        status_text = st.empty()
        progress_bar = st.progress(0)
        
        stages = [
            ("🧬 Reading sandbox string data arrays...", 0.25),
            ("📊 Processing structural hydrophobicity levels...", 0.50),
            ("🎹 Assigning variables to Pentatonic musical targets...", 0.75),
            ("🎧 Compiling final wave audio data profiles...", 1.00)
        ]
        for message, pct in stages:
            status_text.text(message)
            progress_bar.progress(pct)
            time.sleep(0.4)
            
        audio_data, sr = generate_audio_signal(clean_input)
        status_text.empty()
        progress_bar.empty()
        
        st.success(f"✅ Success! Compiled {len(clean_input)} sequence elements.")
        st.audio(audio_data, sample_rate=sr)

# ==============================================================================
# ACOUSTIC CONVERSION REFERENCE LEDGER
# ==============================================================================
st.markdown(" ")
st.markdown("### 📊 Aminos-to-Acoustics Table")
st.caption("Cross-reference observed molecular hydrophobicity values against generated pentatonic pitch scales.")

# Generate a beautifully formatted Markdown layout grid matrix
st.markdown("""

| Amino Acid (FASTA) | Biochemical Index | Assigned MIDI | Scale Pitch / Note | Absolute Frequency |
| :--- | :--- | :---: | :---: | :---: |
| **I** (Isoleucine) | Ultra Hydrophobic (Core) | 36 | Low C (Octave 2) | 65.41 Hz |
| **V** (Valine) | Hydrophobic | 38 | D | 73.42 Hz |
| **L** (Leucine) | Hydrophobic | 40 | E | 82.41 Hz |
| **F** (Phenylalanine) | Hydrophobic | 43 | G | 98.00 Hz |
| **C** (Cysteine) | Hydrophobic | 45 | A | 110.00 Hz |
| **M** (Methionine) | Mildly Hydrophobic | 48 | C (Octave 3) | 130.81 Hz |
| **A** (Alanine) | Mildly Hydrophobic | 50 | D | 146.83 Hz |
| **G** (Glycine) | Mildly Hydrophobic | 52 | E | 164.81 Hz |
| **T** (Threonine) | Neutral / Structural | 55 | G | 196.00 Hz |
| **S** (Serine) | Neutral / Structural | 57 | A | 220.00 Hz |
| **W** (Tryptophan) | Neutral / Structural | 60 | Middle C (Octave 4) | 261.63 Hz |
| **Y** (Tyrosine) | Neutral / Structural | 62 | D | 293.66 Hz |
| **P** (Proline) | Hydrophilic (Surface) | 64 | E | 329.63 Hz |
| **H** (Histidine) | Hydrophilic | 67 | G | 392.00 Hz |
| **E** (Glutamic Acid) | Hydrophilic | 69 | A | 440.00 Hz |
| **Q** (Glutamine) | Hydrophilic | 72 | C (Octave 5) | 523.25 Hz |
| **D** (Aspartic Acid) | Hydrophilic | 74 | D | 587.33 Hz |
| **N** (Asparagine) | Hydrophilic | 76 | E | 659.25 Hz |
| **K** (Lysine) | Ultra Hydrophilic | 79 | G | 783.99 Hz |
| **R** (Arginine) | Ultra Hydrophilic | 81 | A (Octave 5) | 880.00 Hz |
""")
