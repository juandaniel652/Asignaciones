from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        # Crea un botón con un texto inicial
        button = Button(text='Hola, presióname')
        
        # Define la acción cuando el botón es presionado
        button.bind(on_press=self.on_button_press)
        
        return button
    
    # Método que se ejecuta cuando el botón es presionado
    def on_button_press(self, instance):
        instance.text = '¡Has presionado el botón!'

# Ejecuta la aplicación
if __name__ == '__main__':
    MyApp().run()
