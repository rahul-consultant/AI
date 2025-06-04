# Contents of /evisa-visual-impaired/evisa-visual-impaired/src/main.py

import os
import gradio as gr
from utils.audio import talker
from utils.pdf import create_visa_application_pdf
from utils.photo import auto_capture_photo
from utils.openai_api import chat_with_openai
from dotenv import load_dotenv

load_dotenv()

def main():
    history = []
    photo_b64 = None
    collected = {}

    with gr.Blocks() as demo:
        gr.Markdown("## Eazee: Voice-Driven E-Visa Assistant for the Visually Impaired")
        audio_input = gr.Audio(sources=["microphone"], type="filepath", label="Speak to the assistant")
        output_text = gr.Textbox(label="Assistant", interactive=False)
        pdf_file = gr.File(label="Download Visa Application PDF")

        def auto_submit(audio, history, photo_b64):
            return chat_with_openai(audio, history, photo_b64, collected)

        audio_input.change(
            auto_submit,
            inputs=[audio_input, history, photo_b64],
            outputs=[history, photo_b64, pdf_file, output_text]
        )

        gr.Markdown("If you need to repeat, just speak again.")

    demo.launch()

if __name__ == "__main__":
    main()