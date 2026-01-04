import streamlit as st

# --- CẤU HÌNH GIAO DIỆN ---
st.set_page_config(
    page_title="Veo 3.1 Prompter",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS tùy chỉnh để làm đẹp nút bấm
st.markdown("""
<style>
    div.stButton > button:first-child {
        background-color: #FF4B4B;
        color: white;
        font-size: 20px;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 24px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🎬 Veo 3.1: Fashion UGC Generator")
st.markdown("---")

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3048/3048122.png", width=100)
    st.header("⚙️ Settings")
    video_ratio = st.radio("Tỷ lệ khung hình", ["9:16 (TikTok/Shorts)", "16:9 (Youtube)", "1:1 (Insta)"])
    st.info("💡 **Mẹo:** 9:16 là tỷ lệ tốt nhất để AI tập trung vào chi tiết trang phục toàn thân.")

# --- INPUT COLUMNS ---
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("1. Subject (Chủ thể)")
    model_desc = st.text_input("Người mẫu", "A Gen-Z fashion model, asian, short bob hair")
    outfit_desc = st.text_area("Trang phục (Chất liệu & Màu sắc)", 
                               "Oversized beige trench coat, high-quality wool texture, minimalist style")
    
    st.subheader("2. Environment (Bối cảnh)")
    setting = st.selectbox("Địa điểm", 
                           ["Tokyo Shibuya Crossing at night", 
                            "Minimalist White Studio", 
                            "Parisian Cafe Terrace", 
                            "Desert Dunes at Sunset", 
                            "Cyberpunk Neon Street"])

with col2:
    st.subheader("3. Camera & Motion (Chất điện ảnh)")
    camera_move = st.selectbox("Chuyển động máy quay", 
                               ["Tracking Shot (Theo sát mẫu)", 
                                "Dolly Zoom (Hiệu ứng Vertigo)", 
                                "Low Angle (Góc thấp tôn dáng)", 
                                "Gimbal Smooth Walk", 
                                "Slow Motion 60fps"])
    
    action = st.text_input("Hành động", "Walking confidently towards camera, wind blowing hair")
    
    style_vibe = st.multiselect("Phong cách", ["Cinematic", "Vintage Film", "4K", "Sharp Focus", "Soft Lighting"], default=["Cinematic", "4K"])

# --- GENERATE LOGIC ---
if st.button("🚀 TẠO PROMPT VEO 3.1"):
    # Xử lý tỷ lệ
    ar = "--ar 9:16" if "9:16" in video_ratio else "--ar 16:9"
    if "1:1" in video_ratio: ar = "--ar 1:1"
    
    # Ghép từ khóa style
    style_str = ", ".join(style_vibe)
    
    prompt = (
        f"**Prompt:**\n\n"
        f"High fashion cinematic video. {model_desc} wearing {outfit_desc}. "
        f"Action: {action}. Location: {setting}. "
        f"Camera: {camera_move}. "
        f"Details: {style_str}, photorealistic, cloth physics, highly detailed texture. {ar}"
    )
    
    st.success("Copy nội dung bên dưới:")
    st.code(prompt, language="markdown")
