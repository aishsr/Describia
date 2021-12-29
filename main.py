import gradio as gr


# Callback function to use the model
def image_to_text(image):
    description = 'A sample description'
    return description


# Define UI interface
iFace = gr.Interface(
    title='Describia',
    theme ='grass',
    fn=image_to_text,
    inputs=gr.inputs.Image(label='Your image'),
    outputs=gr.outputs.Textbox(label="What I think ..."),
    allow_screenshot=False,
    allow_flagging=False
)

# Launch interface
iFace.launch()
