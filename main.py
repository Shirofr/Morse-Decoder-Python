def decode_morse(s):
    x = s.split(" ")
    message = ""
    for i in x:
       if i == "":
           message += " "
       else:
            y = morse.index(i)
            message += alphabet[y]
    return message

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....',
    '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
    '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-',
    '-.--', '--..']