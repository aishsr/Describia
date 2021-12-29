import gradio as gr


def image_to_text(image):

    description = 'A sample description'
    return description


iface = gr.Interface(
    fn=image_to_text,
    inputs='image',
    outputs='text'
)
iface.launch()
