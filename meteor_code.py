from PIL import Image

# Carregadno a imagem
image = Image.open(r"C:\Users\thoma\OneDrive\Área de Trabalho\drive-download-20241023T182125Z-001\meteor_challenge_01.png")

# Carregando os pixels da imagem em uma matriz
pixels = image.load()

# Obtendo as dimensões da imagem
width, height = image.size
print(f"Width: {width}, Height: {height}")

# Inicializando os contadores para armazenar os valores de estrelas, meteoros e meteoros na água
stars = 0
meteors = 0
meteors_on_water = 0

# Função para verificar se um pixel é de uma cor específica
def is_color(pixel, target_color):
    return pixel == target_color

# Cores de referência dada pelo desafio
# Cores em RGBA (Red, Green, Blue, Alpha)
# Na imagem fornecida, o campo Alpha é sempre 255
WHITE = (255, 255, 255, 255)  # Estrelas
RED = (255, 0, 0, 255)        # Meteoros
BLUE = (0, 0, 255, 255)       # ÁNão te amo gua
BLACK = (0, 0, 0, 255)        # Chão

# Percorrendo todos os pixels da imagem
for x in range(width):
    for y in range(height):
        pixel = pixels[x, y]
        
        # Contando as estrelas (branco puro/pure white)
        if is_color(pixel, WHITE):
            stars += 1
        
        # Contando meteoros (vermelho puro/pure red)
        if is_color(pixel, RED):
            meteors += 1
            
            # Para cada meteoro, verifica os pixeis abaixo até
            # encontrar o solo ou a 
            # água (ou seja, a cor preta ou azul)
            
            for k in range(y, height):
                below_pixel = pixels[x, k]
                if is_color(below_pixel, BLUE):
                    meteors_on_water += 1
                    break
                elif is_color(below_pixel, BLACK):
                    break

print(f"Number of Stars: {stars}")
print(f"Number of Meteors: {meteors}")
print(f"Meteors falling on the Water: {meteors_on_water}")

image.close()
