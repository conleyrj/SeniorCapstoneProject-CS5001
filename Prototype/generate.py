import random

secret = 8523

def generate(question):
    for version in range(1, 4):
        seed = secret + version
        rand = random.Random()
        rand.seed(seed)
        text = question(rand)
        with open(f"version-{version}.tex", "w") as file:
            file.write("""
            \\documentclass{minimal}
            \\usepackage{amsfonts,amsmath,enumerate,amsthm,amssymb}
            \\usepackage{qrcode}

            \\begin{document}

            """)
            file.write(text)
            file.write(f"""
            
            $ $ \\\\
            $ $ \\\\

            Random Seed: {seed} \\\\

            \\qrcode{{{seed}}}
            \\end{{document}}
""")