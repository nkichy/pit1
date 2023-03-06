from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import (Color, Line)
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class PainterWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(1, 1, 1)  # цвет
            if touch.x > 111:
                touch.ud['line'] = Line(points=(touch.x, touch.y), width=15)

    def on_touch_move(self, touch):
        if touch.x > 111:
            touch.ud['line'].points += (touch.x, touch.y)

class PaintApp(App):
    def build(self):
        parent = Widget()

        self.painter = PainterWidget()

        parent.add_widget(self.painter)

        parent.add_widget(Button(text='Clear', on_press=self.clear_canvas, size=(100, 50)))
        parent.add_widget(Button(text='Save', on_press=self.save, size=(100, 50), pos=(0, 500)))

        parent.add_widget(Button(text='1', on_press=self.a, size=(100, 50), pos=(0, 50)))

        parent.add_widget(Button(text='2', on_press=self.a, size=(100, 50), pos=(0, 100)))

        parent.add_widget(Button(text='3', on_press=self.a, size=(100, 50), pos=(0, 150)))

        parent.add_widget(Button(text='4', on_press=self.a, size=(100, 50), pos=(0, 200)))

        parent.add_widget(Button(text='5', on_press=self.a, size=(100, 50), pos=(0, 250)))

        return parent
    def a(self, instance):
        pass
    def clear_canvas(self, instance):
        self.painter.canvas.clear()

    def save(self, instance):
        self.painter.size = (Window.size[0], Window.size[1])
        self.painter.export_to_png('peсунок.png')


if __name__ == '__main__':
    PaintApp().run()
