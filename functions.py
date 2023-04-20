def quest_gen(n=5):
    code = ""
    code += '<form action="/echo" method="POST" class="quest">'
    code += f'<input type="number" id="quantity" name="age2" min="18" max="99">'
    for i in range(1, n):
        code += f'<h3>{i}. Lorem Ipsum Dolor Sit Amet?</h3>'
        for j in range(4):
            code += f'<input type="radio" name="{"quest" + str(i)}" value="{chr(65+j)}">{chr(65+j)} Risposta <br>'
    code += f'Age range: '
    code += f'<input type="range" name="age" min="18" max="99" value="24" step="1" onchange="updateTextInput(this.value);">'
    code += f'<span id="textInput">24</span><br>'
    code += '<input type="submit" value="Invia" ></form>'
    return code