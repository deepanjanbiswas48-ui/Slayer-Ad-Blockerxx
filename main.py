from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
import random

AD_SERVERS = [
    "googleads.g.doubleclick.net",
    "ads.youtube.com",
    "app-measurement.com",
    "vungle.com",
    "applovin.com",
    "unityads.com",
    "facebookads.com",
    "chartboost.com",
    "adcolony.com",
    "inmobi.com",
    "ironsource.com",
    "moatads.com"
]

class FastAdShield(App):
    def build(self):
        self.blocked_ads = 0
        self.blocked_trackers = 0
        self.data_saved = 0

        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=15)

        self.title = Label(
            text="[b][color=00ff00]FAST AD SHIELD[/color][/b]",
            markup=True,
            font_size="28sp"
        )

        self.status = Label(text="Status: Protection Active 🛡️")
        self.ads_label = Label(text="Ads Blocked: 0")
        self.trackers_label = Label(text="Trackers Blocked: 0")
        self.data_label = Label(text="Data Saved: 0 KB")
        self.last_label = Label(text="Last Blocked: None")

        self.layout.add_widget(self.title)
        self.layout.add_widget(self.status)
        self.layout.add_widget(self.ads_label)
        self.layout.add_widget(self.trackers_label)
        self.layout.add_widget(self.data_label)
        self.layout.add_widget(self.last_label)

        Clock.schedule_interval(self.simulate_block, 1)

        return self.layout

    def simulate_block(self, dt):
        domain = random.choice(AD_SERVERS)
        self.blocked_ads += 1
        self.blocked_trackers += random.randint(0, 1)
        self.data_saved += random.randint(20, 120)

        self.ads_label.text = f"Ads Blocked: {self.blocked_ads}"
        self.trackers_label.text = f"Trackers Blocked: {self.blocked_trackers}"
        self.data_label.text = f"Data Saved: {self.data_saved} KB"
        self.last_label.text = f"Last Blocked: {domain}"


if __name__ == "__main__":
    FastAdShield().run()
