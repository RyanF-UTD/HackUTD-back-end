# from huggingface_hub import notebook_login

# # Use a pipeline as a high-level helper
# from transformers import pipeline

# pipe = pipeline("visual-question-answering", model="dandelin/vilt-b32-finetuned-vqa")


# from PIL import Image

# image_path = "./hotel-room-in-bad-condition.jpg"
# image = Image.open(image_path)
# text = "What are the defects in the image? Defects are basically things that seem wrong with all the features in the room."
# text2 = "Describe the image to me."


# out = pipe(image, text)

# print(out)
# print(out2)


# Load model directly
from transformers import ViltProcessor, ViltForQuestionAnswering

def answer_question(question):
    encoding = processor(image, question, return_tensors="pt")
    outputs = model(**encoding)
    sorted_indexs = outputs.logits.argsort(dim=-1, descending=True)[0].tolist()

    top_prediction = model.config.id2label[sorted_indexs[0]]

    return top_prediction

processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

from PIL import Image

image_path = "./hotel-room-in-bad-condition.jpg"
image = Image.open(image_path)

text = "Is this image of the inside or outside of a building?"
if (answer_question(text) == "inside"):

    text = "Is the floor made of valuable materials?"
    if (answer_question(text) == "yes"):
        
        text = "Is the floor made of wood?"
        if (answer_question(text) == "yes"):
            print("The floor is made of wood.")
        elif (answer_question(text) == "no"):
            text = "Is the floor made of marble?"
            if (answer_question(text) == "yes"):
                print("The floor is made of marble.")
            elif (answer_question(text) == "no"):
                print("The floor is made of other valuable materials.")
    elif (answer_question(text) == "no"):
        print("This is the inside of a building with no valuable materials.")

    text = "Do the walls have cracks on them?"
    if (answer_question(text) == "yes"):
        text = "Do the walls look like they are about to collapse?"
        if (answer_question(text) == "yes"):
            print("The walls are cracked and about to collapse.")
        elif (answer_question(text) == "no"):
            print("The walls are cracked but not about to collapse.")
    elif (answer_question(text) == "no"):
        print("The walls are not cracked.")

    text = "Does the ceiling look like it has cracks on it?"
    if (answer_question(text) == "yes"):
        text = "Does the ceiling look like it is about to collapse?"
        if (answer_question(text) == "yes"):
            print("The ceiling is cracked and about to collapse.")
        elif (answer_question(text) == "no"):
            print("The ceiling is cracked but not about to collapse.")
    
    text = "Do the windows have cracks in them?"
    if (answer_question(text) == "yes"):
        print("The windows are cracked.")
    elif (answer_question(text) == "no"):
        print("The windows are not cracked.")

    text = "Do the doors look like they have been damaged?"
    if (answer_question(text) == "yes"):
        print("The doors are damaged.")
    elif (answer_question(text) == "no"):
        print("The doors are not damaged.")

    
elif (answer_question(text) == "outside"):
    text = "Is the building made of valuable materials?"
    if (answer_question(text) == "yes"):
        text = "Is the building made of wood?"
        if (answer_question(text) == "yes"):
            print("The building is made of wood.")
        elif (answer_question(text) == "no"):
            text = "Is the building made of marble?"
            if (answer_question(text) == "yes"):
                print("The building is made of marble.")
            elif (answer_question(text) == "no"):
                print("The building is made of other valuable materials.")

    text = "Do the walls have cracks on them?"
    if (answer_question(text) == "yes"):
        text = "Do the walls look like they are about to collapse?"
        if (answer_question(text) == "yes"):
            print("The walls are cracked and about to collapse.")
        elif (answer_question(text) == "no"):
            print("The walls are cracked but not about to collapse.")
    elif (answer_question(text) == "no"):
        print("The walls are not cracked.")

    text = "Would it be a safe neighborhood to live in?"
    if (answer_question(text) == "yes"):
        print("This is a safe neighborhood.")
    elif (answer_question(text) == "no"):
        print("This is not a safe neighborhood.")