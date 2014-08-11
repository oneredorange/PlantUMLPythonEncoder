"""
An Plantuml extension for generating UML figures from within ipython notebook.
"""
import urllib
import plantumlencoder
from IPython.core.magic import magics_class, cell_magic, Magics
from IPython.display import Image, SVG

@magics_class
class Plantuml(Magics):

    @cell_magic
    def plantuml(self, line, cell):
        self.filename = line
        self.code = ""
        for line in cell.split('\n'):
            newline = line.strip()
            if newline:
                self.code += newline + '\n'

        uri = "http://www.plantuml.com/plantuml/svg/" + plantumlencoder.compress(self.code)

        urllib.urlretrieve(uri, self.filename)

        return SVG(filename=self.filename)    

def load_ipython_extension(ipython):
    ipython.register_magics(Plantuml)