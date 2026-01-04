import streamlit as st

# --- CẤU HÌNH GIAO DIỆN ---
st.set_page_config(
    page_title="Veo 3.1 Director Mode",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS tùy chỉnh giao diện
st.markdown("""
<style>
    div.stButton > button:first-child {
        background-color: #2c3e50;
        color: white;
        font-size: 22px;
        font-weight: bold;
        padding: 15px 30px;
        border-radius: 8px;
        width: 100%;
        border: 1px solid #34495e;
    }
    .section-title {
        font-size: 18px;
        font-weight: 700;
        color: #e67e22; /* Màu cam nổi bật */
        margin-top: 20px;
        margin-bottom: 10px;
        text-transform: uppercase;
        border-bottom: 1px solid #ddd;
    }
    .tooltip {
        font-size: 12px;
        color: #7f8c8d;
    }
</style>
""", unsafe_allow_html=True)

st.title("🎬 Veo 3.1: Fashion Director Mode")
st.markdown("Chế độ đạo diễn: Kiểm soát chi tiết **Góc Quay** và **Phối Hợp Dáng (Mix & Match)**.")
st.markdown("---")

# --- SIDEBAR ---
with st.sidebar:
    st.header("⚙️ Thông số kỹ thuật")
    video_ratio = st.selectbox("Tỷ lệ khung hình", ["9:16 (TikTok/Reels)", "16:9 (Youtube Cinematic)", "4:3 (Classic Film)", "1:1 (Square)"])
    duration = st.slider("Thời lượng video (giây)", 5, 60, 10)
    
    st.divider()
    st.markdown("### 💡 Mẹo góc máy")
    st.info("""
    - **Low Angle:** Hack dáng, chân dài, quyền lực.
    - **High Angle:** Dễ thương, mắt to, art.
    - **Dutch Angle:** Nghiêng máy, tạo cảm giác năng động/phá cách.
    """)

# --- CỘT 1: NỘI DUNG CỐT LÕI ---
col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.markdown('<div class="section-title">1. Diễn viên & Trang phục</div>', unsafe_allow_html=True)
    
    # Upload giữ nguyên vì rất quan trọng
    uploaded_img = st.file_uploader("Ảnh tham khảo (Visual Reference)", type=['jpg', 'png'])
    if uploaded_img:
        st.image(uploaded_img, width=200)

    model_desc = st.text_area("Mô tả người mẫu (Model)", 
                              "A cool Gen-Z fashion model, platinum blonde bob hair, sharp eyeliner", height=70)
    outfit_desc = st.text_area("Mô tả trang phục (Outfit)", 
                               "Oversized leather jacket, baggy denim jeans, silver chunky necklace", height=70)

    st.markdown('<div class="section-title">2. Bối cảnh (Setting)</div>', unsafe_allow_html=True)
    setting_type = st.selectbox("Loại bối cảnh", [
        "Urban/Street (Đường phố)", 
        "Nature/Beach (Thiên nhiên)", 
        "Studio/Abstract (Trong nhà)", 
        "Luxury/Night (Sang trọng)"
    ])
    
    custom_setting = st.text_input("Chi tiết bối cảnh", "Busy Shibuya crossing at night with neon signs")

# --- CỘT 2: ĐẠO DIỄN HÌNH ẢNH (NÂNG CẤP MẠNH) ---
with col2:
    st.markdown('<div class="section-title">3. Góc Quay Điện Ảnh (Camera Angles)</div>', unsafe_allow_html=True)
    
    # Dictionary chứa góc quay và định nghĩa prompt
    cam_options = {
        "🎥 Eye Level (Ngang tầm mắt)": "eye-level shot, neutral perspective, documentary style",
        "🐛 Low Angle (Hất từ dưới - Hack chân)": "low angle shot looking up, worm's-eye view, making subject look tall and powerful, elongating legs",
        "🦅 High Angle (Góc cao - Drone/CCTV)": "high angle shot looking down, drone view, fashion editorial perspective",
        "🤪 Dutch Angle (Nghiêng máy - Cá tính)": "Dutch angle, tilted camera horizon, dynamic and edgy composition",
        "🔍 Close-up Detail (Cận chất liệu/Mặt)": "extreme close-up macro shot, focus on fabric texture and skin details, shallow depth of field",
        "🏃 Tracking Shot (Camera chạy theo mẫu)": "tracking shot moving backwards as model walks forward, smooth gimbal movement",
        "🔄 360 Orbit (Xoay vòng quanh mẫu)": "360-degree orbit camera movement circling around the subject, bullet time effect",
        "🤳 Selfie/POV (Góc nhìn thứ nhất)": "handheld selfie camera angle, POV shot looking down at outfit, authentic vlogger style"
    }
    
    camera_select = st.selectbox("Chọn góc máy chủ đạo:", list(cam_options.keys()))
    
    st.markdown('<div class="section-title">4. Phối Hợp Dáng (Pose Mix & Match)</div>', unsafe_allow_html=True)
    st.caption("Ghép 3 yếu tố để tạo ra hàng trăm kiểu dáng độc nhất.")
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("**A. Thân (Body)**")
        body_pose = st.selectbox("Dáng người:", [
            "Đi catwalk (Walking)",
            "Chạy đùa (Running)",
            "Xoay váy (Spinning)",
            "Đứng tựa tường (Leaning)",
            "Ngồi ghế cao (Sitting Stool)",
            "Ngồi bệt (Sitting Floor)",
            "Nhảy múa (Dancing)",
            "Đứng yên gió thổi (Static)"
        ])
        
    with c2:
        st.markdown("**B. Tay (Hands)**")
        hand_pose = st.selectbox("Tương tác tay:", [
            "Thả lỏng (Relaxed)",
            "Vuốt tóc (Touching hair)",
            "Đút túi (Hands in pocket)",
            "Chỉnh kính/Mũ (Adjusting acc)",
            "Cầm túi xách (Holding bag)",
            "Che nắng (Shielding eyes)",
            "Khoanh tay (Crossed arms)",
            "Cầm điện thoại (Holding phone)"
        ])
        
    with c3:
        st.markdown("**C. Mặt (Face)**")
        face_pose = st.selectbox("Thần thái:", [
            "Nhìn thẳng Cam (Eye contact)",
            "Nhìn xa xăm (Looking away)",
            "Cười rạng rỡ (Laughing)",
            "Nháy mắt (Winking)",
            "Lạnh lùng (Poker face)",
            "Quay đầu lại (Looking back)"
        ])

# --- XỬ LÝ PROMPT ---
st.markdown("---")
if st.button("🎬 ACTION! TẠO PROMPT"):
    # 1. Map dữ liệu
    # Map Body
    body_map = {
        "Đi catwalk (Walking)": "walking confidently like a runway model",
        "Chạy đùa (Running)": "running playfully towards camera",
        "Xoay váy (Spinning)": "twirling around to show the dress movement",
        "Đứng tựa tường (Leaning)": "leaning coolly against a wall",
        "Ngồi ghế cao (Sitting Stool)": "sitting elegantly on a high stool",
        "Ngồi bệt (Sitting Floor)": "sitting on the ground, legs crossed casually",
        "Nhảy múa (Dancing)": "dancing freely to music",
        "Đứng yên gió thổi (Static)": "standing still power pose, wind blowing clothes"
    }
    
    # Map Hands
    hand_map = {
        "Thả lỏng (Relaxed)": "arms relaxed by sides",
        "Vuốt tóc (Touching hair)": "one hand running through hair",
        "Đút túi (Hands in pocket)": "hands casually in pockets",
        "Chỉnh kính/Mũ (Adjusting acc)": "adjusting sunglasses or hat",
        "Cầm túi xách (Holding bag)": "holding a luxury handbag",
        "Che nắng (Shielding eyes)": "hand shielding eyes from the sun",
        "Khoanh tay (Crossed arms)": "arms crossed over chest",
        "Cầm điện thoại (Holding phone)": "holding a smartphone taking a selfie"
    }
    
    # Map Face
    face_map = {
        "Nhìn thẳng Cam (Eye contact)": "intense eye contact with the camera",
        "Nhìn xa xăm (Looking away)": "looking away thoughtfully into the distance",
        "Cười rạng rỡ (Laughing)": "laughing naturally with a bright smile",
        "Nháy mắt (Winking)": "winking playfully at the viewer",
        "Lạnh lùng (Poker face)": "serious, high-fashion cold expression",
        "Quay đầu lại (Looking back)": "looking back over the shoulder"
    }

    # 2. Xử lý kỹ thuật
    ar_code = "--ar 9:16"
    if "16:9" in video_ratio: ar_code = "--ar 16:9"
    elif "4:3" in video_ratio: ar_code = "--ar 4:3"
    elif "1:1" in video_ratio: ar_code = "--ar 1:1"

    cam_prompt = cam_options[camera_select]
    
    # 3. Ghép chuỗi hành động (Quan trọng)
    # Cấu trúc: [Subject] is [Body Action] while [Hand Action], [Face Action].
    action_sequence = f"{body_map[body_pose]} while {hand_map[hand_pose]}, {face_map[face_pose]}"

    # 4. Final Prompt
    final_prompt = (
        f"**Veo 3.1 Prompt:**\n\n"
        f"High quality fashion video. "
        f"**Shot type:** {cam_prompt}. \n"
        f"**Subject:** {model_desc} wearing {outfit_desc}. \n"
        f"**Action:** {action_sequence}. \n"
        f"**Setting:** {custom_setting}. \n"
        f"**Details:** 4k, photorealistic, cinematic lighting, cloth physics simulation. {ar_code}"
    )
    
    st.success("✅ Đã tạo xong kịch bản quay!")
    st.code(final_prompt, language="markdown")
    
    # Gợi ý phân tích prompt
    with st.expander("🔍 Giải thích cấu trúc Prompt này"):
        st.write(f"- **Góc máy:** {camera_select} (Giúp AI định hình không gian)")
        st.write(f"- **Hành động kép:** {body_pose} + {hand_pose} (Tạo sự tự nhiên)")
        st.write(f"- **Thần thái:** {face_pose} (Tạo cảm xúc kết nối)")
