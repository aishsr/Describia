# import gradio as gr
import prepareImageData as prepI
import prepareTextData as prepT
import developModel as devM


def setModel():
    print("Preparing image data ...")
    # prepI.prepareImageData()

    print(' ')

    print("Preparing text data ...")
    prepT.prepareTextData()

    print(' ')

    print("Preparing model ...")
    devM.prepareModel()


# Callback function to use the model
def image_to_text(image):
    description = 'A sample description'
    return description


def startUI():
    # Define UI interface
    iFace = gr.Interface(
        title='Describia',
        theme='default',
        fn=image_to_text,
        inputs=gr.inputs.Image(label='Your image'),
        outputs=gr.outputs.Textbox(label="What I think ..."),
        allow_screenshot=False,
        allow_flagging=False
    )

    # Launch interface
    iFace.launch(
        share=True
    )


def main():
    setModel()


if __name__ == "__main__":
    main()
