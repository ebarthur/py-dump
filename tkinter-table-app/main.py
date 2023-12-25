import tkinter as tk
from tkinter import ttk

class YourApplication:
    def __init__(self, root):
        self.root = root
        self.create_table()

    def create_table(self):
        # Create scroll bars
        self.xscroll = ttk.Scrollbar(self.root, orient="horizontal")
        self.yscroll = ttk.Scrollbar(self.root, orient="vertical")

        # Configure style
        style = ttk.Style(self.root)
        style.configure('Treeview', font=(None, 14), rowheight=27)
        style.configure('Treeview.Heading', font=(None, 16))

        # Create record table
        self.table = ttk.Treeview(self.root)

        # Configure scroll bar
        self.xscroll.configure(command=self.table.xview)
        self.yscroll.configure(command=self.table.yview)
        self.table.config(
            yscrollcommand=self.yscroll.set,
            xscrollcommand=self.xscroll.set,
            selectmode="extended",
        )

        # (Column and heading configurations go here)
        columns = (
            "Batch", "Date", "Machine", "Job", "Color", "Plate",
            "Anilox", "Substrate", "Delta E", "Tech", "Workoff",
            "Fresh", "Total", "Viscosity",
        )
        self.table["columns"] = columns
        # (Column width, heading, and other configurations go here)

        self.populate_table()

        # Display headings
        self.table["show"] = "headings"

        # Place table and scroll bars
        self.table.place(x=5, y=10, width=970, height=400)
        self.xscroll.place(x=10, y=410, width=980, height=20)
        self.yscroll.place(x=975, y=10, width=20, height=400)

    def populate_table(self):
        # Create count variable for striped rows
        count = 0

        # Create row stripe tags for alternative row colors
        self.table.tag_configure("oddrow", background="#D9D9D6")
        self.table.tag_configure("evenrow", background="white")

        # Mock data for demonstration purposes (replace with your actual data)
        data = [
            ("1", "2023-01-01", "Machine 1", "Job 1", "Red", "Plate 1",
             "Anilox 1", "Substrate 1", "1.5", "Tech 1", "Workoff 1",
             "Fresh 1", "Total 1", "Viscosity 1"),
            # Add more rows as needed
        ]

        # Loop through data to add to the table
        for record in data:
            if count % 2 == 0:
                self.table.insert(
                    parent="",
                    index="end",
                    iid=count,
                    text=count,
                    values=record,
                    tags=("evenrow"),
                )
            else:
                self.table.insert(
                    parent="",
                    index="end",
                    iid=count,
                    text=count,
                    values=record,
                    tags=("oddrow"),
                )
            count += 1

if __name__ == "__main__":
    root = tk.Tk()
    app = YourApplication(root)
    root.mainloop()
