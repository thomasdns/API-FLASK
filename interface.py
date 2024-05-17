import customtkinter
from openai import OpenAI

# Initialisez votre client OpenAI avec votre clé API
client = OpenAI(api_key="API KEYS")

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

class RequestsApp(customtkinter.CTk):
    
    user_input = ""
    conversation = []  # Liste pour stocker les messages de la conversation
   
    def __init__(self):
        super().__init__()
        self.title("Mon application #1")
        self.geometry(f"{1100}x{580}")
        
        # Créer une grille de 3 lignes et 3 colonnes
        self.grid_rowconfigure((0,1,2), weight=1)
        self.grid_columnconfigure((0,1), weight=1)

        # Initialisation de la conversation
        self.conversation = []
    
        # Partie bouton et température
        self.buton_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0) 
        self.buton_frame.grid(row=0, column=1, rowspan=2, sticky="nsew")
        
        self.button = customtkinter.CTkButton(master=self.buton_frame, text="Cliquez ici", command=self.update_user_input)
        self.button.grid(pady=20, padx=20)
        
        # Partie température affichage 
        self.temperature_label = customtkinter.CTkLabel(master=self.buton_frame, text="Temperature :")
        self.temperature_label.grid(pady=20, padx=20)
        
        # Partie slider température
        self.temperature_slider = customtkinter.CTkSlider(master=self.buton_frame, from_=0.0, to=2.0, number_of_steps=20, command=self.update_temperature_label)
        self.temperature_slider.set(1.0)  # Valeur par défaut
        self.temperature_slider.grid(pady=20, padx=20)
        
        self.temperature_value_label = customtkinter.CTkLabel(master=self.buton_frame, text="1.0")
        self.temperature_value_label.grid(pady=10, padx=20)
        
        # Partie champs texte
        self.text_frame = customtkinter.CTkFrame(self, width=800, corner_radius=0) 
        self.text_frame.grid(row=0, column=0)
        
        self.user_text = customtkinter.CTkEntry(master=self.text_frame, height=10, width=800)
        self.user_text.grid()
        
        # Partie fil de conversation
        self.conversation_frame = customtkinter.CTkFrame(self, width=1000, corner_radius=0)
        self.conversation_frame.grid(row=1, column=0, columnspan=1)
        
        self.conversation_textbox = customtkinter.CTkTextbox(master=self.conversation_frame, height=400, width=800)
        self.conversation_textbox.grid()
        
        # Bouton pour réinitialiser la conversation
        self.reset_button = customtkinter.CTkButton(master=self.buton_frame, text="Réinitialiser conversation", command=self.reset_conversation)
        self.reset_button.grid(pady=20, padx=20)
       
    def update_user_input(self):
        # Récupérer le texte de l'utilisateur
        t = self.user_text.get()
        self.user_input = t

        # Ajouter le message de l'utilisateur à la conversation
        self.conversation.append({"role": "user", "content": self.user_input})
        
        # Mettre à jour la liste de conversation
        self.update_conversation_textbox()

        # Récupérer la température du slider
        temperature = self.temperature_slider.get()

        # Appeler l'API OpenAI avec la conversation
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=self.conversation,  # Passer tous les messages de la conversation à l'API
                temperature=temperature  # Ajuster la température ici
            )
            self.api_result = response.choices[0].message.content

            # Ajouter la réponse de l'IA à la conversation
            self.conversation.append({"role": "assistant", "content": self.api_result})
            
            # Mettre à jour la liste de conversation
            self.update_conversation_textbox()
        except Exception as e:
            self.conversation_textbox.configure(state="normal")
            self.conversation_textbox.insert("end", f"Erreur lors de la requête : {str(e)}\n")
            self.conversation_textbox.configure(state="disabled")

    def update_temperature_label(self, value):
        # Mettre à jour l'étiquette de la température
        self.temperature_value_label.configure(text=f"{value:.1f}")

    def reset_conversation(self):
        # Réinitialiser la conversation
        self.conversation = []
        # Mettre à jour la liste de conversation
        self.update_conversation_textbox()

    def update_conversation_textbox(self):
        self.conversation_textbox.configure(state="normal")
        self.conversation_textbox.delete("0.0", "end")
        for message in self.conversation:
            role = message["role"]
            content = message["content"]
            self.conversation_textbox.insert("end", f"{role}: {content}\n")
        self.conversation_textbox.see("end")  # Faire défiler jusqu'au dernier message
        self.conversation_textbox.configure(state="disabled")

if __name__ == "__main__":
    app_instance = RequestsApp()
    app_instance.mainloop()
