from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from random import randint


class DiceWheelGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.total_winnings = 0
        self.lucky_numbers = []

        # Интерфейс
        self.info_label = Label(text="Welcome to Dice Wheel!", font_size=24, size_hint=(1, 0.2))
        self.add_widget(self.info_label)

        self.generate_button = Button(text="Generate Lucky Numbers", size_hint=(1, 0.1))
        self.generate_button.bind(on_press=self.generate_lucky_numbers)
        self.add_widget(self.generate_button)

        self.input_section = BoxLayout(size_hint=(1, 0.1))
        self.bet_input = TextInput(hint_text="Enter number(s) to bet (comma separated)", multiline=False)
        self.wager_input = TextInput(hint_text="Enter wager(s) (comma separated)", multiline=False)
        self.input_section.add_widget(self.bet_input)
        self.input_section.add_widget(self.wager_input)
        self.add_widget(self.input_section)

        self.place_bet_button = Button(text="Place Bet", size_hint=(1, 0.1))
        self.place_bet_button.bind(on_press=self.place_bet)
        self.add_widget(self.place_bet_button)

        self.cash_out_button = Button(text="Cash Out", size_hint=(1, 0.1))
        self.cash_out_button.bind(on_press=self.cash_out)
        self.add_widget(self.cash_out_button)

    def generate_lucky_numbers(self, instance):
        self.lucky_numbers = sorted([randint(1, 6) for _ in range(3)])
        self.info_label.text = f"Lucky numbers generated: {self.lucky_numbers}"

    def place_bet(self, instance):
        try:
            bets = [int(num.strip()) for num in self.bet_input.text.split(',')]
            wagers = [int(num.strip()) for num in self.wager_input.text.split(',')]

            if len(bets) != len(wagers):
                self.info_label.text = "Number of bets and wagers must match."
                return

            winnings = 0
            for num, wager in zip(bets, wagers):
                if num < 1 or num > 6:
                    self.info_label.text = f"Invalid bet number: {num}. Must be between 1 and 6."
                    return
                if wager < 1 or wager > 500:
                    self.info_label.text = f"Invalid wager: {wager}. Must be between $1 and $500."
                    return

                count = self.lucky_numbers.count(num)
                if count > 0:
                    winnings += count * wager
                    self.info_label.text += f"\nYou WIN {count} times on {num}!"
                else:
                    winnings -= wager
                    self.info_label.text += f"\nYou LOSE on {num}."

            self.total_winnings += winnings
            self.info_label.text += f"\nTotal Winnings: ${self.total_winnings}"
        except ValueError:
            self.info_label.text = "Invalid input. Please enter valid numbers."

    def cash_out(self, instance):
        self.info_label.text = f"Game Over! Total Winnings: ${self.total_winnings}"
        self.total_winnings = 0
        self.lucky_numbers = []

class DiceWheelApp(App):
    def build(self):
        return DiceWheelGame()


if __name__ == "__main__":
    DiceWheelApp().run()