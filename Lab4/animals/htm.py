# Mike Taatgen
# DPW
# 01-20-14
# Animals assignement

class Page():
    def __init__(self):
            self.__header = '''
<!DOCTYPE>
<html>
    <head>
            <title>Mike Taatgen Lab 4</title>
            <link rel='stylesheet' href='css/main.css' />
</head>
    <body>
            <div id="wrapper">'''
            self.__form='''
                <nav>
                        <a href='/?animal=0'><button>Black Dolphins</button></a>
                        <a href='/?animal=1'><button>Leopard Shark</button></a>
                        <a href='/?animal=2'><button>Blue Marlin</button></a>
                </nav>'''