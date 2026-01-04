import streamlit as st

# --- CẤU HÌNH GIAO DIỆN ---
st.set_page_config(
    page_title="Veo 3.1 UGC Pro: Posing Master",
    page_icon="💃",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS tùy chỉnh
st.markdown("""
<style>
    div.stButton > button:first-child {
        background-color: #000000;
        color: white;
        font-size: 20px;
        font-weight: bold;
        border-radius: 12px;
        padding: 12px 24px;
        width: 100%;
    }
    .sub-header {
        font-size: 18px;
        font-weight: bold;
        color: #333;
        margin-top: 10px;
        margin-bottom: 5px;
        border-bottom: 2px solid #ddd;
        padding-bottom: 5px;
    }
</style>
""", unsafe_allow_html=True)

st.title("💃 Veo 3.1: Fashion Posing & Product Showcase")
st.markdown("Chuyên sâu về các hành động **tạo dáng (Posing)** và **tương tác sản phẩm**.")
st.markdown("---")

# --- SIDEBAR: CẤU HÌNH CHUNG ---
with st.sidebar:
    st.header("⚙️ Cấu hình Video")
    video_ratio = st.radio("Tỷ lệ khung hình", ["9:16 (TikTok/Reels)", "16:9 (Youtube)", "1:1 (Insta)"])
    st.divider()
    st.info("💡 **Tips:** Để video bán hàng tốt, hãy kết hợp 'Hành động toàn thân' với 'Tương tác tay' (ví dụ: Vừa đi vừa chỉnh túi xách).")

# --- CỘT 1: INPUT CƠ BẢN (MẪU & ĐỒ) ---
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown('<div class="sub-header">1. Mẫu & Sản phẩm</div>', unsafe_allow_html=True)
    
    # Upload ảnh (Giữ nguyên từ bản trước vì rất hữu ích)
    uploaded_img = st.file_uploader("Upload ảnh tham khảo (Optional)", type=['png', 'jpg'])
    if uploaded_img:
        st.image(uploaded_img, width=200)

    model_desc = st.text_input("Mô tả Mẫu", "Asian female model, street style look, bob hair")
    outfit_desc = st.text_area("Mô tả Trang phục", "White silk dress, flowy fabric, pearl buttons", height=80)
    
    st.markdown('<div class="sub-header">2. Bối cảnh & Ánh sáng</div>', unsafe_allow_html=True)
    setting = st.selectbox("Địa điểm", [
        "Đường phố (Street/Urban)", "Studio phông trơn (Minimalist)", 
        "Quán Cafe (Lifestyle)", "Công viên/Bãi cỏ (Nature)", "Phòng ngủ (Indoor/Cozy)"
    ])
    lighting = st.selectbox("Ánh sáng", [
        "Nắng tự nhiên (Natural Sunlight)", "Nắng giờ vàng (Golden Hour)", 
        "Ánh sáng cửa sổ (Soft Window Light)", "Đèn Flash (Flash Photography)"
    ])

# --- CỘT 2: HÀNH ĐỘNG CHUYÊN SÂU (MỚI) ---
with col2:
    st.markdown('<div class="sub-header">3. Chọn Hành động (Posing)</div>', unsafe_allow_html=True)
    
    # Chia hành động thành 3 Tab để dễ chọn
    tab_body, tab_interact, tab_detail = st.tabs(["💃 Toàn thân", "🤚 Tương tác/Vải", "👜 Phụ kiện/Giày"])
    
    with tab_body:
        st.caption("Dùng cho video Lookbook, Outfit check")
        body_action = st.radio("Chọn dáng chính:", [
            "Đi thẳng về phía camera (Catwalk)",
            "Xoay vòng 360 độ (Twirl - Khoe váy xòe)",
            "Đứng tựa tường/lan can (Pose tĩnh)",
            "Ngồi cafe/đọc sách (Lifestyle)",
            "Chạy nhảy vui vẻ (Dynamic/Vui tươi)"
        ], index=0)
    
    with tab_interact:
        st.caption("Dùng để mô tả chất lượng sản phẩm")
        hand_action = st.radio("Chọn tương tác tay:", [
            "Không có (None)",
            "Tay vuốt dọc thân áo (Khoe phom dáng)",
            "Cầm vạt váy tung nhẹ (Khoe độ bay)",
            "Chỉnh cổ áo/Cài cúc (Chi tiết may)",
            "Đút tay túi quần (Cool ngầu)",
            "Vuốt tóc/Vén tóc (Tự nhiên)"
        ], index=0)
        
    with tab_detail:
        st.caption("Dùng cho bán Giày, Túi, Trang sức")
        acc_action = st.radio("Chọn góc quay phụ kiện:", [
            "Không có (None)",
            "Cận cảnh túi xách trên tay",
            "Góc thấp quay bước chân/Giày (Low angle)",
            "Zoom vào trang sức (Khuyên tai/Vòng cổ)",
            "Mở túi/lấy đồ (Unboxing vibe)"
        ], index=0)

    st.markdown('<div class="sub-header">4. Cảm xúc (Vibe)</div>', unsafe_allow_html=True)
    vibe = st.select_slider("Thần thái của mẫu", options=["Lạnh lùng/Cool", "Tự tin/Confident", "Vui vẻ/Smiling", "Mơ màng/Dreamy"])

# --- XỬ LÝ LOGIC TẠO PROMPT ---
st.markdown("---")
if st.button("🚀 TẠO PROMPT CHI TIẾT"):
    # 1. Map hành động sang tiếng Anh chuẩn Veo
    action_map = {
        "Đi thẳng về phía camera (Catwalk)": "walking confidently towards the camera, runway walk style",
        "Xoay vòng 360 độ (Twirl - Khoe váy xòe)": "doing a slow 360 degree spin to show the flow of the dress",
        "Đứng tựa tường/lan can (Pose tĩnh)": "leaning casually against a wall, posing for a photo",
        "Ngồi cafe/đọc sách (Lifestyle)": "sitting relaxed at a cafe table, drinking coffee",
        "Chạy nhảy vui vẻ (Dynamic/Vui tươi)": "running playfully, laughing, dynamic movement"
    }
    
    hand_map = {
        "Không có (None)": "",
        "Tay vuốt dọc thân áo (Khoe phom dáng)": "hands running down the fabric to show texture",
        "Cầm vạt váy tung nhẹ (Khoe độ bay)": "holding the skirt hem and playing with the fabric",
        "Chỉnh cổ áo/Cài cúc (Chi tiết may)": "adjusting the collar, fixing the buttons",
        "Đút tay túi quần (Cool ngầu)": "hands in pockets, cool attitude",
        "Vuốt tóc/Vén tóc (Tự nhiên)": "tucking hair behind ear, fixing hairstyle"
    }

    acc_map = {
        "Không có (None)": "",
        "Cận cảnh túi xách trên tay": "focus on the handbag held in hand",
        "Góc thấp quay bước chân/Giày (Low angle)": "low angle shot focusing on shoes walking on pavement",
        "Zoom vào trang sức (Khuyên tai/Vòng cổ)": "extreme close-up on the earrings and necklace",
        "Mở túi/lấy đồ (Unboxing vibe)": "hands opening the bag, interacting with accessories"
    }
    
    lighting_map = {
        "Nắng tự nhiên (Natural Sunlight)": "natural daylight, bright",
        "Nắng giờ vàng (Golden Hour)": "golden hour warm sunlight, lens flare",
        "Ánh sáng cửa sổ (Soft Window Light)": "soft window lighting, diffused",
        "Đèn Flash (Flash Photography)": "direct camera flash, night aesthetic"
    }

    # 2. Xây dựng chuỗi hành động kết hợp
    # Logic: Nếu có action phụ kiện -> Ưu tiên mô tả phụ kiện. Nếu không -> Mô tả dáng + tay.
    combined_action = f"{action_map[body_action]}"
    if hand_action != "Không có (None)":
        combined_action += f", while {hand_map[hand_action]}"
    if acc_action != "Không có (None)":
        combined_action += f", camera emphasizes {acc_map[acc_action]}"

    # 3. Tạo Prompt
    ar = "--ar 9:16" if "9:16" in video_ratio else "--ar 16:9"
    if "1:1" in video_ratio: ar = "--ar 1:1"

    final_prompt = (
        f"**Veo Prompt:**\n\n"
        f"Realistic UGC fashion video, shot on iPhone. "
        f"**Subject:** {model_desc} wearing {outfit_desc}. \n"
        f"**Action:** {combined_action}. \n"
        f"**Vibe:** {vibe} expression. \n"
        f"**Environment:** {setting}, {lighting_map[lighting]}. \n"
        f"**Details:** Real life texture, cloth physics, authentic look, 4k footage. {ar}"
    )

    st.success("Đã tạo prompt với hành động chi tiết!")
    st.code(final_prompt, language="markdown")
    st.caption("Copy và dán vào Veo. Lưu ý: Các hành động như 'Sờ vải' hay 'Xoay' sẽ giúp AI tạo ra chuyển động vật lý rất đẹp.")
