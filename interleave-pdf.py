import PyPDF2
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as fd

class Application(tk.Frame):
	def __init__(self, master=None):
		tk.Tk()

		self.input_path = tk.StringVar();
		self.output_path = tk.StringVar();

		ttk.Frame.__init__(self, master)

		self.master.resizable(False, False)
		self.master.title('Interleave PDF')
		self.grid()

		self.label = ttk.Label(self, text="Input", width=12, anchor=tk.CENTER)
		self.label.grid(row=0, column=0)

		self.entry_in = ttk.Entry(self, width=50, textvariable=self.input_path)
		self.entry_in.grid(row=0, column=1)

		self.button = ttk.Button(self, text="Browse", command=self.load_file, width=12)
		self.button.grid(row=0, column=2)

		self.label = ttk.Label(self, text="Output", width=12, anchor=tk.CENTER)
		self.label.grid(row=1, column=0)

		self.entry_out = ttk.Entry(self, width=50, textvariable=self.output_path)
		self.entry_out.grid(row=1, column=1)

		self.button = ttk.Button(self, text="Browse", command=self.save_file, width=12)
		self.button.grid(row=1, column=2)

		self.button = ttk.Button(self, text="Interleave", command=self.interleave, width=12)
		self.button.grid(row=2, column=2)

	def load_file(self):
		path = fd.askopenfilename(filetypes=(("Adobe PDF Files", "*.pdf"), ("All files", "*.*")))
		self.input_path.set(path)

	def save_file(self):
		path = fd.asksaveasfilename(filetypes=(("Adobe PDF Files", "*.pdf"), ("All files", "*.*")))
		self.output_path.set(path)

	def interleave(self):
		self.input_path = self.entry_in.get()
		self.output_path = self.entry_out.get()

		if self.input_path and self.output_path:
			document = PyPDF2.PdfFileReader(self.input_path)
			writer = PyPDF2.PdfFileWriter()

			for page in document.pages:
				writer.addPage(page)
				writer.addBlankPage()

			outputStream = open(self.output_path, 'wb')
			writer.write(outputStream)
			outputStream.close()

if __name__ == "__main__":
	Application().mainloop()
