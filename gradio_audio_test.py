import gradio as gr
import numpy as np

def process_audio(audio):
    """
    Simple function to verify audio input is working.
    Prints debug info and returns basic audio stats.
    """
    if audio is None:
        return "No audio received"
    
    sr, y = audio
    duration = len(y)/sr
    
    # Basic audio statistics
    stats = f"""
    Audio received:
    - Duration: {duration:.2f}s
    - Sample rate: {sr}Hz
    - Shape: {y.shape}
    - Range: [{np.min(y):.3f}, {np.max(y):.3f}]
    - Mean: {np.mean(y):.3f}
    - RMS: {np.sqrt(np.mean(y**2)):.3f}
    """
    print(stats)  # For server-side debug
    return stats

# Create minimal interface
with gr.Blocks() as demo:
    gr.Markdown("## Gradio Audio Test")
    
    with gr.Row():
        audio_input = gr.Audio(
            sources=["microphone"],
            type="numpy",
            label="Record Audio",
            interactive=True
        )
    
    with gr.Row():
        stats_output = gr.Textbox(
            label="Audio Statistics",
            lines=8
        )
    
    # Process button
    process_btn = gr.Button("Process Audio")
    process_btn.click(
        fn=process_audio,
        inputs=audio_input,
        outputs=stats_output
    )

if __name__ == "__main__":
    demo.queue().launch(share=True, debug=True)