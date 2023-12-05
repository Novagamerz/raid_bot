import asyncio
from telegram_bot import TelegramBot
from pyfiglet import Figlet
from termcolor import colored, cprint  # Make sure to install this library

def rainbowify(text):
    rainbow_text = ''
    colors = ['green', 'cyan', 'blue', 'magenta']
    for i in range(len(text)):
        rainbow_text += colored(text[i], color=colors[i % len(colors)])
    return rainbow_text

async def main():
    # Initialize Figlet object
    fig = Figlet(font='slant')

    # Print rainbow ASCII art
    ascii_art = fig.renderText("naix0x - raid")
    rainbow_ascii_art = rainbowify(ascii_art)
    cprint(rainbow_ascii_art, attrs=['bold'])

    bot = TelegramBot()

    group_id = int(input("Enter group ID: "))
    file_paths = input("Enter text file paths (separated by comma): ").split(',')
    messages = [bot.read_message_from_file(file_path.strip()) for file_path in file_paths]
    time_delay = int(input("Enter time delay (in seconds): "))
    duration = int(input("Enter duration (in seconds): "))

    await bot.send_messages(group_id, messages, time_delay, duration)

if __name__ == "__main__":
    asyncio.run(main())