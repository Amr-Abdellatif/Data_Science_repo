import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk
from authtoken import auth_token 
import torch 
from torch import autocast 
from diffusers import StableDiffusionPipeline
import uuid


#create the app
app = tk.Tk()
app.geometry("532x622")
app.title('AI photo generator')
ctk.set_appearance_mode("dark")

#entry prompt for the description of our photo
prompt = ctk.CTkEntry(height=50,width=500,text_font=("Arial",20),text_color="black",fg_color="white")
prompt.place(x=20,y=10)

#the size of our photo in the GUI
lmain=ctk.CTkLabel(height=512,width=512) 
lmain.place(x=10,y=110)

#calling the model from huggingface.com
modelid ="CompVis/stable-diffusion-v1-4"
device = "cuda"
pipe = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16",torch_dtype=torch.float16  ,use_auth_token=auth_token)
pipe.to(device)

#function to generate the photo and save it
image_path = 'yourpath/folder_to_generate_images_to'
def Generate():
    with autocast(device):
        image=pipe(prompt.get(),guidance_scale=8.5)["sample"][0]
    image.save(f'{image_path}/Generatedimage{uuid.uuid4()}.png')
    img = ImageTk.PhotoImage(image)
    lmain.configure(image=img)

#making a Generate trigger button 
trigger = ctk.CTkButton(height=40,width=120,text_font=("Arial",20),text_color="white",fg_color="blue",command=Generate)
trigger.configure(text="Generate")
trigger.place(x=206,y=70)

app.mainloop()
