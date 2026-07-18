import streamlit as st
from ultralytics import YOLO
from PIL import Image
import ollama 
from datetime import date
st.title("AI System for Industry Quality Assurance")
st.subheader('This is AI model that helps you detect defect in steel surface in your factory and generates AI-powered maintainence report.')
st.write('Enter image below to proceed further')

uploaded_image=st.file_uploader('upload steel surface image here:',type=['png','jpg','jpeg'])
model=YOLO('best.pt')

inspection_date = st.date_input(
    "Select Inspection Date",
    value=date.today()
)

if uploaded_image:
    st.image(uploaded_image,st.write('original image'))
    st.success('image is uploaded successfully :)')
    image=Image.open(uploaded_image)
    if st.button('detect defects'):
        results=model.predict(image)
        img_with_bounded_boxes=results[0].plot()
        st.image(img_with_bounded_boxes,st.write('defects detected'))
        detections = []

        for box in results[0].boxes:
            class_id = int(box.cls)
            confidence = float(box.conf)

            defect_name = model.names[class_id]
            detections.append(
                f"{defect_name} ({confidence*100:.1f}%)"
            )

        if len(detections) == 0:
            detections.append("No defects detected")

        reply=ollama.chat(
         model="llama3.2",
        messages=[
            {
            "role": "user",
            "content": f"""Generate a professional inspection report in exactly this format- Inspection Report, Inspection date:{inspection_date} Detected Defects:Detected Defects:{chr(10).join("- " + d for d in detections)} Summary: Write 2-3 sentences describing the detected defects. Severity:Low, Medium, or High. Recommended Actions:- Action 1, - Action 2, - Action 3"""            
            }
                ]
        )
        st.write(reply["message"]["content"])



   



 