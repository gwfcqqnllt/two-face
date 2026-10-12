import streamlit as st
import subprocess
import os

st.set_page_config(page_title="YOLO 视觉应用", layout="centered")
st.title("📷 YOLO 实时视觉应用")
st.write("上传一张图片，系统将自动进行目标检测。")

uploaded_file = st.file_uploader("选择图片", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img_path = "uploaded_temp.jpg"
    with open(img_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.image(img_path, caption="已上传图片", use_container_width=True)

    if st.button("开始识别"):
        with st.spinner("正在调用 YOLO 模型进行推理..."):
            yolo_exe = r"C:\Users\aojia\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\Scripts\yolo.exe"

            try:
                subprocess.run(
                    [yolo_exe, 'detect', 'predict', 'model=runs/detect/train/weights/best.pt', f'source={img_path}',
                     'save=True'],
                    cwd='.', check=True, timeout=60
                )
                st.success("✅ YOLO 识别成功！")

                base_dir = "runs/detect"
                predict_dirs = [os.path.join(base_dir, d) for d in os.listdir(base_dir) if
                                d.startswith("predict") and os.path.isdir(os.path.join(base_dir, d))]
                predict_dir = max(predict_dirs, key=os.path.getctime) if predict_dirs else ""
                if predict_dir and os.path.exists(predict_dir):
                    files = os.listdir(predict_dir)
                    if files:
                        latest_file = max([os.path.join(predict_dir, f) for f in files], key=os.path.getctime)
                        # 这里把显示宽度改为 use_container_width
                        st.image(latest_file, caption="YOLO 检测结果", use_container_width=True)
                        st.balloons()
                    else:
                        st.warning("预测目录为空。")
                else:
                    st.warning("找不到预测结果目录。")
            except subprocess.TimeoutExpired:
                st.error("推理超时，请重试。")
            except Exception as e:
                st.error(f"发生错误：{e}")