from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.clock import Clock
from plyer import vibrator  # optional, just for feedback
from jnius import autoclass

# Access Android APIs
PythonActivity = autoclass('org.kivy.android.PythonActivity')
View = autoclass('android.view.View')
MotionEvent = autoclass('android.view.MotionEvent')
Context = autoclass('android.content.Context')

class TapApp(App):
    def build(self):
        #Set toggle to be false
        self.tapping = False
        layout = BoxLayout(orientation='vertical')
        self.toggle = ToggleButton(text='Tap: OFF', size_hint=(1, 0.2))
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