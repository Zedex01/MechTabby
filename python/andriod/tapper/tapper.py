from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.clock import Clock
from plyer import vibrator  # optional, just for feedback
from jnius import autoclass
from kivy.uix.floatlayout import FloatLayout


# Access Android APIs
PythonActivity = autoclass('org.kivy.android.PythonActivity')
View = autoclass('android.view.View')
MotionEvent = autoclass('android.view.MotionEvent')
Context = autoclass('android.content.Context')

class TapApp(App):

    def build(self):
        self.tapping = False
        
        layout = FloatLayout()

        self.toggle = ToggleButton(
            text='Tap: OFF',
            size_hint=(0.3, 0.1),   # 30% width, 10% height
            pos_hint={'x': 0, 'top': 1}  # Top-left corner
        )

        self.toggle.bind(on_press=self.toggle_tap)
        layout.add_widget(self.toggle)

        return layout

    def toggle_tap(self, instance):
        self.tapping = not self.tapping
        instance.text = f'Tap: {"ON" if self.tapping else "OFF"}'

        #If Tapping is true:
        if self.tapping:
            Clock.schedule_interval(self.tap_screen, 0.500)  # tap every 500
        else:
            Clock.unschedule(self.tap_screen)

    def tap_screen(self, dt):
        # Coordinates for tapping
        x, y = 500, 1000  # change to your desired spot

        # Use Android MotionEvent to simulate a tap
        activity = PythonActivity.mActivity
        activity.runOnUiThread(lambda: activity.getWindow().getDecorView().dispatchTouchEvent(
            MotionEvent.obtain(0,0,MotionEvent.ACTION_DOWN,x,y,0)
        ))
        activity.runOnUiThread(lambda: activity.getWindow().getDecorView().dispatchTouchEvent(
            MotionEvent.obtain(0,0,MotionEvent.ACTION_UP,x,y,0)
        ))

if __name__ == '__main__':
    TapApp().run()