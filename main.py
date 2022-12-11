'''
Main app entry point
'''

from dotenv import load_dotenv
from src.views.layout import Layout

load_dotenv()

app = Layout()
app.mainloop()
