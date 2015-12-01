import PyPDF2
import tkinter as tk
import tkinter.filedialog as fd

class Application(tk.Frame):
	def __init__(self, master=None):
		self.input_path = None;
		self.output_path = None;

		tk.Frame.__init__(self, master)

		self.master.resizable(False, False)
		self.master.title('Interleave PDF')
		self.grid()

		self.button = tk.Button(self, text="Select input", command=self.load_file, width=12)
		self.button.grid(row=1, column=0)

		self.button = tk.Button(self, text="Select output", command=self.save_file, width=12)
		self.button.grid(row=1, column=2)

		self.button = tk.Button(self, text="Interleave", command=self.interleave, width=12)
		self.button.grid(row=1, column=3)

	def load_file(self):
		self.input_path = fd.askopenfilename(filetypes=(("Adobe PDF Files", "*.pdf"), ("All files", "*.*")))

	def save_file(self):
		self.output_path = fd.asksaveasfilename(filetypes=(("Adobe PDF Files", "*.pdf"), ("All files", "*.*")))

	def interleave(self):
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
