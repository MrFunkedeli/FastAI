import gradio as gr
from fastai.vision.all import *


def is_cat(x): return x[0].isupper()


learn = load_learner('basicFAI.pkl')

categories = ('Dog', 'Cat')


def classify_image(img):
    pred, ids, probs = learn.predict(img)
    return dict(zip(categories, map(float, probs)))


image = gr.inputs.Image(shape=(192, 192))
label = gr.outputs.Label()
examples = ['dog1.jpg', 'cat1.jpg', 'dunno1.jpg']

iface = gr.Interface(fn=classify_image, inputs=image, outputs=label, examples=examples)
iface.launch(inline=False)