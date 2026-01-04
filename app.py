import streamlit as st

# --- CẤU HÌNH GIAO DIỆN ---
st.set_page_config(
    page_title="Veo 3.1 UGC Master",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS làm đẹp giao diện
st.markdown("""
<style>
    div.stButton > button:first-child {
        background-color: #007AFF; /* Màu xanh iPhone */
        color: white;
        font-size: 20px;
        font-weight: bold;
        border-radius: 12px;
        padding: 12px 24px;
    }
    .sub-label {
        font-weight: bold;
        color: #333;
        margin-top: 15px;
        margin-bottom: 5px;
    }
    .highlight {
        color: #007AFF;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

st.title("📱 Veo 3.1: Authentic UGC & Natural Light Generator")
st.markdown("Tạo prompt video phong cách **quay bằng điện thoại (iPhone)**, ánh sáng tự nhiên, chân thực nhất.")
st.markdown("---")

# --- SIDEBAR ---
with st.sidebar:
    st.header("⚙️ Cấu hình Video")
    video_ratio = st.radio("Tỷ lệ khung hình", ["9:16 (TikTok/Reels)", "16:9 (Youtube)", "1:1 (Insta)"])
    
    st.divider()
    st.info("💡 **Mẹo ánh sáng:** Để video giống thật nhất, hãy chọn 'Ánh sáng tự nhiên (Giờ trưa)' hoặc 'Nắng xuyên qua rèm'. Tránh dùng từ 'Cinematic' nếu muốn phong cách UGC.")

# --- INPUT COLUMNS ---
col1, col2 = st.columns([1, 1], gap="medium")

with col1:
    st.subheader("1. Hình ảnh tham khảo")
    
    # Upload ảnh
    st.markdown('<p class="sub-label">📸 Upload ảnh Mẫu & Sản phẩm</p>', unsafe_allow_html=True)
    uploaded_img = st.file_uploader("Tải ảnh lên để dễ viết mô tả", type=['png', 'jpg', 'jpeg'])
    if uploaded_img:
        st.image(uploaded_img, width=200, caption="Ảnh tham khảo")

    # Nhập liệu nội dung
    st.markdown('<p class="sub-label">👤 Mô tả Người mẫu (Model)</p>', unsafe_allow_html=True)
    model_desc = st.text_input("Ví dụ: Cô gái việt nam, tóc đen dài, trang điểm nhẹ", 
                               "Vietnamese young woman, natural skin texture, light makeup, casual daily look")

    st.markdown('<p class="sub-label">👗 Mô tả Trang phục (Outfit)</p>', unsafe_allow_html=True)
    outfit_desc = st.text_area("Ví dụ: Áo phông trắng cotton, chất vải dày dặn", 
                               "White oversized t-shirt, heavy cotton fabric, realistic texture, wrinkles on fabric")

with col2:
    st.subheader("2. Ánh sáng & Camera (Quan trọng)")
    
    # --- PHẦN CHỈNH ÁNH SÁNG NÂNG CAO ---
    st.markdown('<p class="sub-label">☀️ Chọn loại Ánh sáng Tự nhiên</p>', unsafe_allow_html=True)
    
    # Dictionary map lựa chọn của user sang từ khóa AI chuyên sâu
    light_options = {
        "Natural Daylight (Ánh sáng ban ngày tự nhiên, sắc nét)": "natural daylight, bright and airy, crisp lighting, no filter",
        "Direct Sunlight (Nắng gắt, đổ bóng rõ - Rất thật)": "harsh direct sunlight, high contrast shadows, summer vibe, overexposed highlights",
        "Golden Hour (Nắng chiều ấm áp, da đẹp)": "golden hour sun, warm tone, sun flare lens effect, soft backlight on hair",
        "Window Light (Ánh sáng cửa sổ trong nhà - Soft)": "soft natural window light, diffused lighting, indoor daytime, cozy atmosphere",
        "Overcast / Cloudy (Trời râm, ánh sáng đều)": "overcast sky, soft diffused light, flat lighting, realistic rainy day vibe",
        "Flash Photography (Đèn Flash buổi tối - Party vibe)": "camera flash lighting, direct flash, dark background, paparazzi style, night out vibe"
    }
    
    selected_light_key = st.selectbox("Chọn kiểu ánh sáng:", list(light_options.keys()))
    selected_light_prompt = light_options[selected_light_key]

    # --- PHẦN CAMERA IPHONE ---
    st.markdown('<p class="sub-label">📱 Góc quay & Chất lượng</p>', unsafe_allow_html=True)
    camera_style = st.selectbox("Phong cách quay:", 
                                [
                                    "Handheld Selfie Mode (Tự cầm máy quay mặt)",
                                    "POV Shot (Góc nhìn người thứ nhất nhìn xuống đồ)",
                                    "Shakey Handheld (Cầm tay hơi rung nhẹ - Rất thật)",
                                    "Stable Gimbal Walk (Đi bộ mượt mà)",
                                    "Mirror Selfie (Quay qua gương)"
                                ])
    
    st.markdown('<p class="sub-label">📍 Bối cảnh (Background)</p>', unsafe_allow_html=True)
    setting = st.text_input("Bối cảnh đời thường", "Minimalist bedroom with sunlight, street sidewalk, cafe corner")

# --- XỬ LÝ PROMPT ---
st.markdown("---")
if st.button("✨ TẠO PROMPT UGC (IPHONE STYLE)"):
    # Xử lý tỷ lệ
    ar = "--ar 9:16" if "9:16" in video_ratio else "--ar 16:9"
    if "1:1" in video_ratio: ar = "--ar 1:1"
    
    # Các từ khóa "Magic" để biến video thành style iPhone/UGC
    ugc_keywords = "shot on iPhone 15 Pro, 4k raw footage, social media quality, vlog aesthetic, realistic texture, highly detailed skin, authentic look, non-cinematic, amateur videography style."
    
    # Lắp ghép Prompt
    final_prompt = (
        f"**Prompt cho Veo:**\n\n"
        f"Real life footage, {ugc_keywords} \n"
        f"**Subject:** {model_desc} wearing {outfit_desc}. \n"
        f"**Lighting:** {selected_light_prompt}. \n"
        f"**Setting:** {setting}. \n"
        f"**Camera Action:** {camera_style}. \n"
        f"**Details:** Cloth physics, real life textures. {ar}"
    )
    
    st.success("Đã tạo prompt phong cách chân thực!")
    st.code(final_prompt, language="markdown")
    
    st.info("💡 **Giải thích:** App đã tự động thêm các từ khóa như 'Raw footage', 'Shot on iPhone', 'Non-cinematic' để loại bỏ cảm giác giả tạo của AI, giúp ánh sáng trông đời thường nhất.")
