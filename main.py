import cv2


def esconde_mensagem(frase_secreta: str):
    bits_frase_secreta = ''.join(format(c, '08b') for c in bytearray(frase_secreta, "iso-8859-1"))
    img1 = cv2.imread('imgbaleia.jpg')
    pos = 0
    fim = False
    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            v1 = format(img1[i][j][2], '08b')
            v2 = v1[:6] + bits_frase_secreta[pos:pos + 2]
            img1[i][j][2] = int(v2, 2)
            pos += 2
            if pos > len(bits_frase_secreta):
                fim = True
                break
        if fim:
            break
    cv2.imwrite('imagem_encript.png', img1)


def resgata_mensagem(local_imagem: str, tam_mensagem: int):
    img_com_frase = cv2.imread(local_imagem)
    frase = ''
    parte_frase = ''
    cont = 0
    fim = False
    for i in range(img_com_frase.shape[0]):
        for j in range(img_com_frase.shape[1]):
            v1 = format(img_com_frase[i][j][2], '08b')
            parte_frase += v1[6:]
            if len(parte_frase) == 8 and cont <= tam_mensagem:
                aux = int(parte_frase, 2)
                frase += chr(aux)
                parte_frase = ''
                cont += 1
            if cont > tam_mensagem:
                fim = True
                break
        if fim:
            break
    print('frase encontrada: ' + frase)


if __name__ == '__main__':
    frase = 'o caminho para o progresso nao é fácil nem rápido'
    esconde_mensagem(frase)

    resgata_mensagem('imagem_encript.png', len(frase))
