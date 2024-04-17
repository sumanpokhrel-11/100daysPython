import requests
import tkinter as tk



def get_quote():
    """Fetches a random quote from the Game of Thrones Quotes API and updates the display."""
    try:
        response = requests.get(url="https://api.gameofthronesquotes.xyz/v1/random")
        response.raise_for_status()  # Raise an exception for non-200 status codes

        quote_data = response.json()
        sentence = f"{quote_data['sentence']} - {quote_data['character']['name']}"
        canvas.itemconfig(my_quotes, text=sentence)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching quote: {e}")
        # Handle display of error message in the UI (optional)


window = tk.Tk()
window.title("Game of Thrones Quotes")
window.config(padx=50, pady=50)

canvas = tk.Canvas(height=500, width=500)

try:
    # Attempt to load the image
    pic = tk.PhotoImage(file="100daysbootcamp/day 33/games of thrones/got.png")
except tk.TclError as e:
    print(f"Error loading image: {e}")
    # Handle potential image loading errors (optional)

canvas.create_image(250, 150, image=pic if pic else None)  # Only display image if loaded
my_quotes = canvas.create_text(250,400, text="Quotes Here!!", width=400, font=('Times New Roman', 20, 'bold'))
canvas.grid(row=0, column=0)

btn = tk.Button(text="Quote", command=get_quote)
btn.grid(row=1, column=0)

window.mainloop()
