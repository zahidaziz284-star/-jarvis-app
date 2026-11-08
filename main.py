from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.clock import Clock
import datetime, requests, webbrowser, threading

GEMINI_API_KEY = "AQ.Ab8RN6J9izUMsPrL08VYRbdMd9Q0rhSAVZR6QK4aFNBgQ7E6gg"

class JarvisApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        screen = MDScreen()
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=15)
        self.chat_label = MDLabel(text="JARVIS Online...\nZahid Bhai, ready hun!", halign="center")
        self.input = MDTextField(hint_text="Bolo e.g. time kya hai?", size_hint=(1, 0.15))
        btn = MDRaisedButton(text="SEND TO JARVIS", pos_hint={"center_x": 0.5}, size_hint=(1, 0.2))
        btn.bind(on_press=self.process_command)
        layout.add_widget(self.chat_label)
        layout.add_widget(self.input)
        layout.add_widget(btn)
        screen.add_widget(layout)
        return screen
    def speak(self, text):
        self.chat_label.text = text
        try:
            from plyer import tts; tts.speak(text)
        except: pass
    def process_command(self, *args):
        query = self.input.text.lower()
        if "time" in query:
            self.speak(f"Time hai {datetime.datetime.now().strftime('%I:%M %p')}"); return
        self.speak("Soch raha hu...")
        threading.Thread(target=self.ask_gemini, args=(query,)).start()
    def ask_gemini(self, query):
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
            data = {"contents": [{"parts": [{"text": f"You are JARVIS for Zahid, reply in Roman Urdu: {query}"}]}]}
            res = requests.post(url, json=data, timeout=20).json()
            ans = res['candidates'][0]['content']['parts'][0]['text']
            Clock.schedule_once(lambda x: self.speak(ans))
        except:
            Clock.schedule_once(lambda x: self.speak("API Key ka masla hai"))

JarvisApp().run()
