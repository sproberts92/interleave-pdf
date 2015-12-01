import PyPDF2
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

class Application(Frame):
	def __init__(self):
		self.input_path = None;
		self.output_path = None;

		Frame.__init__(self)

		self.master.resizable(False, False)
		self.master.title('Interleave PDF')
		self.grid()

		self.button = Button(self, text="Select input", command=self.load_file, width=12)
		self.button.grid(row=1, column=0, sticky=W)

		self.button = Button(self, text="Select output", command=self.save_file, width=12)
		self.button.grid(row=1, column=2, sticky=W)

		self.button = Button(self, text="Interleave", command=self.interleave, width=12)
		self.button.grid(row=1, column=3, sticky=W)

	def load_file(self):
		self.input_path = askopenfilename(filetypes=(("Adobe PDF Files", "*.pdf"), ("All files", "*.*")))

	def save_file(self):
		self.output_path = asksaveasfilename(filetypes=(("Adobe PDF Files", "*.pdf"), ("All files", "*.*")))

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
