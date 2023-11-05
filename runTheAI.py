# Load model directly
from transformers import ViltProcessor, ViltForQuestionAnswering

def answer_question(question, image_path):
    processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
    model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

    from PIL import Image

    #image_path = "./resiInt/resiInt1.jpeg"
    image = Image.open(image_path)
    encoding = processor(image, question, return_tensors="pt")
    outputs = model(**encoding)
    sorted_indexs = outputs.logits.argsort(dim=-1, descending=True)[0].tolist()

    top_prediction = model.config.id2label[sorted_indexs[0]]

    return top_prediction

#loop over all images in the /resiInt folder and ask the AI questions about them
# get resiInt folder size
import os
path, dirs, files = next(os.walk("./resiInt"))
file_count = len(files)
data_set = {}
for i in range(file_count):
    if (i != file_count-1):
        image_name = "./resiInt/resiInt" + str(i+1) + ".jpeg"

        text = "Is this image of the inside or outside of a building?"
        if (answer_question(text, image_name) == "inside"):

            text = "Is the floor made of valuable materials?"
            if (answer_question(text, image_name) == "yes"):
                
                text = "Is the floor made of wood?"
                if (answer_question(text, image_name) == "yes"):
                    data_set["wood"] = "yes"
                elif (answer_question(text, image_name) == "no"):
                    data_set["wood"] = "no"

                text = "Is the floor made of tiles?"
                if (answer_question(text, image_name) == "yes"):
                    data_set["tiles"] = "yes"
                elif (answer_question(text, image_name) == "no"):
                    data_set["tiles"] = "no"

                text = "Is the floor made of marble?"
                if (answer_question(text, image_name) == "yes"):
                    data_set["marble"] = "yes"
                elif (answer_question(text, image_name) == "no"):
                    data_set["marble"] = "no"

            elif (answer_question(text, image_name) == "no"):
                data_set["valuable materials"] = "no"

            text = "Do the walls have cracks on them?"
            if (answer_question(text, image_name) == "yes"):
                data_set["wallCracks"] = "yes"
                text = "Do the walls look like they are about to collapse?"
                if (answer_question(text, image_name) == "yes"):
                    data_set["wallCollapse"] = "yes"
                elif (answer_question(text, image_name) == "no"):
                    data_set["wallCollapse"] = "no"
            elif (answer_question(text, image_name) == "no"):
                data_set["wallCracks"] = "no"

            text = "Does the ceiling look like it has cracks in it?"
            if (answer_question(text, image_name) == "yes"):
                data_set["ceilingCracks"] = "yes"
                text = "Does the ceiling look like it is about to collapse?"
                if (answer_question(text, image_name) == "yes"):
                    data_set["ceilingCollapse"] = "yes"
                elif (answer_question(text, image_name) == "no"):
                    data_set["ceilingCollapse"] = "no"
            elif (answer_question(text, image_name) == "no"):
                data_set["ceilingCracks"] = "no"
            
            text = "Do the windows look like they have been damaged?"
            if (answer_question(text, image_name) == "yes"):
                data_set["windowsDamaged"] = "yes"
            elif (answer_question(text, image_name) == "no"):
                data_set["windowsDamaged"] = "no"

            text = "Do the doors look like they have been damaged?"
            if (answer_question(text, image_name) == "yes"):
                data_set["doorsDamaged"] = "yes"
            elif (answer_question(text, image_name) == "no"):
                data_set["doorsDamanged"] = "no"
            
        elif (answer_question(text, image_name) == "outside"):
            text = "Is the building made of wood?"
            if (answer_question(text, image_name) == "yes"):
                data_set["outsideMaterialWood"] = "yes"
            elif (answer_question(text, image_name) == "no"):
                data_set["outsideMaterialWood"] = "no" 

            text = "Is the building made of bricks?"
            if (answer_question(text, image_name) == "yes"):
                data_set["outsideMaterialBrick"] = "yes"
            elif (answer_question(text, image_name) == "no"):
                data_set["outsideMaterialBrick"] = "no"

            text = "Is the building made of glass?"
            if (answer_question(text, image_name) == "yes"):
                data_set["outsideMaterialGlass"] = "yes"
            elif (answer_question(text, image_name) == "no"):
                data_set["outsideMaterialGlass"] = "no"

            text = "Is the building made of marble?"
            if (answer_question(text, image_name) == "yes"):
                data_set["outsideMaterialMarble"] = "yes"
            elif (answer_question(text, image_name) == "no"):
                data_set["outsideMaterialMarble"] = "no"

            text = "Do you see any defects in the outside?"
            if (answer_question(text, image_name) == "yes"):
                data_set["doYouSeeDefects"] = "yes"
                text = "What is that defect?"
                data_set["whatIsThatDefect"] = answer_question(text, image_name)
            elif (answer_question(text, image_name) == "no"):
                data_set["doYouSeeDefects"] = "no"

            text = "Would it be a safe neighborhood to live in?"
            if (answer_question(text, image_name) == "yes"):
                data_set["isItASafeNeighborhood"] = "yes"
            elif (answer_question(text, image_name) == "no"):
                data_set["isItASafeNeighborhood"] = "no"