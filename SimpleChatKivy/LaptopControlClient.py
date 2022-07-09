from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import socket


class SayHello(App):
    def build(self):
        # returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.enter_command = Label(
            text="Введіть команду:",
            font_size=18,
            color='#00FFCE'
        )
        self.window.add_widget(self.enter_command)

        self.state_lab = Label(
            text="",
            font_size=18,
            color='#00FFCE'
        )
        self.window.add_widget(self.state_lab)

        # text input widget
        self.command = TextInput(
            #multiline=False,
            padding_y=(20, 20),
            size_hint=(1, 1),
        )

        self.window.add_widget(self.command)

        # button widget
        self.button = Button(
            text="ВИКОНАТИ",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFCE',
            # remove darker overlay of background colour
            # background_normal = ""
        )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect(("127.0.0.1", 50284))
        except ConnectionRefusedError:
            self.state_lab.color = "red"
            self.state_lab.text = "Помилка. Не вдалося під'єднатися до сервера!"

        return self.window

    def callback(self, instance):
        try:
            self.client.send(self.command.text.encode('utf-8'))
        except OSError:
            self.state_lab.color = "red"
            self.state_lab.text = "Помилка. Не вдалося відправити команду!"
        else:
            self.state_lab.text = "Команда успішно надіслана!"
            self.state_lab.color = "green"
            self.command.text = ""


# run Say Hello App Calss
if __name__ == "__main__":
    app = SayHello()
    app.run()
