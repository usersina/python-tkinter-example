'''
Main app entry point
'''

from dotenv import load_dotenv
from src.views.layout import Layout

# Load the env variables from the `.env` file
load_dotenv()

# Instantiate the layout and enter the main loop
app = Layout()
app.mainloop()
