import customtkinter as ctk
from tkinter import messagebox
from deep_translator import GoogleTranslator

# Oyna sozlamalari (Dark Mode)
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")

class TranslatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Global Translator Pro")
        self.geometry("500x700")

        # Sarlavha
        self.title_label = ctk.CTkLabel(self, text="GLOBAL TRANSLATOR", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.pack(pady=30)

        # Asosiy konteyner
        self.container = ctk.CTkFrame(self, corner_radius=20)
        self.container.pack(pady=10, padx=30, fill="both", expand=True)

        # Kiritish qismi
        self.label_in = ctk.CTkLabel(self.container, text="Matnni kiriting:", font=ctk.CTkFont(size=14))
        self.label_in.pack(pady=(20, 5), padx=20, anchor="w")
        
        self.text_entry = ctk.CTkTextbox(self.container, height=120, corner_radius=15, border_width=2)
        self.text_entry.pack(pady=5, padx=20, fill="x")

        # Til tanlash
        self.label_lang = ctk.CTkLabel(self.container, text="Target Language:", font=ctk.CTkFont(size=14))
        self.label_lang.pack(pady=(15, 5), padx=20, anchor="w")
        
        self.lang_selection = ctk.CTkOptionMenu(self.container, 
                                                values=["Arabcha", "O'zbekcha", "English", "Ruscha", "Turkcha", "Nemischa", "Fransuzcha"],
                                                corner_radius=10)
        self.lang_selection.set("Arabcha")
        self.lang_selection.pack(pady=5, padx=20, fill="x")

        # Tarjima tugmasi
        self.translate_btn = ctk.CTkButton(self.container, text="TARJIMA QILISH", 
                                           command=self.translate_text,
                                           font=ctk.CTkFont(size=16, weight="bold"),
                                           height=45, corner_radius=10,
                                           fg_color="#1a73e8", hover_color="#1557b0")
        self.translate_btn.pack(pady=30, padx=20, fill="x")

        # Natija qismi
        self.label_out = ctk.CTkLabel(self.container, text="Natija:", font=ctk.CTkFont(size=14))
        self.label_out.pack(pady=(5, 5), padx=20, anchor="w")
        
        self.output_text = ctk.CTkTextbox(self.container, height=120, corner_radius=15, border_width=2, state="disabled")
        self.output_text.pack(pady=5, padx=20, fill="x")

        # Pastki qism (Copy button)
        self.copy_btn = ctk.CTkButton(self, text="Nusxa olish", width=100, 
                                      fg_color="transparent", border_width=1,
                                      command=self.copy_to_clipboard)
        self.copy_btn.pack(pady=20)

    def translate_text(self):
        input_text = self.text_entry.get("1.0", "end-1c")
        target_lang = self.lang_selection.get()
        
        lang_codes = {
            "Arabcha": "ar", "O'zbekcha": "uz", "English": "en",
            "Ruscha": "ru", "Turkcha": "tr", "Nemischa": "de", "Fransuzcha": "fr"
        }

        if not input_text.strip():
            messagebox.showwarning("Xato", "Iltimos, matn kiriting!")
            return

        try:
            dest_lang = lang_codes.get(target_lang, "ar")
            translator = GoogleTranslator(source='auto', target=dest_lang)
            result = translator.translate(input_text)

            self.output_text.configure(state="normal")
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", result)
            self.output_text.configure(state="disabled")
        except Exception:
            messagebox.showerror("Xatolik", "Internet aloqasini tekshiring!")

    def copy_to_clipboard(self):
        text = self.output_text.get("1.0", "end-1c")
        if text:
            self.clipboard_clear()
            self.clipboard_append(text)
            messagebox.showinfo("Muvaffaqiyat", "Matn nusxalandi!")

if __name__ == "__main__":
    app = TranslatorApp()
    app.mainloop()
