import gradio as gr
import numpy as np

def process_audio(audio):
    print("Audio processing started...")
    if audio is None:
        return "No audio received"
    
    sr, y = audio
    duration = len(y)/sr
    
    stats = f"""
    Audio received:
    - Duration: {duration:.2f}s
    - Sample rate: {sr}Hz
    - Shape: {y.shape}
    - Range: [{np.min(y):.3f}, {np.max(y):.3f}]
    - Mean: {np.mean(y):.3f}
    - RMS: {np.sqrt(np.mean(y**2)):.3f}
    """
    print(stats)
    return stats

demo = gr.Interface(
    fn=process_audio,
    inputs=gr.Audio(
        sources=["microphone"],
        type="numpy",
        streaming=False
    ),
    outputs="text",
    title="Audio Test"
)

if __name__ == "__main__":
    demo.queue().launch(share=True)  # Added queue()